from TP2_problema2.modulos.ABB import ArbolBinarioBusqueda
from TP2_problema2.modulos.Arbol_nodo import NodoArbol

class AVL(ArbolBinarioBusqueda):
    def __init__(self):
        super().__init__()  # Inicializa la clase AVL como una extensión de ArbolBinarioBusqueda

    def agregar(self, clave, valor):
        if self.raiz:
            self._agregar(clave, valor, self.raiz)  # Si hay una raíz, llama al método _agregar
        else:
            self.raiz = NodoArbol(clave, valor)  # Si no hay raíz, crea un nuevo nodo como raíz
        self.tamano = self.tamano + 1  # Aumenta el tamaño del árbol

    def _agregar(self, clave, valor, nodoActual):
        if clave < nodoActual.clave:
            if nodoActual.tieneHijoIzquierdo():
                self._agregar(clave, valor, nodoActual.hijoIzquierdo)  # Llama recursivamente si el nodo tiene un hijo izquierdo
            else:
                nodoActual.hijoIzquierdo = NodoArbol(clave, valor, padre=nodoActual)  # Crea un nuevo nodo como hijo izquierdo
                self.actualizarEquilibrio(nodoActual.hijoIzquierdo)  # Actualiza el factor de equilibrio
        else:
            if nodoActual.tieneHijoDerecho():
                self._agregar(clave, valor, nodoActual.hijoDerecho)  # Llama recursivamente si el nodo tiene un hijo derecho
            else:
                nodoActual.hijoDerecho = NodoArbol(clave, valor, padre=nodoActual)  # Crea un nuevo nodo como hijo derecho
                self.actualizarEquilibrio(nodoActual.hijoDerecho)  # Actualiza el factor de equilibrio

    def eliminar_avl(self, clave):
        if self.tamano > 1:
            nodoAEliminar = self._obtener(clave, self.raiz)  # Busca el nodo a eliminar

            if nodoAEliminar:
                self.actualizarEquilibrio_elim(nodoAEliminar)  # Actualiza el factor de equilibrio después de eliminar el nodo
                self.remover(nodoAEliminar)  # Elimina el nodo
                self.tamano = self.tamano - 1  # Reduce el tamaño del árbol
            else:
                raise KeyError('Error, la clave no está en el árbol')  # Lanza una excepción si la clave no se encuentra
        elif self.tamano == 1 and self.raiz.clave == clave:
            self.raiz = None  # Si el árbol tiene un solo nodo y coincide con la clave a eliminar, elimina la raíz
            self.tamano = self.tamano - 1  # Reduce el tamaño del árbol
        else:
            raise KeyError('Error, la clave no está en el árbol, está vacío')  # Lanza una excepción si el árbol está vacío
        return nodoAEliminar  # Retorna el nodo eliminado

    def actualizarEquilibrio_elim(self, nodo):
        # Verifica si el factor de equilibrio del nodo está fuera del rango [-1, 1]
        if nodo.factorEquilibrio > 1 or nodo.factorEquilibrio < -1:
            self.reequilibrar(nodo)  # Llama al método de reequilibrio si es necesario
            return  # Termina la función
        if nodo.padre is not None:
            if nodo.esHijoIzquierdo():
                nodo.padre.factorEquilibrio -= 1  # Reduce el factor de equilibrio del padre si el nodo es un hijo izquierdo
            elif nodo.esHijoDerecho():
                nodo.padre.factorEquilibrio += 1  # Aumenta el factor de equilibrio del padre si el nodo es un hijo derecho

            if nodo.padre.factorEquilibrio == 0:
                self.actualizarEquilibrio_elim(nodo.padre)  # Si el factor de equilibrio del padre es 0, llama recursivamente

            else:
                return  # Termina la función

    def actualizarEquilibrio(self, nodo):
        # Verifica si el factor de equilibrio del nodo está fuera del rango [-1, 1]
        if nodo.factorEquilibrio > 1 or nodo.factorEquilibrio < -1:
            self.reequilibrar(nodo)  # Llama al método de reequilibrio si es necesario
            return  # Termina la función
        if nodo.padre is not None:
            if nodo.esHijoIzquierdo():
                nodo.padre.factorEquilibrio += 1  # Aumenta el factor de equilibrio del padre si el nodo es un hijo izquierdo
            elif nodo.esHijoDerecho():
                nodo.padre.factorEquilibrio -= 1  # Reduce el factor de equilibrio del padre si el nodo es un hijo derecho

            if nodo.padre.factorEquilibrio != 0:
                self.actualizarEquilibrio(nodo.padre)  # Si el factor de equilibrio del padre no es 0, llama recursivamente

    def rotarIzquierda(self, rotRaiz):
        # Crea un nuevo nodo que sera la nueva raiz (originalmente el hijo derecho del nodo actual).
        nuevaRaiz = rotRaiz.hijoDerecho

        # Actualiza el puntero del hijo derecho del nodo actual para que sea el hijo izquierdo de la nueva raiz.
        rotRaiz.hijoDerecho = nuevaRaiz.hijoIzquierdo

        # Si el hijo izquierdo de la nueva raiz no es None, establece su padre como el nodo actual.
        if nuevaRaiz.hijoIzquierdo is not None:
            nuevaRaiz.hijoIzquierdo.padre = rotRaiz

        # Establece el padre de la nueva raiz como el padre del nodo actual.
        nuevaRaiz.padre = rotRaiz.padre

        # Verifica si el nodo actual es la raiz del arbol.
        if rotRaiz.esRaiz():
            # Si lo es, actualiza la raiz del arbol como la nueva raiz.
            self.raiz = nuevaRaiz
        else:
            # Si no es la raiz, actualiza el puntero del hijo correspondiente del padre del nodo actual
            # para que apunte a la nueva raiz en lugar del nodo actual.
            if rotRaiz.esHijoIzquierdo():
                rotRaiz.padre.hijoIzquierdo = nuevaRaiz
            else:
                rotRaiz.padre.hijoDerecho = nuevaRaiz

        # Establece al nodo actual como el hijo izquierdo de la nueva raiz.
        nuevaRaiz.hijoIzquierdo = rotRaiz

        # Actualiza los factores de equilibrio para mantener el arbol AVL balanceado.
        rotRaiz.padre = nuevaRaiz
        rotRaiz.factorEquilibrio = rotRaiz.factorEquilibrio + 1 - min(nuevaRaiz.factorEquilibrio, 0)
        nuevaRaiz.factorEquilibrio = nuevaRaiz.factorEquilibrio + 1 + max(rotRaiz.factorEquilibrio, 0)


    def rotarDerecha(self, rotRaiz):
        # Crea un nuevo nodo que sera la nueva raiz (originalmente el hijo izquierdo del nodo actual).
        nuevaRaiz = rotRaiz.hijoIzquierdo

        # Actualiza el puntero del hijo izquierdo del nodo actual para que sea el hijo derecho de la nueva raiz.
        rotRaiz.hijoIzquierdo = nuevaRaiz.hijoDerecho

        # Si el hijo derecho de la nueva raiz no es None, establece su padre como el nodo actual.
        if nuevaRaiz.hijoDerecho is not None:
            nuevaRaiz.hijoDerecho.padre = rotRaiz

        # Establece el padre de la nueva raiz como el padre del nodo actual.
        nuevaRaiz.padre = rotRaiz.padre

        # Verifica si el nodo actual es la raiz del arbol.
        if rotRaiz.esRaiz():
            # Si lo es, actualiza la raiz del arbol como la nueva raiz.
            self.raiz = nuevaRaiz
        else:
            # Si no es la raiz, actualiza el puntero del hijo correspondiente del padre del nodo actual
            # para que apunte a la nueva raiz en lugar del nodo actual.
            if rotRaiz.esHijoIzquierdo():
                rotRaiz.padre.hijoIzquierdo = nuevaRaiz
            else:
                rotRaiz.padre.hijoDerecho = nuevaRaiz

        # Establece al nodo actual como el hijo derecho de la nueva raiz.
        nuevaRaiz.hijoDerecho = rotRaiz

        # Actualiza los factores de equilibrio para mantener el arbol AVL balanceado.
        rotRaiz.padre = nuevaRaiz
        rotRaiz.factorEquilibrio = rotRaiz.factorEquilibrio - 1 - max(nuevaRaiz.factorEquilibrio, 0)
        nuevaRaiz.factorEquilibrio = nuevaRaiz.factorEquilibrio - 1 + min(rotRaiz.factorEquilibrio, 0)


    def reequilibrar(self, nodo):
        # Reequilibra el árbol AVL después de una inserción o eliminación
        if nodo.factorEquilibrio < 0:
            if nodo.hijoDerecho.factorEquilibrio > 0:
                # Necesita una doble rotación: derecha-izquierda
                self.rotarDerecha(nodo.hijoDerecho)
                self.rotarIzquierda(nodo)
            else:
                # Necesita una rotación izquierda
                self.rotarIzquierda(nodo)
        elif nodo.factorEquilibrio > 0:
            if nodo.hijoIzquierdo.factorEquilibrio < 0:
                # Necesita una doble rotación: izquierda-derecha
                self.rotarIzquierda(nodo.hijoIzquierdo)
                self.rotarDerecha(nodo)
            else:
                # Necesita una rotación derecha
                self.rotarDerecha(nodo)

    # Metodos para mostrar el arbol
    def mostrar(self):
        if self.raiz is not None:
            self._mostrar(self.raiz, 0)

    def _mostrar(self, nodo, nivel):
        if nodo is not None:
            self._mostrar(nodo.hijoDerecho, nivel + 1)
            print("   " * nivel + str(nodo.clave))
            self._mostrar(nodo.hijoIzquierdo, nivel + 1)

