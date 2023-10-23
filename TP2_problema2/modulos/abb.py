from TP2_problema2.modulos.Arbol_nodo import NodoArbol

class ArbolBinarioBusqueda:

    def __init__(self):
        # Constructor: inicializa un árbol binario de búsqueda vacío.
        self.raiz = None  # Inicializa la raíz como None
        self.tamano = 0  # Inicializa el tamaño del árbol como 0

    def longitud(self):
        # Retorna el tamaño (número de nodos) del árbol binario de búsqueda.
        return self.tamano

    def __len__(self):
        # Permite usar la función len() para obtener el tamaño del árbol.
        return self.tamano

    def agregar(self, clave, valor):
        # Agrega un nuevo nodo con la clave y valor especificados al árbol binario de búsqueda.
        if self.raiz:
            # Si el árbol ya tiene una raíz, llama al método _agregar para encontrar la posición adecuada para el nuevo nodo.
            self._agregar(clave, valor, self.raiz)
        else:
            # Si el árbol está vacío, el nuevo nodo se convierte en la raíz.
            self.raiz = NodoArbol(clave, valor)
        self.tamano = self.tamano + 1  # Incrementa el tamaño del árbol en 1

    def _agregar(self, clave, valor, nodoActual):
        # Método auxiliar para agregar un nuevo nodo.
        # Recorre el árbol de manera recursiva para encontrar la posición correcta para el nuevo nodo según su clave.
        if clave < nodoActual.clave:
            # Si la clave es menor que la clave del nodo actual, se mueve al subárbol izquierdo.
            if nodoActual.tieneHijoIzquierdo():
                # Si el nodo actual tiene un hijo izquierdo, continúa la búsqueda en ese subárbol.
                self._agregar(clave, valor, nodoActual.hijoIzquierdo)
            else:
                # Si no tiene un hijo izquierdo, crea un nuevo nodo con la clave y valor especificados y lo establece como hijo izquierdo.
                nodoActual.hijoIzquierdo = NodoArbol(clave, valor, padre=nodoActual)
        else:
            # Si la clave es mayor o igual a la clave del nodo actual, se mueve al subárbol derecho.
            if nodoActual.tieneHijoDerecho():
                # Si el nodo actual tiene un hijo derecho, continúa la búsqueda en ese subárbol.
                self._agregar(clave, valor, nodoActual.hijoDerecho)
            else:
                # Si no tiene un hijo derecho, crea un nuevo nodo con la clave y valor especificados y lo establece como hijo derecho.
                nodoActual.hijoDerecho = NodoArbol(clave, valor, padre=nodoActual)
            
    def __setitem__(self, c, v):
        # Permite agregar un nuevo nodo utilizando la notación de corchetes, ej: árbol[clave] = valor.
        self.agregar(c, v)

    def obtener(self, clave):
        # Busca un nodo con la clave especificada y devuelve su valor.
        # Si la clave no se encuentra, devuelve None.
        if self.raiz:
            res = self._obtener(clave, self.raiz)
            if res:
                return res.cargaUtil
            else:
                return None
        else:
            return None

    def _obtener(self, clave, nodoActual):
        # Método auxiliar para encontrar un nodo por su clave en el árbol.
        # Busca de manera recursiva en el árbol a partir del nodo actual.
        if not nodoActual:
            return None
        elif nodoActual.clave == clave:
            return nodoActual
        elif clave < nodoActual.clave:
            return self._obtener(clave, nodoActual.hijoIzquierdo)
        else:
            return self._obtener(clave, nodoActual.hijoDerecho)

    def __getitem__(self, clave):
        # Permite recuperar un valor utilizando la notación de corchetes, ej: valor = árbol[clave].
        return self.obtener(clave)

    def __contains__(self, clave):
        # Verifica si el árbol contiene un nodo con la clave especificada.
        # Devuelve True si encuentra la clave y False en caso contrario.
        if self._obtener(clave, self.raiz):
            return True
        else:
            return False

    def eliminar(self, clave):
        # Elimina un nodo con la clave especificada del árbol binario de búsqueda.
        # Si no se encuentra la clave, lanza una excepción KeyError.
        if self.tamano > 1:
            nodoAEliminar = self._obtener(clave, self.raiz)
            if nodoAEliminar:
                self.remover(nodoAEliminar)
                self.tamano = self.tamano - 1  # Disminuye el tamaño del árbol en 1
            else:
                raise KeyError('Error, la clave no está en el árbol')
        elif self.tamano == 1 and self.raíz.clave == clave:
            self.raiz = None
            self.tamano = self.tamano - 1  # Disminuye el tamaño del árbol en 1
        else:
            raise KeyError('Error, la clave no está en el árbol')

    def __delitem__(self, clave):
        # Permite eliminar un nodo utilizando la declaración del, ej: del árbol[clave].
        self.eliminar(clave)


    def remover(self, nodoActual):
        # Método para eliminar un nodo del árbol.
        
        if nodoActual.esHoja():  
            # Comprueba si el nodo es una hoja (no tiene hijos).
            
            if nodoActual == nodoActual.padre.hijoIzquierdo:
                # Si el nodo es el hijo izquierdo de su padre, elimina la referencia al nodo hoja.
                nodoActual.padre.hijoIzquierdo = None
            else:
                # Si el nodo es el hijo derecho de su padre, elimina la referencia al nodo hoja.
                nodoActual.padre.hijoDerecho = None
        elif nodoActual.tieneAmbosHijos():  
            # Comprueba si el nodo tiene dos hijos (es un nodo interior).

            suc = nodoActual.encontrarSucesor()  
            # Encuentra el sucesor del nodo (el nodo con el valor más bajo en el subárbol derecho).
            
            suc.empalmar()  
            # Reemplaza el nodo actual por su sucesor y ajusta los enlaces para mantener la estructura del árbol.
            
            nodoActual.clave = suc.clave
            nodoActual.cargaUtil = suc.cargaUtil
        else:  
            # El nodo tiene un solo hijo.

            if nodoActual.tieneHijoIzquierdo():
                # Si el nodo tiene un hijo izquierdo.

                if nodoActual.esHijoIzquierdo():
                    # Si el nodo es el hijo izquierdo de su padre, actualiza las referencias.
                    nodoActual.hijoIzquierdo.padre = nodoActual.padre
                    nodoActual.padre.hijoIzquierdo = nodoActual.hijoIzquierdo
                elif nodoActual.esHijoDerecho():
                    # Si el nodo es el hijo derecho de su padre, actualiza las referencias.
                    nodoActual.hijoIzquierdo.padre = nodoActual.padre
                    nodoActual.padre.hijoDerecho = nodoActual.hijoIzquierdo
                else:
                    # Reemplaza los datos del nodo actual por los datos de su hijo izquierdo.
                    nodoActual.reemplazarDatoDeNodo(nodoActual.hijoIzquierdo.clave, nodoActual.hijoIzquierdo.cargaUtil, nodoActual.hijoIzquierdo.hijoIzquierdo, nodoActual.hijoIzquierdo.hijoDerecho)
            else:
                # Si el nodo tiene un hijo derecho.

                if nodoActual.esHijoIzquierdo():
                    # Si el nodo es el hijo izquierdo de su padre, actualiza las referencias.
                    nodoActual.hijoDerecho.padre = nodoActual.padre
                    nodoActual.padre.hijoIzquierdo = nodoActual.hijoDerecho
                elif nodoActual.esHijoDerecho():
                    # Si el nodo es el hijo derecho de su padre, actualiza las referencias.
                    nodoActual.hijoDerecho.padre = nodoActual.padre
                    nodoActual.padre.hijoDerecho = nodoActual.hijoDerecho
                else:
                    # Reemplaza los datos del nodo actual por los datos de su hijo derecho.
                    nodoActual.reemplazarDatoDeNodo(nodoActual.hijoDerecho.clave, nodoActual.hijoDerecho.cargaUtil, nodoActual.hijoDerecho.hijoIzquierdo, nodoActual.hijoDerecho.hijoDerecho)
