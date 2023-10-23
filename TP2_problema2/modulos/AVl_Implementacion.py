from TP2_problema2.modulos.AVL import AVL
from datetime import datetime

class AVL_Implementacion:
    def __init__(self):
        # Constructor de la clase. Inicializa un árbol AVL vacío.
        self.avl_implementacion = AVL()

    def guardar_temperatura(self, fecha, temperatura):
        # Convierte la fecha proporcionada en un objeto datetime.
        fecha = datetime.strptime(fecha, "%d/%m/%Y")
        # Agrega la temperatura al árbol AVL.
        self.avl_implementacion.agregar(fecha, temperatura)

    def devolver_temperatura(self, fecha):
        # Convierte la fecha proporcionada en un objeto datetime.
        fecha = datetime.strptime(fecha, "%d/%m/%Y")
        # Obtiene la temperatura asociada a la fecha del árbol AVL y la devuelve.
        return self.avl_implementacion.obtener(fecha)

    def max_temp_rango(self, fecha1, fecha2):
        # Comprueba el orden de las fechas y las ajusta si es necesario.
        if fecha1 > fecha2:
            fecha2, fecha1 = fecha1, fecha2

        # Obtiene las temperaturas en un rango de fechas y retorna la máxima temperatura en ese rango.
        temperaturas_en_rango = self.obtener_rango(fecha1, fecha2)
        if temperaturas_en_rango:
            max_temperatura = max(temperaturas_en_rango, key=lambda x: x[1])  # Compara por temperatura
            return max_temperatura[1]  # Retorna la temperatura del resultado
        else:
            return None

    def obtener_rango(self, fecha_inicio, fecha_fin):
        # Convierte las fechas de inicio y fin en objetos datetime.
        fecha_inicio = datetime.strptime(fecha_inicio, "%d/%m/%Y")
        fecha_fin = datetime.strptime(fecha_fin, "%d/%m/%Y")

        # Inicializa una lista para almacenar las temperaturas en el rango especificado.
        temperaturas_en_rango = []

        # Invoca al método privado para obtener las temperaturas dentro del rango.
        self._obtener_rango(self.avl_implementacion.raiz, fecha_inicio, fecha_fin, temperaturas_en_rango)

        return temperaturas_en_rango

    def _obtener_rango(self, nodo, fecha_inicio, fecha_fin, resultado):
        if nodo is not None:
            if nodo.clave >= fecha_inicio:
                # Si la fecha del nodo es mayor o igual que la fecha de inicio, continúa explorando el subárbol izquierdo.
                self._obtener_rango(nodo.hijoIzquierdo, fecha_inicio, fecha_fin, resultado)

            if fecha_inicio <= nodo.clave <= fecha_fin:
                # Si la fecha del nodo está dentro del rango, agrega la fecha y la temperatura al resultado.
                resultado.append((nodo.clave.strftime("%Y-%m-%d"), nodo.cargaUtil))

            if nodo.clave <= fecha_fin:
                # Si la fecha del nodo es menor o igual que la fecha de fin, continúa explorando el subárbol derecho.
                self._obtener_rango(nodo.hijoDerecho, fecha_inicio, fecha_fin, resultado)

    def min_temp_rango(self, fecha1, fecha2):
        # Comprueba el orden de las fechas y las ajusta si es necesario.
        if fecha1 > fecha2:
            fecha2, fecha1 = fecha1, fecha2

        # Obtiene las temperaturas en un rango de fechas y retorna la mínima temperatura en ese rango.
        temperaturas_en_rango = self.obtener_rango(fecha1, fecha2)
        if temperaturas_en_rango:
            min_temperatura = min(temperaturas_en_rango, key=lambda x: x[1])  # Compara por temperatura
            return min_temperatura[1]  # Retorna la temperatura del resultado
        else:
            return None

    def temp_extremos_rango(self, fecha1, fecha2):
        # Comprueba el orden de las fechas y las ajusta si es necesario.
        if fecha1 > fecha2:
            fecha2, fecha1 = fecha1, fecha2

        # Obtiene las temperaturas en un rango de fechas.
        temperaturas_en_rango = self.obtener_rango(fecha1, fecha2)
        if temperaturas_en_rango:
            # Encuentra la máxima y mínima temperatura en el rango y las retorna.
            max_temperatura = max(temperaturas_en_rango, key=lambda x: x[1])  # Compara por temperatura
            min_temperatura = min(temperaturas_en_rango, key=lambda x: x[1])  # Compara por temperatura
            return max_temperatura[1], min_temperatura[1]
        else:
            return None
    
    def devolver_temperaturas(self, fecha1, fecha2):
        # Obtiene las temperaturas en un rango de fechas y las retorna como una lista de tuplas (fecha, temperatura).
        rango = self.obtener_rango(fecha1, fecha2)
        return rango

    def cantidad_muetras(self):
        # Retorna la cantidad de muestras en el árbol AVL.
        return self.avl_implementacion.longitud()

    def borrar_temperatura(self, fecha):
        # Convierte la fecha proporcionada en un objeto datetime.
        fecha = datetime.strptime(fecha, "%d/%m/%Y")
        # Elimina la temperatura asociada a la fecha y retorna su valor.
        return self.avl_implementacion.eliminar_avl(fecha).cargaUtil