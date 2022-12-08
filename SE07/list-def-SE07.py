

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


def even_odd(num):

    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")


if __name__ == '__main__':
    list1 = [1, 1, 4, 5]
    num = int(input("enter your number: "))
    even_odd(num)
