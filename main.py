import asyncio
from websockets.asyncio.client import connect
from websockets import ConnectionClosed

async def connect_to_data_stream(symbol : str):
    # using the api-finance project in my git repos
    async with connect(f"ws://127.0.0.1:8000/ws/{symbol}") as websocket:
        while True:
            try:
                message = await websocket.recv()
                print(f"{symbol=} received {message=}")
            except ConnectionClosed:
                print("Connection closed")
                break

async def main():
    symbols = [
        "AAPL",
        "IBM",
        "MSFT",
        "GOOGL",
        "AMZN",
        "TSLA",
        "NVDA",
        "JPM",
        "JNJ",
        "V",
        "PG",
        "XOM",
        "CVX",
        "WMT",
        "HD",
        "MA",
        "DIS",
        "PFE",
        "BAC"
    ]

    tasks = [connect_to_data_stream(symbol) for symbol in symbols]

    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
