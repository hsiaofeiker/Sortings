# Selection Sort...在數列中 找出最小. 然後 第一輪跟第1個交換, 第二輪跟第二個交換
# 所以n數走過 n 輪就會做完


numbers= [4,10,14,11,17,8,13,15,12,2,6,9]

def swap (numbers,n,m):
    tmp = numbers[n]
    numbers[n]=numbers[m]
    numbers[m]=tmp
    print(numbers)

numberLen=len(numbers)
print(numbers)

for n in range(numberLen-1):
    minNum=n
    for m in range(n+1,numberLen):
        if numbers[minNum]>numbers[m]:
            minNum=m
    if minNum!=n:
        print('Swap',n,minNum)
        swap(numbers,n,minNum)