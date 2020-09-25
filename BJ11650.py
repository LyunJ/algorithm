import sys
sys.setrecursionlimit(100000)


def partition(lists, left, right, plist):
    pivot = lists[left]
    leftCache = left
    left = left + 1
    isLeftStop = False
    isRightStop = False
    while left < right:
        if pivot >= lists[left]:
            left += 1
        else:
            isLeftStop = True
        if pivot <= lists[right]:
            right -= 1
        else:
            isRightStop = True

        if isLeftStop and isRightStop:
            lists[left], lists[right] = lists[right], lists[left]
            plist[left], plist[right] = plist[right], plist[left]
            isLeftStop = False
            isRightStop = False

    if lists[leftCache] > lists[left]:
        lists[leftCache], lists[left] = lists[left], lists[leftCache]
        plist[leftCache], plist[left] = plist[left], plist[leftCache]
    return left


def quickSort(lists, start, end, plist):
    if start < end:
        pivot = partition(lists, start, end, plist)
        quickSort(lists, start, pivot - 1, plist)
        quickSort(lists, pivot + 1, end, plist)


amount = int(input())

x = []
y = []

for i in range(amount):
    a, b = input().split()
    x.append(int(a))
    y.append(int(b))

quickSort(x, 0, amount - 1, y)

temp = x[0]
count = 1
for i in range(1, amount):
    if temp == x[i]:
        count += 1
        if i == (amount - 1) and count > 1:
            quickSort(y, i - count + 1, i, x)
    else:
        if count > 1:
            quickSort(y, i - count, i - 1, x)
        temp = x[i]
        count = 1

for i in range(amount):
    print(x[i], y[i])


# N = int(input())
# nums = []
# for i in range(N):
#     [a, b] = map(int, input().split())
#     nums.append([a, b])
# nums = sorted(nums)
# for i in range(N):
#     print(nums[i][0], nums[i][1])
