class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.knight = None
        self.connected_nodes = []

    def add_connection(self, node):
        self.connected_nodes.append(node)

class Knight:
    def __init__(self, name, node):
        self.name = name
        self.node = node
        self.path = []
        node.knight = self
        self.solved = False  # Add a solved attribute

    def steps_remaining(self):
        return len(self.path)  # Add a steps_remaining method

class ChessBoard:
    def __init__(self):
        self.nodes = [[Node(i, j) for j in range(3)] for i in range(4)]
        self.knights = [Knight('b1', self.nodes[0][0]), Knight('b3', self.nodes[0][2]), Knight('b2', self.nodes[0][1]),
                        Knight('w1', self.nodes[3][0]), Knight('w3', self.nodes[3][2]), Knight('w2', self.nodes[3][1])]
        self._connect_nodes()
        self.targeted_nodes = set()

    def _connect_nodes(self):
        for i in range(4):
            for j in range(3):
                node = self.nodes[i][j]
                potential_moves = [
                    (i+1, j+2), (i+1, j-2), (i-1, j+2), (i-1, j-2),
                    (i+2, j+1), (i+2, j-1), (i-2, j+1), (i-2, j-1)
                ]
                for move in potential_moves:
                    if 0 <= move[0] < 4 and 0 <= move[1] < 3:
                        node.add_connection(self.nodes[move[0]][move[1]])

    def _place_knights(self):
        for i, knight_name in enumerate(['b1', 'b2', 'b3']):
            knight = Knight(knight_name, self.nodes[0][i])
            self.knights.append(knight)
        for i, knight_name in enumerate(['w1', 'w2', 'w3']):
            knight = Knight(knight_name, self.nodes[3][i])
            self.knights.append(knight)
    
    def find_shortest_path(self, knight):
        target_row = 3 if 'b' in knight.name else 0
        distances = {node: float('inf') for row in self.nodes for node in row}
        previous = {node: None for row in self.nodes for node in row}
        distances[knight.node] = 0

        nodes_to_visit = [knight.node]
        while nodes_to_visit:
            current_node = nodes_to_visit.pop(0)
            for neighbor in current_node.connected_nodes:
                if neighbor in self.targeted_nodes:
                    continue
                if distances[current_node] + 1 < distances[neighbor]:
                    distances[neighbor] = distances[current_node] + 1
                    previous[neighbor] = current_node
                    nodes_to_visit.append(neighbor)

        target_node = min((node for node in self.nodes[target_row] if node not in self.targeted_nodes), key=distances.get)
        self.targeted_nodes.add(target_node)

        # Build the path from the start node to the target node
        path = []
        current_node = target_node
        while current_node is not None:
            path.append(current_node)
            current_node = previous[current_node]
        path.reverse()

        knight.path = path  # Assign the path to knight.path

        return distances[target_node], target_node, path

    def find_all_paths(self):
        for knight in self.knights:
            path_length, target_node, path = self.find_shortest_path(knight)
            #print(f"The shortest path for {knight.name} is {path_length} moves, ending at cell ({target_node.x}, {target_node.y}), with path {[(node.x, node.y) for node in path]}.")

    def visualize(self):
        for i in range(4):
            for j in range(3):
                knight = self.nodes[i][j].knight
                print("{:3}".format(knight.name if knight else 'X'), end=' ')
            print()
    
    def solve(self):
        # Initialize the getBackKnight and currentKnight
        getBackKnight = []
        currentKnight = self.knights[0]  # Assuming b1 is the first knight in the list

        # Initialize a counter for the total steps taken
        total_steps = 0

        # Continue until all knights have reached their target row
        while not self.problem_solved():
            # Check if the currentKnight can go to its next step in its path
            if currentKnight and len(currentKnight.path) > 1:
                next_node = currentKnight.path[1]
            else:
                if getBackKnight:
                    currentKnight = getBackKnight.pop(0)
                    continue
            if next_node is not None and next_node.knight is None:
                # Move the knight to the next node
                currentKnight.node.knight = None
                next_node.knight = currentKnight
                currentKnight.node = next_node

                # Update the path of the knight
                currentKnight.path = currentKnight.path[1:]

                # Increment the total steps counter
                total_steps += 1
                self.visualize()
                print(f"Total steps taken: {total_steps}")

                # Check if the knight has reached its target row
                if len(currentKnight.path) == 1:
                    currentKnight.solved = True

                # Update getBackKnight and currentKnight
                if getBackKnight:
                    currentKnight = getBackKnight.pop(0)
                else:
                    currentKnight = self.get_next_knight(currentKnight, getBackKnight)

            else:
                # Update getBackKnight
                getBackKnight.append(currentKnight)
                temp = self.get_next_knight(currentKnight, getBackKnight)
                if temp == None:
                    currentKnight, getBackKnight, total_steps = self.stuckSolver(currentKnight, getBackKnight, total_steps)
                else:
                    currentKnight = temp

    def stuckSolver(self, currentKnight, getBackKnight, total_steps):
        stuckKnight = getBackKnight.pop(0)
        stuckKnightNode = stuckKnight.node

        # Move the stuck knight to any available node except for the node in its path
        available_nodes = [node for node in stuckKnight.node.connected_nodes if node.knight is None and node != stuckKnight.path[1]]
        if available_nodes:
            random_node = available_nodes[0]
            stuckKnight.node.knight = None
            random_node.knight = stuckKnight
            stuckKnight.node = random_node
            total_steps += 1
            self.visualize()
            print(f"Total steps taken: {total_steps}")

        # Move the current knight to its node
        for i in range(2):
            if currentKnight and len(currentKnight.path) > 1:
                next_node = currentKnight.path[1]
                if next_node.knight is None:
                    currentKnight.node.knight = None
                    next_node.knight = currentKnight
                    currentKnight.node = next_node
                    currentKnight.path = currentKnight.path[1:]
                    total_steps += 1
                    self.visualize()
                    print(f"Total steps taken: {total_steps}")

        # Return the stuck knight to its stuckKnightNode
        stuckKnight.node.knight = None
        stuckKnightNode.knight = stuckKnight
        stuckKnight.node = stuckKnightNode
        total_steps += 1
        self.visualize()
        print(f"Total steps taken: {total_steps}")
        return currentKnight, getBackKnight, total_steps

    def problem_solved(self):
        # Check if all knights have reached their target row
        for knight in self.knights:
            target_row = 3 if 'b' in knight.name else 0
            if knight.node.x != target_row:
                return False
        return True

    def get_next_knight(self, current_knight, getBackKnight):
        # Initialize the next knight and the maximum steps
        next_knight = None
        max_steps = float('-inf')

        # Check all the knights
        for knight in self.knights:
            # If the knight is not solved and has more steps remaining than the current maximum
            if not knight.solved and knight.steps_remaining() > max_steps and knight not in getBackKnight:
                # Update the next knight and the maximum steps
                next_knight = knight
                max_steps = knight.steps_remaining()

        # Return the next knight
        return next_knight


chess_board = ChessBoard()
chess_board.visualize()
chess_board.find_all_paths()
print()
chess_board.solve()