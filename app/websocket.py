import asyncio
import os
from fastapi import WebSocket
from app.log_manager import LogManager
from typing import List


# app/websocket.py

class WebSocketManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
        print("Connection opened")

    async def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)
        await websocket.close()
        print("Connection closed")

    async def send_log(self, websocket: WebSocket, log: str):
        await websocket.send_text(log)

    async def watch_log(self):
        # Implement your log watching logic
        while True:
            # simulate log generation (replace with your actual log watching logic)
            log = "Generated log: Some log message here"
            for connection in self.active_connections:
                await self.send_log(connection, log)
            await asyncio.sleep(2)


    async def send_log(self, log_entry: str):
        for connection in self.connections:
            await connection.send_text(log_entry)
class LogManager:
    def __init__(self):
        # Initialization code here
        pass

manager = LogManager()
