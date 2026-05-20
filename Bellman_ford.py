import time

def bellman_ford_presentation_style(graph, start_node, end_node):
    start_time = time.perf_counter()
    
    # === Phase 1: 悲觀初始化 ===
    # 將起點設為 0，其餘所有節點的最短距離皆預設為無限大 (inf)
    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0
    predecessors = {node: None for node in graph}
    
    # 攤平所有的邊，方便進行無差別掃描
    edges = []
    for u in graph:
        for v, weight in graph[u].items():
            edges.append((u, v, weight))
            
    num_vertices = len(graph)
    total_edges = len(edges)
    
    print(f"=== Phase 1: 初始化完成 ===")
    print(f"節點數 (N) = {num_vertices}, 邊數 (M) = {total_edges}\n")
    print("=== Phase 2 & 3: 開始全局鬆弛掃描 ===")
    
    # 最多進行 N - 1 輪的全面檢查
    for i in range(1, num_vertices):
        # 用來記錄這一輪（掃過 M 條邊）中，有沒有任何數值被更新
        any_updated = False
        
        print(f"  [第 {i} 輪掃描] 開始檢查全部 {total_edges} 條邊...")
        
        # 進行邊的無差別疊加與鬆弛
        for u, v, weight in edges:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                old_dist = distances[v]
                distances[v] = distances[u] + weight
                predecessors[v] = u
                any_updated = True
                print(f"    └─ 鬆弛成功! 節點 {v}: 原本 {old_dist} -> 經由 {u} 更新為 {distances[v]}")
                
        # === Phase 3: 智慧提早結束 ===
        # 如果在一整輪的檢查中，沒有任何節點的距離被更新，代表已達全局最佳解，立刻煞車！
        if not any_updated:
            print(f"  [Phase 3 觸發] 🟢 本輪無任何更新，代表系統已達全局最佳解！立刻煞車提早結束。")
            break

    # --- 檢查負權重迴圈 (Negative Cycle) ---
    has_negative_cycle = False
    for u, v, weight in edges:
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            has_negative_cycle = True
            break

    # --- 重建最短路徑 ---
    path = []
    if not has_negative_cycle:
        current = end_node
        while current is not None:
            path.append(current)
            current = predecessors[current]
        path.reverse()
        if path and path[0] != start_node:
            path = []

    end_time = time.perf_counter()
    return path, distances[end_node], has_negative_cycle, end_time - start_time

# --- 測試資料（包含負權重，模擬簡報中的複雜圖形） ---
graph_data = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 2, 'E': 3},
    'C': {'B': 1, 'F': 5, 'G': 2},
    'D': {},
    'E': {'F': 1},
    'F': {'H': 2},
    'G': {'H': -3},  # 包含負權重
    'H': {'F': 1}
}

# 執行 A 到 F 的最短路徑
start, end = 'A', 'F'
path, total_weight, has_cycle, run_time = bellman_ford_presentation_style(graph_data, start, end)

# --- 格式化結果輸出 ---
print("\n" + "=" * 55)
print(f"【Bellman-Ford 全局視野執行結果】")
print("-" * 55)
if has_cycle:
    print("❌ 偵測到負權重迴圈！無法計算有意義的最短路徑。")
elif path:
    print(f"▶ 最短路徑走法: {' -> '.join(path)}")
    print(f"▶ 最短總路徑權重: {total_weight}")
else:
    print(f"❌ 找不到從 {start} 到 {end} 的路徑")
print("-" * 55)
print(f"實際執行時間: {run_time:.6f} 秒")
print(f"理論時間複雜度: O(N × M)  ※ N=節點數, M=邊數")
print("=" * 55)