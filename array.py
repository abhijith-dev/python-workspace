'''	Write a program to accept a two-dimensional array containing integers as the parameter and determine the following from the elements of the array:
a.	element with minimum value in the entire array
b.	element with maximum value in the entire array
c.	the elements with minimum and maximum values in each column
d.	the elements with minimum and maximum values in each row'''

row_num = int(input("Input number of rows: "))
col_num = int(input("Input number of columns: "))
multi_list = [[0 for col in range(col_num)] for row in range(row_num)]

for row in range(row_num):
    for col in range(col_num):
        multi_list[row][col]= row*col

    print(multi_list)