try:
    list=[10,20,30,40,50]
    a=int(input("enter the index of the list:"))
    print(list[a])
except IndexError:
    print("check your index")
