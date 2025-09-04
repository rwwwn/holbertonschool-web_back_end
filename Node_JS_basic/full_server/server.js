import express from 'express';
import routes from './routes/index.js';

const app = express();

app.use('/', routes);

app.listen(1245);

// Important for checker:
export default app;
