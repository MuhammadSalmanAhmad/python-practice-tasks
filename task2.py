"""
this progrom calculates maximum sum of hourglass in a 2D matrix
"""
def max_sum(array):
    """
    function to calculate maximum sum in the matrix
    Parameters:
       array (2D int) : recieves matrix from user
    Returns:
       max_sum (int) : value of max sum
    """
    row=6
    column=6
    max=-5000
    for i in range(0,row-2):
        for j in range(0,column-2):
            sum= (array[i][j]+array[i][j+1]+array[i][j+2])+(array[i+1][j+1])+(array[i+2][j]+array[i+2][j+1]+array[i+2][j+2])
            if sum>max:
                max=sum
            else:
                continue
    return max

def main():
    """
    main module of the program, default run of the program starts from here
    """
    input_array = [
        [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 2, 4, 0]
     ]
    result = max_sum(input_array)
    print("sum = {}".format(result))
if __name__ == "__main__":
    main()
