module.exports = {
  env: {
    browser: false,
    commonjs: true,
    es2021: true,
    node: true,
    jest: true,
  },
  extends: ['airbnb-base'],
  parserOptions: {
    ecmaVersion: 12,
    sourceType: 'script', // CommonJS for tasks 0–7
  },
  overrides: [
    {
      files: ['full_server/**/*.js'],
      parserOptions: {
        ecmaVersion: 12,
        sourceType: 'module', // ES modules for full_server
      },
      env: {
        node: true,
        es2021: true,
      },
    },
  ],
  rules: {
    'no-console': 'off',
    'no-unused-vars': ['error', { argsIgnorePattern: '^_' }],
    'import/extensions': 'off',
    'consistent-return': 'off'
  },
};
