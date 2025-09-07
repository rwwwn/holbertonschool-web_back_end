const express = require('express');

const app = express();

app.get('/', (_req, res) => {
  res.set('Content-Type', 'text/plain');
  res.status(200).send('Hello Holberton School!');
});

app.listen(1245, () => { /* noop */ });

module.exports = app;
