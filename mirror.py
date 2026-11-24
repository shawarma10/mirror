#!/usr/bin/env python3
import os
from datetime import datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class DumpHandler(BaseHTTPRequestHandler):
    def _handle(self):
        length = int(self.headers.get("Content-Length", 0) or 0)
        body = self.rfile.read(length) if length else b""

        lines = [f"{self.command} {self.path} {self.request_version}"]
        lines += [f"{key}: {value}" for key, value in self.headers.items()]
        if body:
            lines.append("")
            try:
                lines.append(body.decode("utf-8"))
            except UnicodeDecodeError:
                lines.append(f"<{len(body)} bytes of binary data> {body[:200]!r}")
                
        dump = "\n".join(lines) + "\n"

        print("=" * 70)
        print(f"[{datetime.now().isoformat(timespec='seconds')}] "
              f"{self.client_address[0]}:{self.client_address[1]}")
        
        print(dump, flush=True)

        payload = dump.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(payload)

    do_GET = do_POST = do_PUT = do_PATCH = do_DELETE = _handle
    do_HEAD = do_OPTIONS = do_TRACE = do_CONNECT = _handle

    def log_message(self, format, *args):
        pass


def main():
    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", "8000"))

    server = ThreadingHTTPServer((host, port), DumpHandler)
    print(f"Listening on http://{host}:{port} (Ctrl+C to stop)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down.")
        server.server_close()


if __name__ == "__main__":
    main()
