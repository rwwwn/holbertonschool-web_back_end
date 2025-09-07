import { readDatabase } from '../utils.js';

class StudentsController {
  static async getAllStudents(_req, res) {
    const dbPath = process.argv[2];
    try {
      const byField = await readDatabase(dbPath);
      const fields = Object.keys(byField)
        .sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));

      const lines = ['This is the list of our students'];
      for (const field of fields) {
        const list = byField[field] || [];
        lines.push(`Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`);
      }
      res.status(200).send(lines.join('\n'));
    } catch (_err) {
      res.status(500).send('Cannot load the database');
    }
  }

  static async getAllStudentsByMajor(req, res) {
    const { major } = req.params;
    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }
    const dbPath = process.argv[2];
    try {
      const byField = await readDatabase(dbPath);
      const list = byField[major] || [];
      res.status(200).send(`List: ${list.join(', ')}`);
    } catch (_err) {
      res.status(500).send('Cannot load the database');
    }
  }
}

export default StudentsController;
