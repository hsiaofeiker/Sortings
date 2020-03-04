# Selection Sort...在數列中 找出最小. 走一遍,找出 最小值交換, 第二遍,找次小值...
# 所以n個數 就會走n遍, 速度上是 O(n^2), 空間上 沒額外使用空間

numbers= [4,10,14,11,17,8,13,15,12,2,6,9]

def swap (numbers,n,m):
    tmp = numbers[n]
    numbers[n]=numbers[m]
    numbers[m]=tmp
    print('     ',numbers)

numberLen=len(numbers)
print('原始:',numbers)

for n in range(int(numberLen/2)):
    minNum=n
    maxNum=n
    for m in range(n+1,numberLen):
        if numbers[minNum]>numbers[m]:
            minNum=m
    if minNum!=n:
        print('Min Swap',n,minNum)
        swap(numbers,n,minNum)
