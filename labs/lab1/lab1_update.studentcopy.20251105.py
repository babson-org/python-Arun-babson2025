# ==============================
# Main Program
# ==============================
'''
def main():
    while True:
        print("Lab 1 - Python Basics")
        print("1. Draw Diamond")
        print("2. Text Analysis")
        print("3. Caesar Cipher")
        choice = input("Select part to run (1-3): ")
        
        if choice == "1":
            draw_diamond()
        elif choice == "2":
            text_analysis()
        elif choice == "3":
            caesar_cipher()
        else:
            exit()




Lab 1 - Python Basics
Author: <Your Name>
Instructions: Complete each part below. Save your work and commit + sync in Codespaces.


# ==============================
# Part 1: Draw a Diamond
# ==============================
# not much to explain here, straightforward with each part. the first part is basically ensuring user inputs a positive odd number or else the diamond can't run
# the next parts initially i had the diamond filled and not empty, but had to switch it and make the diamond empty
'''

def draw_diamond():
    """
    Ask the user for an odd number for the diamond height
    and print a symmetric diamond of that height.
    """
    height = 0
    # TODO: Prompt user for an odd number
    '''
    indentation here is wrong. what you have above is
    your entire function. what's below is outside the
    function and in global scope.  Need to shift everything
    below by 4 spaces

while True:
    
    use a try catch block with an else here.
    
    
    height = int(input("Enter an odd number for the diamond height: "))
    if height % 2 == 1 and height > 0 : 
        break 
    print ("please enter a positive odd number")

#can't have negative number or even number
        
    
    # TODO: Draw the top half of the diamond
    # when i == 0 this essentially means only draw one x on top row then the rest is hollow. Also had to make it so there was ..x or spaces before the x was inputted because if not 
    #the diamond would be symmetrical
for i in range (height // 2 + 1):
    spaces = " " * (height // 2-i)
    if i == 0: 
        print (spaces + 'x')
    else: 
        inner = 2 * i - 1 # for some reason when i tried to just do the inner 2*i-1 in the print statement it wouldn't work. so i had to make inner a variable and it worked
        print (spaces + 'x' + " " * inner + "x")

    # TODO: Draw the bottom half of the diamond
    #pretty much mirrored, it, the 2 - 1, -1 -1 
for i in range (height // 2 - 1,-1,-1):
    spaces = " " * (height // 2-i)
    if i == 0: 
        print (spaces + 'x')
    else: 
        inner = 2 * i - 1 
        print (spaces + 'x' + " " * inner + "x")
    '''


    # TODO: Draw the top half of the diamond
    # when i == 0 this essentially means only draw one x on top row then the rest is hollow. Also had to make it so there was ..x or spaces before the x was inputted because if not 
    # the diamond would be symmetrical

    while True:
    
    
        height = int(input("Enter an odd number for the diamond height: "))
        if height % 2 == 1 and height > 0 : 
            break 
        print ("please enter a positive odd number")

    for i in range (height // 2 + 1):
        spaces = " " * (height // 2-i)
        if i == 0: 
            print (spaces + 'x')
        else: 
            inner = 2 * i - 1 # for some reason when i tried to just do the inner 2*i-1 in the print statement it wouldn't work. so i had to make inner a variable and it worked
            print (spaces + 'x' + " " * inner + "x")

        # TODO: Draw the bottom half of the diamond
        #pretty much mirrored, it, the 2 - 1, -1 -1 
    for i in range (height // 2 - 1,-1,-1):
        spaces = " " * (height // 2-i)
        if i == 0: 
            print (spaces + 'x')
        else: 
            inner = 2 * i - 1 
            print (spaces + 'x' + " " * inner + "x")

draw_diamond()


# ==============================
# Part 2: Count Letters, Words, and Sentences
# ==============================


def text_analysis():
    """
    Ask the user for a block of text.
    Count and display:
        - Number of letters (only count a-zA-Z)
        - Number of words   (use split())
        - Number of sentences (., ?, !) 
    """
    # TODO: Get user input
    text = input("Enter some text: ")

    # TODO: Count letters
    letters = 0
    for char in text:
        if char .isalpha():
            letters += 1     
    #if characters typed are in the alphabet then the letters go up by 1

    # TODO: Count words
    words = len(text.split())
    #words are counted by len and split used to count individual words

    # TODO: Count sentences
    sentences = 0 
    for char in text:
        if char in "?!.":
            sentences += 1
    #again pretty straight forward, any ending sentence punctuation increases sentence count
        


    # TODO: Print the results
    print(f"Letters: {letters}")
    print(f"Words: {words}")        
    print(f"Sentences: {sentences}")   
# Uncomment to test Part 2
text_analysis()


# ==============================
# Part 3: Caesar Cipher – Encrypt and Decrypt
# ==============================
def caesar_cipher():
    """
    Ask the user for text and a shift value.
    Provide options to encrypt or decrypt the text using a Caesar cipher.
    """

    print("you have some work todo!, caesar_cypher")

    # TODO: Get user input text
    text = input("Enter text: ")

    # TODO: Get shift value
    shift = int(input("Enter shift value (integer): "))
    # how much we will shift each letter by

    # TODO: Ask user whether to encrypt or decrypt
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()
    #straightforward user chooses whether to encrypt or decrypt. lower just ensures E turns into e 
    

    # TODO: Implement encryption and decryption logic
    result = ""
    
    #reverse the shift
    if choice == 'd':
        shift = -shift

    for char in text:
        if char.isalpha():
            if char.isupper(): #if character is uppercase if not the lowercase is below
                base = ord('A') #ord is assigning letters to #'s
                shifted = (ord(char) - base + shift) % 26
                result += chr(shifted + base) #chr is the inverse of ord and essentially reverses the number back to the letter
            else:
                base = ord('a')
                shifted = (ord(char) - base + shift) % 26
                result += chr(shifted + base)
        else:
            result += char 

    # TODO: Print the final result
    print("Result:", result)

# Uncomment to test Part 3
caesar_cipher()


'''

if __name__ == "__main__":
    main()
'''