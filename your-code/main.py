#1. Import the NUMPY package under the name np.
import numpy as np
import random

#2. Print the NUMPY version and the configuration.

print(np.version.version)

#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

a = np.random.rand(2,3,5)


#4. Print a.


print(a)

#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

b = np.ones((5,2,3))


#6. Print b.

print(b)

#7. Do a and b have the same size? How do you prove that in Python code?

print(a==b)

print ("False, no tienen el mismo size")


#8. Are you able to add a and b? Why or why not?

print("Para poner hacer el add tienen que tener el mismo número de filas y de columnas. En este caso no es así")


#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

c = b.transpose (1,2,0)
print(c)

print("en esta pregunta me he liado porque transpose lo entiendo para darle la vuelta al array")
print("he buscado en internet y me aparecía como lo he aplicado arriba y he entendido la lógica")
#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

d = np.add(a,c)
print("ahora si se puede porque son iguales.")

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

print(a)
print(b)



#12. Multiply a and c. Assign the result to e.

e = np.multiply(a,c)
print(e)

#13. Does e equal to a? Why or why not?

print(e==a)

print("True,si son iguales.")

#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

d_max = np.max(d)
d_min = np.min(d)
d_mean = np.mean(d)

print(d_max)
print(d_min)
print(d_mean)

#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

f = np.empty((2,3,5))
print(f)

print("En Jupyter me da diferente a lo que me imprime la terminal")
'''
[[[-0.00000000e+000 -0.00000000e+000  7.90505033e-323  0.00000000e+000
    0.00000000e+000]
  [ 5.02034658e+175  1.22253613e+161  9.41925029e-047  9.68567164e-071
    2.27195119e+184]
  [ 6.14811263e-144  1.12855837e+277  2.87505069e+161  1.47763641e+248
    1.16096346e-028]]

 [[ 9.42863347e-143  4.82337723e+228  1.41946975e+161  1.86282370e+160
    2.61836504e+180]
  [ 1.60535515e-051  4.50617826e-144  3.38040122e-067  8.26108324e-072
    2.29766951e-028]
  [ 9.50116089e-043  1.14484254e+243  9.51498384e-053  1.03723812e-314
    0.00000000e+000]]]

"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.

df[(df.ages > 60) & (df.has_children)]





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