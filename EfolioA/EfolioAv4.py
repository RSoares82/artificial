import heapq
import time

grelha = [
    [
        [1, 1, 1, 1, -1],
        [1, 10, 1, 2, 10],
        [1, -2, 10, 2, 1],
        [10, 10, 1, 1, 1],
        [-1, 1, 1, 2, -2],
    ],
    [
        [-1,1,2,2,-1],
        [1,2,1,1,10],
        [1,1,10,2,2],
        [10,2,1,10,1],
        [-1,2,1,10,-2],
    ],
    [
        [1, 1, 1, 1, 10, -2, 1],
        [1, -2, 10, 1, 1, 10, 1],
        [1, 10, 1, 10, 1, 1, 1],
        [1, 1, -2, 10, 1, 2, 1],
        [2, 1, 10, 1, 2, 1, 10],
        [2, 1, 1, 1, 2, 10, -3],
        [1, -1, 10, 1, 1, 1, 1],
    ],
    [
        [1, -2, 2, 2, 2, -2, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 10, 10, 10, 10, 10, 1],
        [1, 1, -2, 10, 1, 2, 1],
        [2, 2, 2, 10, 2, 10, 10],
        [2, 1, 2, 10, 2, 10, -3],
        [1, -1, 2, 1, 1, 1, 1],
    ],
    [
        [-2, 10, 1, 1, 1, 1, -2, 1, 1],
        [1, 2, -2, 10, 10, 1, 1, 10, 2],
        [1, 1, 1, 1, 1, 10, 10, 1, 1],
        [1, 10, 10, 1, 10, -2, 1, 1, 1],
        [1, 1, 10, 1, 1, 1, 2, 10, 1],
        [2, 1, 1, 10, 1, 2, 10, 1, 1],
        [10, 10, 2, 2, 2, 2, 10, -3, 1],
        [2, 1, 1, 10, 1, 2, 10, 1, 10],
        [-8, 10, 1, 1, 1, 1, 1, 1, 1]
    ],
    [
        [1, -5, 1, 10, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 10, 1, 2, 1, 10, 1, 1, 1, 1],
        [1, 10, 10, 1, 1, 1, 1, 10, 1, -3, 1],
        [1, 2, -1, 10, 2, 2, 1, 2, 10, 1, 1],
        [2, 1, 1, 1, 10, 2, 1, 1, 2, 10, 1],
        [1, 2, 1, 1, 1, 10, -2, 1, 2, 10, 1],
        [2, 1, 2, 10, 1, 1, 10, 1, 1, 10, 1],
        [1, -1, 1, 10, 1, 2, 1, 1, 10, 2, 1],
        [1, 10, 10, 10, 1, 2, -1, 10, 2, 2, 1],
        [1, 1, 1, 1, 1, 2, 10, 1, 1, 1, -4],
        [1, 1, -2, 2, 1, 1, 1, 2, 2, 2, 1]
    ],
    [
        [1, 1, 1, 1, 1, 10, 1, 2, 1, 1, 1, 1, 1],
        [-1, 10, 1, 10, 1, 2, 10, 1, 10, 2, 10, 10, 1],
        [10, 1, 1, 10, 1, 2, 10, 2, 10, 1, 10, -1, 1],
        [1, 1, 10, 1, 1, 1, -1, 1, 10, -1, 1, 10, 10],
        [1, 10, 1, 1, 1, 10, 1, 1, 10, 10, 1, 1, 1],
        [1, 10, -1, 10, 1, 1, 10, 1, 1, 1, 10, 10, 1],
        [1, 10, 1, 1, 10, 1, 1, 10, 10, 1, 1, 10, 1],
        [10, 10, 10, -1, 1, 10, 1, 1, 10, 1, 1, 10, 1],
        [1, 2, 1, 10, 2, 1, 10, 1, 10, -1, 10, 1, 1],
        [1, 10, 2, 1, 10, 2, 10, 1, 10, 1, 10, 1, 1],
        [1, -1, 10, 1, 2, 1, 10, 1, 10, 1, 1, 1, 10],
        [1, 10, 1, 10, 10, 10, 10, 1, 10, 1, 10, 10, -1],
        [1, 1, 1, -1, 1, 1, 1, 1, 10, 1, 1, 1, 1]
    ],
    [
        [-3, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, -3, 1, -2],
        [1, 1, 1, 1, 1, 10, 10, 10, 10, 10, 1, 1, 2, 1, 2],
        [1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, -2],
        [1, 1, 1, 1, 1, 1, -2, 2, 1, -3, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1],
        [1, 10, 1, 1, 1, 2, 2, 1, 2, 1, 1, 1, -1, 10, 1],
        [1, 10, -3, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 10, 1],
        [1, 10, 1, 1, -2, 2, 1, 1, 1, 1, 2, 2, 1, 10, 1],
        [1, 10, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 10, 2],
        [1, 10, -2, 2, 1, 2, 1, 2, 1, 1, 1, 1, 1, 10, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2],
        [-2, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, -3, 1],
        [1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 2, 1, 1, 1, 10, 10, 10, 10, 10, 1, 1, 2, 1, 1],
        [1, 1, -3, 1, 1, 1, 1, 1, 1, 1, 1, -3, 1, 1, -4]
    ],
    [
        [-3, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, -3, 1, -2],
        [1, 1, 1, 1, 1, 10, 10, 10, 10, 10, 1, 1, 2, 1, 2],
        [1, 1, 1, 1, 1, 2, 1, 10, 1, 1, 1, 1, 1, 1, -2],
        [1, 1, 1, 1, 1, 1, -2, 10, 1, -3, 1, 1, 1, 1, 1],
        [1, 10, 10, 10, 1, 10, 1, 10, 1, 10, 1, 10, 10, 10, 1],
        [1, 10, 1, 1, 1, 10, 2, 10, 2, 10, 1, 1, -1, 10, 1],
        [1, 10, -3, 1, 2, 10, 1, 1, 1, 10, 1, 1, 1, 10, 1],
        [1, 10, 1, 1, -2, 10, 10, 10, 10, 10, 2, 2, 1, 10, 1],
        [1, 10, 1, 1, 1, 10, 2, 1, 1, 10, 1, 1, 1, 10, 2],
        [1, 10, -2, 2, 1, 10, 1, 10, 1, 10, 1, 1, 1, 10, 1],
        [1, 10, 10, 10, 1, 10, 1, 10, 1, 10, 2, 10, 10, 10, 2],
        [-2, 1, 1, 2, 1, 2, 1, 10, 1, 2, 1, 2, 1, -3, 1],
        [1, 1, 1, 1, 2, 1, 1, 10, 1, 1, 1, 1, 1, 1, 1],
        [1, 2, 1, 1, 1, 10, 10, 10, 10, 10, 1, 1, 2, 1, 1],
        [1, 1, -3, 1, 1, 1, 1, 1, 1, 1, 1, -3, 1, 1, -4]
    ],
    [
        [-6, 10, 1, 1, 1, 1, 1, 1, 2, 2, 2, 10, -6, 1, -4],
        [1, 10, 1, 10, 1, 10, 10, 10, 10, 10, 1, 1, 2, 10, 2],
        [1, 10, 1, 10, 1, 2, 1, 10, 1, 10, 1, 10, 1, 10, -4],
        [1, 1, 1, 10, 1, 10, -4, 10, 1, -6, 1, 10, 1, 1, 1],
        [1, 10, 10, 10, 1, 10, 1, 10, 1, 10, 1, 10, 10, 10, 1],
        [1, 10, 1, 1, 1, 10, 2, 10, 2, 10, 1, 10, -2, 10, 1],
        [1, 10, -6, 10, 2, 10, 1, 1, 1, 10, 1, 10, 1, 10, 1],
        [1, 10, 1, 10, -4, 10, 10, 10, 10, 10, 2, 2, 1, 10, 1],
        [1, 10, 1, 10, 10, 10, 2, 1, 1, 10, 10, 10, 1, 10, 2],
        [1, 10, -4, 2, 1, 1, 1, 10, 1, 10, 1, 1, 1, 10, 1],
        [1, 10, 10, 10, 1, 10, 1, 10, 1, 10, 2, 10, 10, 10, 2],
        [-4, 1, 1, 2, 1, 10, 1, 10, 1, 2, 1, 2, 1, -6, 1],
        [10, 10, 1, 10, 2, 10, 1, 10, 1, 10, 1, 10, 10, 10, 10],
        [1, 10, 1, 10, 1, 10, 10, 10, 10, 10, 1, 10, 2, 10, 1],
        [1, 1, -6, 10, 1, 1, 1, 1, 1, 1, 1, -6, 1, 1, -8]
    ]
]

