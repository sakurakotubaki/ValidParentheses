# 西暦
N = 2023

# Nが閏年かどうかを判定
# P22を読む
# ネストしてみずらい
# if N % 4 == 0:
#     if N % 100 == 0:
#         if N % 400 == 0:
#             print("閏年です")
#         else:
#             print("平年です")
#     else:
#         print("閏年です")
# else:
#     print("平年です")

# ネストを浅くする
# if N % 4 == 0:
#     print("平年です")
# elif N % 100 != 0:
#     print("閏年です")
# elif N % 400 != 0:
#     print("平年です")
# else:
#     print("閏年です")

# 論理演算子で分岐をまとめる
if N % 4 == 0 and (N % 100 != 0 or N % 400 == 0):
    print("閏年です")
else:
    print("平年です")