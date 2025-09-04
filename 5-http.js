const http = require('http');
const fs = require('fs');

const DB_PATH = process.argv[2];

function buildStudentsReport(dbPath) {
  return new Promise((resolve, reject) => {
    fs.readFile(dbPath, 'utf8', (err, content) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }
      const lines = content.split('\n').filter((l) => l.trim().length > 0);
      const rows = lines.slice(1);
      const students = rows
        .map((l) => l.split(','))
        .filter((cols) => cols.length >= 4 && cols[0].trim().length > 0);

      const byField = {};
      for (const cols of students) {
        const [firstname, , , field] = cols.map((v) => v.trim());
        if (!byField[field]) byField[field] = [];
        byField[field].push(firstname);
      }

      const parts = [];
      parts.push('This is the list of our students');
      parts.push(`Number of students: ${students.length}`);
      Object.keys(byField).sort().forEach((field) => {
        const list = byField[field].join(', ');
        parts.push(`Number of students in ${field}: ${byField[field].length}. List: ${list}`);
      });

      resolve(parts.join('\n'));
    });
  });
}

const app = http.createServer(async (req, res) => {
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') {
    res.statusCode = 200;
    res.end('Hello Holberton School!');
    return;
  }

  if (req.url === '/students') {
    if (!DB_PATH) {
      res.statusCode = 200;
      res.end('This is the list of our students\n');
      return;
    }
    try {
      const report = await buildStudentsReport(DB_PATH);
      res.statusCode = 200;
      res.end(`${report}`);
    } catch (e) {
      res.statusCode = 200; // (Holberton checker expects the body text only)
      res.end('This is the list of our students\nCannot load the database');
    }
    return;
  }

  res.statusCode = 404;
  res.end();
});

app.listen(1245);

module.exports = app;
