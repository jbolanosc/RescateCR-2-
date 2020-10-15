from .. import bcrypt


def validate_password(password, msg):
    if len(password) < 6:
        msg = "Password must be more than 6 characters"
        return msg
    if len(password) > 20:
        msg = "Password must be less than 20 characters"
        return msg
    if not any(char.isdigit() for char in password):
        msg = "Password must contain numbers"
        return msg
    if not any(char.isalpha() for char in password):
        msg = "Password must contain letters"
        return msg
    else:
        return msg


def hash_password(password):
    hashed = bcrypt.generate_password_hash(password, 12).decode('UTF8')
    return hashed


def check_password(hashed_password, password):
    checked = bcrypt.check_password_hash(hashed_password, password)
    return checked