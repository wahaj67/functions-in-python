def calculate_sqr(num):
    return num * num

def main():

    user_input = int(input("Enter a number to check the  square:")) 
    res = calculate_sqr(user_input)
    print(f'your given number suqare is {res}')

if __name__ == "__main__":
    main()