from time import sleep
from rich import print

def error(msg):
    print(f"[red]ERROR:[/] {msg}")
    sleep(1)


def get_valid_name():
    while True:
        name = input("Name: ").strip()
        if not name:
            error("Name cannot be empty!")
            continue
        if not all(c.isalpha() or c.isspace() for c in name):
            error("Only letters allowed!")
            continue
        return name


def get_valid_text(field):
    while True:
        value = input(f"{field}: ").strip()
        if not value:
            error(f"{field} cannot be empty!")
            continue
        return value


def get_valid_number(msg):
    while True:
        try:
            value = float(input(msg))
            if value <= 0:
                error("Must be greater than zero!")
                continue
            return value
        except ValueError:
            error("Invalid number!")
