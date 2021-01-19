#1. Import the NUMPY package under the name np.
import numpy as np


#2. Print the NUMPY version and the configuration.

"""
print(np.__version__)
"""

#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?


a = np.random.randint(0, 10,(2,3,5))



print(a.ndim)


#4. Print a.

print(a)
print ('Esto es A')


#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"


b = np.ones((5, 2 , 3))

#6. Print b.

print(b)
print ('Esto es B')


#7. Do a and b have the same size? How do you prove that in Python code?


print(a.shape == b.shape)
print( 'son iguales??')




#8. Are you able to add a and b? Why or why not?
"""
suma  = a + b
"""
"""
print(suma)   #No , por que tienen shapes diferentes . "with shapes (2,3,5) (5,2,3) ""
"""

#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

c = np.transpose(b, (1,2,0))

print(c)
print ('Esto es c')



#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

d = a + c 

print(d)
print ('Esto es D = a + c ')

#porque a y c son 2x3x5 



#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

print(a)
print('esto es A')


print(d)
print ( ' esto es D')

# la diferencia que veo es que al lado de cada numero en D aparece un punto. se convierte en float al realizar la suma. 



#12. Multiply a and c. Assign the result to e.

e = a * c

print (e)
print (' esto es E = a*c ')

#13. Does e equal to a? Why or why not?
 
iguales = np.allclose(a,e)
print(iguales)



#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

d_max = d.max()

print(d_max)
print('el maximo ')

d_min = d.min()
print(d_min)
print('el minimo')


d_mean = d.mean()
print(d_mean)
print('la media')




#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

f = np.empty( (2,3,5) )

print(f)
print('esto es F empty')






"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""
"""
f[(d_mean>d) & (d>d_min)]=25
f[(d_max>d) & (d>d_mean)]=75
f[d==d_mean]=50
f[d==d_min]=0
f[d==d_max]=100

print(f)
"""

f = []

for num in d: 
        for subnum in num:
                for num3 in subnum:
                        if d_min < num3 < d_mean:
                                f.append(25)
                        elif d_mean < num3 < d_max:
                                f.append(75)
                        elif num3 == d_mean:
                                f.append(50)
                        elif num3 == d_min:
                                f.append(0)
                        elif num3 == d_max:
                                f.append(100)

f = np.array(f).reshape(2,3,5)
print(f)
print ('esta es la matriz nueva F con el for loop ')



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
h = []

for num in f: 
        for subnum in num:
                for num3 in subnum:
                        if num3 == 0:
                                h.append('A')
                        elif num3 == 25:
                                h.append('B')
                        elif num3 == 50:
                                h.append('C')
                        elif num3 == 75:
                                h.append('D')
                        elif num3 == 100:
                                h.append('E')

h = np.array(h).reshape(2,3,5)
print(h)
print ('con letras')
