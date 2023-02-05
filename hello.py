import random

def random_bom(rows: int, cols: int, bom_number: int) -> list:
    mine = [] 
    for row in range(rows):
        row_date = []
        for col in range(cols):
            position = random.randint(0,1)
            if position >= 1 and bom_number >= 0:
                row_date.append(-1)
                bom_number -= 1
            else: 
                row_date.append(0)
        mine.append(row_date)

    while bom_number > 0:
        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - 1)
        if mine[row][col] != -1:
            mine[row][col] = -1
            bom_number -= 1
                
    return mine

if __name__ == "__main__":
    mine = random_bom(5, 5, 5)
    for row in mine:
        print(row)