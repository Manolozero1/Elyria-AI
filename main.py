
import uvicorn
from config import Config
from uvicorn.server import ServerState
from uvicorn.protocols.websockets.websockets_impl import WebSocketProtocol

config = Config()
server_state = ServerState()
app_state = {}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        log_level="info",
        ws=WebSocketProtocol,
        config=config,
        server_state=server_state,
        app_state=app_state,
    )