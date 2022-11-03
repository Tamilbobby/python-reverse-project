#//program no 1
#//03/11/22
#//reverse the four digit number

n = 9876
r = n%10
q = n//10
r1 = q%10
q1 = q//10
s1 = q1%10
t1 = q1//10


print("r value=", r, "\n", "q value=", q, "\n", "r1 value=", r1, "\n", "q1 value=", q1,  "\n" "s1 value=", s1, "\n", "t1 value=", t1)
a = 1000
b = 100
c = 10
d = 1
e = r*a
f = r1*b
g = s1*c
h = t1*d
print("e value=", e, "\n", "f value=", f, "\n", "g value=", g, "\n",  "h value=", h )
add = (e+f+g+h)
print(add)
