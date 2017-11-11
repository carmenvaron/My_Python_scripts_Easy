#Script that deletes position n in a given string and returns the output.
def remove_char():
    #Checking if input variables are right
    input_string=input("Please insert the string: ")
    if len(input_string)==0:
        print("The empty string has nothing that can be deleted")
        return
    n=input("Please insert the position you want to delete: ")
    while (not n.isdigit()) or (int(n) > len(input_string)-1):
        if not n.isdigit():
            print(n, "is not a number.")
            n=input("Please enter a position with a number: ")
        elif int(n) > len(input_string)-1:
            print("The string is shorter than", n, "characters.")
            n=input("Please enter a valid position: ")
        
    #Removing char n
    n=int(n)
    output_string=input_string[:n-1] + input_string[n:]
    print("Solution:\n",output_string)

remove_char()
