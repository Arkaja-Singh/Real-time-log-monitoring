# app/log_manager.py

# app/log_manager.py

import asyncio
import time


LOG_FILE_PATH = "logs/sample.log"

class LogManager:
    def __init__(self):
        self.active_connections = []

    async def connect(self, websocket):
        """Add websocket to active connections"""
        self.active_connections.append(websocket)
        await websocket.send_text("Connected to LogManager")

    async def disconnect(self, websocket):
        """Remove websocket from active connections"""
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        """Send a log message to all active websocket connections"""
        for connection in self.active_connections:
            await connection.send_text(message)

    async def watch_log(self):
        """Simulate monitoring logs and broadcasting them to all connections"""
        # Example of watching a log or a data stream
        while True:
            log_message = "New log entry at " + time.strftime("%Y-%m-%d %H:%M:%S")
            await self.broadcast(log_message)
            await asyncio.sleep(5)  # Wait for 5 seconds before sending the next log message


