/**
 * Reads a name from stdin and prints:
 * - "Welcome to Holberton School, what is your name?"
 * - "Your name is: <name>"
 * And on stdin end (piped input), prints closing line.
 */
process.stdout.write('Welcome to Holberton School, what is your name?\n');

process.stdin.setEncoding('utf8');

process.stdin.on('data', (chunk) => {
  const name = String(chunk).trim();
  if (name.length > 0) {
    console.log(`Your name is: ${name}`);
  } else {
    console.log('Your name is: ');
  }
});

process.stdin.on('end', () => {
  console.log('This important software is now closing');
});
