import sys
sys.stdin = open("input", "r")


T = input()
U = input()

i = 0
# IM - directly set constrain for i, not checking lenT-i < lenU each time
# IM - use "<=" to include lenT-lenU, not "<"
while i <= len(T) - len(U):
    # check if i-starting str is valid for all char in U, a sub-task, i remains the same.
    # IM - Inner loop shouldn't use two separate pointers cur_i/cur_j for a co-linear scan,
    # because start/end is fixed, there is no back and forth, or skipping.
    # Thus should use *For Loop*, and use j and i+j (i stays the same)
    if all(T[i+j] == U[j] or T[i+j] == '?' for j in range(len(U))):
        print("Yes")
        exit()
    i += 1

print("No")


'''
Example input/output:

tak??a?h?
nashi
Yes

??e??e
snuke
No
'''

'''TOO VERBOSE BELOW

i = j = 0
ni, nj= len(t), len(u)

while i < ni and j < nj:
  print(f"i = {i}, j={j}")
  if ni - i < nj - j:
    print("No")
    exit()
  cur_i, cur_j = i, j
  while cur_i < ni and cur_j < nj:
    if t[cur_i] == u[cur_j] or t[cur_i] == '?':
      cur_i += 1
      cur_j += 1
    else:
      i += 1
      j = 0
      break
  if cur_j == nj:
    print("Yes")
    exit()

if j == nj:
  print("Yes")
else:
  print("No")
  
  '''