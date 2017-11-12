#Code that resolves this exercise: https://www.codechef.com/problems/ANKPAL:
    #You have to write a program that answers Q queries on a string S.
    #Each query contains four integers (i, j, k, l). For every query, first reverse the substring s[i, j] (inclusive) and then report if substring s[k, l] (inclusive) is a palindrome.

#Input variables and checking if they are right
s=input("Please introduce your string: ")
if len(s)==0:
    print("With the empty string, whatever the other inputs are, the answer is going to be Yes")
else:
    q=input("Please introduce how many queries you are going to do: ")
    flag=0
    while flag==0:
        try:
            q=int(q)
            if q<=0:
                print("The number of queries has to be positive.")
                q=input("Please introduce a positive number of queries to be performed: ")
            else:
                flag=1
        except ValueError:
            print(q,"is not a number.")
            q=input("Please introduce a number of queries to be performed: ")
    
    for b in range(q):
        numbers=input("Please introduce i,j,k,l separated by a comma: ").split(',')
        while len(numbers)<4:
            print("Four positions are needed.")
            numbers=input("Please introduce the 4 positions separated by a comma: ").split(',')
        flag=0
        while flag==0:
            try:
                i=int(numbers[0]) 
                j=int(numbers[1])
                k=int((numbers[2]))
                l=int((numbers[3]))
                if i<=0 or j<=0 or k<=0 or l<=0:
                    print("The positions have to be positive numbers.")
                elif i>len(s) or j>len(s) or k>len(s) or l>len(s):
                    print("The 4 positions can be as maximum", len(s), "(the lenght of the string)")
                elif i>j:
                    print("i has to be smaller than j")
                elif k>l:
                    print("k has to be smaller than l")
                else:
                    flag=1
            except ValueError:
                print("All the positions have to be numbers")
            if flag==0:
                numbers=input("Please introduce the 4 positions separated by a comma: ").split(',')
                
    #Reversing the substring s[i, j]
        if i==1:
            s_reverse=s[:i-1]+s[j-1::-1]+s[j:]
        else:
            s_reverse=s[:i-1]+s[j-1:i-2:-1]+s[j:]
            
    #Checking if s[k,l] is palindromic
        sol=[]
        result='Yes'
        if k==1:
            if s_reverse[k-1:l:] != s_reverse[l-1::-1]:
               result='No'
        else:
            if s_reverse[k-1:l:] != s_reverse[l-1:k-2:-1]:
                result='No'
        sol.append(result)
    
    #Solution
    print("\nSolution:\n")
    for d in range(q):
        print("Palindromic query", d+1, ":", sol[d])
