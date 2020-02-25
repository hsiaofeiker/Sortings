#        [   4  10  14  11  17   8  13  15  12   2   6   9]
# 這好像是種變種的 quick Sort寫法..
# 第一步 把最右邊的 9放入 pivot, 接下來可以看成這樣 11位置 空出來
#        [   4  10  14  11  17   8  13  15  12   2   6    ?]
#                i--------------------------------------->
#        [   4   ?  14  11  17   8  13  15  12   2   6   10]
#                <-----------------------------------j
#        [   4   6  14  11  17   8  13  15  12   2   ?   10]
#                    i------------------------------>
#        [   4   6   ?  11  17   8  13  15  12   2   14  10]
#                     <--------------------------j
#        [   4   6   2  11  17   8  13  15  12   ?   14  10]
#                        i---------------------->
#        [   4   6   2   ?  17   8  13  15  12   11  14  10]
#                         <------j
#        [   4   6   2   8  17  ?   13  15  12   ?   14  10]
#                            i->
#        [   4   6   2   8  ?  17  13   15  12   11  14  10]
#                           p
#        [   4   6   2   8  9  17  13   15  12   11  14  10]
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
        print(tmpList[high],tmpList[low], ' 準備做 low copy 到 high')
        tmpList[high] = tmpList[low]
        print(tmpList[high], tmpList[low], ' 做完')
        print(tmpList,'<--1')
        # pivot 設定在最尾,這段必須後寫, 若 pivot 設在最頭,則此段先寫
        while low < high and tmpList[high] >= pivot:
            high -= 1
        print(tmpList[high], tmpList[low], ' 準備做 high copy 到 low')
        tmpList[low] = tmpList[high]
        print(tmpList[high], tmpList[low], ' 做完')
        print(tmpList,'<--2')
    print('位置',low,rgt, '對調,  已完成位置:',low)
    tmpList[low] = pivot

    quick_Sort(tmpList, lft, low-1)
    quick_Sort(tmpList, low+1, rgt)

numbers= [4,10,14,11,17,8,13,15,12,2,6,9]
#numbers= [11,10,9,8,7,6,5,4,3,2,1,0]

print(numbers,'<--原始')
quick_Sort(numbers,0,len(numbers)-1)
print(numbers,'<--emd')