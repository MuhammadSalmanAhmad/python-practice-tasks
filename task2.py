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
    max=-5000
    for i in range(len(array)-2):
        for j in range(len(array[i])-2):
            local_sum= sum(array[i][j:j+3]+array[i+2][j:j+3])+array[i+1][j+1]
            print(local_sum)
            if local_sum>max:
                max=local_sum
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
