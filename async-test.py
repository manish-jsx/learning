# async-test.py 

import asyncio

async def example_coroutine():
    print("Start Coroutine")
    await asyncio.sleep(2)  # Simulate a non-blocking operation
    print("End Coroutine")

async def main():
    task1 = asyncio.create_task(example_coroutine())
    task2 = asyncio.create_task(example_coroutine())

    print("Before await")

    await asyncio.gather(task1, task2)

    print("After await")

if __name__ == "__main__":
    asyncio.run(main())

