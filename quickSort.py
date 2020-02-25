#內部小迴圈
#012345  ---> 極端狀況1  p最大, i一直往右,最後i與p同位置,處置?
#543210  ---> 極端狀況2  p最小, j一直往左,最後j與i交叉,處置?
#23   ---> 極端狀況3  i,j同位, p比ij大,處置?
#32   ---> 極端狀況4  i,j同位, p比ij小,處置?
#一般狀況 --> 找到i比p大,找到j比p小,對調..繼續做,直到ji 交叉,對調ip或是 j+1跟p對調
#012356784 -> i跑到5,j跑到3,交叉,對調ip或是 j+1跟p對調

#[   4  10  14  11  17   8  13  15  12   2   6   9]
def quick_Sort(tmpList,lft,rgt):
    print(tmpList,'  處理', lft,' ~ ', rgt,' <-new ')
    if lft>=rgt:
        return
    pivot = tmpList[rgt] # pivot 設定在最尾,若想改成設在最頭,則=tmpList[lft]
    low = lft
    high = rgt
    while low< high:
        # pivot 設定在最尾,這段必須先寫, 若 pivot 設在最頭,則此段後寫
        while low <high and tmpList[low] < pivot:
            low += 1
        print(tmpList[high],tmpList[low], ' before1')
        tmpList[high] = tmpList[low]
        print(tmpList[high], tmpList[low], '   after1')
        print(tmpList,'<--1')
        # pivot 設定在最尾,這段必須後寫, 若 pivot 設在最頭,則此段先寫
        while low < high and tmpList[high] >= pivot:
            high -= 1
        print(tmpList[high], tmpList[low], ' before2')
        tmpList[low] = tmpList[high]
        print(tmpList[high], tmpList[low], '   after2')
        print(tmpList,'<--2')
    print('位置',low,rgt, '對調,  已完成位置:',low)
    tmpList[low] = pivot

    quick_Sort(tmpList, lft, low-1)
    quick_Sort(tmpList, low+1, rgt)

numbers= [4,10,14,11,17,8,13,15,12,2,6,9]

print(numbers,'<--原始')
quick_Sort(numbers,0,len(numbers)-1)
print(numbers,'<--emd')