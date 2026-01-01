import validators

if validators.email(input("Email: ").strip()):
    print("Valid")
else:
    print("Invalid")

