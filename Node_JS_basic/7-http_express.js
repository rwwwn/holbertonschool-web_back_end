const express = require('express');
const fs = require('fs');

const app = express();

function readDatabase(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }
      const lines = data
        .trim()
        .split('\n')
        .map((l) => l.trim())
        .filter((l) => l.length > 0);

      if (lines.length <= 1) {
        resolve({});
        return;
      }

      const header = lines[0].split(',').map((h) => h.trim());
      const idxFirstname = header.indexOf('firstname');
      const idxField = header.indexOf('field');

      const byField = {};
      for (let i = 1; i < lines.length; i += 1) {
        const parts = lines[i].split(',');
        if (parts.length >= 4) {
          const firstname = String(parts[idxFirstname] || '').trim();
          const field = String(parts[idxField] || '').trim();
          if (firstname && field) {
            if (!byField[field]) byField[field] = [];
            byField[field].push(firstname); // preserve file order
          }
        }
      }
      resolve(byField);
    });
  });
}

app.get('/', (_req, res) => {
  res.set('Content-Type', 'text/plain');
  res.status(200).send('Hello Holberton School!');
});

app.get('/students', (_req, res) => {
  const dbPath = process.argv[2];
  res.set('Content-Type', 'text/plain');
  readDatabase(dbPath)
    .then((byField) => {
      const fields = Object.keys(byField)
        .sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));
      const lines = ['This is the list of our students'];
      let total = 0;
      for (const f of fields) {
        const list = byField[f] || [];
        total += list.length;
      }
      lines.push(`Number of students: ${total}`);
      for (const f of fields) {
        const list = byField[f] || [];
        lines.push(`Number of students in ${f}: ${list.length}. List: ${list.join(', ')}`);
      }
      res.status(200).send(lines.join('\n'));
    })
    .catch((_e) => {
      // Spec wants header + exact error line when DB missing
      res.status(500).send('This is the list of our students\nCannot load the database');
    });
});

app.listen(1245, () => { /* noop */ });

module.exports = app;
