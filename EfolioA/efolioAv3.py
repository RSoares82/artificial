from collections import deque
import time

grelha = [
    [
        [1, 1, 1, 1, -1],
        [1, 10, 1, 2, 10],
        [1, -2, 10, 2, 1],
        [10, 10, 1, 1, 1],
        [-1, 1, 1, 2, -2]
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
geracao = 1

# Define o Estado da Grelha
class EstadoGrelha:
    def __init__(self, pai=None, movimento=None, geracao=0, nivel=0, expansao=0, posicao=None, custo=0, tempototal=0, pessoassalvas = 0, custototal=0):
        self.pai = pai
        self.movimento = movimento
        self.geracao = geracao
        self.custo = custo
        self.custoTotal = custototal
        self.nivel = nivel
        self.expansao = expansao
        self.posicao = posicao
        self.pessoasSalvas = pessoassalvas
        self.tempoTotal = tempototal

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


def refazerCaminho(estadoAtual):
    caminho = []

    if estadoAtual.pai is None:
        return caminho

    caminho.extend(refazerCaminho(estadoAtual.pai))
    caminho.append(estadoAtual.posicao)

    return caminho

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

def gerarSucessores(grelha, portas, estadoAtual, k, objetivo):
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

def custoMovimento(sx, sy, grelha):
    #print("item grelha:")
    #print(grelha[sx][sy])
    # if grelha[sx][sy] == 1:
    #     return 1
    if grelha[sx][sy] == 2:
        return 2
    else:
        return 1


def bfs(grelha, estado, portas, k):
    global expansao
    global geracao
    salvos = set()
    queue = deque([estado])
    solucao = []
   # salvos = 0
    objetivo = "Salvar"

    while queue:
        estadoAtual = queue.popleft()

        expansao += 1
        estadoAtual.expansao = expansao
        #print(f"Expansao: {estadoAtual.expansao}, Geracao: {estadoAtual.geracao}")
        #imprimeGrelha(estadoAtual, grelha)
        #print(f"Custo Total: {estadoAtual.custoTotal}")

        # Continuar a procurar pessoas enquanto n tivermos K
        if pessoaEncontrada(estadoAtual, grelha) and estadoAtual.pessoasSalvas < k:
            if estadoAtual.posicao not in salvos:
                #print("##########")
                #imprimeGrelha(estadoAtual, grelha)
                # print(f"Pos: {estadoAtual.posicao}")
                # caminho = refazerCaminho(estadoAtual)
                # print(caminho)
                #imprimeGrelha2(caminho, grelha)
                #print(f"Tempo: {estadoAtual.tempoTotal}")
                salvos.add(estadoAtual.posicao)
                sx, sy = estadoAtual.posicao
                estadoAtual.tempoTotal += abs(grelha[sx][sy])
                #salvos += 1
                estadoAtual.pessoasSalvas += 1
                #print(f"Tempo atualizado: {estadoAtual.tempoTotal}")
                #print(f"Custo Total: {estadoAtual.custoTotal}")
                if estadoAtual.pessoasSalvas < k:
                    solucao.append(estadoAtual)
                    caminho = refazerCaminho(estadoAtual)
                    print(caminho)

                # Cortamos os Estados Anteriores que já não nos interessam continuamos a BFS do estado Atual
                queue.clear()
                queue.append(estadoAtual)

                #input("Press Enter to continue to the next person...")  # Wait for user to press Enter
                #elif estadoAtual.tempoTotal <= int(len(grelha) / 2) and estadoAtual.posicao in portas and estadoAtual.pessoasSalvas == k:
        elif estadoAtual.tempoTotal <= int(len(grelha) / 2) and estadoAtual.posicao in portas and estadoAtual.pessoasSalvas == k:
            # Adicionar custo de sair da grelha
            objetivo = "Sair"
            estadoAtual.custoTotal += 1
            solucao.append(estadoAtual)
            caminho = refazerCaminho(estadoAtual)
            print(caminho)
            #print("Fim")
            return solucao

        # if estadoAtual.tempoTotal <= 0:
        #     print("The End")
        #     caminho = refazerCaminho(estadoAtual)
        #     print(caminho)
        #     imprimeGrelha2(caminho, grelha)
        #     print(f"Tempo: {estadoAtual.tempoTotal}")
        #     return "Fim"




        if estadoAtual.geracao == 1:
            sucessores = gerarSucessoresIniciais(grelha, portas)
            # Ordenar Sucessores por Custo
            sucessores = sorted(sucessores, key=lambda pos: custoMovimento(pos[0], pos[1], grelha))
            #print(sucessores)

            if sucessores:
                geracao = estadoAtual.geracao
                for (sx, sy) in sucessores:
                    geracao += 1
                    #print(f"Geracao: {geracao}")
                    custo = custoMovimento(sx, sy, grelha)
                    estadoGerado = EstadoGrelha(posicao=(sx, sy), geracao=geracao, pai=estadoAtual, custo=custo, tempototal=estadoAtual.tempoTotal - custo, pessoassalvas=estadoAtual.pessoasSalvas, custototal=estadoAtual.custoTotal + custo)
                    #print(f"Custo de mover para a posicao ({sx},{sy}): {custo} Tempo Total: {estadoGerado.tempoTotal}")
                    queue.append(estadoGerado)
                    #imprimeGrelha(estadoGerado, grelha)
        else:
            sucessores = gerarSucessores(grelha, portas, estadoAtual, k, objetivo)
            #print(f"Pos EstadoAtual: {estadoAtual.posicao}, Sucessores: {sucessores}")
            #sucessores = sorted(sucessores, key=lambda pos: custoMovimento(pos[0], pos[1], grelha))
            if sucessores:
                for (sx, sy) in sucessores:
                    if (sx, sy) not in salvos:
                        geracao += 1
                        #print(f"Geracao: {geracao}")
                        custo = custoMovimento(sx, sy, grelha)
                        estadoGerado = EstadoGrelha(posicao=(sx, sy), geracao=geracao, pai=estadoAtual, custo=custo, tempototal=estadoAtual.tempoTotal - custo, pessoassalvas=estadoAtual.pessoasSalvas, custototal=estadoAtual.custoTotal + custo)
                        #print(f"Custo de mover para a posicao ({sx},{sy}): {custo} Tempo Total: {estadoGerado.tempoTotal}")
                        queue.append(estadoGerado)
                        #imprimeGrelha(estadoGerado, grelha)

    return solucao


def get_exits(grid):
    # Calculate grid size
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    # List of relative exit positions (fixed positions based on a smaller grid)
    exits = [(0, cols // 2), (rows - 1, cols // 2), (rows // 2, 0), (rows // 2, cols - 1)]

    return exits



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
    grelha = grelha[grid_choice - 1]
    print("You have selected Grid 1")
    estadoInicial = EstadoGrelha(geracao=geracao, tempototal=10)
    imprimeGrelha(estadoInicial, grelha)
    portas = get_exits(grelha)
    print("Exits for grid1:", portas)
    k = 2
elif grid_choice == 2:
    grelha = grelha[grid_choice - 1]
    print("You have selected Grid 2")
    estadoInicial = EstadoGrelha(geracao=geracao, tempototal=20)
    imprimeGrelha(estadoInicial, grelha)
    portas = get_exits(grelha)
    print("Exits for grid1:", portas)
    k = 3
elif grid_choice == 3:
    grelha = grelha[grid_choice - 1]
    print("You have selected Grid 3")
    estadoInicial = EstadoGrelha(geracao=geracao, tempototal=15)
    imprimeGrelha(estadoInicial, grelha)
    portas = get_exits(grelha)
    print("Exits for grid1:", portas)
    k = 3
elif grid_choice == 4:
    grelha = grelha[grid_choice - 1]
    print("You have selected Grid 3")
    estadoInicial = EstadoGrelha(geracao=geracao, tempototal=20)
    imprimeGrelha(estadoInicial, grelha)
    portas = get_exits(grelha)
    print("Exits for grid1:", portas)
    k = 4
elif grid_choice == 5:
    grelha = grelha[grid_choice - 1]
    print("You have selected Grid 2")
    estadoInicial = EstadoGrelha(geracao=geracao, tempototal=19)
    imprimeGrelha(estadoInicial, grelha)
    portas = get_exits(grelha)
    print("Exits for grid1:", portas)
    k = 4
elif grid_choice == 6:
    grelha = grelha[grid_choice - 1]
    print("You have selected Grid 3")
    estadoInicial = EstadoGrelha(geracao=geracao, tempototal=48)
    imprimeGrelha(estadoInicial, grelha)
    portas = get_exits(grelha)
    k = 6
elif grid_choice == 7:
    grelha = grelha[grid_choice - 1]
    print("You have selected Grid 3")
    estadoInicial = EstadoGrelha(geracao=geracao, tempototal=120)
    imprimeGrelha(estadoInicial, grelha)
    portas = get_exits(grelha)
    print("Exits for grid1:", portas)
    k = 10
elif grid_choice == 8:
    grelha = grelha[grid_choice - 1]
    print("You have selected Grid 2")
    estadoInicial = EstadoGrelha(geracao=geracao, tempototal=30)
    imprimeGrelha(estadoInicial, grelha)
    portas = get_exits(grelha)
    print("Exits for grid1:", portas)
    k = 10
elif grid_choice == 9:
    grelha = grelha[grid_choice - 1]
    print("You have selected Grid 3")
    estadoInicial = EstadoGrelha(geracao=geracao, tempototal=45)
    imprimeGrelha(estadoInicial, grelha)
    portas = get_exits(grelha)
    print("Exits for grid1:", portas)
    k = 10
elif grid_choice == 10:
    grelha= grelha[grid_choice - 1]
    print("You have selected Grid 3")
    estadoInicial = EstadoGrelha(geracao=geracao, tempototal=45)
    imprimeGrelha(estadoInicial, grelha)
    portas = get_exits(grelha)
    print("Exits for grid1:", portas)
    k = 15
else:
    print("Invalid selection. Please choose a valid grid number.")

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
start_time = time.time()

solucaoFinal = bfs(grelha, estadoInicial, portas, k)

end_time = time.time()
elapsed_time = end_time - start_time

total = len(solucaoFinal)
for index, item in enumerate(solucaoFinal):
    if index == 0:
        caminho = refazerCaminho(item)
        print(" ")
        print(caminho)
        print(f"Parte {index + 1}, passos: {len(caminho)}")
        imprimeGrelha2(caminho, grelha)
        print(f"Tempo: {item.tempoTotal} ({index + 1}/{total}), custo: {item.custoTotal}")
    else:
        item_anterior = solucaoFinal[index - 1]
        caminho_anterior = len(refazerCaminho(item_anterior))
        caminho = refazerCaminho(item)
        passos = len(caminho) - caminho_anterior + 1
        print(" ")
        print(caminho)
        print(f"Parte {index + 1}, passos: {passos}")
        imprimeGrelha2(caminho, grelha)
        print(f"Tempo: {item.tempoTotal} ({index + 1}/{total}), custo: {item.custoTotal}")

print(f"\nTime taken to find the solution: {elapsed_time:.4f} seconds")
