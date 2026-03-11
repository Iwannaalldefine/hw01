# src/queens.py
def solve_n_queens(n=8):
    """
    求解n皇后问题，返回所有合法的皇后摆放位置
    :param n: 棋盘大小，默认n=8（八皇后问题）
    :return: 列表的列表，每个子列表代表一种解法，格式为[[行号, 列号], ...]
    """
    solutions = []  # 存储所有合法解
    board = [-1] * n  # 用数组表示棋盘，board[row] = col
    
    def is_valid(row, col):
        """
        检查在(row, col)位置放置皇后是否合法
        只需要检查当前行之前的所有行，因为逐行放置
        """
        for i in range(row):
            # 同列 或 对角线（行差 == 列差）
            if board[i] == col or abs(row - i) == abs(col - board[i]):
                return False
        return True
    
    def backtrack(row):
        """
        回溯法：逐行放置皇后
        """
        if row == n:
            # 找到一个完整解，转换为[[行, 列], ...]的格式
            solution = [[i, board[i]] for i in range(n)]
            solutions.append(solution)
            return
        # 尝试在当前行的每一列放置皇后
        for col in range(n):
            if is_valid(row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1  # 回溯
    
    backtrack(0)
    return solutions
#运行
if __name__ == "__main__":
    # 测试八皇后问题
    solutions = solve_n_queens(8)
    print(f"八皇后问题共有 {len(solutions)} 种解法")
    # 打印前2种解法，方便查看
    for i, sol in enumerate(solutions[:2]):
        print(f"解法 {i+1}: {sol}")