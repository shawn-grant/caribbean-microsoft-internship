

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# REVERSE A LIST
def reverseList(arr):
    i, size = 0, len(arr)
    
    while(i < size//2):
        arr[i], arr[size-i-1] = arr[size-i-1], arr[i]
        i += 1

    return arr

# REVERSE A LINKED LIST
def reverseList(head: ListNode) -> ListNode:
    cur_node = head
    new_list = None

    while cur_node:
        # keep link to original
        next = cur_node.next
        # point next node to new list head
        cur_node.next = new_list
        new_list = cur_node
        # mov down original list
        cur_node = next

    return new_list

# CHECK IF A LINKED LIST IS A PALINDROME
def isPalindrome(head: [ListNode]) -> bool:
    arr = []
    while head != None:
        arr.append(head.val)
        head = head.next

    # check reverse
    i = 0
    while i < len(arr) // 2:
        if arr[i] != arr[len(arr)-i-1]:
            return False
        i += 1
    
    return True

# TWO SUM
def twoSum(nums: [int], target: int) -> [int]:
    nums_index = {}
    output = []
    
    for i in range(len(nums)):
        val = nums[i]
        dif = (target - val)
        
        if dif in nums_index:
            output = [i, nums_index[dif]]
            return output
        else:
            nums_index[val] = i
        
    return []

# TREE TRAVERSAL (DFS)
def dfs(root):
    if root:
        # condition checks
        print(root.val)
        dfs(root.left)
        dfs(root.right)

# LEAF NODES (DFS)
def getLeafs(root):
    leafs = []
    if root:
        if not root.left and not root.right:
            leafs.append(root.val)
        else:
            getLeafs(root.left)
            getLeafs(root.right)
    print(leafs)

# Build Tree from Preorder and Inorder Traversal
def buildTree(self, preorder: [int], inorder: [int]) -> TreeNode:
    if len(inorder) > 0:
        # find root in inorder
        root_index = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[root_index])

        # find L and R subtree
        left_tree = inorder[:root_index]
        right_tree = inorder[root_index + 1: len(inorder)]

        root.left = self.buildTree(preorder, left_tree)
        root.right = self.buildTree(preorder, right_tree)

        return root

# move zeroes to the start, ones to the end
#  for an array of 1s and zeroes only
def moveOnesAndZeroes(arr):
    left = 0  # Pointer starting from the beginning of the array
    right = len(arr) - 1  # Pointer starting from the end of the array

    # Move left pointer until it finds a non-zero element
    while arr[left] == 0 and left < right:
        left += 1
    
    # Move right pointer until it finds a non-one element
    while arr[right] == 1 and left < right:
        right -= 1
    
    if left < right:
        # Swap the elements at left and right pointers
        arr[left], arr[right] = arr[right], arr[left]
        left += 1  # Move the left pointer to the next position
        right -= 1  # Move the right pointer to the previous position

# move zeroes to the end of array
def moveZeroes(nums: [int]) -> None:
    right = 0
    
    for left in range(len(nums)):
        if nums[left] != 0:
            # Swap the elements at left and right pointers
            nums[left], nums[right] = nums[right], nums[left]
            right += 1
    
# palindrome numbers
def isPalindrome(self, x: int) -> bool:
    original, reverse = x, 0

    # nevatives will never be palindromes
    if x < 0:
        return False
    
    # reverse the number
    while x > 0:
        reverse = (reverse * 10) + (x % 10)
        x //= 10

    # compare reversed version and original number
    return reverse == original

# longest substring without repeating characters
def lengthOfLongestSubstring(self, s: str) -> int:
    cur_len = 0
    for i in range(len(s)):
        visited = [s[i]]
        
        for j in range(i+1, len(s)):
            if s[j] in visited:
                break
            visited.append(s[j])

        if len(visited) > cur_len:
            cur_len = len(visited)

    return cur_len
    
# remove duplicates from sorted array
def removeElement(self, nums: List[int], val: int) -> int:
    writer = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[writer] = nums[i]
            writer += 1
    
    return writer

# NUMBER OF ISLANDS
def numIslands(self, grid: List[List[str]]) -> int:
    num_islands = 0
    visited = set()
    
    def search(i, j):
        visited.add((i, j))
        directions = [
            [i, j + 1],
            [i, j - 1],
            [i + 1, j],
            [i - 1, j]
        ]

        for x, y in directions:
            if x not in range(len(grid)) or y not in range(len(grid[0])):
                continue
            if grid[x][y] == '1' and (x, y) not in visited:
                search(x, y)
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '1' and (i, j) not in visited:
                # search
                search(i, j)
                num_islands += 1

    return num_islands

#  length of last word
def lengthOfLastWord(s: str) -> int:
    non_spaces = 0
    for i in range(len(s)-1, -1, -1):
        if s[i] != " ":
            non_spaces += 1

        if s[i] == " " and non_spaces > 0:
            break

    return non_spaces


# MAIN
# print(twoSum([2,7,11,15], 9))
# dfs(root)
# leafs(root)