expansao = 0
geracao = 0

# Define o Estado da Grelha
class Estado:
    def __init__(self, posicao, pai=None, acao=None, custo=0, tempo=None):
        self.posicao = posicao
        self.pai = pai
        self.acao = acao
        self.custo = custo
        self.tempo = tempo

    # To compare nodes based on path cost for the priority queue
    def __lt__(self, other):
        return self.custo < other.custo

class Problema:
    def __init__(self, grelha, tamanho_grelha, funcao_custo, objetivo="Salvar"):
        self.grelha = grelha
        self.tamanho_grelha = tamanho_grelha  # Size of the grid (5x5)
        self.funcao_custo = funcao_custo  # A function to get the cost of an action
        self.objetivo = objetivo


    def verifica_objetivo(self, estado):
        if self.grelha[estado.posicao[0]][estado.posicao[1]] < 0:
            return True

    def gerar_sucessores(self, estado, problema, portas, objetivo):
        global expansao
        # Expand a node to generate child nodes by moving in the grid
        sucessores = []
        acoes_possiveis = [
            (-1, 0),  # cima
            (1, 0),   # baixo
            (0, -1),  # esquerda
            (0, 1)    # direita
        ]

        if expansao == 1:
            for (sx, sy) in portas:
                # Instead of modifying the grid, just store the position of 'X'
                if grelha[sx][sy] != 10:
                    pos_prox_estado = (sx, sy)
                    if grelha[sx][sy] == 1:
                        custo = 1
                    elif grelha[sx][sy] == 2:
                        custo = 2
                    sucessor = Estado(posicao=pos_prox_estado, pai=estado, custo=estado.custo + custo, tempo=estado.tempo - custo)
                    sucessores.append(sucessor)
        else:
            for acao in acoes_possiveis:
                pos_prox_estado = (estado.posicao[0] + acao[0], estado.posicao[1] + acao[1])
                # Check if the next state is within grid bounds
                if 0 <= pos_prox_estado[0] < len(self.grelha) and 0 <= pos_prox_estado[1] < len(self.grelha[0]):

                    if problema.grelha[pos_prox_estado[0]][pos_prox_estado[1]] != 10:
                        custo = self.funcao_custo(estado.posicao, pos_prox_estado)
                        if estado.tempo > 0:
                            sucessor = Estado(posicao=pos_prox_estado, pai=estado, acao=acao, custo=estado.custo + custo, tempo=estado.tempo - custo)
                            sucessores.append(sucessor)

        #Cortar sucessores k nos afastem da nossa saida
        if problema.objetivo == "Sair":
            sucessorProximoSaida = saidaMaisProxima(sucessores, portas)
            sucessores.clear()
            sucessores.append(sucessorProximoSaida)
            return sucessores

        return sucessores

    # def __init__(self, pai=None, movimento=None, geracao=0, nivel=0, expansao=0, posicao=None, custo=0, tempototal=0, pessoassalvas = 0, custototal=0):
    #     self.pai = pai
    #     self.movimento = movimento
    #     self.geracao = geracao
    #     self.custo = custo
    #     self.custoTotal = custototal
    #     self.nivel = nivel
    #     self.expansao = expansao
    #     self.posicao = posicao
    #     self.pessoasSalvas = pessoassalvas
    #     self.tempoTotal = tempototal

