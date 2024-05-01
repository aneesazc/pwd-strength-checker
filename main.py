import getpass
from check_strength import check_strength
from validate import validate

def main():
    password = getpass.getpass("Enter password:")
    if not validate(password):
        print("Password is invalid.")
        return
    score = check_strength(password)
    if score == 5:
        print("Password is very strong.")
    elif score == 4:
        print("Password is strong.")
    elif score >= 2:
        print("Password is moderate.")
    else:
        print("Password is weak.")
    # print("Password entered:", password)

if __name__ == "__main__":
    main()