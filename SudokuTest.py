''''''
'''
does not test for squares in a 9x9
study pass by value vs pass by ref to understand creation of 
variable truelist'''

''' checks sudoku or should be and just using or here as a test '''
def check_sudoku(squarelist):
    truelist = squarelist
    return check_col(truelist) and check_row(truelist)

'''checks rows for duplicates'''
def check_row(squarelist):
    for row in squarelist:
        while row:
          num = row.pop()
          if num in row or num > len(squarelist) or type(num) != int:
             return False
    return True

'''check coloums for duplicates '''
def check_col(squarelist):
    rotatedsquarelist = list(zip(*squarelist[::-1]))
    for col in rotatedsquarelist:
        listcol = list(col)
        while listcol:
            num = listcol.pop()
            if num in listcol or num > len(squarelist) or type(num) != int:
                return False
    return True



correct = [[1, 2, 3],
           [2, 3, 1],
           [3, 1, 2]]

print check_sudoku(correct)

incorrect = [[1, 4, 3, 1],
             [2, 3, 1, 3],
             [3, 1, 2, 2],
             [4, 2, 4, 4]]


# print check_row(incorrect)
print check_sudoku(incorrect)
# print check_col(incorrect)

incorrect2 = [[1, 2, 3, 4],
              [2, 3, 1, 4],
              [4, 1, 2, 3],
              [3, 4, 1, 2]]
print check_sudoku(incorrect2)
# print check_row(incorrect2)
#print check_col(incorrect2)

incorrect3 = [[1, 2, 3, 4, 5],
              [2, 3, 1, 5, 6],
              [4, 5, 2, 1, 3],
              [3, 4, 5, 2, 1],
              [5, 6, 4, 3, 2]]
print check_sudoku(incorrect3)
incorrect4 = [['a', 'b', 'c'],
              ['b', 'c', 'a'],
              ['c', 'a', 'b']]

incorrect5 = [[1, 1.5],
              [1.5, 1]]
print check_sudoku(incorrect5)