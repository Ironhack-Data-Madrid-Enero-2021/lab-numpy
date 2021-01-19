#1. Import the NUMPY package under the name np.

import numpy as np

#2. Print the NUMPY version and the configuration.

print(np.version.version)

#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

a = np.random.randint(0, 100, (2, 3, 5))

#4. Print a.

print("a:")
print(a)

#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

b = np.ones((5, 2, 3))

#6. Print b.

print("b:")
print(b)

#7. Do a and b have the same size? How do you prove that in Python code?

print("Do they have the same shape?: ", a.shape == b.shape)
print("Do they have the same size?: ", a.size == b.size)


#8. Are you able to add a and b? Why or why not?

        #print(a+b)
print("We can't add a and b because their shape is not the same, they don't have the same dimensions")

#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

c = b.reshape((2, 3, 5))
print("c:")
print(c)


#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

d = a + c
print("d:")
print(d)

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

print("a:")
print(a)
print("d:")
print(d)
print("With reshape it works because you can add two matrixes with the same dimensions")


#12. Multiply a and c. Assign the result to e.

e=a*c
print("e: ")
print(e)


#13. Does e equal to a? Why or why not?

print("Is e=a? ")
print(e==a)
print("It is the same because you multiply by 1, c is a matrix with all the elements equal to 1.")


#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

d_max = d.max()
d_min = d.min()
d_mean = d.mean()
print(f"The maximum value is {d_max}, the minimum is {d_min}, and the mean is {d_mean.round(2)}.")


#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

f = np.empty((2, 3, 5))
print("f: ")
print(f)


"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""

f[(d_mean>d) & (d>d_min)]=25
f[(d_max>d) & (d>d_mean)]=75
f[d==d_mean]=50
f[d==d_min]=0
f[d==d_max]=100



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

print("e: ")
print(e)
print("New f: ")
print(f)
print("I have my expected f :)")

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
print(f.shape[0])
print(f.shape[1])
print(f.shape[2])

dim1=[]
dim2=[]
dim3=[]
for i in range(f.shape[0]):
        for j in range(f.shape[1]):
                for k in range(f.shape[2]):
                        if (d_mean>e[i][j][k]) and (e[i][j][k]>d_min):
                                dim1.append('A')
                        elif (d_max>e[i][j][k]) and (e[i][j][k]>d_mean):
                                dim1.append('B')
                        elif e[i][j][k]==d_mean:
                                dim1.append('C')
                        elif e[i][j][k]==d_min:
                                dim1.append('D')
                        elif e[i][j][k]==d_max:
                                dim1.append('E')
                dim2.append(dim1)
                dim1=[]
        dim3.append(dim2)
        dim2=[]
                
                        
print(dim3)
