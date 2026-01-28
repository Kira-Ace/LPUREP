# Legaspi, Jazztinn Kyle G. | CS 101

def main():
    x = int(input("What's even? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return (n % 2 == 0) # simplified
    # if n % 2 == 0 return True else Even

main()