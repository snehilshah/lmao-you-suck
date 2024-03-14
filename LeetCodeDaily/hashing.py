import bcrypt

password = b"password"

# Adding the salt to password
salt = bcrypt.gensalt()
# Hashing the password
hashed = bcrypt.hashpw(password, salt)

# printing the salt
print("Salt :")
print(salt)

# printing the hashed
print("Hashed")
print(hashed)

trying_password = "$2b$12$UqwWD.Gkpah2ypvHsRIEzOZFg.flmcdxRfbaYqx3t4nfyhrmLiRqG"

if hashed == trying_password:
    print("Password hacked")
