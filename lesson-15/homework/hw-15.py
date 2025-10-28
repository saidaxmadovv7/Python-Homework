#1. Convert List to 1D Array
#Write a NumPy program to convert a list of numeric values into a one-dimensional NumPy array.

#Expected Output:

#Original List: [12.23, 13.32, 100, 36.32] One-dimensional NumPy array: [ 12.23 13.32 100. 36.32]

import numpy as np

arr = np.array([12.23, 13.32, 100, 36.32])
print(arr)




#2. Create 3x3 Matrix (2?10)
#Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.

#Expected Output:

#[[ 2 3 4] [ 5 6 7] [ 8 9 10]]

import numpy as np

matrix = np.array(([2,3,4],[5,6,7],[8,9,10]))
print(matrix)

print (matrix.shape)




#3. Null Vector (10) & Update Sixth Value
#Write a NumPy program to create a null vector of size 10 and update the sixth value to 11.

#[ 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

#Update sixth value to 11 [ 0. 0. 0. 0. 0. 0. 11. 0. 0. 0.]

import numpy as np

arr = np.zeros(10)

print("Original array:")
print(arr)

arr[5] = 11

print("\nUpdated array:")
print(arr)




#4. Array from 12 to 38
#Write a NumPy program to create an array with values ranging from 12 to 38.

#Expected Output:

#[12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37]

import numpy as np
arr = np.arange(12, 38)
print(arr)




#5. Convert Array to Float Type
#Write a NumPy program to convert an array to a floating type.

#Sample output:

#Original array [1, 2, 3, 4]

import numpy as np

arr = np.array([1, 2, 3, 4])
print("Original array:", arr)

float_arr = arr.astype(float)
print("Array converted to float:", float_arr)





#6. Celsius to Fahrenheit Conversion
#Write a NumPy program to convert Centigrade degrees into Fahrenheit degrees. Centigrade values are stored in a NumPy array.

#Sample Array [0, 12, 45.21, 34, 99.91] [-17.78, -11.11, 7.34, 1.11, 37.73, 0. ]

#Expected Output:

#Values in Fahrenheit degrees: [ 0. 12. 45.21 34. 99.91 32. ]

#Values in Centigrade degrees: [-17.78 -11.11 7.34 1.11 37.73 0. ]

#Values in Centigrade degrees: [-17.78 -11.11 7.34 1.11 37.73 0. ]

#Values in Fahrenheit degrees: [-0. 12. 45.21 34. 99.91 32. ]

import numpy as np

c_values = np.array([0, 12, 45.21, 34, 99.91])

# Selsiy → Farangeyt formulasi: F = (9/5) * C + 32
f_values = (9/5) * c_values + 32

print("Values in Centigrade degrees:", c_values)
print("Values in Fahrenheit degrees:", f_values)





#7. Append Values to Array (Do self-tudy)
# Write a NumPy program to append values to the end of an array.

#Expected Output:

#Original array: [10, 20, 30]

#After append values to the end of the array: [10 20 30 40 50 60 70 80 90]

import numpy as np

arr = np.array([10, 20, 30])
print("Original array:", arr)

new_arr = np.append(arr, [40, 50, 60, 70, 80, 90])

print("After append values to the end of the array:", new_arr)





#8. Array Statistical Functions (Do self-tudy)
# Create a random NumPy array of 10 elements and calculate the mean, median, and standard deviation of the array.

import numpy as np

arr = np.random.rand(10)

print("Random array:", arr)

mean_value = np.mean(arr)

median_value = np.median(arr)

std_value = np.std(arr)

print("Mean:", mean_value)
print("Median:", median_value)
print("Standard Deviation:", std_value)





#9 Find min and max
#Create a 10x10 array with random values and find the minimum and maximum values.

import numpy as np

arr = np.random.rand(10, 10)

print("10x10 random array:\n", arr)

min_value = np.min(arr)
max_value = np.max(arr)

print("\nMinimum value:", min_value)
print("Maximum value:", max_value)





#10
#Create a 3x3x3 array with random values.

import numpy as np

arr = np.random.rand(3, 3, 3)

print("3x3x3 random array:\n", arr)
