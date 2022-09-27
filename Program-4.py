take_input = input("Enter the list : ").strip('[,]').split(',')
# print(take_input)
# input_list = [1,2,8,9,12,46,76,82,15,20,30]
new_dict = {}
for i in range(1, 10):
    count1= 0
    for num in take_input:
        if int(num) % i == 0 :
            count1 += 1
    new_dict[i] = count1
print(new_dict)