file_handler = open("sample.txt","r") #reads the file if present
try:
        print("Reading file content: \n")
        print("Line 1: ", file_handler.readline())#prints 1st line of the text file
        print("Line 2: ", file_handler.readline())#prints 2nd line of the text file
except:
    print("Error: The file'sample.txt' was not found.")#to print if file not present
file_handler.close()