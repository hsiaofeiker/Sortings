# Selection Sort...在數列中 找出最小. 走一遍,找出 最小值交換, 第二遍,找次小值...
# 所以n個數 就會走n遍, 速度上是 O(n^2), 空間上 沒額外使用空間
# 加強版 是一次就找到 最小跟最大...一次就先搞定 最小跟最大的2邊,再來 次小 次大...
#numbers= [4,10,14,11,17,8,13,15,12,2,6,9]
#numbers= [4,10,14,11,17,8,13,15,12,2,6]
numbers= [17,16,8]
def swap (numbers,n,m):
    tmp = numbers[n]
    numbers[n]=numbers[m]
    numbers[m]=tmp
    print(numbers)

numberLen=len(numbers)
print('Selection Sort 是排序中 前幾名快的')
print('若有100個數,   速度是 100x100 = 10000')
print('加強版,速度加倍 是 100x(100/2) = 5000')
print('原始:',numbers)
print('Begin:')

#for n in range(numberLen-1):                       #原始版
for n in range(int(numberLen/2)):                   #加強版
    minNum=n
    maxNum=n                                        #加強版
    print('search range:',n+1,'~',numberLen-n-1)
    #if n != numberLen-n-1:
    for m in range(n+1,numberLen-n):
        if numbers[minNum]>numbers[m]:
            minNum=m
        if numbers[maxNum]<numbers[m]:          #加強版
            maxNum=m                            #加強版

    if minNum!=n:
        print('Min Swap',n,minNum)
        swap(numbers,n,minNum)
    #print('n&M:',n,m)
    if maxNum!=n:                               #加強版
        print('Max Swap',numberLen-n-1,maxNum) #加強版
        swap(numbers,numberLen-n-1,maxNum)      #加強版
    print('     ', numbers)