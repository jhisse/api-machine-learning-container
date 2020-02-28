class Ping:
    def on_get(self, req, resp):
        resp.media = {"ping": "pong"}
