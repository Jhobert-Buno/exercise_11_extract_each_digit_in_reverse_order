# Exercise 11: Write a Program to extract each digit from an integer in the reverse order.
# For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits

#create functions
def extract_and_reverse(number):
    print("The number is: ", number)
    original_number = str(number)
    reverse_number = original_number[::-1]
    
    #to extract the numbers
    for digit in reverse_number:
        print( digit, end=' ')


#given
given_number = 7536
extract_and_reverse(given_number)