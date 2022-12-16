"""
4 kyu A Knight's Tour
https://www.codewars.com//kata/5664740e6072d2eebe00001b
"""

def knights_tour(start, size):
    def find_next_pos(row, col):
        return [(row + 2, col + 1), (row + 2, col - 1), (row - 2, col + 1), (row - 2, col - 1),
                (row + 1, col + 2), (row + 1, col - 2), (row - 1, col + 2), (row - 1, col - 2)]

    def num_moves(curr_pos):
        next_positions = find_next_pos(curr_pos[0], curr_pos[1])
        return sum(0 <= r < size and 0 <= c < size and board[r][c] == 0 for r, c in next_positions)

    def solve_tour(board, row, col, step):
        if step == size ** 2 + 1:
            return True
        for r, c in sorted(find_next_pos(row, col), key=num_moves):
            if 0 <= r < size and 0 <= c < size and not board[r][c]:
                board[r][c] = step
                if solve_tour(board, r, c, step + 1):
                    return True
                board[r][c] = 0
        return False

    board = [[0 for _ in range(size)] for _ in range(size)]
    board[start[0]][start[1]] = 1
    solve_tour(board, start[0], start[1], 2)
    res = [None for _ in range(size ** 2)]
    for i in range(size ** 2):
        res[board[i // size][i % size] - 1] = i // size, i % size
    return res