class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # 1. Kiểm tra từng hàng
        for row in board:
            seen = set()

            for num in row:
                if num == ".":
                    continue

                if num in seen:
                    return False

                seen.add(num)

        # 2. Kiểm tra từng cột
        for j in range(9):
            seen = set()

            for i in range(9):
                num = board[i][j]

                if num == ".":
                    continue

                if num in seen:
                    return False

                seen.add(num)

        # 3. Kiểm tra từng ô vuông 3x3
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                seen = set()

                for i in range(row, row + 3):
                    for j in range(col, col + 3):
                        num = board[i][j]

                        if num == ".":
                            continue

                        if num in seen:
                            return False

                        seen.add(num)

        return True