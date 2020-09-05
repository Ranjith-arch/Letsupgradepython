In [3]:
#1st question

num = int(input("Enter the altitude :"))
if (num <= 1000):
    print("Land the plane")
elif (num > 1000 and num < 5000):   
    print("Come down to 1000ft")
else :
    print("Go around and try later")
Enter the altitude : 8012
Go around and try later