def saidaMaisProxima(coordinates, portas):
    # List of possible exits
    #saidas = [(0, 2), (2, 0), (4, 2), (2, 4)]

    # Initialize the minimum distance as a large number
    min_distance = float('inf')
    closest_coordinate = None

    # Loop through all coordinates and find the closest one
    for coord in coordinates:
        # Check distance to each exit and pick the closest one
        for saida in portas:
            distance = manhattan_distance(coord, saida)
            if distance < min_distance:
                min_distance = distance
                closest_coordinate = coord
                #print(f"GGGGGGGGGGGGGGGGGGGGGGGGG         {closest_coordinate} ")

    return closest_coordinate

def imprimeGrelha(estado, grelha):
    transformaGrelha = []  # To store the new transformed grid

    # print(type(self.posicao))
    for i, row in enumerate(grelha):
        transformaLinha = []

        for j, value in enumerate(row):
            coord_tuple = (i, j)
            if estado.posicao == coord_tuple:
                # print("aqui")
                # print(f"({i},{j})")
                if value == 1:
                    transformaLinha.append('(.)')
                elif value == 10:
                    transformaLinha.append(' # ')
                elif value == 2:
                    transformaLinha.append('(:)')
                else:
                    transformaLinha.append('(' + str(abs(value)) + ')')  # Absolute value for negative numbers
            else:
                if value == 1:
                    transformaLinha.append(' . ')
                elif value == 10:
                    transformaLinha.append(' # ')
                elif value == 2:
                    transformaLinha.append(' : ')
                else:
                    transformaLinha.append(' ' + str(abs(value)) + ' ')  # Absolute value for negative numbers

        # Append the transformed row to the grid
        transformaGrelha.append("".join(transformaLinha))

    for row in transformaGrelha:
        print(row)

    # Return the transformed grid
    #return transformaGrelha

