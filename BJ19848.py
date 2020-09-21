S = input()

s_length = S.length()

D = [0 for col in range(s_length)]
R = [0 for col in range(s_length)]

res = 0
index = 0
for i in S:
    res = res + 1 if i == 1 else res - 1
    D[index] = res
    index += 1

rev_res = 0
reverse_index = s_length - 1
for i in reversed(S):
    rev_res = rev_res + 1 if i == 1 else rev_res - 1
    R[reverse_index] = rev_res
    reverse_index -= 1

for i in range(s_length):
