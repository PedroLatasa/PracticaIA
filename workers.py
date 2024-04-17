import simpy
import random

workers_parameters = {
    'peruvian': {
        'waiter': {'salary_per_hour': (8, 15), 'work_hours': (30, 40)},
        'chef': {'salary_per_hour': (15, 25), 'work_hours': (40, 50)},
        'cleaner': {'salary_per_hour': (8, 12), 'work_hours': (20, 30)}
    },
    'fast-Food': {
        'waiter': {'salary_per_hour': (8, 15), 'work_hours': (20, 30)},
        'chef': {'salary_per_hour': (12, 15), 'work_hours': (35, 45)},
        'cleaner': {'salary_per_hour': (7, 12), 'work_hours': (15, 25)}
    },
    'mexican': {
        'waiter': {'salary_per_hour': (10, 15), 'work_hours': (25, 35)},
        'chef': {'salary_per_hour': (15, 20), 'work_hours': (45, 55)},
        'cleaner': {'salary_per_hour': (9, 15), 'work_hours': (20, 30)}
    },
    'american': {
        'waiter': {'salary_per_hour': (10, 15), 'work_hours': (30, 40)},
        'chef': {'salary_per_hour': (15, 25), 'work_hours': (40, 50)},
        'cleaner': {'salary_per_hour': (8, 12), 'work_hours': (20, 30)}
    },
    'chinese': {
        'waiter': {'salary_per_hour': (9, 14), 'work_hours': (25, 35)},
        'chef': {'salary_per_hour': (14, 20), 'work_hours': (35, 45)},
        'cleaner': {'salary_per_hour': (8, 12), 'work_hours': (20, 30)}
    },
    'japanese': {
        'waiter': {'salary_per_hour': (10, 15), 'work_hours': (30, 40)},
        'chef': {'salary_per_hour': (16, 22), 'work_hours': (40, 50)},
        'cleaner': {'salary_per_hour': (9, 15), 'work_hours': (20, 30)}
    },
    'spanish': {
        'waiter': {'salary_per_hour': (9, 14), 'work_hours': (25, 35)},
        'chef': {'salary_per_hour': (14, 20), 'work_hours': (35, 45)},
        'cleaner': {'salary_per_hour': (8, 12), 'work_hours': (20, 30)}
    },
    'argentinan': {
        'waiter': {'salary_per_hour': (11, 15), 'work_hours': (30, 40)},
        'chef': {'salary_per_hour': (17, 23), 'work_hours': (40, 50)},
        'cleaner': {'salary_per_hour': (10, 15), 'work_hours': (20, 30)}
    },
    'african': {
        'waiter': {'salary_per_hour': (9, 14), 'work_hours': (25, 35)},
        'chef': {'salary_per_hour': (14, 20), 'work_hours': (35, 45)},
        'cleaner': {'salary_per_hour': (8, 12), 'work_hours': (20, 30)}
    },
    'indian': {
        'waiter': {'salary_per_hour': (10, 15), 'work_hours': (30, 40)},
        'chef': {'salary_per_hour': (16, 22), 'work_hours': (40, 50)},
        'cleaner': {'salary_per_hour': (9, 15), 'work_hours': (20, 30)}
    }
}


class  Workers():
     def __init__(self, env, type, work_hours, payment ) -> None:
       self.env = env
       self.type = type
       self.work_hours = work_hours
       self.payment = payment

def create_workers(env, restaurant_type)-> object:
    total_cost = 0
    for worker_type, parameters in workers_parameters[restaurant_type].items():
        salary = random.randint(parameters['salary'][0], parameters['salary'][1])
        work_hours = random.randint(parameters['work_hours'][0], parameters['work_hours'][1])
        payment = salary * work_hours
        total_cost += payment
        worker = Workers(env, worker_type, work_hours, payment)
        print(f"Created {worker_type} worker with salary {salary}, work hours {work_hours}, and payment {payment}")
    print(f"Total cost for {restaurant_type} workers: {total_cost}")
    return worker
