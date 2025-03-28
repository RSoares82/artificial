from collections import deque

grelha = [
    [1, 10, 1, 1, -1],
    [1, 10, 1, 2, 10],
    [1, -2, 10, 2, 1],
    [10, 10, 1, 1, 1],
    [-1, 1, 1, 2, -2]
]

expansao = 0

# Define o Estado da Grelha
class EstadoGrelha:
    def __init__(self, grelha, pai=None, movimento=None, geracao=1, nivel=0, expansao=0, posicao=None):
        self.grelha = grelha
        self.pai = pai
        self.movimento = movimento
        self.geracao = geracao
        self.nivel = nivel
        self.expansao = expansao
        self.posicao = posicao

    def imprimeGrelha(self):
        transformaGrelha = []  # To store the new transformed grid

        # print(type(self.posicao))
        for i, row in enumerate(self.grelha):
            transformaLinha = []

            for j, value in enumerate(row):
                coord_tuple = (i, j)
                if self.posicao == coord_tuple:
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


def gerarSucessoresIniciais(grelha, portas):
    successors = []  # To store the positions where 'X' will be placed

    # Generate successors for each starting point
    for (sx, sy) in portas:
        # Instead of modifying the grid, just store the position of 'X'
        successors.append((sx, sy))  # Append the coordinates of the 'X'

    return successors

def gerarSucessores(grelha, portas, posicao):
    # Define the possible movement directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # (dy, dx) for up, down, left, right

    possible_moves = []

    # Get the current position (row, col)
    row, col = posicao

    for dy, dx in directions:
        new_row, new_col = row + dy, col + dx

        # Check if the new position is within bounds
        if 0 <= new_row < len(grelha) and 0 <= new_col < len(grelha[0]):
            # Verificação de Parede
            if grelha[new_row][new_col] != 10:
                print(f"( {grelha[new_row][new_col]} )")
                possible_moves.append((new_row, new_col))

    return possible_moves


def bfs(estado, portas):
    #visited = set()
    queue = deque([estado])

    while queue:
        estadoAtual = queue.popleft()
        # if estado.grelha not in visited:
        #     visited.add(estado.grelha)

        if estadoAtual.geracao == 1:
            sucessores = []
            sucessores = gerarSucessoresIniciais(estado.grelha, portas)

            if sucessores:
                geracao = estadoAtual.geracao
                for (sx, sy) in sucessores:
                    geracao += 1
                    print(f"Geracao: {geracao}")
                    estadoGerado = EstadoGrelha(grelha, posicao=(sx, sy), geracao=geracao)
                    queue.append(estadoGerado)
                    # print(grelha)
                    estadoGerado.imprimeGrelha()
        else:
            sucessores = gerarSucessores(estadoAtual.grelha, portas, estadoAtual.posicao)
            if sucessores:
                geracao = estadoAtual.geracao
                for (sx, sy) in sucessores:
                    geracao += 1
                    print(f"Geracao: {geracao}")
                    estadoGerado = EstadoGrelha(grelha, posicao=(sx, sy), geracao=geracao)
                    queue.append(estadoGerado)
                    # print(grelha)
                    #estadoGerado.imprimeGrelha()

    return "Solucao nao encontrada"



# portas
portas = [(0, 2), (4, 2), (2, 0), (2, 4)]

# self, grelha, pai=None, movimento=None, geracao=1, nivel=0, expansao=0):

# Inicialização do objeto do estado
estadoInicial = EstadoGrelha(grelha)
#estadoInicial.imprimeGrelha()

# Executar a procura em Largura
print(bfs(estadoInicial, portas))