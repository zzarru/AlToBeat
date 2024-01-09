# board = []
# count = []
#
# for i in range(5):
#     row = list(input())
#     if len(row)<=15:
#         row.extend('*'*(15-len(row)))
#         board.append(row)
#
# for j in range(15):
#     for i in range(5):
#         if board[i][j] != '*':
#             print(board[i][j],end='')

#간단한 방법
# board = [input() for i in range(5)]
#
# for j in range(15):
#     for i in range(5):
#         if j<len(board[i]):
#             print(board[i][j],end='')

#다른 방법/ 메모리가 많이 듦
# board = [input() for _ in range(5)]
#
# for i in range(15):
#     for j in range(5):
#         try:
#             print(board[j][i],end='')
#         except:
#             pass
