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
    'consistent-return': 'off',
    'import/prefer-default-export': 'off',
    'max-len': ['error', {
      code: 120, ignoreComments: true, ignoreStrings: true, ignoreTemplateLiterals: true,
    }],
    // Allow for..of (keep Airbnb's other restricted syntaxes)
    'no-restricted-syntax': [
      'error',
      {
        selector: 'ForInStatement',
        message: 'for..in loops iterate over the entire prototype chain. Use Object.{keys,values,entries} with forEach.',
      },
      {
        selector: 'LabeledStatement',
        message: 'Labels are a form of GOTO; using them makes code confusing and hard to maintain.',
      },
      {
        selector: 'WithStatement',
        message: '`with` is disallowed in strict mode because it makes code impossible to predict and optimize.',
      },
    ],
  },
};
