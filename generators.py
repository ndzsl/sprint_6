from data import OrderData
import random


def generate_name():
    return random.choice(OrderData.NAME)


def generate_surname():
    return random.choice(OrderData.SURNAME)


def generate_address():
    return random.choice(OrderData.ADDRESS)

def generate_station():
    return random.choice(OrderData.STATION)


def generate_phone():
    number = random.randint(1111111, 9999999)
    return f'8916{number}'


def generate_rental_period():
    return random.choice(OrderData.RENTAL_PERIOD)


def generate_color():
    return random.choice(OrderData.COLOR)


def generate_comment():
    return random.choice(OrderData.COMMENT)