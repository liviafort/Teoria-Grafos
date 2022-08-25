import unittest
from meu_grafo import *
from bibgrafo.grafo_exceptions import *

class TestGrafo(unittest.TestCase):

    def setUp(self):

        # Grafos da Paraíba com PESO
        self.g_pP1 = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_pP1.adicionaAresta('a1', 'J', 'C', 5)
        self.g_pP1.adicionaAresta('a2', 'C', 'E', 3)
        self.g_pP1.adicionaAresta('a3', 'C', 'E', 4)
        self.g_pP1.adicionaAresta('a4', 'P', 'C', 2)
        self.g_pP1.adicionaAresta('a5', 'P', 'C', 1)
        self.g_pP1.adicionaAresta('a6', 'T', 'C', 5)
        self.g_pP1.adicionaAresta('a7', 'M', 'C', 7)
        self.g_pP1.adicionaAresta('a8', 'M', 'T', 8)
        self.g_pP1.adicionaAresta('a9', 'T', 'Z', 9)

        self.g_pP2 = MeuGrafo(['J', 'C', 'E', 'P'])
        self.g_pP2.adicionaAresta('a1', 'J', 'C', 2)
        self.g_pP2.adicionaAresta('a2', 'J', 'E', 6)
        self.g_pP2.adicionaAresta('a3', 'J', 'P', 4)
        self.g_pP2.adicionaAresta('a4', 'E', 'C', 2)
        self.g_pP2.adicionaAresta('a5', 'P', 'C', 5)
        self.g_pP2.adicionaAresta('a6', 'P', 'E', 3)

        # grafos com peso para testes
        self.g_p_COMPESO = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_COMPESO.adicionaAresta('a1', 'J', 'C', 5)
        self.g_p_COMPESO.adicionaAresta('a2', 'C', 'E', 3)
        self.g_p_COMPESO.adicionaAresta('a5', 'P', 'C', 1)
        self.g_p_COMPESO.adicionaAresta('a6', 'T', 'C', 5)
        self.g_p_COMPESO.adicionaAresta('a7', 'M', 'C', 7)
        self.g_p_COMPESO.adicionaAresta('a9', 'T', 'Z', 9)

        self.g_p_COMPESO2 = MeuGrafo(['J', 'C', 'E', 'P'])
        self.g_p_COMPESO2.adicionaAresta('a1', 'J', 'C', 2)
        self.g_p_COMPESO2.adicionaAresta('a4', 'E', 'C', 2)
        self.g_p_COMPESO2.adicionaAresta('a6', 'P', 'E', 3)


        # Grafo TESTE CICLO
        self.g_pNOVO3 = MeuGrafo(['J', 'C', 'E', 'P', 'M'])
        self.g_pNOVO3.adicionaAresta('a1', 'J', 'C')
        self.g_pNOVO3.adicionaAresta('a2', 'C', 'E')
        self.g_pNOVO3.adicionaAresta('a3', 'C', 'J')
        self.g_pNOVO3.adicionaAresta('a4', 'M', 'P')

        # Grafo TESTE CONEXO
        self.g_pNOVO2 = MeuGrafo(['J', 'C', 'E', 'P', 'M'])
        self.g_pNOVO2.adicionaAresta('a1', 'J', 'C')
        self.g_pNOVO2.adicionaAresta('a2', 'C', 'E')
        self.g_pNOVO2.adicionaAresta('a3', 'C', 'E')
        self.g_pNOVO2.adicionaAresta('a4', 'M', 'P')

        #Grafo TESTE CONEXO
        self.g_pNOVO = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z', 'K', 'W'])
        self.g_pNOVO.adicionaAresta('a1', 'J', 'C')
        self.g_pNOVO.adicionaAresta('a2', 'C', 'E')
        self.g_pNOVO.adicionaAresta('a3', 'C', 'E')
        self.g_pNOVO.adicionaAresta('a4', 'P', 'C')
        self.g_pNOVO.adicionaAresta('a5', 'P', 'C')
        self.g_pNOVO.adicionaAresta('a6', 'T', 'C')
        self.g_pNOVO.adicionaAresta('a7', 'M', 'C')
        self.g_pNOVO.adicionaAresta('a8', 'M', 'T')
        self.g_pNOVO.adicionaAresta('a9', 'T', 'Z')
        self.g_pNOVO.adicionaAresta('a10', 'K', 'W')

        # Grafo da Paraíba
        self.g_p = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p.adicionaAresta('a1', 'J', 'C')
        self.g_p.adicionaAresta('a2', 'C', 'E')
        self.g_p.adicionaAresta('a3', 'C', 'E')
        self.g_p.adicionaAresta('a4', 'P', 'C')
        self.g_p.adicionaAresta('a5', 'P', 'C')
        self.g_p.adicionaAresta('a6', 'T', 'C')
        self.g_p.adicionaAresta('a7', 'M', 'C')
        self.g_p.adicionaAresta('a8', 'M', 'T')
        self.g_p.adicionaAresta('a9', 'T', 'Z')

        # Clone do Grafo da Paraíba para ver se o método equals está funcionando
        self.g_p2 = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p2.adicionaAresta('a1', 'J', 'C')
        self.g_p2.adicionaAresta('a2', 'C', 'E')
        self.g_p2.adicionaAresta('a3', 'C', 'E')
        self.g_p2.adicionaAresta('a4', 'P', 'C')
        self.g_p2.adicionaAresta('a5', 'P', 'C')
        self.g_p2.adicionaAresta('a6', 'T', 'C')
        self.g_p2.adicionaAresta('a7', 'M', 'C')
        self.g_p2.adicionaAresta('a8', 'M', 'T')
        self.g_p2.adicionaAresta('a9', 'T', 'Z')

        # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
        # Esse tem um pequena diferença na primeira aresta
        self.g_p3 = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p3.adicionaAresta('a', 'J', 'C')
        self.g_p3.adicionaAresta('a2', 'C', 'E')
        self.g_p3.adicionaAresta('a3', 'C', 'E')
        self.g_p3.adicionaAresta('a4', 'P', 'C')
        self.g_p3.adicionaAresta('a5', 'P', 'C')
        self.g_p3.adicionaAresta('a6', 'T', 'C')
        self.g_p3.adicionaAresta('a7', 'M', 'C')
        self.g_p3.adicionaAresta('a8', 'M', 'T')
        self.g_p3.adicionaAresta('a9', 'T', 'Z')

        # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
        # Esse tem um pequena diferença na segunda aresta
        self.g_p4 = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p4.adicionaAresta('a1', 'J', 'C')
        self.g_p4.adicionaAresta('a2', 'J', 'E')
        self.g_p4.adicionaAresta('a3', 'C', 'E')
        self.g_p4.adicionaAresta('a4', 'P', 'C')
        self.g_p4.adicionaAresta('a5', 'P', 'C')
        self.g_p4.adicionaAresta('a6', 'T', 'C')
        self.g_p4.adicionaAresta('a7', 'M', 'C')
        self.g_p4.adicionaAresta('a8', 'M', 'T')
        self.g_p4.adicionaAresta('a9', 'T', 'Z')

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_sem_paralelas.adicionaAresta('a1', 'J', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a2', 'C', 'E')
        self.g_p_sem_paralelas.adicionaAresta('a3', 'P', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a4', 'T', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a5', 'M', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a6', 'M', 'T')
        self.g_p_sem_paralelas.adicionaAresta('a7', 'T', 'Z')

        # Grafos completos
        self.g_c = MeuGrafo(['J', 'C', 'E', 'P'])
        self.g_c.adicionaAresta('a1', 'J', 'C')
        self.g_c.adicionaAresta('a2', 'J', 'E')
        self.g_c.adicionaAresta('a3', 'J', 'P')
        self.g_c.adicionaAresta('a4', 'E', 'C')
        self.g_c.adicionaAresta('a5', 'P', 'C')
        self.g_c.adicionaAresta('a6', 'P', 'E')

        self.g_c2 = MeuGrafo(['Nina', 'Maria'])
        self.g_c2.adicionaAresta('amiga', 'Nina', 'Maria')

        self.g_c3 = MeuGrafo(['J'])

        # Grafos com laco
        self.g_l1 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l1.adicionaAresta('a1', 'A', 'A')
        self.g_l1.adicionaAresta('a2', 'A', 'B')
        self.g_l1.adicionaAresta('a3', 'A', 'A')

        self.g_l2 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l2.adicionaAresta('a1', 'A', 'B')
        self.g_l2.adicionaAresta('a2', 'B', 'B')
        self.g_l2.adicionaAresta('a3', 'B', 'A')

        self.g_l3 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l3.adicionaAresta('a1', 'C', 'A')
        self.g_l3.adicionaAresta('a2', 'C', 'C')
        self.g_l3.adicionaAresta('a3', 'D', 'D')
        self.g_l3.adicionaAresta('a4', 'D', 'D')

        self.g_l4 = MeuGrafo(['D'])
        self.g_l4.adicionaAresta('a1', 'D', 'D')

        self.g_l5 = MeuGrafo(['C', 'D'])
        self.g_l5.adicionaAresta('a1', 'D', 'C')
        self.g_l5.adicionaAresta('a2', 'C', 'C')

        # Grafos desconexos
        self.g_d = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_d.adicionaAresta('asd', 'A', 'B')

        self.g_d2 = MeuGrafo(['A', 'B', 'C', 'D'])

    def test_adiciona_aresta(self):
        self.assertTrue(self.g_p.adicionaAresta('a10', 'J', 'C'))
        with self.assertRaises(ArestaInvalidaException):
            self.assertTrue(self.g_p.adicionaAresta('b1', '', 'C'))
        with self.assertRaises(ArestaInvalidaException):
            self.assertTrue(self.g_p.adicionaAresta('b1', 'A', 'C'))
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('')
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('aa-bb')
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('x', 'J', 'V')
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('a1', 'J', 'C')

    def test_eq(self):
        self.assertEqual(self.g_p, self.g_p2)
        self.assertNotEqual(self.g_p, self.g_p3)
        self.assertNotEqual(self.g_p, self.g_p_sem_paralelas)
        self.assertNotEqual(self.g_p, self.g_p4)

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(self.g_p.vertices_nao_adjacentes(),
                         {'J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-Z', 'E-P', 'E-M', 'E-T', 'E-Z', 'P-M', 'P-T', 'P-Z',
                          'M-Z', 'E-J', 'P-J', 'M-J', 'T-J', 'Z-J', 'Z-C', 'P-E', 'M-E', 'T-E', 'Z-E', 'M-P', 'T-P',
                          'Z-P',
                          'Z-M'})
        self.assertEqual(self.g_d.vertices_nao_adjacentes(), {'A-C', 'A-D', 'B-C', 'B-D', 'C-D', 'C-A', 'D-A', 'C-B', 'D-B', 'D-C'})
        self.assertEqual(self.g_d2.vertices_nao_adjacentes(), {'A-B', 'A-C', 'A-D', 'B-C', 'B-D', 'C-D', 'B-A', 'C-A', 'D-A', 'C-B', 'D-B', 'D-C'})
        self.assertEqual(self.g_c.vertices_nao_adjacentes(), set())
        self.assertEqual(self.g_c3.vertices_nao_adjacentes(), set())
    def test_ha_laco(self):
        self.assertFalse(self.g_p.ha_laco())
        self.assertFalse(self.g_p2.ha_laco())
        self.assertFalse(self.g_p3.ha_laco())
        self.assertFalse(self.g_p4.ha_laco())
        self.assertFalse(self.g_p_sem_paralelas.ha_laco())
        self.assertFalse(self.g_d.ha_laco())
        self.assertFalse(self.g_c.ha_laco())
        self.assertFalse(self.g_c2.ha_laco())
        self.assertFalse(self.g_c3.ha_laco())
        self.assertTrue(self.g_l1.ha_laco())
        self.assertTrue(self.g_l2.ha_laco())
        self.assertTrue(self.g_l3.ha_laco())
        self.assertTrue(self.g_l4.ha_laco())
        self.assertTrue(self.g_l5.ha_laco())

    def test_grau(self):
        # Paraíba
        self.assertEqual(self.g_p.grau('J'), 1)
        self.assertEqual(self.g_p.grau('C'), 7)
        self.assertEqual(self.g_p.grau('E'), 2)
        self.assertEqual(self.g_p.grau('P'), 2)
        self.assertEqual(self.g_p.grau('M'), 2)
        self.assertEqual(self.g_p.grau('T'), 3)
        self.assertEqual(self.g_p.grau('Z'), 1)
        with self.assertRaises(VerticeInvalidoException):
            self.assertEqual(self.g_p.grau('G'), 5)

        self.assertEqual(self.g_d.grau('A'), 1)
        self.assertEqual(self.g_d.grau('C'), 0)
        self.assertNotEqual(self.g_d.grau('D'), 2)
        self.assertEqual(self.g_d2.grau('A'), 0)

        # Completos
        self.assertEqual(self.g_c.grau('J'), 3)
        self.assertEqual(self.g_c.grau('C'), 3)
        self.assertEqual(self.g_c.grau('E'), 3)
        self.assertEqual(self.g_c.grau('P'), 3)

        # Com laço. Lembrando que cada laço conta 2 vezes por vértice para cálculo do grau
        self.assertEqual(self.g_l1.grau('A'), 5)
        self.assertEqual(self.g_l2.grau('B'), 4)
        self.assertEqual(self.g_l4.grau('D'), 2)

    def test_ha_paralelas(self):
        self.assertTrue(self.g_p.ha_paralelas())
        self.assertFalse(self.g_p_sem_paralelas.ha_paralelas())
        self.assertFalse(self.g_c.ha_paralelas())
        self.assertFalse(self.g_c2.ha_paralelas())
        self.assertFalse(self.g_c3.ha_paralelas())
        self.assertTrue(self.g_l1.ha_paralelas())

    def test_arestas_sobre_vertice(self):
        self.assertEqual(self.g_p.arestas_sobre_vertice('J'), {'a1'})
        self.assertEqual(self.g_p.arestas_sobre_vertice('C'), {'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7'})
        self.assertEqual(self.g_p.arestas_sobre_vertice('M'), {'a7', 'a8'})
        self.assertEqual(self.g_l2.arestas_sobre_vertice('B'), {'a1', 'a2', 'a3'})
        self.assertEqual(self.g_d.arestas_sobre_vertice('C'), set())
        self.assertEqual(self.g_d.arestas_sobre_vertice('A'), {'asd'})
        with self.assertRaises(VerticeInvalidoException):
            self.g_p.arestas_sobre_vertice('A')

    def test_eh_completo(self):
        self.assertFalse(self.g_p.eh_completo())
        self.assertFalse((self.g_p_sem_paralelas.eh_completo()))
        self.assertTrue((self.g_c.eh_completo()))
        self.assertTrue((self.g_c2.eh_completo()))
        self.assertTrue((self.g_c3.eh_completo()))
        self.assertFalse((self.g_l1.eh_completo()))
        self.assertFalse((self.g_l2.eh_completo()))
        self.assertFalse((self.g_l3.eh_completo()))
        self.assertFalse((self.g_l4.eh_completo()))
        self.assertFalse((self.g_l5.eh_completo()))
        self.assertFalse((self.g_d.eh_completo()))
        self.assertFalse((self.g_d2.eh_completo()))

    def test_dfs(self):
        self.assertEqual(self.g_p.dfs('J'), ['J-C', 'C-E', 'P-C', 'T-C', 'M-T', 'T-Z'])
        self.assertEqual(self.g_p.dfs('C'), ['J-C', 'C-E', 'P-C', 'T-C', 'M-T', 'T-Z'])
        self.assertEqual(self.g_p.dfs('E'), ['C-E', 'J-C', 'P-C', 'T-C', 'M-T', 'T-Z'])
        self.assertEqual(self.g_p.dfs('M'), ['M-C', 'J-C', 'C-E', 'P-C', 'T-C', 'T-Z'])
        self.assertEqual(self.g_p.dfs('T'), ['T-C', 'J-C', 'C-E', 'P-C', 'M-C', 'T-Z'])
        self.assertEqual(self.g_p.dfs('Z'), ['T-Z', 'T-C', 'J-C', 'C-E', 'P-C', 'M-C'])
        self.assertEqual(self.g_p.dfs('P'), ['P-C', 'J-C', 'C-E', 'T-C', 'M-T', 'T-Z'])

    def test_bfs(self):
        self.assertEqual(self.g_p.bfs('J'), ['J-C', 'C-E', 'P-C', 'T-C', 'M-C', 'T-Z'])
        self.assertEqual(self.g_p.bfs('C'), ['J-C', 'C-E', 'P-C', 'T-C', 'M-C', 'T-Z'])
        self.assertEqual(self.g_p.bfs('E'), ['C-E', 'J-C', 'P-C', 'T-C', 'M-C', 'T-Z'])
        self.assertEqual(self.g_p.bfs('M'), ['M-C', 'M-T', 'J-C', 'C-E', 'P-C', 'T-Z'])
        self.assertEqual(self.g_p.bfs('T'), ['T-C', 'M-T', 'T-Z', 'J-C', 'C-E', 'P-C'])
        self.assertEqual(self.g_p.bfs('Z'), ['T-Z', 'T-C', 'M-T', 'J-C', 'C-E', 'P-C'])
        self.assertEqual(self.g_p.bfs('P'), ['P-C', 'J-C', 'C-E', 'T-C', 'M-C', 'T-Z'])

    def test_eh_conexo(self):
        self.assertEqual(self.g_p.eh_conexo(), True)
        self.assertEqual(self.g_pNOVO.eh_conexo(), False)
        self.assertEqual(self.g_pNOVO2.eh_conexo(), False)

    def test_ha_ciclo(self):
        self.assertEqual(self.g_pNOVO2.ha_ciclo(), True)
        self.assertEqual(self.g_pNOVO.ha_ciclo(), True)
        self.assertEqual(self.g_pNOVO3.ha_ciclo(), False)
        self.assertEqual(self.g_p.ha_ciclo(), True)


    def test_caminho(self):
        self.assertEqual(self.g_p.caminho(8), False)
        self.assertEqual(self.g_pNOVO2.caminho(3), ['J', 'a1', 'C', 'a2', 'E'])
        self.assertEqual(self.g_pNOVO.caminho(2), ['J', 'a1', 'C'])
        self.assertEqual(self.g_pNOVO3.caminho(10), False)
        self.assertEqual(self.g_pNOVO3.caminho(5), False)

    def test_dijkstra_drone(self):
        self.assertEqual(self.g_p.djikstra("J", "Z"), ['J', 'C', 'T', 'Z'])
        self.assertEqual(self.g_pNOVO.djikstra("E", "W"), False)
        self.assertEqual(self.g_pNOVO2.djikstra("C", "E"), ['C', 'E'])
        self.assertEqual(self.g_p2.djikstra("P", "M"), ['P', 'C', 'M'])

    def test_kruskall(self):
        self.assertEqual(self.g_pP1.kruskall(), self.g_p_COMPESO)
        self.assertEqual(self.g_pP2.kruskall(), self.g_p_COMPESO2)

    def test_prim(self):
        self.assertEqual(self.g_pP1.prim(), self.g_p_COMPESO)











