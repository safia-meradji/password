import re

def is_valid_password(password):
    # Vérifie si le mot de passe respecte les exigences de sécurité
    return (
        len(password) >= 8 and
        any(char.isupper() for char in password) and
        any(char.islower() for char in password) and
        any(char.isdigit() for char in password) and
        any(char in '!@#$%^&*' for char in password)
    )

def get_valid_password():
    while True:
        password = input("Choisissez un mot de passe : ")
        if is_valid_password(password):
            print("Mot de passe valide. Cryptage en cours...")
            return password
        else:
            print("Erreur: Le mot de passe ne respecte pas les exigences de sécurité.")

# Main program
user_password = get_valid_password()
import hashlib

def hash_password(password):
    # Utilise l'algorithme SHA-256 pour hacher le mot de passe
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

# Cryptage du mot de passe
hashed_user_password = hash_password(user_password)
print(f"Mot de passe crypté (SHA-256) : {hashed_user_password}")
import json

def save_password_to_file(username, hashed_password):
    # Sauvegarde du mot de passe dans un fichier JSON
    data = {username: hashed_password}
    with open('passwords.json', 'a') as file:
        json.dump(data, file)
        file.write('\n')  # Ajoute une nouvelle ligne pour séparer les entrées

def load_passwords_from_file():
    # Charge tous les mots de passe depuis le fichier JSON
    try:
        with open('passwords.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Utilisation
username = input("Entrez votre nom d'utilisateur : ")
save_password_to_file(username, hashed_user_password)
loaded_passwords = load_passwords_from_file()
print(f"Mots de passe enregistrés : {loaded_passwords}")
import random
import string

def generate_random_password():
    # Génère un mot de passe aléatoire qui respecte les exigences
    characters = string.ascii_letters + string.digits + '!@#$%^&*'
    return ''.join(random.choice(characters) for _ in range(12))

# Utilisation
random_password = generate_random_password()
print(f"Mot de passe aléatoire : {random_password}")