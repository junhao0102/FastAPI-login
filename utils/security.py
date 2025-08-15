import bcrypt

def hashPassword(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def verifyPassword(password,hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))