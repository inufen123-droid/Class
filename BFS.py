from collections import deque
import time  # 1. 引入時間模組

def bfs(graph, start_node):
    # 紀錄開始時間（使用效能更好的 perf_counter）
    start_time = time.perf_counter()
    
    visited = set()
    queue = deque([start_node])
    visited.add(start_node)
    order_of_visit = []
    
    print("\n--- 🔍 BFS 詳細走訪過程開始 ---")
    step = 1
    
    while queue:
        # 印出當前佇列的狀態
        print(f"【步驟 {step}】")
        print(f"  當前佇列 (Queue): {list(queue)}")
        
        current_node = queue.popleft()
        print(f"  👉 彈出節點: {current_node}")
        
        order_of_visit.append(current_node)
        
        # 檢查鄰居
        neighbors_added = []
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                neighbors_added.append(neighbor)
        
        if neighbors_added:
            print(f"  ➕ 發現未走訪鄰居，加入佇列: {neighbors_added}")
        else:
            print(f"  ⚪ 沒有新鄰居需要加入")
            
        print(f"  當前已拜訪名單: {list(order_of_visit)}")
        print("-" * 30)
        step += 1
                
    # 紀錄結束時間
    end_time = time.perf_counter()
    # 計算時間差（單位：秒）
    execution_time = end_time - start_time
    
    print("--- 🔍 BFS 詳細走訪過程結束 ---\n")
    
    return order_of_visit, execution_time

# --- 測試資料 ---
my_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# 2. 接收走訪結果與執行時間
result, run_time = bfs(my_graph, 'A')

# 3. 漂亮的格式化輸出
print("=" * 40)
print(f"最終走訪順序: {' -> '.join(result)}")
print("-" * 40)
print(f"實際執行時間: {run_time:.6f} 秒")  # 顯示到小數點後 6 位
print(f"理論時間複雜度: O(V + E)")
print(f"  └─ 註：目前圖形節點數 V = {len(my_graph)}, 邊數 E = {sum(len(v) for v in my_graph.values()) // 2}")
print("=" * 40)