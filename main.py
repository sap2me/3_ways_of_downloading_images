from time import time

from sync_way import dowload_images_sync
from threading_way import dowload_images_threading
from async_way import dowload_images_async


def timeit(func, times=3, args=(), kwargs={}):

	total_time = 0

	print('-' * 80)
	for i in range(1, times + 1):
		print("Function '{}' started {} time".format(func.__name__, i))
		start_time = time()
		func(*args, **kwargs)
		diff_time = time() - start_time
		total_time += diff_time
		print("Function '{}' finished {} time in {} secs".format(func.__name__, i, diff_time))

	print("{} tests finished in {}".format(times, total_time))
	print("Average time is {} secs".format(total_time / times))
	print('-' * 80)
	print()


if __name__ == '__main__':

	# Testing all methods of downloading images

	images_amount = 10

	timeit(dowload_images_sync, kwargs={"amount": images_amount})
	timeit(dowload_images_threading, kwargs={"amount": images_amount})
	timeit(dowload_images_async, kwargs={"amount": images_amount})