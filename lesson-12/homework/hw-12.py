import threading
import math

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    limit = int(math.isqrt(n))
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True

def _worker(nums, out_list, lock):
    local_primes = [n for n in nums if is_prime(n)]
    if local_primes:
        with lock:
            out_list.extend(local_primes)

def threaded_prime_range(start: int, end: int, num_threads: int = 4):
    if start > end:
        start, end = end, start
    num_threads = max(1, int(num_threads))
    all_numbers = list(range(start, end + 1))
    # split roughly evenly
    chunk_size = (len(all_numbers) + num_threads - 1) // num_threads
    chunks = [all_numbers[i:i + chunk_size] for i in range(0, len(all_numbers), chunk_size)]

    threads = []
    results = []
    lock = threading.Lock()

    for chunk in chunks:
        t = threading.Thread(target=_worker, args=(chunk, results, lock))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    return sorted(results)

# Example usage
if __name__ == "__main__":
    # modify these values or prompt the user as needed
    start = 1
    end = 200
    num_threads = 8

    primes = threaded_prime_range(start, end, num_threads)
    print(f"Primes in range [{start}, {end}] (found with {num_threads} threads):")
    print(primes)



# ---------------------------------------------
# Exercise 2: Threaded File Processing
#
# This cell implements a threaded solution to count word occurrences
# in a text file. It splits the file by lines across threads, each
# thread computes a local Counter which is then aggregated.
# ---------------------------------------------

from collections import Counter
import re
import os

def _word_count_worker(lines_chunk, results, lock, thread_index=None):
	"""Worker to count words in a chunk of lines."""
	local_counter = Counter()
	word_re = re.compile(r"\w+", flags=re.UNICODE)
	for line in lines_chunk:
		words = word_re.findall(line.lower())
		if words:
			local_counter.update(words)
	# append local result under lock
	with lock:
		results.append(local_counter)

def threaded_word_count(filepath: str, num_threads: int = None):
	"""
	Count words in `filepath` using `num_threads` threads.
	If num_threads is None, it will try to use the notebook variable `num_threads`
	if available, otherwise defaults to 4.
	Returns a collections.Counter with aggregated word counts.
	"""
	# honor notebook-level num_threads if provided
	if num_threads is None:
		num_threads = globals().get('num_threads', 4)
	num_threads = max(1, int(num_threads))

	if not os.path.exists(filepath):
		raise FileNotFoundError(f"File not found: {filepath}")

	# read all lines once
	with open(filepath, "r", encoding="utf-8") as f:
		lines = f.readlines()

	if not lines:
		return Counter()

	# split lines into roughly equal chunks
	chunk_size = (len(lines) + num_threads - 1) // num_threads
	chunks = [lines[i:i + chunk_size] for i in range(0, len(lines), chunk_size)]

	results = []
	lock = threading.Lock()
	threads = []

	for i, chunk in enumerate(chunks):
		t = threading.Thread(target=_word_count_worker, args=(chunk, results, lock, i))
		t.start()
		threads.append(t)

	for t in threads:
		t.join()

	# aggregate results
	total = Counter()
	for c in results:
		total.update(c)

	return total

# Example usage: create a sample file if not present and run the threaded counter.
sample_file = "sample_text.txt"
if not os.path.exists(sample_file):
	sample_lines = [
		"This is a sample line with some words.\n",
		"Some words appear more than once: sample sample words.\n",
		"Threaded processing of text files is useful.\n",
		"This example repeats lines to simulate a larger file.\n",
	]
	# write many times to simulate larger file
	with open(sample_file, "w", encoding="utf-8") as f:
		for _ in range(500):  # ~2000 lines
			f.writelines(sample_lines)

# Use notebook-level `num_threads` if present, else default inside function.
try:
	counts = threaded_word_count(sample_file)
	# print top 20 most common words
	print("Top 20 words:")
	for word, cnt in counts.most_common(20):
		print(f"{word}: {cnt}")
except Exception as e:
	print(f"Error running threaded_word_count: {e}")
