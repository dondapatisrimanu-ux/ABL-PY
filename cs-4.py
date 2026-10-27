import string
import getpass
def validate_password(password):
    results = {
        "Minimum 8 characters": len(password) >= 8,
        "At least one uppercase letter": any(
            ch.isupper() for ch in password
        ),
        "At least one lowercase letter": any(
            ch.islower() for ch in password
        ),
        "At least one digit": any(
            ch.isdigit() for ch in password
        ),
        "At least one special character": any(
            ch in string.punctuation for ch in password
        ),
        "No whitespace characters": not any(
            ch.isspace() for ch in password
        )
    }
    return results
def main():
    print("=" * 40)
    print(" PASSWORD POLICY VALIDATION ENGINE")
    print("=" * 40)
    password = getpass.getpass("Enter your password: ")
    results = validate_password(password)
    print("\nPASSWORD VALIDATION REPORT")
    print("-" * 40)
    for rule, passed in results.items():
        status = "PASS" if passed else "FAIL"
        print(f"{rule:<32} : {status}")
    if all(results.values()):
        print("\nResult: Password is VALID.")
    else:
        print("\nResult: Password is INVALID.")
        print("Please correct the failed rules.")

    print("-" * 40)


if __name__ == "__main__":
    main()