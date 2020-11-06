class Node():
    def __init__(self, state, parent, action):
        # Actor name
        self.state = state
        # Actor name that called the current actor
        self.parent = parent
        # Movie title
        self.action = action

    def get_state(self):
        return self.state

    def get_parent(self):
        return self.parent

    def get_action(self):
        return self.action


class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier(StackFrontier):

    def __init__(self):
        self.frontier = []
        self.copy = []

    def queue(self, node):
        self.frontier.append(node)
        self.copy.append(node)

    def dequeue(self):
        return self.frontier.pop(0)

    def contains_state(self, state):

        # Loop in all nodes in copy list
        for node in self.copy:
            # Check if exists one node with actor name passed by param
            if node.get_state() == state:
                return node

        return None

    def recovery_path(self, target_node):

        path = []

        # Get the node of target actor
        node = self.contains_state(target_node.get_state())

        # While the current node yet not reach the source actor
        while node.get_parent() is not None:
            # Append on path (the current actor name and movie title)
            path.append([node.get_action(), node.get_state()])
            # Get the parent actor node of current actor
            node = self.contains_state(node.get_parent())

        path.reverse()

        return path
