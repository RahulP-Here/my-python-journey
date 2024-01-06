print("Python Program to Swap Two Variables".center(100, "."))

def swap(a, b):
    temp = a
    a = b
    b = temp
    print("\n--> Swapping Value <--")
    print(f"\n a: {a} \n b: {b}")

a = input("a : ")
b = input("b : ")
swap(a, b)
