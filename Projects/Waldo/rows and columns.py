"""Karma Woeser
Waldo Rows and Columns practice
"""

Waldo = 'W'
Other = '.'

# for all rows, there exists waldo in each column
def all_row_exists_waldo(matrix: list) -> bool:
    """For all rows in the matrix, Waldo is in some column"""
    if len(matrix) == 0:
        return True

    for row in matrix:
        found_waldo = False
        for i in range(len(row)):
            if row[i] is Waldo:
                found_waldo = True
                break

        if not found_waldo:
            return False

    return True


def all_col_exists_waldo(matrix: list) -> bool:
    # Columns
    """For all columns in the matrix, Waldo is in some row"""
    if len(matrix) == 0:
        return True

    for col in range(len(matrix[0])):
        found_waldo = False
        for row in range(len(matrix)):
            print(matrix[row][col])
            if matrix[row][col] is Waldo:
                found_waldo = True
                break

        if not found_waldo:
            return False
    return True



# for all there all
def all_row_all_waldo(matrix: list) -> bool:
    """For all rows in the matrix, Waldo is in every column"""
    if len(matrix) == 0:
        return True

    for row in matrix:
        for i in range(len(row)):
            print(row[i])
            if Waldo != row[i]:
                return False
    return True



def all_col_all_waldo(matrix: list) -> bool:
    """For all the columns in the matrix, Waldo is in every row"""
    if len(matrix) == 0:
        return True

    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            # matrix[row][col] = column
            if Waldo != matrix[row][col]:
                return False
    return True


# There exists for all
def exists_row_all_waldo(matrix: list) -> bool:
    """There is some row in the matrix in which Waldo is in every column"""
    if len(matrix) == 0:
        return False

    for row in matrix:
        found_all_waldo = False
        for element in row:

            if element != Waldo:

                found_all_waldo = True
                break
        if not found_all_waldo:
            return True
    return False



def exists_col_all_waldo(matrix: list) -> bool:
    """There is some column in the matrix in which Waldo is in every row"""
    if len(matrix) == 0:
        return False

    for col in range(len(matrix[0])):
        found_all_waldo = False
        for row in range(len(matrix)):
            print(matrix[row][col])
            if matrix[row][col] != Waldo:
                found_all_waldo = True
                break
        if not found_all_waldo:
            return True
    return False


# there exists, there exists
def exists_row_exists_waldo(matrix: list) -> bool:
    """There is some row in the matrix in which Waldo is in some column"""
    if len(matrix) == 0:
        return False

    for row in matrix:
        for i in range(len(row)):
            if Waldo in row[i]:
                return True
    return False


def exists_col_exists_waldo(matrix: list) -> bool:
    """There is some column in the matrix in which Waldo is in some row"""
    if len(matrix) == 0:
        return False

    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            if Waldo in matrix[row][col]:
                return True
    return False

