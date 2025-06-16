print('hello this is just for demo')
print('Step 1 complete')
print('Added Step 2')

# app.py
def is_prime(n):
    """Returns True if n is a prime number, else False."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("Krithi"))
    def main():
    print("Choose an option:")
    print("1. Greet")
    print("2. Square a number")
    print("3. Factorial")
    print("4. Reverse string")
    print("5. Check if number is prime")   # <== ✅ Add this

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        print(greet(name))
    elif choice == "2":
        n = int(input("Enter number: "))
        print(square(n))
    elif choice == "3":
        n = int(input("Enter number: "))
        print(factorial(n))
    elif choice == "4":
        s = input("Enter string: ")
        print(reverse_string(s))
    elif choice == "5":   # <== ✅ Add this block
        n = int(input("Enter number: "))
        print(is_prime(n))
    else:
        print("Invalid choice")


