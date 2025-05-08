# app/main.py

import os
import asyncio
import aiofiles
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

from app.log_manager import LOG_FILE_PATH  # get constant path from one place
from app.log_manager import LogManager
# from app.websocket import WebSocketManager  # Not used anymore

app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost", "http://127.0.0.1"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

manager = LogManager()

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(manager.watch_log())

@app.get("/")
def home():
    return {"message": "Welcome to Real-Time Log Monitoring!"}

@app.websocket("/ws/logs")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            await asyncio.sleep(1)  # Adding a small delay to prevent excessive checking
            if not os.path.exists("logs/sample.log"):
                continue

            # Read the log file asynchronously
            async with aiofiles.open("logs/sample.log", mode='r') as file:
                lines = await file.readlines()
                if lines:
                    try:
                        # Only attempt to send data if WebSocket is still connected
                        if websocket.client_state == WebSocketState.CONNECTED:
                            await websocket.send_text("".join(lines[-10:]))
                    except WebSocketDisconnect:
                        # If the WebSocket disconnects during sending, exit the loop
                        print("WebSocket disconnected while sending")
                        break
                    except Exception as e:
                        print(f"Error while sending message: {e}")
                        break
    except WebSocketDisconnect:
        print("Client disconnected")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        try:
            await websocket.close()
        except Exception as e:
            print(f"Error closing WebSocket: {e}")