# 第一個練習寫的 Python程式 2020 Feb 20

# bubble Sort 是 每次相臨的2格 Array 做比較,1號位跟2號位比,2號位跟3號位比, 若是大於,就交換..
# 第一次的 iteration 比5次,第二次的 iteration 比4次,第三次的 iteration 比3次..
# 因此每一次 iteration(最大的迴圈),都能確定 最大值在同一個iteration範圍中會被排到最右.

def sort(nums):
    for i in range(len(nums)-1, 0,-1):  # 範圍從 Array nums的長度-1 到 0, 每次跳-1,
        print("前", i+1 , "個數比", i , "次")
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
            print(nums)
        print("確認最大數在第",i+1,"位")
        print()
# Python 中 # 是註解
# def 是副程式
# range(a,b,c) -> a:起始,b:結束,c:每次跳多少  , range(10)->a省略值為0, c省略值為1
# len(nums) -> Array nums 長度.
# print('good', end='.') -> 表示印出good.換行在句點後
# print("a",' b',' c') -> output = a b c
# print("a",' b',' c',sep = '/') -> output = a/ b/ c


numbers= [4,10,14,11,17,8,13,15,12,2,6,9]
sort(numbers)

print(numbers,"<- 最後排完的樣子")