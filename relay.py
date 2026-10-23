"""Tiny relay so the After Hours page can talk to Bale.
Run it with:  python relay.py   (on Windows you can also try: py relay.py)
Leave the window open while you use the Bale chat tab. Press Ctrl+C to stop."""
import http.server, json, sys, urllib.request, urllib.error

# Default is Bale. Run "python relay.py telegram" to relay Telegram instead.
BASE = "https://api.telegram.org" if "telegram" in sys.argv[1:] else "https://tapi.bale.ai"

class Relay(http.server.BaseHTTPRequestHandler):
    def cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Access-Control-Allow-Private-Network", "true")

    def do_OPTIONS(self):
        self.send_response(204); self.cors(); self.end_headers()

    def forward(self):
        if not self.path.lower().startswith("/bot"):
            self.send_response(404); self.cors(); self.end_headers(); return
        n = int(self.headers.get("Content-Length") or 0)
        body = self.rfile.read(n) if n else None
        req = urllib.request.Request(BASE + self.path, data=body, method=self.command)
        if body:
            req.add_header("Content-Type", self.headers.get("Content-Type", "application/json"))
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                code, data = r.status, r.read()
        except urllib.error.HTTPError as e:
            code, data = e.code, e.read()
        except Exception as e:
            code = 502
            data = json.dumps({"ok": False, "description": "Relay could not reach Bale: %s" % e}).encode()
        self.send_response(code); self.cors()
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers(); self.wfile.write(data)

    do_GET = do_POST = forward

    def log_message(self, *args):
        pass

print("Relay for " + BASE + " running at http://127.0.0.1:8787  (leave this window open; Ctrl+C to stop)")
http.server.ThreadingHTTPServer(("127.0.0.1", 8787), Relay).serve_forever()
