import asyncio
import aiohttp

from time import time


url = "https://loremflickr.com/320/240"


def save_image(image):
	file_name = int(time() * 1000)
	with open("images/{}.jpg".format(file_name), "wb") as file:
		file.write(image)

async def get_image(session):
	async with session.get(url, allow_redirects=True) as response:
		image = await response.read()
		save_image(image)

async def _dowload_images(amount):
	tasks = []

	async with aiohttp.ClientSession() as session:
		for i in range(amount):
			task = asyncio.create_task(get_image(session))
			tasks.append(task)

		await asyncio.gather(*tasks)


def dowload_images_async(amount=10):
	asyncio.run(_dowload_images(amount))
