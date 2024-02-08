import itertools


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


# print(generateParenthesis(4))


def HaidyTrainAssignment(numTrains, bookings, booklen):

    inputList = []
    for i in range(bookings):
        # inputList = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
        inputList.append(list(map(int, input().split(' '))))

    outputlist = [10000]*numTrains  # [10000, 10000, 10000, 10000, 10000] price
    trainList = list(range(1, numTrains+1))  # [1, 2, 3, 4, 5]
    for outer in inputList:
        (start, end, value) = (outer)
        for i in trainList:
            if i in range(start, end+1):
                outputlist[i-1] -= value

    return outputlist
# print(HaidyTrainAssignment(4, 5, 3))


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


def seiveOfEratosthenes(num):
    '''
    prints all prime number till the given number
      '''
    prime_arr = [True]*(num+1)

    if num < 2:
        raise Exception("No prime number exists")

    p = 2
    while p*p <= num:
        if prime_arr[p]:
            for j in range(p*p, num+1, p):
                prime_arr[j] = False
        p += 1
    for p in range(2, num+1):
        if prime_arr[p]:
            print(p)


# print(seiveOfEratosthenes(11))

def minSubarrayCount(arr, val):
    left = right = 0
    count = float('inf')
    if len(arr) <= 1 and arr[0] != val:
        return "Invalid array"
    while left <= right and right < len(arr):
        cursum = sum(arr[left:right+1])
        if cursum >= val:
            count = min(count, right-left+1)
            left += 1
        else:
            right += 1
    return count


arr = [1]
# print(minSubarrayCount(arr, val=15))


def maxLengthBetweenEqualCharacters(s: str) -> int:

    maxlen = curr = -1
    if len(s) <= 1:
        return -1
    for left in range(0, len(s)-1):
        for right in range(left+1, len(s)):
            if s[left] == s[right]:
                curr = (right-left)-1
        maxlen = max(curr, maxlen)
    return maxlen


# s = "aa"
# print(maxLengthBetweenEqualCharacters(s))

def findMatrix(nums):  # leet -2610 :Convert an Array Into a 2D Array With Conditions

    def helper(nums, output):
        if len(nums) == 0:
            return output
        else:
            hashset = set()
            # Deep  copy [any changes made to a copy of the object do not reflect in the original object]
            arr = nums.copy()
            for ele in nums:
                if ele not in hashset:
                    hashset.add(ele)
                    arr.remove(ele)
            output.append(list(hashset))
            return helper(arr, output)
    return helper(nums, output=[])


# print(findMatrix([1, 3, 4, 1, 2, 3, 1]))


def gcd_Two(a, b):
    gcd = 1
    # if u want large range iter = itertools.zip_longest
    for i, j in zip(range(1, a+1), range(1, b+1)):
        if a % i == 0 and b % j == 0:
            gcd = i
    return gcd


print(gcd_Two(3, 7))


def findDuplicate(arr):
    num = 1
    for ele in arr:
        num = num ^ ele  # num ^ num =0  / num ^ 1 =num
    return num


# print(findDuplicate([2, 1, 5, 3, 4, 5]))

# leetcode :  2125. Number of Laser Beams in a Bank
def numberOfBeams(bank: List[str]) -> int:
    lasercount = []
    for floor in bank:
        val = floor.count("1")
        if val > 0:  # ignre 0 ease of multiplication
            lasercount.append(val)  # [3, 2, 1]

    # try sliding windwow k=2
    ans = 0
    for idx in range(0, len(lasercount)-1):
        ans += lasercount[idx]*lasercount[idx+1]  # ans = [3*2]+[2*1]
    return ans


print(numberOfBeams([]))
