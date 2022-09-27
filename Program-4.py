take_input = input("Enter the list : ").strip('[,]').split(',')
new_dict = {}
for i in range(1, 10):
    count1= 0
    for num in take_input:
        if int(num) % i == 0 :
            count1 += 1
    new_dict[i] = count1
print(new_dict)
