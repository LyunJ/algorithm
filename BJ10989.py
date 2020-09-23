#야매(근데 백준에선 이렇게 해야됨)
import sys

N = int(input())

count = [0 for i in range(10000)]
max = 0
for i in range(N):
    nums = int(sys.stdin.readline()) #input()보다 sys.stdin.readline()이 읽는 속도가 더 빠름
    count[nums - 1] += 1
    if max < nums:
        max = nums

for i in range(max):
    if count[i] != 0:
        plusOne = i + 1
        countNum = count[i]
        for j in range(countNum):
            print(plusOne)



#카운팅 정렬 정석
# N = int(input())

# lists = [0 for i in range(N)]

# max = 0
# for i in range(N):
#     lists[i] = int(input())
#     if max < lists[i]:
#         max = lists[i]
# count = [0 for i in range(max)]
# for i in lists:
#     count[i - 1] += 1

# sum = [0 for i in range(max)]
# check = 0
# for i in range(max):
#     if count[i] != 0:
#         sum[i] = check + count[i]
#         check = sum[i]
#     else:
#         sum[i] = 0

# results = [0 for i in range(N)]
# for i in lists:
#     results[sum[i - 1] - 1] = i
#     sum[i - 1] -= 1

# for i in results:
#     print(i)
