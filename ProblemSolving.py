def generateParenthesis(n):
    def dfs(open, close, outputStr):
        if len(outputStr) == n*2:
            outputList.append(outputStr)
            print("Return")
            return
        if open < n:
            dfs(open+1, close, outputStr+'(')
        if close < open:
            dfs(open, close+1, outputStr+')')

    outputList = []
    dfs(0, 0, "")
    return outputList
# print(generateParenthesis(2))


def Solve(numTrains, bookings, booklen):

    inputList = []
    for i in range(bookings):
        # inputList = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
        inputList.append(list(map(int, input().split(' '))))

    outputlist = [10000]*numTrains  # [10000, 10000, 10000, 10000, 10000]
    trainList = list(range(1, numTrains+1))  # [1, 2, 3, 4, 5]
    for outer in inputList:
        start = outer[0]
        end = outer[1]
        value = outer[2]
        for i in trainList:
            if i in range(start, end+1):
                outputlist[i-1] -= value

    return outputlist
# print(Solve(4, 5, 3))


def duplicateIndex(str):
    for ele in str:
        if str.index(ele) == str.rindex(ele):
            return str.index(ele)
    else:
        return -1
# print(duplicateIndex('abcda'))


def binarySearch(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = left+(right-left)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid+1
        else:
            right = mid-1
    return "not found"
# print(binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9,22, 23, 24, 25, 26, 27, 55, 66, 67], 25))


def binarySearchRecursive(arr, left, right, target):
    if left <= right:
        mid = left+(right-left)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binarySearchRecursive(arr, mid+1, right, target)
        else:
            return binarySearchRecursive(arr, left, mid-1, target)
    else:
        return -1
# arr = [1, 2, 3, 4, 5]
# left, right = 0, len(arr)-1
# target = 5
# print(binarySearchRecursive(arr, left, right, target))


def lengthOfLongestSubstring(s: str) -> int:
    seen = {}
    left = 0
    maxlen = 0
    for right in range(len(s)):
        char = s[right]
        if char in seen and seen[char] >= left:
            left = seen[char]+1
        else:
            maxlen = max(maxlen, right-left+1)
        seen[char] = right
    return maxlen
# print(lengthOfLongestSubstring("abcabcbb"))
    """for key, val in hashmap.items():
        print(key, '', val)
        if val > maxval:
            maxval = val"""


def majorityElement(nums):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
            count += 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    return candidate

# print(majorityElement(nums=[1, 2, 3, 4, 1, 4]))
