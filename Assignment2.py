# Function 1: Lists - Finding the Maximum and Second Maximum in a List
# This function takes a list of numbers as input and returns the maximum and second maximum values.
def max_two_in_list(numbers):
    if len(numbers) < 1:
        return None, None
    if len(numbers) == 1:
        return numbers[0], None


    max1 = max2 = float('-inf')

    for num in numbers:
        if num > max1:
            max2 = max1
            max1 = num

        elif num > max2 and num != max1:
            max2 = num

        if max2 == float('-inf'):
            max2 == max1
    return (max1, max2 if max2 != float('-inf') else None)
# Function 2: Lists - Removing Duplicates and Sorting
# This function takes a list of numbers and returns a sorted list with duplicates removed.
def remove_duplicates_and_sort(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers
# Function 3: Single-Dimensional Arrays - Cumulative Sum
# This function takes an array (list) of numbers and returns a new list where each element is the cumulative sum of the previous elements.
def cumulative_sum(arr):
    cum_sum = []
    current_sum = 0

    for num in arr:
        current_sum += num
        cum_sum.append(current_sum)
    return cum_sum

# Function 4: Two-Dimensional Arrays - Matrix Transpose
# This function takes a 2D list (matrix) and returns its transpose.
def transpose_matrix(matrix):
    if not matrix:
        return []

    
    return [list(row) for row in zip(*matrix)]
# Function 5: Slicing - Extracting Every Nth Element
# This function takes a list and a step value N and returns every Nth element
def slice_every_nth(lst, step):
    return lst[::step]
# Function 6: Arithmetic Operations with Arrays - Dot Product
# This function takes two lists of the same length and returns their dot product.
def dot_product(list1, list2):
    return sum(x * y for x, y in zip(list1, list2))
# Function 7: Arithmetic Operations with Arrays - Matrix Multiplication
# This function takes two 2D lists (matrices) and returns their matrix product.
def matrix_multiplication(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            row.append(sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix2))))
        result.append(row)
    return result