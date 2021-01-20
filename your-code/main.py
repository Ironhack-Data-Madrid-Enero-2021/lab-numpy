#1. Import the NUMPY package under the name np.

import numpy as np

#2. Print the NUMPY version and the configuration.


print(np.__version__)

1.19.5

print(np.show_config())


#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?


a = np.random.random((2,3,5))

array = np.arange(30).reshape(2,3,5)



#4. Print a.

print(a)

array([[[0.02472889, 0.03156034, 0.51580717, 0.46631697, 0.56668133],
        [0.53013533, 0.3724969 , 0.19797413, 0.36729391, 0.99045247],
        [0.57633789, 0.73761658, 0.45033151, 0.18644739, 0.3014748 ]],

       [[0.39116425, 0.29086419, 0.47789771, 0.46487231, 0.16095184],
        [0.36504902, 0.87508774, 0.25568776, 0.10814261, 0.00561579],
        [0.64513572, 0.15694519, 0.26318638, 0.63254261, 0.23976145]]])


#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

b = np.ones((5,2,3))


#6. Print b.

print(b)

array([[[1., 1., 1.],
        [1., 1., 1.]],

       [[1., 1., 1.],
        [1., 1., 1.]],

       [[1., 1., 1.],
        [1., 1., 1.]],

       [[1., 1., 1.],
        [1., 1., 1.]],

       [[1., 1., 1.],
        [1., 1., 1.]]])

#7. Do a and b have the same size? How do you prove that in Python code?

a.size
b.size

a.size == b.size

True


#8. Are you able to add a and b? Why or why not?

other = np.add(a,b)
#operands could not be broadcast together with shapes (2,3,5) (5,2,3) 
#tienen misma dimensión pero diferente "distribución"


#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

c = b.transpose().reshape(2,3,5)

print(c)

[[[1. 1. 1. 1. 1.]
  [1. 1. 1. 1. 1.]
  [1. 1. 1. 1. 1.]]

 [[1. 1. 1. 1. 1.]
  [1. 1. 1. 1. 1.]
  [1. 1. 1. 1. 1.]]]

#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

d = np.add(a,c)

print(d)


[[[1.02472889 1.03156034 1.51580717 1.46631697 1.56668133]
  [1.53013533 1.3724969  1.19797413 1.36729391 1.99045247]
  [1.57633789 1.73761658 1.45033151 1.18644739 1.3014748 ]]

 [[1.39116425 1.29086419 1.47789771 1.46487231 1.16095184]
  [1.36504902 1.87508774 1.25568776 1.10814261 1.00561579]
  [1.64513572 1.15694519 1.26318638 1.63254261 1.23976145]]]

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

print(a)
print(d)

#.shape y .ndim son iguales, cambian los valores ya que el resultado de d es el de a + 1.

#12. Multiply a and c. Assign the result to e.

e = np.multiply(a, c)

print(e)

array([[[0.02472889, 0.03156034, 0.51580717, 0.46631697, 0.56668133],
        [0.53013533, 0.3724969 , 0.19797413, 0.36729391, 0.99045247],
        [0.57633789, 0.73761658, 0.45033151, 0.18644739, 0.3014748 ]],

       [[0.39116425, 0.29086419, 0.47789771, 0.46487231, 0.16095184],
        [0.36504902, 0.87508774, 0.25568776, 0.10814261, 0.00561579],
        [0.64513572, 0.15694519, 0.26318638, 0.63254261, 0.23976145]]])


#13. Does e equal to a? Why or why not?


e == a

array([[[ True,  True,  True,  True,  True],
        [ True,  True,  True,  True,  True],
        [ True,  True,  True,  True,  True]],

       [[ True,  True,  True,  True,  True],
        [ True,  True,  True,  True,  True],
        [ True,  True,  True,  True,  True]]])

#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

d_max = np.nanmax(d) 1.9904524741236012

d_min = np.nanmin(d) 1.0056157881193843

d_mean = np.mean(d) 1.388285339202042

#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

f = np.empty([2,3,5])

array([[[0.02472889, 0.03156034, 0.51580717, 0.46631697, 0.56668133],
        [0.53013533, 0.3724969 , 0.19797413, 0.36729391, 0.99045247],
        [0.57633789, 0.73761658, 0.45033151, 0.18644739, 0.3014748 ]],

       [[0.39116425, 0.29086419, 0.47789771, 0.46487231, 0.16095184],
        [0.36504902, 0.87508774, 0.25568776, 0.10814261, 0.00561579],
        [0.64513572, 0.15694519, 0.26318638, 0.63254261, 0.23976145]]])


"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""
for i in range(len(d)):
    for y in range(len(d[0])):
        for z in range(len(d[0, 0])):
            if d[i, y, z] > d_min and d[i, y, z,] < d_mean:
                f[i, y, z] = 25
            elif d[i, y, z] > d_mean and d[i,y,z,] < d_max:
                f[i, y, z] = 75
            elif d[i, y, z] == d_mean:
                f[i, y, z] = 50
            elif d[i, y, z] == d_min:
                f[i, y, z] = 0
            elif d[i, y, z] == d_max:
                f[i, y, z] = 100
             
# creo que voy bien encaminado por aquí, de hecho no se porqué no me sale, lo veré en clase...😩


"""
#17. Print d and f. Do you have your expected f?
For instance, if your d is:
array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])

Your f should be:
array([[[ 75.,  75.,  75.,  25.,  75.],
        [ 75.,  75.,  25.,  25.,  25.],
        [ 75.,  25.,  75.,  75.,  75.]],

       [[ 25.,  25.,  25.,  25., 100.],
        [ 75.,  75.,  75.,  75.,  75.],
        [ 25.,  75.,   0.,  75.,  75.]]])
"""


"""
#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
("A", "B", "C", "D", and "E") to label the array elements? You are expecting the result to be:
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
Again, you don't need Numpy in this question.
"""