def imprimeGrelha2(caminho, grelha):
    # Create a transformed grid to store the updated grid with the path
    transformaGrelha = []

    # Iterate over each row in the original grid
    for i, row in enumerate(grelha):
        transformaLinha = []  # Temporary list to store the transformed row

        # Iterate over each column in the row
        for j, value in enumerate(row):
            coord_tuple = (i, j)

            if coord_tuple in caminho:  # Check if the current position is in the path
                # If it's part of the path, mark it differently
                if value == 1:
                    transformaLinha.append('(.)')  # Path on a walkable cell
                elif value == 10:
                    transformaLinha.append(' # ')  # Obstacle, no path here
                elif value == 2:
                    transformaLinha.append('(:)')  # Special point, like start or goal
                else:
                    transformaLinha.append('(' + str(abs(value)) + ')')  # Negative values or other custom marks
            else:
                # Regular transformation for non-path positions
                if value == 1:
                    transformaLinha.append(' . ')  # Walkable area
                elif value == 10:
                    transformaLinha.append(' # ')  # Obstacle
                elif value == 2:
                    transformaLinha.append(' : ')  # Special point
                else:
                    transformaLinha.append(' ' + str(abs(value)) + ' ')  # Negative values or other custom marks

        # Append the transformed row to the transformed grid
        transformaGrelha.append("".join(transformaLinha))

    # Print the final grid with the path
    for row in transformaGrelha:
        print(row)

def refazerCaminho(estado):
    caminho = []

    while estado is not None:
        caminho.append(estado.posicao)
        estado = estado.pai

    return caminho[::-1]  # Reverse the path to get it from the start to the goal

def manhattan_distance(start, exit):
    # Calculate Manhattan distance between start and exit
    return abs(start[0] - exit[0]) + abs(start[1] - exit[1])

def saidaMaisProxima(coordinates, portas):
    # List of possible exits
    #saidas = [(0, 2), (2, 0), (4, 2), (2, 4)]

    # Initialize the minimum distance as a large number
    min_distance = float('inf')
    closest_coordinate = None

    # Loop through all coordinates and find the closest one
    for coord in coordinates:
        # Check distance to each exit and pick the closest one
        for saida in portas:
            distance = manhattan_distance(coord, saida)
            if distance < min_distance:
                min_distance = distance
                closest_coordinate = coord
                #print(f"GGGGGGGGGGGGGGGGGGGGGGGGG         {closest_coordinate} ")

    return closest_coordinate

def gerarSucessoresIniciais(grelha, portas):
    successors = []  # To store the positions where 'X' will be placed

    # Generate successors for each starting point
    for (sx, sy) in portas:
        # Instead of modifying the grid, just store the position of 'X'
        if grelha[sx][sy] != 10:
            successors.append((sx, sy))  # Append the coordinates of the 'X'

    return successors

