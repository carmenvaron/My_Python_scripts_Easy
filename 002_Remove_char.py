#Script that deletes position n in a given string and returns the output.

#Checking if input variables are right
input_string=input("Please insert the string: ")
if len(input_string)==0:
    print("The empty string has nothing that can be deleted")
else:
    n=input("Please insert the position you want to delete: ")
    while (not n.isdigit()) or (int(n) > len(input_string)-1) or (int(n)==0):
        if not n.isdigit():
            print(n, "is not a number.")
        elif int(n) > len(input_string)-1:
            print("The string is shorter than", n, "characters.")
        else:
            print("The position has to be a positive number")
        n=input("Please enter a valid position: ")
        
    #Removing char n
    n=int(n)
    output_string=input_string[:n-1] + input_string[n:]
    print("Solution:\n",output_string)
