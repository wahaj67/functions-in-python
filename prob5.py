def greet_user(name="Guest"):
    
    return f'{name} nice  to meet you'

def main():
    user = input('Enter your name:').strip()
    if not user:
        res = greet_user()
    else:
        res = greet_user(user)
    print(res)
if __name__ == "__main__":
    main()