def gerarSucessores(grelha, portas, estadoAtual, k, objetivo, ):
    # Define the possible movement directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # (dy, dx) for up, down, left, right

    possible_moves = []

    # Get the current position (row, col)
    row, col = estadoAtual.posicao

    for dy, dx in directions:
        new_row, new_col = row + dy, col + dx

        # Check if the new position is within bounds
        if 0 <= new_row < len(grelha) and 0 <= new_col < len(grelha[0]):
            # Verificação de Parede
            if grelha[new_row][new_col] != 10:
                # print(f"( {grelha[new_row][new_col]} )")
                if (new_row, new_col) == estadoAtual.pai.posicao:
                    possible_moves.append((new_row, new_col))
                else:
                    possible_moves.insert(0, (new_row, new_col))


        #print(f"posicao pai: {estadoAtual.pai.posicao}")

        # Se os sucessores forem pelo menos dois, evitar percorrer o caminho contrario
        # A não ser que só tenhamos esse caminho para voltar para traz
        # if len(possible_moves) >= 2 and estadoAtual.pai.posicao in possible_moves:
        #     possible_moves.remove(estadoAtual.pai.posicao)

        # É altura de sair eliminar sucessores que nos afastem da saida
        # if len(possible_moves) >= 2 and estadoAtual.pessoasSalvas == k:
        if objetivo == "Sair":
            print("É para Sair !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            caminho = refazerCaminho(estadoAtual)
            print(" ")
            print(caminho)
            imprimeGrelha2(caminho, grelha)
            print(f"Pos: {estadoAtual}")
            sucessorProximoSaida = saidaMaisProxima(possible_moves, portas)
            possible_moves.clear()
            possible_moves.append(sucessorProximoSaida)
            return possible_moves

    return possible_moves

def pessoaEncontrada(estadoAtual, grelha):
    if estadoAtual.posicao:
        row, col = estadoAtual.posicao
        #print(estadoAtual.posicao)
        if grelha[row][col] < 0:
            return True

    return False

def custo_movimento(estado, prox_estado):
    #print("item grelha:")
    #print(grelha[sx][sy])
    # if grelha[sx][sy] == 1:
    #     return 1
    if grelha[prox_estado[0]][prox_estado[1]] == 2:
        return 2
    else:
        return 1

def custo_uniforme(problema, tempo, k, portas):
    global expansao
    global geracao

    # Create initial node
    estado = Estado(posicao=None, custo=1, tempo=tempo)

    # Priority Queue (Min-Heap)
    fronteira = []
    heapq.heappush(fronteira, estado)


    solucao = []
    encontrados = set()
    salvos = 0
    # Set of reached states to avoid revisiting
    visitado = set()

    while fronteira:
        # Pop the node with the least cost
        estado = heapq.heappop(fronteira)
        expansao += 1

        # If it's a goal node, return it
        if problema.objetivo != "Sair":
            if expansao != 1 and problema.verifica_objetivo(estado) and estado.posicao not in encontrados:
                salvos += 1

                encontrados.add(estado.posicao)
                sx, sy = estado.posicao
                estado.tempo += abs(problema.grelha[sx][sy])
                fronteira.clear()
                visitado.clear()

                if salvos < k:
                    heapq.heappush(fronteira, estado)
                    solucao.append(estado)

                # if k == salvos:
                #     return solucao
        #if estado.tempo <= int(len(problema.grelha) / 2) and estado.posicao in portas and salvos == k:
        if  estado.posicao in portas and salvos == k:
            problema.objetivo = "Sair"
            estado.custo += 1
            solucao.append(estado)

            # caminho = refazerCaminho(estado)
            # print(caminho)
            # #print("Fim")
            return solucao

        # Expand the node and add children to the frontier
        for filho in problema.gerar_sucessores(estado, problema, portas, problema.objetivo):
            if filho.posicao not in visitado:
                visitado.add(filho.posicao)
                heapq.heappush(fronteira, filho)
                geracao += 1

    return None

def tamanhoGrelha(grid):
    result = len(grid)        # Number of rows
    return (result, result)

def calcular_portas(grelha):
    # Calculate grid size
    rows = len(grelha)
    cols = len(grelha) if rows > 0 else 0

    # List of relative exit positions (fixed positions based on a smaller grid)
    portas = [(0, cols // 2), (rows - 1, cols // 2), (rows // 2, 0), (rows // 2, cols - 1)]

    return portas



# portas
#portas = [(0, 2), (4, 2), (2, 0), (2, 4)]

# self, grelha, pai=None, movimento=None, geracao=1, nivel=0, expansao=0):

# Display available grid options to the user
print("Select a grid:")
for i, grid in enumerate(grelha):
    print(f"{i + 1}. Grid {i + 1}")

# Let the user select a grid
grid_choice = int(input("Enter the number of the grid you want to use: "))

# Switch logic
if grid_choice == 1:
    grelha = grelha[0]
    tamanho_grelha = tamanhoGrelha(grelha[0])
    portas = calcular_portas(grelha[0])
    tempo = 10
    k = 2
elif grid_choice == 2:
    grelha = grelha[1]
    tamanho_grelha = tamanhoGrelha(grelha[1])
    portas = calcular_portas(grelha[1])
    tempo = 20
    k = 3
elif grid_choice == 3:
    grelha = grelha[2]
    tamanho_grelha = tamanhoGrelha(grelha[2])
    portas = calcular_portas(grelha[2])
    tempo = 15
    k = 3
elif grid_choice == 4:
    grelha = grelha[3]
    tamanho_grelha = tamanhoGrelha(grelha[3])
    portas = calcular_portas(grelha[3])
    tempo = 20
    k = 4
elif grid_choice == 5:
    grelha = grelha[4]
    tamanho_grelha = tamanhoGrelha(grelha[4])
    portas = calcular_portas(grelha[4])
    tempo = 19
    k = 4
elif grid_choice == 6:
    grelha = grelha[5]
    tamanho_grelha = tamanhoGrelha(grelha[5])
    portas = calcular_portas(grelha[5])
    tempo = 48
    k = 6
elif grid_choice == 7:
    grelha = grelha[6]
    tamanho_grelha = tamanhoGrelha(grelha[6])
    portas = calcular_portas(grelha[6])
    tempo = 120
    k = 10
elif grid_choice == 8:
    grelha = grelha[7]
    tamanho_grelha = tamanhoGrelha(grelha[7])
    portas = calcular_portas(grelha[7])
    tempo = 30
    k = 10
elif grid_choice == 9:
    grelha = grelha[8]
    tamanho_grelha = tamanhoGrelha(grelha[8])
    portas = calcular_portas(grelha[8])
    tempo = 45
    k = 10
elif grid_choice == 10:
    grelha = grelha[9]
    tamanho_grelha = tamanhoGrelha(grelha[9])
    portas = calcular_portas(grelha[9])
    tempo = 45
    k = 15
else:
    print("Escolha invalida!")
    exit()

start_time = time.time()

# solucaoFinal = bfs(grelha, estadoInicial, portas, k)
# Create a problem instance
problema = Problema(grelha=grelha, tamanho_grelha=tamanho_grelha, funcao_custo=custo_movimento)

# Run the Uniform-Cost Search
resultado = custo_uniforme(problema, tempo, k, portas)

# Print the result path
if resultado:
    for index, item in enumerate(resultado):
        print(f"Parte {index + 1} passos ")
        caminho = refazerCaminho(item)
        print(caminho)
        imprimeGrelha2(caminho, grelha)

        print(f"Tempo: {item.tempo} ({index + 1}/{len(resultado)}), custo: {item.custo}")
        print(f"Expansoes: {expansao}")
        print(f"Geracoes: {geracao}")
else:
    print("No solution found")

end_time = time.time()
elapsed_time = end_time - start_time

print(f"\nTime taken to find the solution: {elapsed_time:.4f} seconds")

#     #estadoInicial = EstadoGrelha(geracao=geracao, tempototal=10)
#     #imprimeGrelha(estadoInicial, grelha)
#     #portas = get_exits(grelha)
#     #print("Exits for grid1:", portas)
#     k = 2
# elif grid_choice == 2:
#     grelha = grelha[grid_choice - 1]
#     print("You have selected Grid 2")
#     estadoInicial = EstadoGrelha(geracao=geracao, tempototal=20)
#     imprimeGrelha(estadoInicial, grelha)
#     portas = get_exits(grelha)
#     print("Exits for grid1:", portas)
#     k = 3
# elif grid_choice == 3:
#     grelha = grelha[grid_choice - 1]
#     print("You have selected Grid 3")
#     estadoInicial = EstadoGrelha(geracao=geracao, tempototal=15)
#     imprimeGrelha(estadoInicial, grelha)
#     portas = get_exits(grelha)
#     print("Exits for grid1:", portas)
#     k = 3
# elif grid_choice == 4:
#     grelha = grelha[grid_choice - 1]
#     print("You have selected Grid 3")
#     estadoInicial = EstadoGrelha(geracao=geracao, tempototal=20)
#     imprimeGrelha(estadoInicial, grelha)
#     portas = get_exits(grelha)
#     print("Exits for grid1:", portas)
#     k = 4
# elif grid_choice == 5:
#     grelha = grelha[grid_choice - 1]
#     print("You have selected Grid 2")
#     estadoInicial = EstadoGrelha(geracao=geracao, tempototal=19)
#     imprimeGrelha(estadoInicial, grelha)
#     portas = get_exits(grelha)
#     print("Exits for grid1:", portas)
#     k = 4
# elif grid_choice == 6:
#     grelha = grelha[grid_choice - 1]
#     print("You have selected Grid 3")
#     estadoInicial = EstadoGrelha(geracao=geracao, tempototal=48)
#     imprimeGrelha(estadoInicial, grelha)
#     portas = get_exits(grelha)
#     k = 6
# elif grid_choice == 7:
#     grelha = grelha[grid_choice - 1]
#     print("You have selected Grid 3")
#     estadoInicial = EstadoGrelha(geracao=geracao, tempototal=120)
#     imprimeGrelha(estadoInicial, grelha)
#     portas = get_exits(grelha)
#     print("Exits for grid1:", portas)
#     k = 10
# elif grid_choice == 8:
#     grelha = grelha[grid_choice - 1]
#     print("You have selected Grid 2")
#     estadoInicial = EstadoGrelha(geracao=geracao, tempototal=30)
#     imprimeGrelha(estadoInicial, grelha)
#     portas = get_exits(grelha)
#     print("Exits for grid1:", portas)
#     k = 10
# elif grid_choice == 9:
#     grelha = grelha[grid_choice - 1]
#     print("You have selected Grid 3")
#     estadoInicial = EstadoGrelha(geracao=geracao, tempototal=45)
#     imprimeGrelha(estadoInicial, grelha)
#     portas = get_exits(grelha)
#     print("Exits for grid1:", portas)
#     k = 10
# elif grid_choice == 10:
#     grelha= grelha[grid_choice - 1]
#     print("You have selected Grid 3")
#     estadoInicial = EstadoGrelha(geracao=geracao, tempototal=45)
#     imprimeGrelha(estadoInicial, grelha)
#     portas = get_exits(grelha)
#     print("Exits for grid1:", portas)
#     k = 15
# else:
#     print("Invalid selection. Please choose a valid grid number.")

# # Inicialização do objeto do estado
# estadoInicial = EstadoGrelha(geracao=geracao)
# imprimeGrelha(estadoInicial, grelha)
#
# portas = get_exits(grelha)
#
# print("Exits for grid1:", portas)





# k = 2
# # Executar a procura em Largura
#
# # Record start time


# total = len(solucaoFinal)
# for index, item in enumerate(solucaoFinal):
#     if index == 0:
#         caminho = refazerCaminho(item)
#         print(" ")
#         print(caminho)
#         print(f"Parte {index + 1}, passos: {len(caminho)}")
#         imprimeGrelha2(caminho, grelha)
#         print(f"Tempo: {item.tempoTotal} ({index + 1}/{total}), custo: {item.custoTotal}")
#         print(f"Expansoes: {item.expansao}")
#         print(f"Geracoes: {item.geracao}")
#     else:
#         item_anterior = solucaoFinal[index - 1]
#         caminho_anterior = len(refazerCaminho(item_anterior))
#         caminho = refazerCaminho(item)
#         passos = len(caminho) - caminho_anterior + 1
#         print(" ")
#         print(caminho)
#         print(f"Parte {index + 1}, passos: {passos}")
#         imprimeGrelha2(caminho, grelha)
#         print(f"Tempo: {item.tempoTotal} ({index + 1}/{total}), custo: {item.custoTotal}")
#         print(f"Expansoes: {item.expansao}")
#         print(f"Geracoes: {item.geracao}")
#
# print(f"\nTime taken to find the solution: {elapsed_time:.4f} seconds")
