const express = require('express');
const app = express();
const port = 5000;

app.use(express.json()); // Middleware to parse JSON bodies

// Handle DELETE request at /route_3
app.delete('/route_3', (req, res) => {
  res.send("I'm a DELETE request");
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});

