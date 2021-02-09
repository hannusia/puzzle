"""
Check if game board fits the rules.
https://github.com/hannusia/puzzle.git
"""
def check_lines(board: list) -> bool:
    """
    Check if lines fit to rules.
    >>> check_lines(['****1****', '*** 1****', '**2  ****', '*   3****',
         ' 4       ', '5   5   *', '  6    **', ' 7    ***', '8    ****'])
    False
    >>> check_lines(['****1****', '***12****', '**123****', '*1234****',
         '123456789', '23456789*', '3456789**', '456789***', '56789****'])
    True
    """
    lines = {0: [], 1: [], 2: [], 3: [], 4: [],
             5: [], 6: [], 7: [], 8: []}
    for i in range(len(board)):
        for j in board[i]:
            if j in '123456789':
                lines[i].append(j)
    for i in lines:
        if len(set(lines[i])) != len(lines[i]):
            return False
    return True


def check_rows(board: list) -> bool:
    """
    Check if rows fit to rules.
    >>> check_rows(['****1****', '*** 1****', '**2  ****', '*   3****',
         ' 4       ', '5   5   *', '  6    **', ' 7    ***', '8    ****'])
    False
    >>> check_rows(['****1****', '***12****', '**123****', '*1234****',
         '123456789', '23456789*', '3456789**', '456789***', '56789****'])
    True
    """
    rows = {0: [], 1: [], 2: [], 3: [], 4: [],
            5: [], 6: [], 7: [], 8: []}
    for i in board:
        for j in range(len(i)):
            if i[j] in '123456789':
                rows[j].append(i[j])
    for i in rows:
        if len(set(rows[i])) != len(rows[i]):
            return False
    return True


def check_colors(board: list) -> bool:
    """
    Check if colors fit to rules.
    >>> check_colors(['****1****', '*** 1****', '**2  ****', '*   3****',
         ' 4       ', '5   5   *', '  6    **', ' 7    ***', '8    ****'])
    False
    >>> check_colors(['****1****', '***12****', '**123****', '*1234****',
         '123456789', '23456789*', '3456789**', '456789***', '56789****'])
    True
    """
    colors = {0: [], 1: [], 2: [], 3: [], 4: []}
    for k in range(5):
        i = 8 - k
        j = k
        if board[i][j] in '123456789':
            colors[k].append(board[i][j])
        if board[i-1][j] in '123456789':
            colors[k].append(board[i-1][j])
        if board[i-2][j] in '123456789':
            colors[k].append(board[i-2][j])
        if board[i-3][j] in '123456789':
            colors[k].append(board[i-3][j])
        if board[i-4][j] in '123456789':
            colors[k].append(board[i-4][j])
        if board[i][j+1] in '123456789':
            colors[k].append(board[i][j+1])
        if board[i][j+2] in '123456789':
            colors[k].append(board[i][j+2])
        if board[i][j+3] in '123456789':
            colors[k].append(board[i][j+3])
        if board[i][j+4] in '123456789':
            colors[k].append(board[i][j+4])
    for i in colors:
        if len(set(colors[i])) != len(colors[i]):
            return False
    return True


def validate_board(board: list) -> bool:
    """
    Check if board is ready for a game.
    >>> validate_board(['****1****', '*** 1****', '**2  ****', '*   3****',
         ' 4       ', '5   5   *', '  6    **', ' 7    ***', '8    ****'])
    False
    >>> validate_board(['****1****', '***12****', '**123****', '*1234****',
         '123456789', '23456789*', '3456789**', '456789***', '56789****'])
    True
    """
    return check_lines(board) and check_rows(board) and check_colors(board)
