import asyncio
from websockets.asyncio.client import connect
from websockets import ConnectionClosed

async def get_data_stream(symbols : str):
    # using the api-finance project in my git repos
    async with connect(f"ws://127.0.0.1:8000/ws?symbols={symbols}") as websocket:
        while True:
            try:
                message = await websocket.recv()
                print(f"received {message=}")
            except ConnectionClosed:
                print("Connection closed")
                break

if __name__ == "__main__":
    asyncio.run(get_data_stream("AAPL,IBM,MSFT"))