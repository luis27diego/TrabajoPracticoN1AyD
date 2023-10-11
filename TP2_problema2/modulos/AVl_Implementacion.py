from TP2_problema2.modulos.AVL import AVL
from datetime import datetime

class AVL_Implementacion:
    def __init__(self):
        self.avl_implementacion = AVL()

    def guardar_temperatura(self,fecha,temperatura):
        fecha = datetime.strptime(fecha, "%d/%m/%Y")
        self.avl_implementacion.agregar(fecha,temperatura)
    
    def devolver_temperatura(self,fecha):
        return self.avl_implementacion.obtener(fecha)
    
    def max_temp_rango(self, fecha1, fecha2):
        if fecha1 > fecha2:
            fecha2, fecha1 = fecha1, fecha2

        temperaturas_en_rango = self.obtener_rango(fecha1, fecha2)
        if temperaturas_en_rango:
            max_temperatura = max(temperaturas_en_rango, key=lambda x: x[1])  # Compara por temperatura
            # print(temperaturas_en_rango)
            return max_temperatura[1]  # Retorna la temperatura del resultado
        else:
            return None

    def obtener_rango(self, fecha_inicio, fecha_fin):
        fecha_inicio = datetime.strptime(fecha_inicio, "%d/%m/%Y")
        fecha_fin = datetime.strptime(fecha_fin, "%d/%m/%Y")

        temperaturas_en_rango = []
        self._obtener_rango(self.avl_implementacion.raiz, fecha_inicio, fecha_fin, temperaturas_en_rango)
        return temperaturas_en_rango

    def _obtener_rango(self, nodo, fecha_inicio, fecha_fin, resultado):
        if nodo is not None:
            
            if nodo.clave >= fecha_inicio:
                self._obtener_rango(nodo.hijoIzquierdo, fecha_inicio, fecha_fin, resultado)

            if fecha_inicio <= nodo.clave <= fecha_fin:
                resultado.append((nodo.clave, nodo.cargaUtil))
            
            if nodo.clave <= fecha_fin:
                self._obtener_rango(nodo.hijoDerecho, fecha_inicio, fecha_fin, resultado)

    def min_temp_rango(self, fecha1, fecha2):
        if fecha1 > fecha2:
            fecha2, fecha1 = fecha1, fecha2

        temperaturas_en_rango = self.obtener_rango(fecha1, fecha2)
        if temperaturas_en_rango:
            min_temperatura = min(temperaturas_en_rango, key=lambda x: x[1])  # Compara por temperatura
            return min_temperatura[1]  # Retorna la temperatura del resultado
        else:
            return None
        
    def temp_extremos_rango(self,fecha1, fecha2):
        if fecha1 > fecha2:
            fecha2, fecha1 = fecha1, fecha2
        temperaturas_en_rango = self.obtener_rango(fecha1, fecha2)
        if temperaturas_en_rango:
            max_temperatura = max(temperaturas_en_rango, key=lambda x: x[1])  # Compara por temperatura
             # Retorna la temperatura del resultado
            min_temperatura = min(temperaturas_en_rango, key=lambda x: x[1])  # Compara por temperatura
            
            return max_temperatura[1],min_temperatura[1]
        else:
            return None
    
    def devolver_temperaturas(self,fecha1, fecha2):
        rango = self.obtener_rango(fecha1,fecha2)
        return rango


    def cantidad_muetras(self):
        return self.avl_implementacion.longitud()


    
 
        

# Crear una instancia de Temperaturas_DB
db = AVL_Implementacion()

# Agregar algunas temperaturas
db.guardar_temperatura("01/01/2023",25.5)
db.guardar_temperatura("02/02/2023",30.0)
db.guardar_temperatura("08/01/2023",55.0)
db.guardar_temperatura("04/01/2023",37.0)
db.guardar_temperatura("07/01/2023",88.0)
db.guardar_temperatura("03/01/2023",14.0)



# Calcular la temperatura máxima en un rango
fecha1 = "02/01/2023"
fecha2 ="07/02/2023"
max_temperatura = db.max_temp_rango(fecha1, fecha2)
min_temperatura = db.min_temp_rango(fecha1, fecha2)
extremos = db.temp_extremos_rango (fecha1,fecha2)
devolver_temp = db.devolver_temperaturas(fecha1,fecha2)
cantidad_db = db.cantidad_muetras()
print(cantidad_db)



if max_temperatura is not None:
    print(f"La temperatura máxima en el rango entre {fecha1} y {fecha2} es: {max_temperatura} ºC")
else:
    print(f"No se encontraron temperaturas en el rango entre {fecha1} y {fecha2}")

if min_temperatura is not None:
    print(f"La temperatura máxima en el rango entre {fecha1} y {fecha2} es: {min_temperatura} ºC")

if extremos is not None:
    print(f"Las temperaturas Extremas dentro del rango entre {fecha1} y {fecha2} es: {extremos} ºC")

if devolver_temp is not None:
    print(f"Las temperaturas dentro del rango entre {fecha1} y {fecha2} es: {devolver_temp} ºC")


