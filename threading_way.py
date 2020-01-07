import requests

from threading import Thread
from time import time, sleep


url = "https://loremflickr.com/320/240"

def get_image():
	response = requests.get(url, allow_redirects=True, timeout=(10, 10))
	response.raise_for_status()
	return response

def save_image(response):
	file_name = str(time() % 1) + "_" + response.url.split("/")[-1]
	image = response.content
	with open("images/{}".format(file_name), "wb") as file:
		file.write(image)

def dowload_images_threading(amount=10):
	threads = []
	try:
		for i in range(amount):
			thread = Thread(target=_dowload_image)
			threads.append(thread)
			thread.start()

		while any([thread.isAlive() for thread in threads]):
			sleep(0.01)

	except Exception as e:
		print("Some error occur: {}".format(e))

def _dowload_image():
	img_response = get_image()
	save_image(img_response)
