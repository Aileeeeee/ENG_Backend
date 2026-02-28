def is_valid_password(password):
    return(
        len(password) >= 8 and 
        any(char.isupper() for char in password) and
        any(char.islower() for char in password) and
        any(char.isdigit() for char in password)
    )
