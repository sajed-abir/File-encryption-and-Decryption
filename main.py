from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open("mykey.key", "wb") as mykey:
    mykey.write(key)

with open("Group_1-1.pdf", "rb") as original_file: #Put the original file name
    original = original_file.read()

f = Fernet(key)
encrypted = f.encrypt(original)

with open("enc_Group_1-1.pdf", "wb") as encrypted_file: 
    encrypted_file.write(encrypted)

decrypted = f.decrypt(encrypted)

with open("dec_Group_1-1.pdf", "wb") as decrypted_file:
    decrypted_file.write(decrypted)
