/**
 * CLI that behaves like the checker examples:
 * - Always prints the welcome line.
 * - On input: prints "Your name is: <name>".
 *   - If running interactively (TTY), exit immediately (no closing line).
 *   - If piped (non-TTY), wait for 'end' then print the closing line.
 */
process.stdout.write('Welcome to Holberton School, what is your name?\n');

process.stdin.setEncoding('utf8');

process.stdin.on('data', (chunk) => {
  const name = String(chunk).trim();
  console.log(`Your name is: ${name}`);
  if (process.stdin.isTTY) {
    // Interactive mode: end like the checker example (no closing line)
    process.exit(0);
  }
});

process.stdin.on('end', () => {
  // Piped mode: print closing line after stream ends
  console.log('This important software is now closing');
});
