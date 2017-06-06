
def fun1(num):
    return num*num

a = 10
b = fun1(a)

print(b)
print("########################")

###########################################

def fun2(str):
    print(str)

my_str = "String"

fun2(my_str)
print("########################")


###########################################

def fun3(a, b, c, d=1, e=2):
    return a+b+c+d+e

a = 5
b = 5
c = 5
d = 5
e = 5

x = fun3(a, b, c, d, e)

print(x)
print("########################")


###########################################

def fun4_1(v1):
    return v1/2

def fun4_2(v2):
    return v2*4

val = 10

result = fun4_1(val)

print(result)

result = fun4_2(result)

print(result)
print("########################")


###########################################

def fun5(str):
    try:
        return float(str)
    except ValueError:
        print("Enter a number dummy")

str = "8"

result = fun5(str)

if(result):
    print(result)

