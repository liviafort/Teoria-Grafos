from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_exceptions import *


class MeuGrafo(GrafoListaAdjacencia):

    def vertices_nao_adjacentes(self):
        lista = set()
        for v1 in self.N:
            for v2 in self.N:
                achei = False
                for a in self.A:
                    if v1 != v2:
                        if (v1 == self.A[a].getV1() and v2 == self.A[a].getV2()) or (v2 == self.A[a].getV1() and v1 == self.A[a].getV2()):
                            achei = True
                if not achei and v1 != v2:
                    lista.add("{}-{}".format(v1, v2))
        return lista

    def ha_laco(self):
        for a in self.A:
            if self.A[a].getV1() == self.A[a].getV2():
                return True

    def grau(self, V=''):
        contGrau = 0
        if V not in self.N:
            raise VerticeInvalidoException("O vértice passado como parâmetro não existe")
        else:
            for a in self.A:
                if self.A[a].getV1() == V:
                    contGrau += 1
                if self.A[a].getV2() == V:
                    contGrau += 1
            return contGrau

    def ha_paralelas(self):
        cont = 0
        for a1 in self.A:
            for a2 in self.A:
                if a1 != a2:
                    if (self.A[a1].getV1() == self.A[a2].getV1()) and (self.A[a1].getV2() == self.A[a2].getV2()) or \
                            (self.A[a1].getV1() == self.A[a2].getV2()) and (self.A[a1].getV2() == self.A[a2].getV1()):
                        cont+=1
        if cont==0:
            return False
        return True


    def arestas_sobre_vertice(self, V=''):
        lista = set()
        if V not in self.N:
            raise VerticeInvalidoException
        else:
            for a in self.A:
                if self.A[a].getV1() == V or self.A[a].getV2() == V:
                    lista.add(self.A[a].getRotulo())
            return lista

    def arestas_sobre_vertice2(self, V=''):
        lista = list()
        if V not in self.N:
            raise VerticeInvalidoException
        else:
            for a in self.A:
                if self.A[a].getV1() == V or self.A[a].getV2() == V:
                    lista.append(self.A[a].getRotulo())
            return lista

    def dfs(self, V=''):
        arvore = list()
        visitados = list()
        self.dfsprincipal(visitados, arvore, V)
        return arvore

    def dfsprincipal(self, visitados, arvore, V=''):
        if V not in visitados:
            visitados.append(V)
            for a in self.arestas_sobre_vertice2(V):
                if self.A[a].getV2() not in visitados or self.A[a].getV1() not in visitados:
                    arvore.append("{}-{}".format(self.A[a].getV1(), self.A[a].getV2()))
                if V == self.A[a].getV1():
                    self.dfsprincipal(visitados, arvore, self.A[a].getV2())
                else:
                    self.dfsprincipal(visitados, arvore, self.A[a].getV1())
        return arvore

    def bfs(self, V=''):
        arvore = list()
        visitados = list()
        visitados.append(V)
        fila = []
        fila.append(V)
        while fila:
            verticeRetirado = fila.pop(0)
            for i in self.arestas_sobre_vertice2(verticeRetirado):
                if self.A[i].getV1() != verticeRetirado:
                    novoV = self.A[i].getV1()
                else:
                    novoV = self.A[i].getV2()
                if novoV not in visitados:
                    fila.append(novoV)
                    arvore.append("{}-{}".format(self.A[i].getV1(), self.A[i].getV2()))
                    visitados.append(novoV)
        return arvore


    def eh_completo(self):
        cont1 = len(self.A)
        cont2 = len(self.N)
        if (cont1 == cont2 * (cont2 - 1) / 2):
            return True
        return False

    def eh_conexo(self):
        listaArestas = list()
        listaAux = []
        vertices = self.N
        for a in self.A:
            listaArestas.append(self.A[a].getV1()+"-"+self.A[a].getV2())
        for v in vertices:
            if len(listaAux) < 1:
                listaAux.append(v)
            if v in listaAux:
                for aresta in listaArestas:
                    if v in aresta:
                        if v == aresta[0] and aresta[2] not in listaAux:
                            listaAux.append(aresta[2])
                        elif v == aresta[2] and aresta[0] not in listaAux:
                            listaAux.append(aresta[0])
        if len(listaAux) == len(self.N):
            return True
        else:
            return False

    def ha_ciclo(self):
        lista = []
        v = self.N
        lista = self.ha_ciclo_recursiva(v[0], lista)
        for i in range(len(lista)):
            for j in range(i + 1, len(lista)):
                if lista[i] == lista[j]:
                    return True
        return False

    def ha_ciclo_recursiva(self, v, lista):
        lista_aresta = self.A
        lista_v = self.arestas_sobre_vertice(v)
        if v not in lista:
            lista.append(v)
        else:
            lista.append(v)
            return
        for i in lista_v:
            if i not in lista:
                v1 = lista_aresta[i].getV1()
                v2 = lista_aresta[i].getV2()
                if v1 != v:
                    lista.append(i)
                    self.ha_ciclo_recursiva(v1, lista)
                if v2 != v:
                    lista.append(i)
                    self.ha_ciclo_recursiva(v2, lista)
        return lista

    def total_v(self, lis):
        lista_v = self.N
        cont = 0
        for a in lis:
            if a in lista_v:
                cont += 1
        return cont

    def caminho_dois_v(self, x, y):
        lista_a = self.A
        for aresta in lista_a:
            if (lista_a[aresta].getV1() == x) and (lista_a[aresta].getV2() == y):
                return aresta

    def caminho(self, tamanho):
        lista = []
        lista_v = self.N
        v = lista_v[0]
        lista = self.caminho_rec(v, tamanho, lista)
        if lista is None:
            return False
        return lista

    def caminho_rec(self, v, tam, lis):
        lista_aresta = self.A
        keys = list(lista_aresta.keys())
        n = 0
        if v not in lis:
            if len(lis) > 0:
                ar = self.caminho_dois_v(lis[(len(lis) - 1)], v)
                lis.append(ar)
            lis.append(v)
            for aresta in lista_aresta:
                v1 = lista_aresta[aresta].getV1()
                v2 = lista_aresta[aresta].getV2()
                paralela = self.ha_paralelas()
                if paralela:
                    v1 = lista_aresta[keys[n + 1]].getV1()
                    v2 = lista_aresta[keys[n + 1]].getV2()
                    if n == len(keys):
                        n = 0
                    if tam == self.total_v(lis):
                        return lis
                    if v1 != v:
                        self.caminho_rec(v1, tam, lis)
                    elif v2 != v:
                        self.caminho_rec(v2, tam, lis)
                else:
                    if n == len(keys):
                        n = 0
                    if tam == self.total_v(lis):
                        return lis
                    if v1 != v:
                        self.caminho_rec(v1, tam, lis)
                    elif v2 != v:
                        self.caminho_rec(v2, tam, lis)


