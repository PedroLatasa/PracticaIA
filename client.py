import simpy
import random


restaurant_parameters = {
    'peruvian': {'child': (10, 15), 'adult': (20, 45)},
    'fast-Food': {'child': (3, 13), 'adult': (6, 25)},
    'mexican': {'child': (12, 30), 'adult': (15, 50)},
    'american': {'child': (12, 19), 'adult': (15, 45)},
    'chinese': {'child': (15, 30), 'adult': (20, 60)},
    'japanese': {'child': (15, 22), 'adult': (20, 60)},
    'spanish': {'child': (10, 15), 'adult': (15, 45)},
    'argentinan': {'child': (12, 24), 'adult': (20, 80)},
    'african': {'child': (10, 15), 'adult': (20, 45)},
    'indian': {'child': (15, 25), 'adult': (20, 70)}
}
import random

# Rangos de clientes por restaurante y por día de la semana
clients_parameters = {
    'peruvian': {
        'mon_thu': (60, 80),
        'fri_sun': (80, 100)
    },
    'fast-Food': {
        'mon_thu': (40, 60),
        'fri_sun': (60, 80)
    },
    'mexican': {
        'mon_thu': (50, 70),
        'fri_sun': (70, 90)
    },
    'american': {
        'mon_thu': (60, 80),
        'fri_sun': (80, 100)
    },
    'chinese': {
        'mon_thu': (50, 70),
        'fri_sun': (70, 90)
    },
    'japanese': {
        'mon_thu': (60, 80),
        'fri_sun': (80, 100)
    },
    'spanish': {
        'mon_thu': (60, 80),
        'fri_sun': (80, 100)
    },
    'argentinan': {
        'mon_thu': (60, 80),
        'fri_sun': (80, 100)
    },
    'african': {
        'mon_thu': (50, 70),
        'fri_sun': (70, 90)
    },
    'indian': {
        'mon_thu': (60, 80),
        'fri_sun': (80, 100)
    }
}

# Función para obtener el número de clientes para un restaurante y día específico
def determine_clients(restaurant_name, day):
    if day in ['mon', 'tue', 'wed', 'thu']:
        return random.randint(*clients_parameters[restaurant_name]['mon_thu'])
    else:
        return random.randint(*clients_parameters[restaurant_name]['fri_sun'])

# Ejemplo de uso:
restaurant_name = 'peruvian'
day = 'mon'
num_clients = determine_clients(restaurant_name, day)
print(f"Number of clients for {restaurant_name} on {day}: {num_clients}")



class Client():
    def __init__ (self, age: int, spent: int)-> None:
        self.age = age
        self.spent = spent
        
        
def generate_clients(num_clients: int, restaurant_name: str)-> object:
    for client in num_clients: 
        age = random.randint(4,80)
        client= Client(age, determinate_spent(age, restaurant_name))
        return client
        
def determinate_spent(age: int , restaurant_name: str) -> int:
    spent = 0
    if restaurant_name in restaurant_parameters:
        if age < 14: 
            spent = random.randint(restaurant_parameters[restaurant_name]['child'][0], restaurant_parameters[restaurant_name]['child'][1])
        else: 
            spent = random.randint(restaurant_parameters[restaurant_name]['adult'][0], restaurant_parameters[restaurant_name]['adult'][1])
    return spent
