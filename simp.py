'''
itertools (mirar librería)
The idea is to simulate the work of a restaurant during a specific amount of time,
which in our case will be days of the year.
Simulation about a restaurants:
1. peruano
2. comida rápida
3. mexicano
4. americano
5. chino
6. japonés
7. español
8. argentino
9. africano
10. indio
'''
import simpy
import random
from restaurant import Restaurant
from client import determine_clients


restaurant_parameters = {
    'peruvian': {'food': {'chefs': (6, 8), 'waiters': (7, 9), 'cleaners': (4, 6), 'customers': (80, 100)},
                 'dinner': {'chefs': (6, 8), 'waiters': (7, 9), 'cleaners': (4, 6), 'customers': (60, 80)}},
    'fast-Food': {'breakfast': {'chefs': (4, 6), 'waiters': (5, 7), 'cleaners': (3, 5), 'customers': (50, 80)},
                'lunch': {'chefs': (4, 6), 'waiters': (3, 5), 'cleaners': (2, 4), 'customers': (100, 150)}},
    'mexican': {'food': {'chefs': (5, 7), 'waiters': (6, 8), 'cleaners': (4, 6), 'customers': (70, 90)},
                'dinner': {'chefs': (5, 7), 'waiters': (6, 8), 'cleaners': (4, 6), 'customers': (50, 70)}},
    'american': {'food': {'chefs': (6, 8), 'waiters': (7, 9), 'cleaners': (4, 6), 'customers': (80, 100)},
                 'dinner': {'chefs': (6, 8), 'waiters': (7, 9), 'cleaners': (4, 6), 'customers': (70, 90)}},
    'chinese': {'food': {'chefs': (5, 7), 'waiters': (6, 8), 'cleaners': (4, 6), 'customers': (60, 80)},
                'dinner': {'chefs': (5, 7), 'waiters': (6, 8), 'cleaners': (4, 6), 'customers': (50, 70)}},
    'japanese': {'food': {'chefs': (6, 8), 'waiters': (7, 9), 'cleaners': (4, 6), 'customers': (70, 90)},
                 'dinner': {'chefs': (6, 8), 'waiters': (7, 9), 'cleaners': (4, 6), 'customers': (60, 80)}},
    'spanish': {'food': {'chefs': (5, 7), 'waiters': (6, 8), 'cleaners': (4, 6), 'customers': (80, 100)},
                'dinner': {'chefs': (5, 7), 'waiters': (6, 8), 'cleaners': (4, 6), 'customers': (70, 90)}},
    'argentinan': {'food': {'chefs': (6, 8), 'waiters': (7, 9), 'cleaners': (4, 6), 'customers': (70, 90)},
                   'dinner': {'chefs': (6, 8), 'waiters': (7, 9), 'cleaners': (4, 6), 'customers': (60, 80)}},
    'african': {'food': {'chefs': (5, 7), 'waiters': (6, 8), 'cleaners': (4, 6), 'customers': (60, 80)},
                'dinner': {'chefs': (5, 7), 'waiters': (6, 8), 'cleaners': (4, 6), 'customers': (50, 70)}},
    'indayn': {'food': {'chefs': (6, 8), 'waiters': (7, 9), 'cleaners': (4, 6), 'customers': (70, 90)},
               'dinner': {'chefs': (6, 8), 'waiters': (7, 9), 'cleaners': (4, 6), 'customers': (60, 80)}}
}


def generator_components(restaurant, time_day):
    clients = determine_clients(restaurant, time_day)
    cookers, waiters, cleaners = 0, 0, 0
   
    parameters = restaurant_parameters.get(restaurant, {})
    if not parameters:
        raise ValueError(f"No parameters found for the restaurant {restaurant}")



    parameters_moment = parameters.get(time_day, {})
    if not parameters_moment:
        raise ValueError(f"No parameters found for the time of day {time_day} at the restaurant {restaurant}")


    cookers = random.randint(*parameters_moment['cookers'])
    waiters = random.randint(*parameters_moment['waiters'])
    cleaners = random.randint(*parameters_moment['cleaners'])
   
    return clients, cookers, waiters, cleaners


def day_simulation(env, restaurant):
    with restaurant.cookers.request() as cookers_req:
        yield cookers_req
        print(f"{env.now}: Cooking food at {restaurant.name}")
        yield env.process(restaurant.servir_comida())


    with restaurant.waiters.request() as waiters_req:
        yield waiters_req
        print(f"{env.now}: Serving food at {restaurant.name}")


    with restaurant.clients.request() as clients_req:
        yield clients_req
        print(f"{env.now}: Eating at {restaurant.name}")


    with restaurant.cleaners.request() as cleaners_req:
        yield cleaners_req
        print(f"{env.now}: Cleaning at {restaurant.name}")
        yield env.process(restaurant.clean_restaurant())


def simulate_life(env, restaurant, num_days):
    for day in range(num_days):
        print(f"Day {day + 1}:")
        for time_day in ['brekfast', 'lunch', 'dinner']:
            clients, cookers, waiters, cleaners = generator_components(restaurant.name, time_day)
            env.process(day_simulation(env, restaurant, clients))
            yield env.timeout(1)  # Simular un día por cada unidad de tiempo


def main():
    env = simpy.Environment()
    num_days = int(input('Enter the number of days for the simulation: '))
    for restaurant_name, parameters in restaurant_parameters.items():
        print(f"Simulation for {restaurant_name}:")
        restaurant = Restaurant(env, restaurant_name, None, None, None, None)
        env.process(simulate_life(env, restaurant, num_days))
        env.run(until=num_days)
        print()
    print()



if __name__ == '__main__':  
    main()
