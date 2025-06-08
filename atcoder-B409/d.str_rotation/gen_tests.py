
import random
import string

n = 10
with open('input', 'a') as f:
    print(n, file=f)
    for i in range(n):
        length = random.randint(1, 100)
        print(length, file=f)
        rand_str = ''.join(random.choices(string.ascii_lowercase, k=length))
        print(rand_str, file=f)