def treasureMap():
    row1 = [' ', ' ', ' ']
    row2 = [' ', ' ', ' ']
    row3 = [' ', ' ', ' ']
    map = [row1, row2, row3]
    print(row1)
    print(row2)
    print(row3)

    position = input("Where do you want to put the reasure(2 digits, row|column)?: ")
    if(len(position) != 2):
        print("Enter 2 digits")
        exit()
    if(int(position[0]) > len(map)):
        print(f"use rows from 0 to {len(map) - 1}")
        exit()
    column = int(position[0]) - 1
    if(int(position[1]) > len(row1)):
        print(f"use columns from 0 to {len(row1) - 1}")
        exit()
    row = int(position[1]) - 1
    map[row][column] = 'x'
    print(row1)
    print(row2)
    print(row3)
    
