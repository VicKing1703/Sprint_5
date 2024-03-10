from faker import Faker
import random

def generate_random_email():
    dummy = Faker()
    return dummy.email()

def random_password(password_length):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!-'
    password = ""
    for index in range(password_length):
        password = password + random.choice(characters)
    return password

