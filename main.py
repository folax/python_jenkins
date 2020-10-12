def changeValues(a, b):
    print("input A = [%d] B = [%d]" % (a, b))
    a=a+b
    b=a-b
    a=a-b
    str=("output A = [%d] B = [%d]" % (a, b)) 
    return str

print(changeValues(3, 5))
