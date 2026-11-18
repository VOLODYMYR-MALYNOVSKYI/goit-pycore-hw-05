# Завдання 1

def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n in cache:
            return cache[n]
        if n <= 0:
            return 0
        if n == 1:
            return 1
        
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

        return cache[n]
    
    return fibonacci

fib = caching_fibonacci()
print(fib(10))
print(fib(15))

# Завдання 2

import re
from typing import Callable

def generator_numbers(text: str):
    pattern = r"\b\d+\.\d+\b"
    numbers = re.findall(pattern, text)
    for number in numbers:
        yield float(number)

def sum_profit(text: str, func: Callable) -> float:
    numbers_generator = func(text)

    return sum(numbers_generator)

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

# Завдання 3 не обов'язково (пропускаю)

# Завдання 4

# Декоратор для обробки помилок

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter user name."
    return inner

# Допоміжні функції

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError
    name, phone = args
    name_lower = name.lower()
    for key in contacts:
        if key.lower() == name_lower:
            return "Error: contact already exists."

    contacts[name_lower] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        raise ValueError
    name, phone = args
    name_lower = name.lower()
    for key in contacts:
        if key.lower() == name_lower:
            contacts[key] = phone
            return "Contact updated."
    else:
        return "Error: contact not found."


@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        raise IndexError
    name = args[0].lower()
    for key in contacts:
        if key.lower() == name:
            return contacts[key]
    else:
        return "Error: contact not found."


def show_all(contacts):
    if not contacts:
        return "Error: no contacts found."
    result = "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    return result

# Головна функція для взаємодії з користувачем

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        if not user_input.strip():
            continue

        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()