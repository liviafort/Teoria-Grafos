from bibgrafo.grafo_matriz_adj_nao_dir import GrafoMatrizAdjacenciaNaoDirecionado
from bibgrafo.grafo_exceptions import *
import math
from copy import deepcopy

class MeuGrafo(GrafoMatrizAdjacenciaNaoDirecionado):

    def vertices_nao_adjacentes(self):
        aux = set()
        vertices = set()
        for i in range(len(self.M)):
            for j in range(len(self.M)):
                for x in self.M[i][j]:
                    if len(self.M[i][j]) > 0 and self.M[i][j] != '-':
                        aux.add("{}-{}".format(self.M[i][j][x].getV1(), self.M[i][j][x].getV2()))
                        aux.add("{}-{}".format(self.M[i][j][x].getV2(), self.M[i][j][x].getV1()))
        for i in self.N:
            for x in self.N:
                if i != x:
                    if str(i) + "-" + str(x) not in aux and str(x) + "-" + str(i) not in vertices:
                        vertices.add("{}-{}".format(str(i), str(x)))
                        vertices.add("{}-{}".format(str(x), str(i)))
        return vertices

    def eh_conexo(self):
        vertices = self.N
        conexos = set()

        self.eh_conexo_aux(vertices[0], conexos)

        for i in vertices:
            if i not in conexos:
                return False
        return True

    def eh_conexo_aux(self, vertice='', conexos=set()):
        matriz = self.M
        vertices = self.N

        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if i - j < 0 and len(matriz[i][j]) > 0:
                    if i == vertices.index(vertice) and vertices[j] not in conexos:
                        conexos.add(vertices[j])
                        self.eh_conexo_aux(vertices[j], conexos)

                    if j == vertices.index(vertice) and vertices[i] not in conexos:
                        conexos.add(vertices[i])

                        self.eh_conexo_aux(vertices[i], conexos)

    def ha_laco(self):
        for i in range(len(self.M)):
            if len(self.M[i][i]) > 0:
                return True
            return False

    def grau(self, V=''):
        if V not in self.N:
            raise VerticeInvalidoException
        cont = 0
        for i in range(len(self.M)):
            for j in range(len(self.M)):
                for x in self.M[i][j]:
                    if len(self.M[i][j]) > 0 and self.M[i][j] != '-':
                        if self.M[i][j][x].getV1() == V or self.M[i][j][x].getV2() == V:
                            if self.M[i][j][x].getV1() == self.M[i][j][x].getV2():
                                cont += 2
                            else:
                                cont += 1
        return cont

    def ha_paralelas(self):
        for i in range(len(self.M)):
            for j in range(len(self.M)):
                for x,v1 in enumerate(self.M[i][j]):
                    for z, v2 in enumerate(self.M[i][j]):
                        if x > z and ([self.M[i][j][v1].getV1(), self.M[i][j][v1].getV2()] == [self.M[i][j][v2].getV2(), self.M[i][j][v2].getV1()] or
                                      [self.M[i][j][v1].getV1(), self.M[i][j][v1].getV2()] == [self.M[i][j][v2].getV1(), self.M[i][j][v2].getV2()]):
                            return True
        return False

    def arestas_sobre_vertice(self, V):
        if V not in self.N:
            raise VerticeInvalidoException
        arestas = set()
        for i in range(len(self.M)):
            for j in range(len(self.M)):
                for x in self.M[i][j]:
                    if len(self.M[i][j]) > 0 and self.M[i][j] != '-':
                        if self.M[i][j][x].getV1() == V or self.M[i][j][x].getV2() == V:
                            arestas.add(self.M[i][j][x].getRotulo())
        return arestas

    def eh_completo(self):
        if self.ha_laco() or self.vertices_nao_adjacentes() or self.ha_paralelas():
            return False
        return True

    def vertices_partindo_de(self, vertice):
        lista = []
        n = 0
        for i in range(len(self.M)):
            for j in range(len(self.M[i])):
                if self.M[i][j] != self.SEPARADOR_ARESTA:
                    n = len(self.M[i][j])
                    if ((n >= 1) and (self.N[i] == vertice or self.N[j] == vertice)):
                        for c in range(n):
                            if self.N[i] == vertice:
                                if self.N[j] not in lista:
                                    lista.append(self.N[j])
                            elif self.N[j] == vertice:
                                if self.N[i] not in lista:
                                    lista.append(self.N[i])

        return lista

    def djikstra(self, vi, vf):
        import math
        vertices = self.N
        lista_menor_caminho = []
        beta = {}
        pi = {}
        nao_visitados = []
        for vertice in vertices:
            beta[vertice] = math.inf
            pi[vertice] = '0'
            nao_visitados.append(vertice)
        beta[vi] = 0
        nao_visitados.remove(vi)
        R = 0
        r_menor_beta = 0
        w = vi
        while w != vf:
            lista_aresta = self.vertices_partindo_de(w)
            for r in lista_aresta:
                if r in nao_visitados:
                    if beta[r] > (beta[w] + 1):
                        beta[r] = (beta[w] + 1)
                        pi[r] = w
            menor_beta = math.inf

            for r in nao_visitados:
                if beta[r] < menor_beta:
                    menor_beta = beta[r]
                    r_menor_beta = r

            if menor_beta == math.inf:
                return False

            R = r_menor_beta
            nao_visitados.remove(R)
            w = R

        lista_menor_caminho.append(vf)
        while vf != vi:
            lista_menor_caminho.append(pi[vf])
            vf = pi[vf]
        lista_menor_caminho.reverse()
        return lista_menor_caminho
