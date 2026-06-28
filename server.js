const http = require('http');

const PORT = 3000;
let requestCount = 0;

const server = http.createServer((req, res) => {
  requestCount++;
  const ts = new Date().toISOString();

  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Content-Type', 'application/json');

  if (req.url === '/api/message' && req.method === 'GET') {
    res.writeHead(200);
    res.end(JSON.stringify({
      status: 'ok',
      message: 'Hello from the server!',
      timestamp: ts,
      requests: requestCount
    }));

  } else if (req.url === '/api/echo' && req.method === 'POST') {
    let body = '';
    req.on('data', chunk => body += chunk);
    req.on('end', () => {
      res.writeHead(200);
      res.end(JSON.stringify({
        echo: JSON.parse(body),
        received_at: ts
      }));
    });

  } else if (req.url === '/api/status') {
    res.writeHead(200);
    res.end(JSON.stringify({
      server: 'running',
      port: PORT,
      total_requests: requestCount
    }));

  } else {
    res.writeHead(404);
    res.end(JSON.stringify({ error: 'not found' }));
  }
});

server.listen(PORT, '127.0.0.1', () =>
  console.log(`Server running → http://127.0.0.1:${PORT}`));
