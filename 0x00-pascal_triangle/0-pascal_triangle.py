#!/usr/bin/python3
"""
Pascal's Triangle Calculation
"""

def pascal_triangle(n):
    """
    This function returns a list of lists of integers representing the Pascal's triangle of n.
    If n is less than or equal to 0, it returns an empty list.
    """
    if n <= 0:
        return []

    # initialize an empty list to hold the result
    pascal = []  
    for i in range(n):
        
        # create an empty list of i+1 length to hold the row values
        row = [0] * (i + 1)  
        
        # assign first and last values to 1
        row[0], row[-1] = 1, 1  
        
        # iterate over the remaining positions in the row
        for j in range(1, len(row)-1):  
            
            # calculate the value of the position
            row[j] = pascal[i-1][j-1] + pascal[i-1][j]  
        
        # add the row to the pascal list
        pascal.append(row)  

    # return the pascal list
    return pascal  


# def print_triangle(triangle):
#     """
#     Print the triangle
#     """
#     for row in triangle:
#         print("[{}]".format(",".join([str(x) for x in row])))
    
# print_triangle(pascal_triangle(6))
