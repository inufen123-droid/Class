def bubble_sort(arr):   #第一題
    n = len(arr)
    # 外層迴圈控制需要執行多少輪
    for i in range(n):
        # 內層迴圈進行兩兩比較
        # 因為每一輪結束後，最大的數會被排到最後面，所以可以減少比較的次數 (- i)
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # 如果前面的比後面的大，就交換位置
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# 測試函數
arr = [5, 1, 4, 2, 8]
print(f"排序前的列表:{arr}")

sorted_arr = bubble_sort(arr)

print(f"排序後的列表: {sorted_arr}\n")  

#######第2題#######
def factorial(n):       
    # 終止條件：當 n 為 0 或 1 時，回傳 1
    if n <= 1:
        return 1
    # 遞歸呼叫：n 乘以 (n-1) 的階乘
    else:
        return n * factorial(n - 1)

# 測試函數並印出結果
result = factorial(5)
print(f"factorial(5) 的值是: {result}\n")

######第三題######
def min_coins(amount):
    # 面額由大到小排序
    denominations = [25, 10, 5, 1]
    all_selected_coins = []  # 用來存放所有被選中的硬幣

    for coin in denominations:
        # 當剩餘金額大於等於目前面額時，持續放入該硬幣
        while amount >= coin:
            all_selected_coins.append(coin)
            amount -= coin
        
    return all_selected_coins

# 測試金額 63
amount_to_change = 63
result_coins = min_coins(amount_to_change)

# 印出最終結果
print(f"硬幣總數：{len(result_coins)} 個")
print(f"選出的所有硬幣為：")
print(result_coins)
print()

######第四題######
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def dfs_search(node, target):
    # 基礎情況：如果節點為空，代表沒找到
    if node is None:
        return False
    
    # 如果當前節點值等於目標值，回傳 True
    if node.val == target:
        return True
    
    # 遞歸搜尋左子樹與右子樹
    # 只要其中一邊找到（or），就代表找到了
    return dfs_search(node.left, target) or dfs_search(node.right, target)

# 1. 建立樹狀結構
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)

# 2. 執行搜尋並印出結果
target_value = 7
if dfs_search(root, target_value):
    print("Found\n")
else:
    print("Not Found\n")

#####第五題######
from collections import deque

# --- 堆疊 (Stack): 後進先出 (LIFO) ---
stack = []
stack.append(10)  # 入棧
stack.append(20)  # 入棧
stack.pop()       # 出棧 (移除 20)
stack.append(30)  # 入棧
print(f"堆疊：{stack}")

# --- 佇列 (Queue): 先進先出 (FIFO) ---
queue = deque()
queue.append(10)  # 入隊
queue.append(20)  # 入隊
queue.popleft()   # 出隊 (移除 10)
queue.append(30)  # 入隊
print(f"佇列：{list(queue)}\n") # 轉回 list 格式以便與預期結果對照

#######第六題######
class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None  # 指向下一個節點的指標

def print_linked_list(head):
    current = head
    result = []
    # 遍歷鏈結串列，直到 current 變成 None
    while current:
        result.append(str(current.val))
        current = current.next  # 移動到下一個節點
    
    # 將所有值合併成字串並列印
    print(" ".join(result))

# 1. 建立節點
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

# 2. 串接節點 (1 -> 2 -> 3 -> 4)
node1.next = node2
node2.next = node3
node3.next = node4

# 3. 遍歷並列印
print_linked_list(node1)
print()


#######第七題######
import math

# 定義點的坐標
points = {
    'A': (1, 1),
    'B': (4, 4),
    'C': (6, 1)
}
P = (3, 2)

def calculate_distances(points, target):
    l1_results = {}
    l2_results = {}
    
    for name, coord in points.items():
        # L1 距離: |x1 - x2| + |y1 - y2|
        l1 = abs(coord[0] - target[0]) + abs(coord[1] - target[1])
        l1_results[name] = l1
        
        # L2 距離: sqrt((x1 - x2)^2 + (y1 - y2)^2)
        l2 = math.sqrt((coord[0] - target[0])**2 + (coord[1] - target[1])**2)
        l2_results[name] = round(l2, 2) # 四捨五入到小數點後兩位
        
    return l1_results, l2_results

# 執行計算
l1_dist, l2_dist = calculate_distances(points, P)

# 找出最近鄰 (距離最小者)
nearest_l1 = min(l1_dist, key=l1_dist.get)
nearest_l2 = min(l2_dist, key=l2_dist.get)

# 印出結果
print(f"P點座標為:{P},ABC的座標為:{points}")
print(f"L1 距離(曼哈頓): {l1_dist}")
print(f"L1 度量下的最近鄰: {nearest_l1}")
print(f"L2 距離(歐式): {l2_dist}")
print(f"L2 度量下的最近鄰: {nearest_l2}")