from collections import deque

geracao = 1
expansao = 0

class State:
    def __init__(self, numbers, bucket1, bucket2):
        self.numbers = tuple(numbers)  # The list of numbers in the state
        self.bucket = (bucket1, bucket2)  # Two buckets as a tuple

    def __repr__(self):
        return f"{self.numbers}, {self.bucket}"

    def generate_successors(self):
        global geracao
        # Generate all the next states by moving one number to either bucket
        next_states = []

        # for i, num in enumerate(self.numbers):
            # Only consider non-zero numbers to move
            #if num > 0:
        # Create a copy of the list of numbers
        new_numbers = list(self.numbers)
        number = new_numbers.pop(0)  # Decrease the number from the list

        # Move the number to bucket 1
        if self.bucket[0] + number <= limite:
            new_state_bucket1 = State(new_numbers, self.bucket[0] + number, self.bucket[1])
            next_states.append(new_state_bucket1)
            # next_states.insert(0,new_state_bucket1)
            geracao += 1
            print(f"G-{geracao} {new_state_bucket1.numbers} {new_state_bucket1.bucket}")

        # Move the number to bucket 2
        if self.bucket[1] + number <= limite:
            new_state_bucket2 = State(new_numbers, self.bucket[0], self.bucket[1] + number)
            next_states.append(new_state_bucket2)
            #next_states.insert(0, new_state_bucket2)
            geracao += 1
            print(f"G-{geracao} {new_state_bucket2.numbers} {new_state_bucket2.bucket}")

        return next_states

    def dfs(self, visited=None):
        global expansao
        depth = len(self.numbers)
        if visited is None:
            visited = set()  # Initialize the set of visited states
        else:
            if self.bucket[0] == self.bucket[1]:
                return self  # Return the solution state

        # If the current state is already visited, return an empty list (no need to explore it again)
        if self in visited:
            return []

        # Mark this state as visited
        visited.add(self)

        # Goal condition: check if the left bucket sum equals the right bucket sum
        #if self.buckets[0] == self.buckets[1]:
        #    return [self]  # If the goal is reached, return this state
        if depth > 0:
            # Generate the next states
            next_states = self.generate_successors()
            result = []  # We'll collect results here
            if next_states:
                for state in next_states:
                    expansao += 1
                    print(f"E-{expansao} {state.numbers} {state.bucket}")
                    result = state.dfs(visited)  # Recursively explore next states

                    # If we find a goal state, we stop exploring further
                    if result:
                        return result
            else:
                return None
        else:
            return None
        return None

    def bfs(self, visited=None):
        global expansao
        global geracao
        queue = deque([self])
        visited = set()

        while queue:
            state = queue.popleft()
            expansao += 1
            print(f"E-{expansao} {state.numbers} {state.bucket}")

            if state not in visited:
                visited.add(state)
                next_states = state.generate_successors()
                if next_states:
                    for state in next_states:
                        if state not in visited:
                            #geracao += 1
                            queue.append(state)
                            #print(f"G-{geracao} {state.numbers} {state.bucket}")
                            if (state.bucket[0] == limite) and (state.bucket[1] == limite):
                                return state
        print("Goal not found")
        return False

# Example usage
initial_state = State([5, 4, 3, 2, 2], 0, 0)
limite = sum(initial_state.numbers) / 2
print(initial_state)

# Perform DFS starting from the initial state
visited_states = initial_state.dfs()
#visited_states = initial_state.bfs()
if visited_states:
    print("Goal State Found:") # The goal state is the last one found
    print(visited_states)
else:
    print("No goal state found.")
