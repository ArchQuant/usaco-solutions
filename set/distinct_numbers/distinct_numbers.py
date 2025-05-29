import sys
sys.stdin = open("input", "r")

n = int(input()) # unused

import random
RANDOM = random.randrange(2**62)

# IM - introduce random to speed up the set addition
def Wrapper(x):
    return x ^ RANDOM
arr = {Wrapper(int(i)) for i in input().split()}
print(len(arr))

'''
# IM - skip the list, directly add elem into a set
# but this still Exceeds Time Limit for worst-case hash collision to O(N^2)
# see below the hack Case Generator: https://usaco.guide/bronze/intro-sets?lang=py#solution---distinct-numbers
# poor input causes key collision and degrade the performance from O(1) to O(N)

arr = {int(i) for i in input().split()}
print(len(arr))
'''

import time

def anti_hash_hack(n: int, cpython: bool = False, for_set=False):
	"""
	Args:
	    integer n > 0
	    cpython: CPython or Pypy
	    for_set: set or dict
	Output: List A of length n
	such that 1 <= A[i] <= 2**(n.bit_length() + 2) + 10
	"""
	pow2 = 2 ** (n.bit_length() + 2)

	A = []

	def add_all(x):
		for i in range(10 if (cpython and for_set) else 1):
			A.append(x + i)

	add_all(pow2 + 1)
	i = 6 if cpython else 7
	while len(A) < n // 2:
		assert i > 0
		add_all(i)
		i = (5 * i + 1) % pow2

	while len(A) < n:
		A.append(1)

	return A


N = 200000
A = anti_hash_hack(N, False, False)

# https://cses.fi/problemset/task/1640/
print_test = False
if print_test:
	print(N, 1)
	print(" ".join(str(x) for x in A))

do_test = True
if do_test:
	print("Creating set:")
	start = time.time()
	set(A) # anti hash hack is fast when creating a hashmap
	print("Done", time.time() - start) # time: 0.006s

	print("Creating dict:")
	start = time.time()
	my_dict = {}
	for i in range(N):
		my_dict[A[i]] = i
	print("Done", time.time() - start) # time 0.033s