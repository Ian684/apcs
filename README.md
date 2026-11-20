# APCS 題型練習

完整題號、來源與執行方式見 [CATALOG.md](CATALOG.md)，機器可讀清單見 [EXERCISES.json](EXERCISES.json)。

以下保留起步練習的說明；其餘題目按完整目錄閱讀。

根目錄 apcs_*.py 保留原本解題檔案。新增 [practice/](practice/) 是自訂題型練習，**不是官方歷屆題目**。每題可由標準輸入執行。

需要 Python 3.10 以上。在根目錄執行 python -m unittest discover -s tests -v。

| 題目 | 要處理的問題 | 方法／複雜度 |
|---|---|---|
| range_queries.py | 多次查詢陣列閉區間總和 | 前綴和，O(n+q) |
| maze.py | S 到 G 的四方向最短步數 | BFS，O(hw) |
| meeting_rooms.py | 同時進行的活動最少需要幾間教室 | 排序與最小堆積，O(n log n) |
| shipping.py | 原順序運貨的最小每日容量 | 二分答案，O(n log sum(weights)) |

## 1. 區間總和

第一行 n q，第二行 n 個整數，接著 q 行 l r，端點為 1-based 且皆包含。

    5 3
    2 -3 5 7 1
    1 5
    2 4
    3 3

執行 python -m practice.range_queries < input.txt，依序輸出 12、9、5。負數不影響前綴和；公式為 prefix[r]-prefix[l-1]。

## 2. 迷宮

第一行 h w，後面 h 列地圖，包含一個 S、一個 G；. 可通行，# 是牆，不能走斜角。無路可走輸出 -1。

    3 3
    S..
    ##.
    ..G

python -m practice.maze < input.txt 輸出 4。BFS 在入佇列時標記，避免同一格重複排隊。

## 3. 教室安排

第一行 n，後面 n 行 start end。活動區間是 [start,end)，活動結束即可開始下一場。

    3
    0 5
    1 2
    2 4

python -m practice.meeting_rooms < input.txt 輸出 2。比較時用 ends[0]<=start，端點相等不重疊。

## 4. 運貨容量

第一行 n days，後面 n 個正整數重量，不能打亂順序或拆開單件物品。

    5 3
    1 2 3 4 5

python -m practice.shipping < input.txt 輸出 6。容量可行性有單調性，搜尋下界是最重單件，上界是總重量。

測試把運貨結果與所有切割位置比較，把教室數與逐時刻重疊數比較。原有解答沒有重新送到線上評測。
