from TP2_problema2.modulos.ABB import ArbolBinarioBusqueda
from TP2_problema2.modulos.Arbol_nodo import NodoArbol

class AVL(ArbolBinarioBusqueda):
    def __init__(self):
        super().__init__()  # Llama al constructor de la clase padre
    
    def agregar(self,clave,valor):
        if self.raiz:
            self._agregar(clave,valor,self.raiz)
        else:
            self.raiz = NodoArbol(clave,valor)
        self.tamano = self.tamano + 1

    def _agregar(self,clave,valor,nodoActual):
        if clave < nodoActual.clave:
            if nodoActual.tieneHijoIzquierdo():
                    self._agregar(clave,valor,nodoActual.hijoIzquierdo)
            else:
                    nodoActual.hijoIzquierdo = NodoArbol(clave,valor,padre=nodoActual)
                    self.actualizarEquilibrio(nodoActual.hijoIzquierdo)
        else:
            if nodoActual.tieneHijoDerecho():
                    self._agregar(clave,valor,nodoActual.hijoDerecho)
            else:
                    nodoActual.hijoDerecho = NodoArbol(clave,valor,padre=nodoActual)
                    self.actualizarEquilibrio(nodoActual.hijoDerecho)

    def eliminar_avl(self, clave):
        if self.tamano > 1:
            nodoAEliminar = self._obtener(clave, self.raiz)

            if nodoAEliminar:
                self.actualizarEquilibrio_elim(nodoAEliminar)
                self.remover(nodoAEliminar)
                self.tamano = self.tamano - 1
                # self.reequilibrarDespuesEliminar(nodoAEliminar)  # Reequilibrar después de eliminar
            else:
                raise KeyError('Error, la clave no está en el árbol')
        elif self.tamano == 1 and self.raiz.clave == clave:
            self.raiz = None
            self.tamano = self.tamano - 1
        else:
            raise KeyError('Error, la clave no está en el árbol, esta vacio')
        return nodoAEliminar

    def actualizarEquilibrio_elim(self, nodo):
        if nodo.factorEquilibrio > 1 or nodo.factorEquilibrio < -1:
            self.reequilibrar(nodo)
            return
        if nodo.padre != None:
            if nodo.esHijoIzquierdo():
                nodo.padre.factorEquilibrio -= 1
            elif nodo.esHijoDerecho():
                nodo.padre.factorEquilibrio += 1

            if nodo.padre.factorEquilibrio == 0:
                self.actualizarEquilibrio_elim(nodo.padre)

    # si el nodo padre es desquilibrado (-2 o 2), hay que actualizarlo
            # else:
            #     if nodo.padre.factorEquilibrio > 1 or nodo.padre.factorEquilibrio < -1:
            #         self.actualizarEquilibrio_elim(nodo.padre)

            #     else:                                                                                  
            #         return
            else:
                 return

    def actualizarEquilibrio(self,nodo):
        if nodo.factorEquilibrio > 1 or nodo.factorEquilibrio < -1:
            self.reequilibrar(nodo)
            return
        if nodo.padre != None:
            if nodo.esHijoIzquierdo():
                    nodo.padre.factorEquilibrio += 1
            elif nodo.esHijoDerecho():
                    nodo.padre.factorEquilibrio -= 1

            if nodo.padre.factorEquilibrio != 0:
                    self.actualizarEquilibrio(nodo.padre)

    def rotarIzquierda(self,rotRaiz):
        nuevaRaiz = rotRaiz.hijoDerecho
        rotRaiz.hijoDerecho = nuevaRaiz.hijoIzquierdo
        if nuevaRaiz.hijoIzquierdo != None:
            nuevaRaiz.hijoIzquierdo.padre = rotRaiz
        nuevaRaiz.padre = rotRaiz.padre
        if rotRaiz.esRaiz():
            self.raiz = nuevaRaiz
        else:
            if rotRaiz.esHijoIzquierdo():
                    rotRaiz.padre.hijoIzquierdo = nuevaRaiz
            else:
                rotRaiz.padre.hijoDerecho = nuevaRaiz
        nuevaRaiz.hijoIzquierdo = rotRaiz
        rotRaiz.padre = nuevaRaiz
        rotRaiz.factorEquilibrio = rotRaiz.factorEquilibrio + 1 - min(nuevaRaiz.factorEquilibrio, 0)
        nuevaRaiz.factorEquilibrio = nuevaRaiz.factorEquilibrio + 1 + max(rotRaiz.factorEquilibrio, 0)

    def rotarDerecha(self, rotRaiz):
        nuevaRaiz = rotRaiz.hijoIzquierdo
        rotRaiz.hijoIzquierdo = nuevaRaiz.hijoDerecho
        if nuevaRaiz.hijoDerecho != None:
            nuevaRaiz.hijoDerecho.padre = rotRaiz
        nuevaRaiz.padre = rotRaiz.padre
        if rotRaiz.esRaiz():
            self.raiz = nuevaRaiz
        else:
            if rotRaiz.esHijoIzquierdo():
                rotRaiz.padre.hijoIzquierdo = nuevaRaiz
            else:
                rotRaiz.padre.hijoDerecho = nuevaRaiz
        nuevaRaiz.hijoDerecho = rotRaiz
        rotRaiz.padre = nuevaRaiz
        rotRaiz.factorEquilibrio = rotRaiz.factorEquilibrio - 1 - max(nuevaRaiz.factorEquilibrio, 0)
        nuevaRaiz.factorEquilibrio = nuevaRaiz.factorEquilibrio - 1 + min(rotRaiz.factorEquilibrio, 0)

    def reequilibrar(self,nodo):
        if nodo.factorEquilibrio < 0:
            if nodo.hijoDerecho.factorEquilibrio > 0:
                self.rotarDerecha(nodo.hijoDerecho)
                self.rotarIzquierda(nodo)
            else:
                self.rotarIzquierda(nodo)
        elif nodo.factorEquilibrio > 0:
            if nodo.hijoIzquierdo.factorEquilibrio < 0:
                self.rotarIzquierda(nodo.hijoIzquierdo)
                self.rotarDerecha(nodo)
            else:
                self.rotarDerecha(nodo)

    def mostrar(self):
        if self.raiz is not None:
            self._mostrar(self.raiz, 0)

    def _mostrar(self, nodo, nivel):
        if nodo is not None:
            self._mostrar(nodo.hijoDerecho, nivel + 1)
            print("   " * nivel + str(nodo.clave))
            self._mostrar(nodo.hijoIzquierdo, nivel + 1)

# # Crear un árbol AVL
# mi_arbol_avl = AVL()

# # Agregar elementos al árbol
# mi_arbol_avl.agregar(1, "Dato 1")
# mi_arbol_avl.agregar(2, "Dato 2")
# mi_arbol_avl.agregar(8, "Dato 8")
# mi_arbol_avl.agregar(4, "Dato 4")
# mi_arbol_avl.agregar(7, "Dato 7")
# mi_arbol_avl.agregar(3, "Dato 3")



# mi_arbol_avl.eliminar(1)
# mi_arbol_avl.eliminar(3)


# ESTO COMMENT
# # mi_arbol_avl.eliminar(7)
# # mi_arbol_avl.eliminar(8)

# # mi_arbol_avl.eliminar(8)
# HASTA AQUI


# mi_arbol_avl.mostrar()
