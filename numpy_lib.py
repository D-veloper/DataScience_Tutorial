import numpy as np

# Section 1 - Numpy Arrays

#   1.1 Initializing numpy arrays.

array_one = np.array([1, 2, 3])  # create a simple 1 x 3 matrix.
array_two = np.array([4, 5, 6])

array_zero = np.array([  # create a simple 3 x 3 matrix
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
])

array_three = array_one + array_two  # vector addition.
# print(array_three)  # -- output: [5, 7, 9].
# print(array_zero[2][0])  # -- output: 7. Access values like regular python lists.

array_four = np.zeros((2, 2, 2))  # create an array with the specified dimensions and initialise all values to zero.
array_five = np.ones((3, 4))  # same effect as above but initialise all values to one instead.
# print(array_four)
# print(array_five)

array_six = np.full((2, 2, 2), 5)  # create array with specified dimension and fill with desired value.
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
# for element in array_zero.flat:  # .flat returns a 1-D iterator of the array that we can loop over.
#     print(element)

# print(array_zero)  # array shape has not changed because .flat doesn't modify the array.

array_eleven = np.array([1, 2, 3], dtype=float)  # how to set the datatype of the array during initialization

# Section 2 - Numpy Functions

#   2.1 Mathematical Functions - Perform element-wise mathematical operations on array elements.
# print(np.sqrt(array_zero))  # perform square root operation on each array element.
# print(np.exp(array_zero))  # exponent of each array element.
# print(np.sin(array_zero) + np.cos(array_zero) + np.tan(array_zero))  # trigonometric operations
# print(np.log(array_zero))  # logarithmic operations.

#   2.2 Aggregate Functions - Compute summary statistics or aggregate values along specified axes.
# print(array_eleven.sum())  # returns sum of all elements in array.
# print(array_eleven.min())  # returns smallest element in array.
# print(array_eleven.max())  # returns largest element in array.
# print(array_eleven.mean())  # returns the mean of all values in array.
# print(np.median(array_eleven))  # returns median value in array.
# print(np.std(array_zero))  # returns the standard deviation of values in array.

#   2.3 Shape Manipulation Functions - Change the shape or structure of the array.
# array_zero = array_zero.reshape((2, 6))  # change dimensions of array_zero.
# print(array_zero)

# array_zero = array_zero.reshape((4, 3))

array_zero = array_zero.transpose()  # swap rows and columns.
# print(array_zero, "\n")
#
# array_12 = np.concatenate([array_zero, array_five], 1)  # like python list addition plus can specify axis.
# print(array_12, "\n")
#
# array_13 = np.split(array_12, 2, 1)[0]  # split the array plus can specify axis.
# print(array_13, "\n")
#
# array_14 = np.stack((array_13, array_five))  # adds an extra dimension. each array is element in new array.
# print(array_14, "\n")
#
# array_15 = array_14[0]
#
# if np.array_equal(array_15, array_zero):
#     print(array_15, "yes. \n")

# array_zero = np.append(array_zero, array_five)  # flattens out array and extends it.
# print(array_zero)

# array_zero = np.append(array_zero, array_five, axis=0)  # preserves the dimensions when joining arrays.
# print(array_zero)

# array_zero = np.insert(array_zero, 0, [0, 0, 0, 0], axis=0)  # insert new row or column as specified.
# print(array_zero)

# # array_zero = np.vstack((array_zero, array_five))  # like concatenate on axis 0 (rows).
# # array_zero = np.hstack((array_zero, array_five))  # like concatenate on axis 1 (columns).

# array_zero = array_zero.flatten()  # make array one-dimensional.
# print(array_zero)
