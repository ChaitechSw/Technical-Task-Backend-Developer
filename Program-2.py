integer = int(input("Enter a : "))
count= 0 
for i in range(1, 100, 2):
    if count != integer:
        print(i, end=' ')
        count+=1    
    