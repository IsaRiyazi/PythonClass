list1 = [1, 1, 4, 5]

def list_def(list1):
    if list1:
        if list1 != list(set(list1)):
            print(False)
        elif list1 == sorted(list1):
            print("true")

        else:
            print("not true")
    else:
        print("trueeee")


num = int(input("enter your number: "))
def even_odd(num):

    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")


even_odd(num)
