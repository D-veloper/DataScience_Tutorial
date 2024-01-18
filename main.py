import numpy as np

# Section 1 - Numpy Arrays

#   1.1 Initializing numpy arrays.

array_one = np.array([1, 2, 3])  # create a simple 1 x 3 matrix.
array_two = np.array([4, 5, 6])

array_zero = np.array([  # create a simple 3 x 3 matrix
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

array_three = array_one + array_two  # vector addition.
# print(array_three)  # -- output: [5, 7, 9].
# print(array_zero[2][0])  # -- output: 7. Access values like regular python lists.

array_four = np.zeros((2, 2, 2))  # create an array with the specified dimensions and initialise all values to zero.
array_five = np.ones((3, 4, 5))  # same effect as above but initialise all values to one instead.
# print(array_four)
# print(array_five)

array_six = np.full((2, 2, 2), 5)  # create an array with a specified dimension and fill it with desired value.
# print(array_six)

array_seven = np.empty((3, 2, 2))  # create array with specified dimensions but filled with uninitialised/garbage data.
# print(array_seven)

array_eight = np.random.random((3, 2, 2))  # array with specified dimension filled with random values between 0 and 1
# print(array_eight)

array_nine = np.arange(0, 50, 5)  # create 1D array with sequential values from 0 to 50 with step increase of 5
# print(array_nine)

array_ten = np.linspace(0, 10, 3)  # create 1D array of three elements evenly distributed from 0 to 10
# print(array_ten)

#   1.2 Some attributes of numpy arrays

# print(array_one.shape)  # returns the dimensions of the array.
# print(array_two.size)  # returns the number of elements in the array.
# print(array_three.ndim)  # returns the number of columns.
# print(array_four.dtype)  # returns the datatype of the array.

array_eleven = np.array([1, 2, 3], dtype=float)  # how to set the datatype of the array during initialization
