matrix = []

# دریافت ورودی
for _ in range(3):
    matrix.append(list(input()))

counterX = sum(row.count('X') for row in matrix)
counterO = sum(row.count('O') for row in matrix)

# بررسی تعداد X و O
if counterO > counterX or counterX > counterO + 1:
    print("Invalid")
    exit()

# تابع بررسی سطرها
def findRow(value):
    for row in matrix:
        if row == [value, value, value]:
            return True
    return False

# تابع بررسی ستون‌ها
def findColumn(value):
    for col in range(3):
        if matrix[0][col] == value and matrix[1][col] == value and matrix[2][col] == value:
            return True
    return False

# تابع بررسی قطرها
def findDiagonal(value):
    if (matrix[0][0] == value and matrix[1][1] == value and matrix[2][2] == value) or \
       (matrix[0][2] == value and matrix[1][1] == value and matrix[2][0] == value):
        return True
    return False

# محاسبه وضعیت بازی
def calculate():
    if findRow('X') or findColumn('X') or findDiagonal('X'):
        print("X")
    elif findRow('O') or findColumn('O') or findDiagonal('O'):
        print("O")
    elif any('?' in row for row in matrix):
        print("Unfinished")
    else:
        print("Draw")

calculate()