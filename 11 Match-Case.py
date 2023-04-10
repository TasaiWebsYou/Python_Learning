x=int(input("Enter value of X: "))

match x :
    case 0:
        print("X is zero")
    case _ if x==90:
        print("X is equal to 90")
    case _ if x==70:
        print("X = 70")
    case _ if x==x:
        print("X is a number")