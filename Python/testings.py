two_dimensional_list= [[0] * 3] * 5
for  row in range(5):
    for column in range(3):
        two_dimensional_list[row][column] = int(input("Enter integer value for row " + \
                                                      str(row+1) + \
                                                      ", column " + str(column+1) + ": "))


