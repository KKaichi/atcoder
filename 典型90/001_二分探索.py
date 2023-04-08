N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

# 判定問題 (すべての長さを x 以上にすることは可能か？)
def check(x):
    num = 0  # 何個切れたか
    pre = 0  # 前回の切れ目
    for i in range(N):
        # x を超えたら切断
        if A[i] - pre >= x:
            num += 1
            pre = A[i]

    # 最後のピースが x 以上なら加算
    if L - pre >= x:
        num += 1

    return num >= K + 1


# 二分探索
left, right = -1, L + 1
while right - left > 1:
    mid = (left + right) // 2
    if check(mid):
        left = mid
    else:
        right = mid
print(left)

"""
input
3 34
1
8 13 26

1. ・mid=(35+(-1))//2=17cm
   ・17cm以上の長さで切ることが可能かどうか
   ・全てのピースを17以上にすることは不可能
   ・rightを17へ
2. ・mid=(17+(-1))//2=8cm
   ・8cm以上の長さで切ることが可能かどうか
   ・全てのピースを8以上にすることは可能
   ・leftを8へ
3. ・mid=(17+8)//2=12cm
   ・12cm以上の長さで切ることが可能かどうか
   ・全てのピースを12以上にすることは可能
   ・leftを12へ
3. ・mid=(17+12)//2=14cm
   ・14cm以上の長さで切ることが可能かどうか
   ・全てのピースを14以上にすることは不可能
   ・rightを14へ
3. ・mid=(14+12)//2=13cm
   ・13cm以上の長さで切ることが可能かどうか
   ・全てのピースを13以上にすることは可能
   ・rightを13へ
4. right-left=1より終了
答えは13
"""
