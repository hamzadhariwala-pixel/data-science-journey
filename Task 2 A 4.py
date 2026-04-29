user_input_1 = input("Enter text to write to the file: ")#taking first input.
fh = open("output.txt","w")#using write mode so that if a file exists/does not exist will not matter.
fh.write(str(user_input_1))#writing the first line of the new text file
print("Data successfully written to output.txt")

user_input_2 = input("Enter additional text to append: ")#taking second input.
fh = open('output.txt','a') #using append mode to be able to append the existing file.
fh.write("\n")#adding new line to get the favourable output.
fh.write(user_input_2)#writing the new line given by the user.
print("Data successfully appended.\n")

fh =open("output.txt","r")#using read mode so as to get the output correctly.
print("Final content of output.txt: \n")
print(fh.readline())#prints line 1
print(fh.readline())#prints line 2