'''
Take input from user: That how many number you want to found out as palindrome
If user type a palindrome than return as it is and if it is not than type the next palindrome
Input:3
451
10
2133

Output:
Next palindrome for 451 is 454
Next palindrome for 10 is 11
Next palindrome for 2133 is 2222
'''

def next_palindrome(n):
    n=n+1
    while not is_palindrome(n):
        n+=1
    return n
def is_palindrome(n):
    return str(n) == str(n)[::-1]

if __name__ == '__main__':

    n=int(input("Enter the number of test cases"))
    numbers=[]

    for i in range(n):
        number=int(input("Enter the number:\n"))
        numbers.append(number)

    print(numbers)

    for i in range(n):
        print(f"Next palindrome for {numbers[i]} is {next_palindrome(numbers[i])}")