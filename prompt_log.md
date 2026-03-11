# AI 交互日志
## 1. 初始需求 Prompt（优化前）
写一个八皇后求解器

## 2. 初始需求 Prompt（优化后）
请完成以下 Python 代码开发：
1. 工程结构：代码放在 src/queens.py 中；
2. 核心函数：实现 solve_n_queens(n=8)，返回所有合法解，格式为[[行号, 列号], ...]；
3. 代码规范：添加详细注释，符合 PEP8 规范；
4. 附加要求：包含示例调用代码，可直接运行测试。

## 3. Bug 定位修复 Prompt
问题：运行 solve_n_queens(8) 生成了错误解，皇后在对角线上互相攻击。
错误代码：
def is_valid(row, col):
    for i in range(row):
        if board[i] == col:
            return False
    return True
要求：定位问题并修复，同时解释修复逻辑。

## 4. 代码重构 Prompt
要求：将 solve_n_queens 函数拆分为更小的函数（如 is_valid、backtrack），添加函数注释，符合 PEP8 格式。