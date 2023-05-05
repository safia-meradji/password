import hashlib
def password_check(password):
    symboles_spécials=["!","@","#","$","*"]
    return_val=True
    if len(password)<8:
        print("votre mot de passe doit contenir au moins 8 caractères")
        return_val=False
    if not any(char.isdigit()for char in password):
        print("votre mot de passe doit contenir au moins un chiffre")
        return_val=False
    if not any(char.isupper()for char in password):
        print("votre mot de passe doit contenir au moins une lettre majuscule")
    if not any(char.islower()for char in password):
        return_val=False
    if not any (char in symboles_spécials for char in password):
        print("votre mot de passe doit contenir au moins un caractère spécial: !,@,#,$,*")
        return_val=False
    if return_val :
        print("le mot de passe est:"+password)
        password_bytes = password.encode('utf8')
        hash_obj = hashlib.sha256(password_bytes)
        return("hachage hexadécimal :"+hash_obj.hexdigest())
    return return_val
password =input("entrez votre mot de passe" )
print (password_check("password="))

