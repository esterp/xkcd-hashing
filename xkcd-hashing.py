#!/usr/bin/env python3
import multiprocessing, signal, time, skein, gmpy, random, string, urllib.request, urllib.parse

TARGET = '5b4da95f5fa08280fc9879df44f418c8f9f12ba424b7757de02bbdfbae0d4c4fd' + \
	'f9317c80cc5fe04c6429073466cf29706b8c25999ddd2f6540d4475cc977b87f4757be' + \
	'023f19b8f4035d7722886b78869826de916a79cf9c94cc79cd4347d24b567aa3e2390' + \
	'a573a373a48a5e676640c79cc70197e1c5e7f902fb53ca1858b6'

TARGET = gmpy.mpz(TARGET, 16)

RANDOM_BIT_LEN = 512

def init_worker():
	signal.signal(signal.SIGINT, signal.SIG_IGN)

def submit(word):
	url = "http://almamater.xkcd.com/?edu=mit.edu"
	data = urllib.parse.urlencode({'hashable': word})
	binarydata = data.encode('ascii')
	urllib.request.urlopen(url, binarydata)
	
def run_worker(do_submit=True, time_limit=None):
	best = float('inf')
	guess = random.getrandbits(RANDOM_BIT_LEN)
	t = time.time()
	i = 0
	while True:
		encoded = gmpy.digits(guess, 62).encode('ascii')
		digest = gmpy.mpz(skein.skein1024(encoded).digest()[::-1] + b'\0', 256)
		diff = gmpy.hamdist(digest, TARGET)
		if diff < best:
			best = diff
			if do_submit:
				submit(guess)
			print('Found new best input with diff [%.3d]: \"%s\"' %
				(diff, guess))
		i += 1
		if time_limit and time.time() - t > time_limit:
			break
		guess += 1
	return i

def main():
	run_worker()
	cpus = multiprocessing.cpu_count()
	pool = multiprocessing.Pool(cpus, init_worker)
	for i in range(cpus):
		pool.apply_async(run_worker)
	try:
		while True:
			time.sleep(100)
	except KeyboardInterrupt:
		print('Terminating...')
		pool.terminate()
		pool.join()
	else:
		print('Quitting...')
		pool.close()
		pool.join()

if __name__ == '__main__':
	import sys
	if len(sys.argv) > 1 and sys.argv[1] == 'time':
		iters = run_worker(do_submit=False, time_limit=1)
		print('Processed', iters, 'guesses in 1 second')
	else:
		main()
