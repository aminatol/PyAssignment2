#1
def max_mum(x, y):
    maxNum = x.index(max(x))
    print ("The maximum number is", maxNum + 1)
 

x = [3, 4, 1, 3, 4, 5]
max_mum(x, len(x))

#2

def mult_list(list): 
    result = 1
    for x in list:
        result= result*x
    return result
list=[2,4,6,8,7,5,4,3,2]
print(mult_list(list))

def rev_string(x):
    string= ''
    for i in x:
        string= i+string
    return string
x= "PythonisAwesome"
print(rev_string(x))

def num_within(x):
    if 3 <= x <= 8:
        print("Yes. The number is in range")
    else:
        print("No. The number is not in range")
num_within(x)