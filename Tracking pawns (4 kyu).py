"""
Tracking pawns (4 kyu)
https://www.codewars.com//kata/56b012bbee8829c4ea00002c
"""

def pawn_move_tracker(moves):
    b = [[".",".",".",".",".",".",".","."],
         ["p","p","p","p","p","p","p","p"],
         [".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".","."],
         ["P","P","P","P","P","P","P","P"],
         [".",".",".",".",".",".",".","."]]
    for index,move in enumerate(moves):
        p = 'p' if index%2 else 'P'
        if 'x' in move:
            t,j,i = ord(move[0])-97,ord(move[2])-97,abs(int(move[3])-8)
            mass = [[-1,-1],[-1,1]] if index%2 else [[1,-1],[1,1]]
            for di,dj in mass:
                y,x = i+di,j+dj
                if b[y][x]==p:
                    b[y][x],b[i][j] = '.',p
                    break
            else:
                return f'{move} is invalid'
        else:
            j,i = ord(move[0])-97,abs(int(move[1])-8)
            for di in range(1,3):
                y = i+di*(-1 if index%2 else 1)
                if b[y][j]==p and b[i][j]=='.':
                    b[y][j],b[i][j] = '.',p
                    break
            else:
                return f'{move} is invalid'
    return b