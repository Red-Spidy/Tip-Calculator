import sys
print('Welcome to the Tip Calculator')
a = float(input("Enter The Bill amount = "))
b = float(input('Enter the Percentage of Tip = '))
c = int(input('Enter the number of Persons for which you want to split the Bill= '))
total_bill = a + b*a/100
if c==1:
    split_bill = total_bill / c
    print(f'You have to pay {split_bill:.2f}')
elif c==0:
    print("Invalid Input")
    sys.exit()
else:
    split_bill = total_bill / c
    print(f'Each Person has to pay {split_bill:.2f}')
