import express from 'express';
import { createProxyMiddleware } from 'http-proxy-middleware';

const app = express();
const PORT = process.env.PORT || 8080;

app.use('/api/pedidos', createProxyMiddleware({
  target: 'http://localhost:5002',
  changeOrigin: true
}));

app.use('/api/productos', createProxyMiddleware({
  target: 'http://localhost:5001',
  changeOrigin: true
}));

app.listen(PORT, () => {
  console.log(`API Gateway ejecutándose en http://localhost:${PORT}`);
});
