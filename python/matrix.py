def print_matrix(matrix):
    print matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print ("value at matrix[{0}][{1}] = {2}".format(i,j,matrix[i][j]))

def reverse(input):
    reversed_input = []
    length = len(input)
    while length>0:
        reversed_input += input[length-1]
        length -=1
    return reversed_input
def rotate(matrix):
    matrix = matrix[::-1]
    for i in range(len(matrix)):
        for j in range(i):
            # print("length of i {0}".format(len(matrix[i])))
            # temp = matrix[i][j]
            matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]
            # matrix[len(matrix[i])-1][i] = temp
            print ("value at matrix[{0}][{1}] = {2}".format(i,j,matrix[i][j]))
            print ("value at matrix[{0}][{1}] = {2}".format(j,i,matrix[j][i]))
    print (matrix)
matrix = [[1,2,3],[4,5,6],[7,8,9]]
#matrix = [[1,2], [3,4]]
#print_matrix(matrix)
rotate(matrix)
