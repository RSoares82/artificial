class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.depth = 0 if parent is None else parent.depth + 1

    def __repr__(self):
        return f"Node({self.state})"


def iterative_deepening_search(problem):
    depth = 0
    while True:
        result = depth_limited_search(problem, depth)
        if result != "cutoff":
            return result
        depth += 1


def depth_limited_search(problem, limit):
    frontier = [Node(problem.initial)]
    result = "failure"

    while frontier:
        node = frontier.pop()

        if problem.is_goal(node.state):
            return node

        if node.depth > limit:
            result = "cutoff"
        else:
            if not is_cycle(node):
                for child_state in problem.expand(node.state):
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


# Example Problem Class
def simple_graph_problem():
    class Problem:
        def __init__(self):
            self.initial = "A"
            self.goal = "G"
            self.graph = {
                "A": ["B", "C"],
                "B": ["D", "E"],
                "C": ["F", "G"],
                "D": [], "E": ["G"], "F": [], "G": []
            }

        def is_goal(self, state):
            return state == self.goal

        def expand(self, state):
            return self.graph.get(state, [])

    return Problem()


# Running IDS on a simple graph
problem = simple_graph_problem()
solution = iterative_deepening_search(problem)

# Print the solution path if found
if solution:
    path = []
    while solution:
        path.append(solution.state)
        solution = solution.parent
    print("Solution Path:", " -> ".join(reversed(path)))