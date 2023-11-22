#An example of how to handle synchronous code (Pillow) in an asynchronous environment using ThreadPoolExecutor.
import discord
import asyncio
from concurrent.futures import ThreadPoolExecutor
from gen import GenerateImage

POOL = ThreadPoolExecutor()
  
async def task_ImageGeneration(loop):
    result = await loop.run_in_executor(POOL, GenerateImage, ImageConfigs)
  
async def main():
    loop = asyncio.get_event_loop()
    loop.create_task(task_ImageGeneration(loop)) # create a task if you dont want the execution of main() to be blocked, else just call loop.run_in_executor here directly.


asyncio.run(main())