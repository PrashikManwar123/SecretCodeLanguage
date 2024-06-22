import random
import string


# Function for coding :
def code() :
    string1 = input("Enter the word you want to code :")
    
    def CodeForGreaterThan3(string1) : # This func appends the first character to the last and remaining string is as it is. 
        if len(string1)==0 :    # For string length zero   
            print(string1)
        else : # for string length greater than 3
            x = string1[1:] + string1[0]
            # Below is the code for inserting 3 random chars at starting and ending of the string 
            # Here, "new_string" will be our string in coded form.
            original_string = x 
            def random_chars(length = 3) :
                return "".join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k = length))
    
            prefix = random_chars(3)
            suffix = random_chars(3)

            new_string = prefix + original_string + suffix
            print(new_string)
            

    def CodeForLessThan3(string1) : # This is a function which reverses the string1
        if len(string1)==0 :
            return string1
        else :
            return (CodeForLessThan3(string1[1:]) + string1[0])

    print("The coded word is :")
    if len(string1)<3 :
        print(CodeForLessThan3(string1))
    else :
        print(CodeForGreaterThan3(string1))
        
        
        
        
# Function for decoding :
def decode() :
    string1 = input("Enter the word you want to decode :")
    
    def DeCodeForGreaterThan3(string1) : # Here the func removes starting and ending 3 letters in the string and 
        if len(string1)==0 :             # places the last character of the remaining string at the starting
            print(string1)
        else :
            print(string1[9] + string1[3:9])
            
    def DeCodeForLessThan3(string1) : # This func reverses the string 1
        if len(string1)==0 :
            return string1
        else :
            return (string1[-1] + DeCodeForLessThan3(string1[:-1]))
        
    print("The decoded word is :")
    if len(string1)<3 :
        print(DeCodeForLessThan3(string1))
    else :
        print(DeCodeForGreaterThan3(string1))
        
        
        
        
                
# Function for selection whether to code or decode
def selection() :
    a = int(input("select 1 for code and 2 for decode : "))

    if a == 1 :
        print(code())
    else :
        print(decode())
        
        

selection()

        
        
            

    

    






    
