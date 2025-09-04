const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, content) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = content.split('\n').filter((l) => l.trim().length > 0);
      const rows = lines.slice(1);
      const students = rows
        .map((l) => l.split(','))
        .filter((cols) => cols.length >= 4 && cols[0].trim().length > 0);

      console.log(`Number of students: ${students.length}`);

      const byField = {};
      for (const cols of students) {
        const [firstname, , , field] = cols.map((v) => v.trim());
        if (!byField[field]) byField[field] = [];
        byField[field].push(firstname);
      }

      Object.keys(byField).sort().forEach((field) => {
        const list = byField[field].join(', ');
        console.log(`Number of students in ${field}: ${byField[field].length}. List: ${list}`);
      });

      resolve();
    });
  });
}

module.exports = countStudents;
