def excel_sheet_column_number(s):
    ''' Given a column title as it would appear in an Excel spreadsheet,
        return its corresponding column number. Column names and numbers
        follow a consistent pattern:

        A -> 1
        B -> 2
        C -> 3
        ...
        Z -> 26
        AA -> 27
        AB -> 28
    '''
    expn = 0
    col_num = 0
    for char in reversed(s):
        col_num += (ord(char) - ord('A') + 1) * (26 ** expn)
        expn += 1

    return col_num
