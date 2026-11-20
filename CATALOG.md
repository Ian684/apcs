# 練習目錄

目錄列出各題的實作位置與執行入口。

## 執行與驗證

    python -m unittest discover -s tests -v
    python -m practice.more --list
    python -m practice.more 5 '[12345]'

## 題目

| 題號 | 任務／學習重點 | 來源 | 入口 |
|---|---|---|---|
| 01 | 區間總和 | [range_queries.py](practice/range_queries.py) | solve |
| 02 | 迷宮最短路 | [maze.py](practice/maze.py) | shortest_route |
| 03 | 教室安排 | [meeting_rooms.py](practice/meeting_rooms.py) | minimum_rooms |
| 04 | 運貨容量 | [shipping.py](practice/shipping.py) | minimum_capacity |
| 05 | 數字加總：整數拆位，負號不計 | [more.py](practice/more.py) | digit_sum |
| 06 | 反覆數字加總：終止條件與 0 | [more.py](practice/more.py) | digital_root |
| 07 | 整數反轉：符號與前導 0 | [more.py](practice/more.py) | reverse_integer |
| 08 | 進位轉換：商、餘數與字元表 | [more.py](practice/more.py) | base_digits |
| 09 | 閏年：條件的優先順序 | [more.py](practice/more.py) | leap_year |
| 10 | 時間進位：跨日取餘數 | [more.py](practice/more.py) | add_minutes |
| 11 | 時鐘夾角：連續移動的時針 | [more.py](practice/more.py) | clock_angle |
| 12 | 成績級距：計數陣列與 100 分 | [more.py](practice/more.py) | grade_histogram |
| 13 | 加權平均：以分數保存精確值 | [more.py](practice/more.py) | weighted_fraction |
| 14 | 影像旋轉：矩形座標變換 | [more.py](practice/more.py) | rotate_matrix |
| 15 | 行列轉置：長寬交換 | [more.py](practice/more.py) | transpose_matrix |
| 16 | 螺旋讀取：四個邊界逐層縮小 | [more.py](practice/more.py) | spiral_order |
| 17 | 踩地雷提示：八方向鄰格邊界 | [more.py](practice/more.py) | mine_counts |
| 18 | 島嶼數量：四方向連通區塊 | [more.py](practice/more.py) | island_count |
| 19 | 機器人走格子：狀態更新與越界拒絕 | [more.py](practice/more.py) | robot_position |
| 20 | 收銀台排隊：最早空閒的機台 | [more.py](practice/more.py) | checkout_time |
| 21 | 報數淘汰：環狀串列的索引 | [more.py](practice/more.py) | josephus |
| 22 | 堆疊命令：空堆疊與輸出序列 | [more.py](practice/more.py) | stack_commands |
| 23 | 後序運算式：運算元順序 | [more.py](practice/more.py) | postfix_value |
| 24 | 括號檢查：巢狀配對與忽略文字 | [more.py](practice/more.py) | balanced_brackets |
| 25 | 火車調度：單一側線堆疊 | [more.py](practice/more.py) | train_reorder |
| 26 | 連續壓縮：分組與最後一段 | [more.py](practice/more.py) | run_length |
| 27 | 時間交集：半開區間 | [more.py](practice/more.py) | intersection_length |
| 28 | 油漆覆蓋：重疊區間不能重複計數 | [more.py](practice/more.py) | covered_length |
| 29 | 最均衡分割：前綴與總和 | [more.py](practice/more.py) | balanced_cut |
| 30 | 達標最短連續段：正數滑動視窗 | [more.py](practice/more.py) | minimum_window |
| 31 | 配對總和：重複值按位置計數 | [more.py](practice/more.py) | target_pairs |
| 32 | 數字三角形：由底往上 DP | [more.py](practice/more.py) | triangle_path |
| 33 | 硬幣組合數：組合不是排列 | [more.py](practice/more.py) | coin_combinations |
| 34 | 障礙格走法：只能往右或往下 | [more.py](practice/more.py) | grid_paths |
| 35 | 線段格點：座標差與 gcd | [more.py](practice/more.py) | lattice_points |
| 36 | 矩形交疊面積：水平與垂直交集 | [more.py](practice/more.py) | rectangle_overlap |
| 37 | 山峰位置：嚴格大於左右鄰居 | [more.py](practice/more.py) | mountain_peaks |
| 38 | 天際線能見度：嚴格刷新最高值 | [more.py](practice/more.py) | visible_buildings |
| 39 | 競賽排名：同分同名次 | [more.py](practice/more.py) | dense_ranks |
| 40 | 集合交集：雙指標與去重 | [more.py](practice/more.py) | sorted_intersection |
| 41 | 矩陣乘法：三層迴圈與維度 | [more.py](practice/more.py) | matrix_product |
| 42 | 多項式求值：Horner 法 | [more.py](practice/more.py) | polynomial |
| 43 | 最大公因數與最小公倍數：先除再乘 | [more.py](practice/more.py) | gcd_lcm |
| 44 | 範圍內質數數量：篩法與 0、1 | [more.py](practice/more.py) | prime_count |
| 45 | 因數列舉：平方根配對避免重複 | [more.py](practice/more.py) | divisors |
| 46 | 最接近數字：排序後只比較鄰居 | [more.py](practice/more.py) | closest_pair_gap |
| 47 | 單次買賣：維護歷史最低價格 | [more.py](practice/more.py) | max_profit |
| 48 | 票數最多者：平手取字典序最小 | [more.py](practice/more.py) | frequency_winner |
| 49 | 括號深度：合法性與最大巢狀 | [more.py](practice/more.py) | parentheses_depth |
| 50 | 二元排序交換：錯放的 1 數量 | [more.py](practice/more.py) | minimum_swaps_binary |

每個新增單元的正常值與邊界案例可在 tests/、check.py 或 testbench 找到。先預測輸出，再執行，再修改輸入觀察；不是把通過單一範例視為正式部署或線上 AC。
