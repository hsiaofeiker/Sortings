#Bucket Sort 本身不是個 Sort 的演算法, 它是一個處理的概念.
#將 數組 放到 從小到大的 n 個不同的籃子, 然後再對每個籃子內做 Sort, 可用 selection Sort 比較快
#要將數字從小到大先找到最大跟最小值, 從中分幾個籃
#[4,10,14,11,17,8,13,15,12,2,6,9] 最小是2, 最大是17, 共12 , 若我們分成3籃 (17-2)/3=5, 2~6,7~12,13~17
#[4,2,6],[10,11,8,12,9],[14,17,13,15] , 再依這3籃,進行排序
#square root Buckets by using selection Sort 這是挑戰最快排序法
#假設 n有10個數.分0~100籃 分10個籃,
#沒寫完, 我之前是用 幾個數的總數開耕號, 但事實上好像要用數字的大小開耕號來分幾籃
#log(n)=4, nlog(n)=40000, n^n = 100000000
#我預估 我的速度是 100籃*(50數x50)= 250000

#這程式的特點是用 動態的 Array 2D[][]來處理 , 再針對每個[] 來做 Selection sort

import math

def swap (numbers,n,m):
    tmp = numbers[n]
    numbers[n]=numbers[m]
    numbers[m]=tmp
    #print(numbers)

numbers= [4,10,14,11,17,8,13,15,12,2,6,9]
#numbers= [26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2]
#numbers= [27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3 ]
maxN=max(numbers)   #得到數列中的最大值
minN=min(numbers)   #得到數列中的最小值
bucketsN=round(math.sqrt(len(numbers))) #依照 開耕號的方式後4捨5入 來算出 需要幾個籃子
baseN=(maxN-minN+1)/bucketsN            #下個籃子離這個籃子的距離, 也就是 每個籃子有多寬

print('原數組:', numbers)

print('數組長度:',len(numbers),'    裝幾個籃:',bucketsN,'   最小值:',minN,'   最大值:',maxN,'  最大最小差:',maxN-minN,'  每籃距離',baseN)
outter=[]
print('分組規則:')
for n in range(bucketsN):  #建例n個籃子
    print('        ',n,'籃  Begin:',minN+n*baseN,'~',minN+(n+1)*baseN)
    outter.append([])
print('起始 有',bucketsN,'個空籃:',outter)

for n in range(len(numbers)):
    buckets=math.floor((numbers[n]-minN)/baseN) #第n個數 的值,是歸於 哪個籃
    outter[buckets].append(numbers[n])  #放入相對應的籃子
print('各籃狀況:',outter)
print()


print('每籃各自做 selection sort')
for i in range(len(outter)):    #做n籃
    numberLen = len(outter[i])  #每籃中 有幾個數
    #print(numberLen,outter[i])

    # for n in range(numberLen-1):                       #原始版
    for n in range(int(numberLen / 2)):                     # 加強版 是selection sort,一次排好2個,最小在最左,最大在最右
        minNum = n
        maxNum = n                                          # 加強版 預設最大值
        #print('search range:', n + 1, '~', numberLen - n - 1)
        # if n != numberLen-n-1:
        for m in range(n + 1, numberLen - n):
            if outter[i][minNum] > outter[i][m]:
                minNum = m
            if outter[i][maxNum] < outter[i][m]:            # 加強版
                maxNum = m                                  # 加強版,找最大值的位置

        if minNum != n:
            #print('Min Swap', n, minNum)
            swap(outter[i], n, minNum)  #把最小的換到最左
        # print('n&M:',n,m)
        if maxNum != n:                                     # 加強版
            #print('Max Swap', numberLen - n - 1, maxNum)    # 加強版
            swap(outter[i], numberLen - n - 1, maxNum)      # 加強版,把最大的換到最右

print('排序完:',outter)
