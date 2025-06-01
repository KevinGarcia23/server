# Python HTTP Server

A minimal HTTP server built from scratch in Python, to learn how HTTP requests and responses work under the hood without using any web framework.

## Why?
- I wanted to understand how TCP sockets translate into HTTP transactions.
- I’m learning Python and wanted to build something “from the ground up” instead of relying on Flask or Django.
- Through this project, I learned about socket programming, basic HTTP methods, and response formatting.

## Features
- Listens on port 8080 (configurable in `server.py`).
- Parses a raw HTTP GET request (just enough to extract the path).
- Serves a static `index.html` (and returns 404 for unknown routes).
- Returns “405 Method Not Allowed” for any non-GET request.

# Clone the repo
git clone https://github.com/KevinGarcia23/server
cd python-http-server

# Launch the server
python3 server.py

# Then open your browser to http://localhost:8080

## Learning Points
- How to use Python's `socket` module to accept TCP connections.
- How raw HTTP requests look (request line, headers, etc.) and how to build a valid HTTP response.
- The importance of correct status lines (e.g., `HTTP/1.1 200 OK\r\n\r\n`) so that browsers properly render the page.
- How blocking I/O works—requests queue up if you don’t spawn new threads or async handlers.
- Basic debugging tips: printing out the raw request, splitting lines, etc.
