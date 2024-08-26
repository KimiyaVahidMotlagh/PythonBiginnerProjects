matrix_A = []
matrix_B = []
result = []


def matrix_input():
    matrix = []
    row = int(input("enter #row: "))
    col = int(input("enter #col: "))

    for i in range(0, row, 1):
        matrix_row = list(map(int, input(">>").split()))
        if len(matrix_row) != col:
            i -= 1
        else:    
            matrix.append(matrix_row)
    return matrix  

def vector_input(matrix):
    print("enter augmented vector: \n")
    vector = list(map(int, input(">>").split()))
    for i in range(len(matrix)):
        matrix[i].append(vector[i])
    return matrix

def add_Identical_matrix(matrix):
    for i in range(len(matrix)):
        temp_row = []
        for j in range(len(matrix[i])):
            if i == j: temp_row.append(1)
            else: temp_row.append(0)    
        for j in range(len(temp_row)):
         matrix[i].append(temp_row[j])
    return matrix
    
def check_below_rows(matrix, row_index, pivot_index ):
    for i in range(row_index+1,len(matrix)):
        if matrix[i][pivot_index] != 0:
            return i
    return -1 

def row_multiply(row, scaler):
    result = [ scaler*item for item in row]
    return result

def row_echolen_form(matrix):
    pivot_counter= 0
    for row_index,main_row in enumerate(matrix):
        
        if main_row[pivot_counter] == 0 :
            good_row = check_below_rows(matrix, row_index, pivot_counter)
            if good_row == -1 :
                pivot_counter += 1
                continue
            else: 
                matrix[row_index], matrix[good_row] = matrix[good_row], matrix[row_index]
                main_row = matrix[row_index]
                
        for i, row in enumerate(matrix[row_index+1:]):
            scaler = row[pivot_counter]/ matrix[row_index][pivot_counter]
            mult_row = row_multiply(main_row, scaler)
            matrix[row_index+i+1] = [row[x] - mult_row[x] for x in range(len(mult_row))]
            
        pivot_counter += 1
    return matrix

def pivot_index_finder(row):
    pivot = 0
    for i in range(len(row)):
        if row[i] != 0:
            break
        pivot += 1
    return pivot

def reduced_row_echolen_form(matrix):
    matrix.reverse()
    for row_index,main_row in enumerate(matrix):
        pivot_index = pivot_index_finder(main_row)
        matrix[row_index] = row_multiply(main_row, 1/main_row[pivot_index])
        main_row =  matrix[row_index]
        for i, row in enumerate(matrix[row_index+1:]):
            scaler = row[pivot_index]/ main_row[pivot_index]
            mult_row = row_multiply(main_row, scaler)
            matrix[row_index+i+1] = [row[x] - mult_row[x] for x in range(len(mult_row))]
    matrix.reverse()
    return matrix

def initiate_result_value(matrix_A, matrix_B):
    for i in range(len(matrix_A)):
        temp_list =[]
        for j in range(len(matrix_B[0])):
            temp_list.append(0)
        result.append(temp_list)    

def multiply(matrix_A, matrix_B):
    for row in range(len(matrix_A)):
        for col in range(len(matrix_B[0])):
            for i in range(len(matrix_A[0])):
                result[row][col] += matrix_A[row][i]* matrix_B[i][col]
                
def print_matrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])
  
def get_vactor(matrix):
    final_vactor = []
    for row in matrix:
        final_vactor.append(row[len(matrix)-1])

    return final_vactor    

def get_inverse_matrix(matrix):
    final_matrix = []
    for row in matrix:
        temp_row = []
        for index in range(int(len(row)/2), len(row)):
            temp_row.append(row[index])
        final_matrix.append(temp_row)
    return final_matrix

matrix_A = matrix_input()
matrix_A = add_Identical_matrix(matrix_A)
echolen_matrix_A = row_echolen_form(matrix_A)
print_matrix(echolen_matrix_A)
print("*"*30)
reduced_matrix_A = reduced_row_echolen_form(echolen_matrix_A)
print_matrix(get_inverse_matrix(reduced_matrix_A))