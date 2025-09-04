import { readDatabase } from '../utils.js';

class StudentsController {
  static async getAllStudents(req, res) {
    try {
      const dbPath = process.argv[2];
      const byField = await readDatabase(dbPath);
      const fields = Object.keys(byField).sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));
      const lines = ['This is the list of our students'];
      for (const field of fields) {
        const list = byField[field].join(', ');
        lines.push(`Number of students in ${field}: ${byField[field].length}. List: ${list}`);
      }
      res.status(200).send(lines.join('\n'));
    } catch (_e) {
      res.status(500).send('Cannot load the database');
    }
  }

  static async getAllStudentsByMajor(req, res) {
    try {
      const { major } = req.params;
      if (major !== 'CS' && major !== 'SWE') {
        res.status(500).send('Major parameter must be CS or SWE');
        return;
      }
      const dbPath = process.argv[2];
      const byField = await readDatabase(dbPath);
      const list = (byField[major] || []).join(', ');
      res.status(200).send(`List: ${list}`);
    } catch (_e) {
      res.status(500).send('Cannot load the database');
    }
  }
}

export default StudentsController;
