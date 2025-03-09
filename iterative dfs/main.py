initial_state = [
        [1, 2, 3],
        [4, 6, 0],
        [7, 5, 8]
    ]

objective_state = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

global_depth = 1
geracao = 0
expansao = 0

def convert_to_tuple(state_2d):
    return tuple(num for row in state_2d for num in row)

class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.depth = global_depth if parent is None else parent.depth - 1
    def __repr__(self):
        return f"Node({self.state})"


def iterative_deepening_search(problem):
    global global_depth
    while True:
        result = depth_limited_search(problem)
        if result != "cutoff":
            return result
        global_depth += 1


def depth_limited_search(problem, limit=0):
    global expansao
    global geracao
    frontier = [Node(problem.initial)]
    result = "failure"
    while frontier:
        node = frontier.pop()
        if problem.is_goal(node.state):
            return node
        if node.depth <= limit:
            expansao += 1
            print(f"Expanção: {expansao}: {node.state} limite")
            result = "cutoff"
        else:
            if not is_cycle(node):
                expansao += 1
                geracao += 1
                print(f"Geracao: {geracao} Expanção: {expansao} estado: {node.state}")
                for child_state in problem.generate_successors(node.state):
                    frontier.append(Node(child_state, node))
    return result


def is_cycle(node):
    current = node
    seen_states = set()
    while current:
        if current.state in seen_states:
            return True
        seen_states.add(current.state)
        current = current.parent
    return False


# Example Problem Class, creates the instance class for the problem
def simple_graph_problem(initial, goal, depth):
    class Problem:
        def __init__(self):
            self.initial = initial
            self.goal = goal
            self.depth = 0
            self.generation = 0
            self.expansion = 0

        def is_goal(self, state):
            return state == self.goal

        def generate_successors(self, state):
            """Generate all possible moves from the current state."""
            global geracao
            neighbors = []
            zero_index = state.index(0)
            moves = {
                "up": -3, "left": -1, "down": 3, "right": 1
            }

            for move, delta in moves.items():
                new_index = zero_index + delta
                if 0 <= new_index < 9 and not (
                        move == "left" and zero_index % 3 == 0 or
                        move == "right" and zero_index % 3 == 2
                ):
                    new_state = list(state)
                    new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
                    neighbors.append(tuple(new_state))
                    geracao += 1
                    print(f"Geracao: {geracao} estado: {tuple(new_state)}")

            #self.expansion += 1  # Increase expansion order count
            #print(neighbors)
            return neighbors

    return Problem()


# # Running IDS on a simple graph
initial = convert_to_tuple(initial_state)
goal = convert_to_tuple(objective_state)

problem = simple_graph_problem(initial, goal, depth=global_depth)
print(problem.initial)
print(problem.goal)

# sucessores = problem.generate_successors(problem.initial)
solution = iterative_deepening_search(problem)

# Print the solution path if found
if solution:
    path = []
    while solution:
        path.append(solution.state)
        solution = solution.parent
    print("Solution Path:", " -> ".join(map(str, reversed(path))))