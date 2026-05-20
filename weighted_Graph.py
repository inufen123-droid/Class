import heapq
import time

def dijkstra_with_path(graph, start_node, end_node):
    start_time = time.perf_counter()
    
    # 初始化距離與前驅節點
    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0
    predecessors = {node: None for node in graph}
    
    priority_queue = [(0, start_node)]
    
    print("--- 權重更新（鬆弛操作）動態過程 ---")
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # 如果已經走到終點，且這是最短的選擇，其實可以提早結束
        if current_node == end_node:
            continue
            
        if current_distance > distances[current_node]:
            continue
            
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # 發現更短的路徑，進行權重更新！
            if distance < distances[neighbor]:
                old_dist = distances[neighbor]
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
                
                print(f"  更新節點 {neighbor}: 原本累積權重 {old_dist} -> 經由 {current_node} 更新為 {distance}")
                
    # --- 回溯重建從 start_node 到 end_node 的最短路徑 ---
    path = []
    current = end_node
    while current is not None:
        path.append(current)
        current = predecessors[current]
    path.reverse()  # 因為是從終點回溯的，所以要反轉回來
    
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    
    # 如果起點跟終點不連通，路徑長度會是 1 (只有終點自己)
    if path[0] != start_node:
        path = []
        
    return path, distances[end_node], execution_time

# --- 測試資料（與前面相同） ---
weighted_graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'D': 2, 'E': 3},
    'C': {'A': 2, 'B': 1, 'F': 5},
    'D': {'B': 2},
    'E': {'B': 3, 'F': 1},
    'F': {'C': 5, 'E': 1}
}

# 執行從 A 到 F 的最短路徑搜尋
start, end = 'A', 'F'
shortest_path, total_weight, run_time = dijkstra_with_path(weighted_graph, start, end)

# --- 漂亮的格式化輸出 ---
print("\n" + "=" * 45)
print(f"【Dijkstra 搜尋結果：從 {start} 到 {end}】")
print("-" * 45)
if shortest_path:
    print(f"▶ 最短路徑走法: {' -> '.join(shortest_path)}")
    print(f"▶ 總路徑權重: {total_weight}")
else:
    print(f"❌ 找不到從 {start} 到 {end} 的路徑")
print("-" * 45)
print(f"實際執行時間: {run_time:.6f} 秒")
print(f"理論時間複雜度: O((V + E) log V)")
print("=" * 45)