const http = require('http');
const PORT = 3000;
const TARGET_LAT = 29.7604, TARGET_LON = -95.3698;

const server = http.createServer((req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, OPTIONS');
  res.setHeader('Content-Type', 'application/json');

  if (req.method === 'OPTIONS') {
    res.writeHead(204);
    res.end();
    return;
  }

  if (req.url === '/api/matrix-shadow' && req.method === 'GET') {
    const now = Date.now() / 1000;
    const simLat = TARGET_LAT + (2.5 * Math.sin(now / 3600));
    const simLon = TARGET_LON + (2.5 * Math.cos(now / 3600));
    const dLat = simLat - TARGET_LAT;
    const dLon = simLon - TARGET_LON;
    const distance = Math.sqrt(dLat * dLat + dLon * dLon);

    const payload = {
      timestamp: new Date().toISOString(),
      upstream_reality: { x_node: +(dLon * 1000).toFixed(4), y_node: +(dLat * 1000).toFixed(4), status: 'synchronized' },
      dark_space: { u_axis: +(Math.cos(distance) * 255).toFixed(2), v_axis: +(Math.sin(distance) * 255).toFixed(2) }
    };
    res.writeHead(200);
    res.end(JSON.stringify(payload));
  } else {
    res.writeHead(404);
    res.end(JSON.stringify({ error: 'Route not found' }));
  }
});
server.listen(PORT, () => console.log('[*] Native Throughput Bridge Active on Port: ' + PORT));
