'''
给你两个整数数组 nums1 和 nums2 ，请你以数组形式返回两数组的交集。
返回结果中每个元素出现的次数，应与元素在两个数组中都出现的次数一致（如果出现次数不一致，则考虑取较小值）。
可以不考虑输出结果的顺序。

示例 1：
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]

示例 2:
输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]

'''

def intersect(nums1: list, nums2: list) -> list:

        m = len(nums1)
        n = len(nums2)
        o = m > n
        hashMap = {}
        intersectionList = []
        
        #store hash map
        if o:
            for i in range(n):
                if str(nums2[i]) in hashMap:
                    hashMap[str(nums2[i])] += 1
                else:
                    hashMap[str(nums2[i])] = 1    
        else:
            for i in range(m):
                if str(nums1[i]) in hashMap:
                    hashMap[str(nums1[i])] += 1
                else:
                    hashMap[str(nums1[i])] = 1
        #read the hash map 
        if o:
            for i in range(m):
                    if str(nums1[i]) in hashMap:
                        if hashMap[str(nums1[i])] > 0:
                            intersectionList.append(nums1[i])
                            hashMap[str(nums1[i])] -=  1
                        
        else:
            for i in range(n):
                if str(nums2[i]) in hashMap:
                    if hashMap[str(nums2[i])] > 0:
                        intersectionList.append(nums2[i])
                        hashMap[str(nums2[i])] -=  1
                    
        
        return intersectionList