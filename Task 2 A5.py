list = [] #empty list
for i in range(1,11):#range from 1 to 11 as 1 is included and 11 is excluded.
    list.append(i)
print(f"Original list: {list}")
extracted_list = list[0:5] #extracting first 5 elements using slicing.
print(f"Ectracted first five elements are: {extracted_list}")
reverse_list = extracted_list[::-1] # slicing the list using step as -1 so as to reverse it.
print(f"Reversed extracted elements: {reverse_list}")