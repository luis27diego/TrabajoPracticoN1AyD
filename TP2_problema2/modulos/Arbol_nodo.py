class NodoArbol:
   
    def __init__(self, clave, valor, izquierdo=None, derecho=None, padre=None):
        # Constructor: inicializa un nodo del árbol.
        self.clave = clave  # Clave del nodo.
        self.cargaUtil = valor  # Valor asociado al nodo.
        self.hijoIzquierdo = izquierdo  # Hijo izquierdo del nodo.
        self.hijoDerecho = derecho  # Hijo derecho del nodo.
        self.padre = padre  # Padre del nodo.
        self.factorEquilibrio = 0  # Factor de equilibrio utilizado en árboles AVL.

    def tieneHijoIzquierdo(self):
        # Verifica si el nodo tiene un hijo izquierdo.
        return self.hijoIzquierdo

    def tieneHijoDerecho(self):
        # Verifica si el nodo tiene un hijo derecho.
        return self.hijoDerecho

    def esHijoIzquierdo(self):
        # Verifica si el nodo es el hijo izquierdo de su padre.
        return self.padre and self.padre.hijoIzquierdo == self

    def esHijoDerecho(self):
        # Verifica si el nodo es el hijo derecho de su padre.
        return self.padre and self.padre.hijoDerecho == self

    def esRaiz(self):
        # Verifica si el nodo es la raíz del árbol.
        return not self.padre

    def esHoja(self):
        # Verifica si el nodo es una hoja (no tiene hijos).
        return not (self.hijoDerecho or self.hijoIzquierdo)

    def tieneAlgunHijo(self):
        # Verifica si el nodo tiene al menos un hijo.
        return self.hijoDerecho or self.hijoIzquierdo

    def tieneAmbosHijos(self):
        # Verifica si el nodo tiene tanto un hijo izquierdo como un hijo derecho.
        return self.hijoDerecho and self.hijoIzquierdo
    
    def reemplazarDatoDeNodo(self, clave, valor, hizq, hder):
        # Reemplaza los datos del nodo por los valores proporcionados.
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = hizq
        self.hijoDerecho = hder
        # Actualiza los padres de los hijos si existen.
        if self.tieneHijoIzquierdo():
            self.hijoIzquierdo.padre = self
        if self.tieneHijoDerecho():
            self.hijoDerecho.padre = self

    def encontrarSucesor(self):
        # Encuentra el nodo sucesor (el nodo con la clave siguiente) en el árbol.
        suc = None
        if self.tieneHijoDerecho():
            suc = self.hijoDerecho.encontrarMin()
        else:
            if self.padre:
                if self.esHijoIzquierdo():
                    suc = self.padre
                else:
                    # Temporalmente elimina el enlace derecho, encuentra el sucesor y restablece el enlace.
                    self.padre.hijoDerecho = None
                    suc = self.padre.encontrarSucesor()
                    self.padre.hijoDerecho = self
        return suc

    def encontrarMin(self):
        # Encuentra el nodo con el valor mínimo en el subárbol izquierdo.
        actual = self
        while actual.tieneHijoIzquierdo():
            actual = actual.hijoIzquierdo
        return actual

    def empalmar(self):
        # Realiza un empalme para eliminar el nodo actual.
        if self.esHoja():
            # Si es una hoja, simplemente elimina el enlace desde su padre.
            if self.esHijoIzquierdo():
                self.padre.hijoIzquierdo = None
            else:
                self.padre.hijoDerecho = None
        elif self.tieneAlgunHijo():
            if self.tieneHijoIzquierdo():
                if self.esHijoIzquierdo():
                    # Reemplaza el enlace del padre por el hijo izquierdo del nodo.
                    self.padre.hijoIzquierdo = self.hijoIzquierdo
                else:
                    # Reemplaza el enlace del padre por el hijo izquierdo del nodo.
                    self.padre.hijoDerecho = self.hijoIzquierdo
                # Actualiza el padre del hijo izquierdo.
                self.hijoIzquierdo.padre = self.padre
            else:
                if self.esHijoIzquierdo():
                    # Reemplaza el enlace del padre por el hijo derecho del nodo.
                    self.padre.hijoIzquierdo = self.hijoDerecho
                else:
                    # Reemplaza el enlace del padre por el hijo derecho del nodo.
                    self.padre.hijoDerecho = self.hijoDerecho
                # Actualiza el padre del hijo derecho.
                self.hijoDerecho.padre = self.padre

    def __iter__(self):
        # Permite la iteración a través de los nodos del árbol en orden.
        if self:
            if self.tieneHijoIzquierdo():
                # Itera a través de los nodos del subárbol izquierdo.
                for elem in self.hijoIzquierdo:
                    yield elem
            yield self.clave  # Devuelve la clave del nodo actual.
            if self.tieneHijoDerecho():
                # Itera a través de los nodos del subárbol derecho.
                for elem in self.hijoDerecho:
                    yield elem