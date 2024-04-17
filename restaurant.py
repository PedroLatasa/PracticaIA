import simpy


class Restaurant:
    def __init__(self, env, name, cocineros, camareros, limpiadores, clientes)-> None:
        self.env = env
        self.name = name
        self.cocineros = simpy.Resource(env, capacity=cocineros)
        self.camareros = simpy.Resource(env, capacity=camareros)
        self.limpiadores = simpy.Resource(env, capacity=limpiadores)
        self.clientes = simpy.Resource(env, capacity=clientes)

    def servir_comida(self):
        yield self.env.timeout(1)  # Tiempo necesario para servir la comida

    def limpiar_restaurante(self):
        yield self.env.timeout(1)  # Tiempo necesario para limpiar el restaurante
