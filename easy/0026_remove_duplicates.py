#26. 删除有序数组中的重复项
#给你一个 非严格递增排列的数组 nums ，请你原地删除重复出现的元素，使每个元素只出现一次 ，返回删除后数组的新长度。元素的相对顺序应该保持一致 。然后返回 nums 中唯一元素的个数。
#考虑 nums 的唯一元素的数量为 k。去重后，返回唯一元素的数量 k。
#nums 的前 k 个元素应包含 排序后 的唯一数字。下标 k - 1 之后的剩余元素可以忽略。

def removeDuplicates(nums):
    if not nums:
        return 0
        #如果数组为空（长度0），直接返回0（新长度为0）not nums 是Python判断列表空的方式
    write_index = 1
    #初始化一个“写指针” write_index = 1，意思：从第1位（下标1）开始写不重复的数，为什么从1开始？因为第0位肯定保留（第一个数不可能重复）
    for i in range(1, len(nums)):
        #从下标1开始遍历整个数组（i是“读指针”），range(1, len(nums))：从1到数组长度-1，为什么从1开始？因为我们要和前一个数比较
        if nums[i] != nums[i-1]:
            #如果当前数 nums[i] 和前一个数 nums[i-1] 不一样，说明这是一个新的不重复数，要保留！
            nums[write_index] = nums[i]
            #把这个新数“写”到 write_index 的位置，直接覆盖原数组（题目允许原地修改）
            write_index += 1
            #写完后，写指针往右移一位，准备放下一个新数
    return write_index
    #遍历完后，write_index 就是不重复数的个数（新长度），返回它，LeetCode会用前write_index个元素判断正确性