import fs from 'fs';

export function readDatabase(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, content) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }
      const lines = content.split('\n').filter((l) => l.trim().length > 0);
      const rows = lines.slice(1);
      const byField = {};
      for (const line of rows) {
        const cols = line.split(',');
        if (cols.length >= 4 && cols[0].trim().length > 0) {
          const firstname = cols[0].trim();
          const field = cols[3].trim();
          if (!byField[field]) byField[field] = [];
          byField[field].push(firstname);
        }
      }
      resolve(byField);
    });
  });
}
