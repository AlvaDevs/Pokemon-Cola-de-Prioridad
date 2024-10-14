import heapq

# Implementación de una cola de prioridad para las batallas Pokémon
class ColaPrioridadBatallas:
    def __init__(self):
        self.cola_prioridad = []  # Usamos una lista para simular la cola de prioridad

    def agregar_pokemon(self, pokemon, prioridad):
        # Añadir un Pokémon con su prioridad (cuanto menor sea el número, más prioridad)
        heapq.heappush(self.cola_prioridad, (prioridad, pokemon))
        print(f"{pokemon} ha sido añadido a la cola de batalla con prioridad {prioridad}.")

    def atender_pokemon(self):
        # Remover y devolver el Pokémon con mayor prioridad (menor número)
        if self.cola_prioridad:
            prioridad, pokemon = heapq.heappop(self.cola_prioridad)
            print(f"{pokemon} ha sido atendido en la batalla (prioridad {prioridad}).")
            return pokemon
        else:
            print("No hay Pokémon en la cola de batalla.")
            return None

    def mostrar_cola(self):
        # Mostrar todos los Pokémon en la cola con su prioridad
        if not self.cola_prioridad:
            print("La cola de batalla está vacía.")
        else:
            print("Pokémon en la cola de batalla:")
            for prioridad, pokemon in sorted(self.cola_prioridad):
                print(f"- {pokemon} (prioridad {prioridad})")


# Programa principal
if __name__ == "__main__":
    cola_batallas = ColaPrioridadBatallas()

    # Añadir Pokémon con prioridades
    cola_batallas.agregar_pokemon("Sprigatito", 2)
    cola_batallas.agregar_pokemon("Fuecoco", 1)
    cola_batallas.agregar_pokemon("Quaxly", 3)

    # Mostrar la cola de prioridad
    cola_batallas.mostrar_cola()

    # Atender Pokémon por prioridad
    cola_batallas.atender_pokemon()
    cola_batallas.atender_pokemon()

    # Mostrar la cola después de atender
    cola_batallas.mostrar_cola()
