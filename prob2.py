def multiple_parameter(num1:int,num2:int)->int:
    return num1 + num2

def main():
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number to add: '))

    print(f'The sum of {num1} and {num2} is {multiple_parameter(num1,num2)}')

if __name__ == "__main__":
    main()