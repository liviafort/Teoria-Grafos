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


    sets = {}

    def criar_floresta(self, v):
        self.sets[v] = [v]

    def procura(self, v):
        for i, x in self.sets.items():
            if v in x:
                return i
        return None

    def uniao(self, v1, v2):
        vertice1 = self.procura(v1)
        vertice2 = self.procura(v2)
        self.sets[vertice1] = self.sets[vertice1] + self.sets[vertice2]
        del self.sets[vertice2]

    def kruskall(self):
        arvore_minima = MeuGrafo()

        for i in self.N:
            self.criar_floresta(i)

        arvore = []
        dicionarioArestasComPesos = self.menor_peso_da_aresta()
        arestas_menor_peso = self.menor_peso_da_aresta()
        arestas_menor_peso = arestas_menor_peso.values()
        vertices_não_presentes_na_arvore = self.N
        if self.eh_conexo():
            for a in arestas_menor_peso:
                for i in dicionarioArestasComPesos:
                    if dicionarioArestasComPesos[i] == a:
                        if self.procura(i[0]) != self.procura(i[2]):
                            v1 = i[0]
                            v2 = i[2]
                            arvore.append(i)
                            arvore.append(v1)
                            arvore.append(v2)
                            existe_vertice1 = arvore_minima.existeVertice(v1)
                            existe_vertice2 = arvore_minima.existeVertice(v2)
                            if not existe_vertice1:
                                arvore_minima.adicionaVertice(v1)
                            if not existe_vertice2:
                                arvore_minima.adicionaVertice(v2)
                            if not (existe_vertice1 and existe_vertice2) or (existe_vertice1 and existe_vertice2):
                                arvore_minima.adicionaAresta(i, a)
                            self.uniao(v1, v2)
            return arvore_minima

    def procurar_na_arvore(self, vertice, lista=[]):
        if vertice not in lista:
            return True
        else:
            return False

    def dicionario_peso_aresta(self):
        dic = {}
        copia = deepcopy(self.M)
        for i in range(len(self.M)):
            for j in range(len(self.M[i])):
                if (len(self.M[i][j]) != 0) and (self.M[i][j] != self.SEPARADOR_ARESTA):
                    aresta = '{}{}{}'.format(self.N[i], self.SEPARADOR_ARESTA, self.N[j])
                    dic[aresta] = self.M[i][j]

        return dic

    def vertices_adjacentes(self, v):
        lista_vertices_adjacentes = []
        posição = self.N.index(v)
        for i in range(len(self.M)):
            if i < posição:
                if self.M[i][posição]:
                    lista_vertices_adjacentes.append(self.N[i])
            elif i == posição:
                for j in range(posição, len(self.M[i])):
                    if self.M[i][j]:
                        lista_vertices_adjacentes.append(self.N[j])
            else:
                break
        return lista_vertices_adjacentes

    def criar_aresta(self, v1, v2):
        aresta = "{}{}{}".format(v1, self.SEPARADOR_ARESTA, v2)
        return aresta

    def PrimModificado(self):
        from math import inf
        vertices = deepcopy(self.N)
        arestas = []
        for i in range(len(self.M)):
            for j in range(len(self.M[i])):
                if (len(self.M[i][j]) != 0) and (self.M[i][j] != self.SEPARADOR_ARESTA):
                    aresta1 = '{}{}{}'.format(self.N[i], self.SEPARADOR_ARESTA, self.N[j])
                    arestas.append(aresta1)
        dic_peso = self.dicionario_peso_aresta()
        Jet = {}
        P = {}
        guarda_peso = inf
        guarda_aresta = ''
        arvore = MeuGrafo()
        for vertice in vertices:
            Jet[vertice] = inf
            P[vertice] = None

        for aresta in arestas:
            listap = dic_peso[aresta]
            peso = listap[0]
            if peso < guarda_peso:
                guarda_peso = peso
                guarda_aresta = aresta
                v1, v2 = aresta.split(self.SEPARADOR_ARESTA)
        Jet[v1] = 0
        lista_prioridade = deepcopy(self.N)
        while (len(lista_prioridade) != 0):
            menor_peso = inf
            vertice_menor_peso = ''
            for v in lista_prioridade:
                if isinstance(Jet[v], list) == True:  # problema é aqui
                    jet = Jet[v][0]
                    if jet < menor_peso:
                        pesolista = Jet[v]
                        menor_peso = pesolista[0]
                        vertice_menor_peso = v
                else:
                    if Jet[v] < menor_peso:
                        menor_peso = Jet[v]
                        vertice_menor_peso = v
            x = vertice_menor_peso

            lista_prioridade.pop(lista_prioridade.index(vertice_menor_peso))
            lista_vertices_adjacente = self.vertices_adjacentes(x)
            for vertice_adjacente in lista_vertices_adjacente:
                aresta_y = x + "-" + vertice_adjacente
                if aresta_y not in arestas:
                    aresta_y = vertice_adjacente + '-' + x
                pesoy = dic_peso[aresta_y][0]
                jety = Jet[vertice_adjacente]
                if isinstance(jety, list) == True:
                    if vertice_adjacente in lista_prioridade and pesoy < jety[0]:
                        P[vertice_adjacente] = x
                        Jet[vertice_adjacente] = dic_peso[aresta_y]
                else:
                    if vertice_adjacente in lista_prioridade and pesoy < jety:
                        P[vertice_adjacente] = x
                        Jet[vertice_adjacente] = dic_peso[aresta_y]
        for v in vertices:
            arvore.adicionaVertice(v)
        lista_final = []
        for a, i in P.items():
            if i:
                lista_final.append(self.criar_aresta(i, a))
        dic_menor_peso = self.menor_peso_da_aresta()
        for i in lista_final:
            if i in dic_menor_peso:
                arvore.adicionaAresta(i, dic_menor_peso[i])

        return arvore

    def __str__(self):
        espaco = ' ' * (self.__maior_vertice)
        grafo_str = espaco + ' '

        for v in range(len(self.N)):
            grafo_str += self.N[v]
            if v < (len(self.N) - 1):
                grafo_str += ' '

        grafo_str += '\n'

        for l in range(len(self.M)):
            grafo_str += self.N[l] + ' '
            for c in range(len(self.M)):
                if self.M[l][c] == '-':
                    grafo_str += '-' + ' '
                else:
                    grafo_str += str(len(self.M[l][
                                             c])) + ' '
            grafo_str += '\n'

        return grafo_str
