#//program no 2
#//03/11/22
#//reverse the three digit number

n = 987
r = n%10
q = n//10
r1 = q%10
q1 = q//10


print("r value=", r, "\n", "q value=", q, "\n", "r1 value=", r1, "\n", "q1 value=", q1)
a = 100
b = 10
c = 1
e = r*a
f = r1*b
g = q1*c

print("e value=", e, "\n", "f value=", f, "\n", "g value=", g)
add = (e+f+g)
print(add)
