"""Write a program that reads values from the user 
until a blank line is entered. Display
the total of all of the values entered by the user 
(or 0.0 if the first value entered is
a blank line). Complete this task using recursion. 
Your program may not use any loops."""

def blank_counter(ch):
    s = input("enter value: ")
    
    if s != " ":
         print ("no blank line detected")
         ch = ch + 1
         blank_counter(ch)
     
    else: 
        return print(ch, "values were entered before a blank was detected") 
     
ch = 0
ch = blank_counter(ch)

#%%

"""Write a program that implements Euclid’s algorithm and uses it to determine the
greatest common divisor of two integers entered by the user. Test your program with
some very large integers. The result will be computed quickly, even for huge numbers
consisting of hundreds of digits, because Euclid’s algorithm is extremely efficient."""

def mcd (a,b):
    if b == 0:
        return 0
    else:
        return mcd(b, a % b)
            

numa = int(input("Ingrese un numero a: "))
numb = int(input("ingrese un numero b: "))

print("the mcd is", mcd(numa,numb))

#%%

"""
Write a recursive function that converts a non-negative decimal number to binary.
Treat 0 and 1 as base cases which return a string containing the appropriate digit.
 
For all other positive integers, n, you should compute the next digit using the remainder
operator and then make a recursive call to compute the digits of n // 2. 

Finally, you should concatenate the result of the recursive call (which will be a string) and the
next digit (which you will need to convert to a string) and return this string as the
result of the function.

Write a main program that uses your recursive function to convert a non-negative
integer entered by the user from decimal to binary. Your program should display an
appropriate error message if the user enters a negative value.
"""

def binary(n):
    if n < 0:
        return print("null")
    elif n == 1:
        return "1"
    elif n == 0:
        return "0"
    
    else:
        return binary(n // 2) + str (n % 2)
        

n = int(input("escriba un numero: "))
print(binary(n))

#%%

"""Write a program that reads a word from the user and then displays its phonetic
spelling. For example, if the user enters Hello then the program should output
Hotel Echo Lima Lima Oscar. Your program should use a recursive function to perform this task. 
Do not use a loop anywhere in your solution. Any non-letter
characters entered by the user should be ignored."""
    
def phonetic (p,nato_alphabet):
    
    if p.isalpha() == True:
        
        for i in range(len(p)): 
            if p[i].upper() in nato_alphabet:
                print(nato_alphabet[p[i].upper()])
                
    else:
        return []



p = str(input("introduzca una palabra: "))
nato_alphabet = {
    'A': 'Alpha',
    'B': 'Bravo',
    'C': 'Charlie',
    'D': 'Delta',
    'E': 'Echo',
    'F': 'Foxtrot',
    'G': 'Golf',
    'H': 'Hotel',
    'I': 'India',
    'J': 'Juliet',
    'K': 'Kilo',
    'L': 'Lima',
    'M': 'Mike',
    'N': 'November',
    'O': 'Oscar',
    'P': 'Papa',
    'Q': 'Quebec',
    'R': 'Romeo',
    'S': 'Sierra',
    'T': 'Tango',
    'U': 'Uniform',
    'V': 'Victor',
    'W': 'Whiskey',
    'X': 'Xray',
    'Y': 'Yankee',
    'Z': 'Zulu'
}
phonetic(p,nato_alphabet)

#%%

"""Create a recursive function that converts a Roman numeral to an integer. Your
function should process one or two characters at the beginning of the string, and
then call itself recursively on all of the unprocessed characters. Use an empty string,
which has the value 0, for the base case. In addition, write a main program that reads
a Roman numeral from the user and displays its value. You can assume that the value
entered by the user is valid. Your program does not need to do any error checking."""

def roman(a,numeros):
    if a in numeros: 
        
        n = numeros[a]
        return n
    
    else:
        
        if numeros[a[0]] > numeros[a[1]] :
           n = numeros[a[0]] + numeros[a[1]]
           
        elif numeros[a[0]] < numeros[a[1]] :
            n = numeros[a[1]] - numeros[a[0]] 
        
        return n
     
        
        

    
a = (input("enter a number in roman numerals: ")).upper()
numeros = {'M' : 1000, 'D':500, 'C':100, 'X':10, 'V':5, 'I':1 }
n = roman(a,numeros)
print (n)

#%%

"""Write a recursive function that decompresses a run-length encoded list. Your
recursive function will take a run-length compressed list as its only argument. It will
return the decompressed list as its only result. Create a main program that displays
a run-length encoded list and the result of decoding it."""

def decompress(lista):
    
    if not lista:
        return []

    value, count = lista[0], lista[1]
    pito = value * count
    
    print (pito)
    return (pito) , decompress(lista[2:])

    

lista = ["A", 12, "B", 4, "A", 6, "B", 1]

decompress(lista)
    
#%%

"""
fibionacci
"""

n = int(input("enter a number for the fib sequence: "))

def fibio (n):
    if n < 2:
        return n
    else:
        return fibio(n - 1) + fibio(n-2)
    

print(fibio(n))
