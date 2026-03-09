import threading
import time

# 共享資源
global_counter = 0
# 互斥鎖，用於保護共享資源
lock = threading.Lock()

# --- 1. 單執行緒版本 (Simple/Fast) ---
def shared_resource_single(num_increments):
    """在單執行緒中更新計數器。"""
    global global_counter
    for _ in range(num_increments):
        global_counter += 1

# --- 2. 多執行緒版本 (High Contention) ---
def shared_resource_worker(num_increments):
    """需要鎖定才能更新共享計數器的執行緒任務。"""
    global global_counter
    global lock
    
    for _ in range(num_increments):
        # *** 每次更新都需要獲取和釋放鎖 (主要的性能瓶頸) ***
        lock.acquire() 
        global_counter += 1 
        lock.release() 
        # 由於鎖的存在，同一時間只有一個執行緒能更新計數器

# --- 概念分析 ---
# 設置一個總的增量次數 (例如 1,000,000)
# 讓多個執行緒去執行 `shared_resource_worker`
# 雖然有 4 個核心可以並行，但由於每次增量都需要鎖定，
# 只有一個執行緒可以在鎖內執行。
# 所有的並行執行緒都將花費大量的時間在等待鎖，
# 因此，總時間會是單執行緒執行時間，再加上數百萬次鎖操作的額外開銷，
# 最終導致比單執行緒慢。