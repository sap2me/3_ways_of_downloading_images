import requests

from time import time


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

def dowload_images_sync(amount=10):
	try:
		for i in range(amount):
			img_response = get_image()
			save_image(img_response)

	except Exception as e:
		print("Some error occur: {}".format(e))
