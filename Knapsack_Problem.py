import time

def knapsack_01(weights, values, item_names, capacity): # 傳入 item_names 方便印出名字
    start_time = time.perf_counter()
    
    n = len(weights)
    # 建立一個 (n + 1) x (capacity + 1) 的二維表格 dp
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    print("\n--- 📝 DP 表格動態填表與選擇過程開始 ---")
    
    # 填表過程（動態規劃核心）
    for i in range(1, n + 1):
        current_name = item_names[i - 1]
        current_weight = weights[i - 1]
        current_value = values[i - 1]
        
        print(f"\n考慮物品【{current_name}】(重量: {current_weight}, 價值: {current_value})：")
        print("-" * 60)
        
        for w in range(1, capacity + 1):
            print(f"  當背包限重為 {w} 時：")
            
            if current_weight <= w:
                # 兩種選擇取最大值：
                # 1. 不拿：承襲同重量下、前一個物品的最佳解
                option_skip = dp[i - 1][w]
                # 2. 拿：扣除當前重量後的最佳解 + 當前物品價值
                option_take = dp[i - 1][w - current_weight] + current_value
                
                # 決定最大值
                dp[i][w] = max(option_skip, option_take)
                
                # 標記勝出者
                winner = "【拿】" if option_take > option_skip else "【不拿】"
                if option_take == option_skip:
                    winner = "【皆可，數值相同】"
                
                print(f"    ❌ 選擇[不拿]的價值: {option_skip}")
                print(f"    💰 選擇[ 拿 ]的價值: {dp[i-1][w-current_weight]} (剩餘重量 {w-current_weight} 的最佳解) + {current_value} (當前價值) = {option_take}")
                print(f"    🏆 決策結果: 選擇 {winner} -> 此格填入 {dp[i][w]}")
                
            else:
                # 當前物品太重，根本裝不下，只能選擇不拿    
                dp[i][w] = dp[i - 1][w]
                print(f"    ⚠️ 重量 {current_weight} 大於背包限重 {w}，根本裝不下！直接繼承不拿的價值 -> 此格填入 {dp[i][w]}")
                
    print("\n--- 📝 DP 表格動態填表與選擇過程結束 ---\n")
                
    # --- 回溯找出到底拿了哪些物品 ---
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)  # 記錄物品索引
            w -= weights[i - 1]           # 背包剩餘容量減少
            
    selected_items.reverse()  # 反轉讓物品順序正向排列
    
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    
    return dp[n][capacity], selected_items, dp, execution_time

# --- 測試資料 ---
item_names = [  "手機",  "相機",  "水壺" ,"零食","玩具",  "筆電"]
weights    = [    1,      2,      2,      1,     2,      3]  # 各物品重量
values     = [   15,     20,     10,      5,     5,     30 ]  # 各物品價值
knapsack_capacity = 6                                            # 背包限重

# 執行演算法 (記得要把 item_names 傳進去給函式用來印字)
max_val, items, dp_table, run_time = knapsack_01(weights, values, item_names, knapsack_capacity)

# --- 漂亮的格式化輸出 ---
print("=" * 50)
print("【0/1 背包問題 - 動態規劃最佳解】")
print("-" * 50)
print(f"🎒 背包最大限制重量: {knapsack_capacity}")
print("📦 可選擇的物品清單:")
for name, w, v in zip(item_names, weights, values):
    print(f"  └─ {name} (重量: {w}, 價值: {v})")
print("-" * 50)

print(f"▶ 最終能裝入的最大總價值: {max_val}")
print("▶ 決定打包帶走的物品:")
for idx in items:
    print(f"  ✔ {item_names[idx]} (重量: {weights[idx]}, 價值: {values[idx]})")
print(f"▶ 實際打包總重量: {sum(weights[i] for i in items)}")
print("-" * 50)

print(f"實際執行時間: {run_time:.6f} 秒")
print(f"理論時間複雜度: O(N × W)")
print(f"  └─ 註：N = {len(weights)} (物品數), W = {knapsack_capacity} (背包限重)")
print("=" * 50)