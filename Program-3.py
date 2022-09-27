integer = int(input("Enter a : "))
count= 0 
if integer % 2 != 0:
    for i in range(1, 100, 2):
            if count != integer:
                print(i, end=' ')
                count+=1
else:
    for i in range(1, 100, 2):
            if count != integer-1:
                print(i, end=' ')
                count+=1