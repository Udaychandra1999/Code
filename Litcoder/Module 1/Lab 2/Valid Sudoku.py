def is_valid_sudoku(board):
    def has_duplicates(lst):
        seen = set()
        for num in lst:
            if num != '.':
                if num in seen:
                    return "NO"
                seen.add(num)
        return "YES"

    for i in range(9):
        if has_duplicates(board[i]) == "NO":
            print("NO")
            return
        if has_duplicates([board[j][i] for j in range(9)]) == "NO":
            print("NO")
            return

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            sub_box = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
            if has_duplicates(sub_box) == "NO":
                print("NO")
                return

    print("YES")

n = int(input())
board = [input().split() for _ in range(n)]
is_valid_sudoku(board)
                       