import math
from nodes import Node
import config

class SpiderWeb:
    def __init__(self):
        self.connections = []

    def update_between_hands(self, hand1, hand2):
        self.connections = []

        left_nodes = [Node(*hand1[i]) for i in config.FINGER_IDS]
        right_nodes = [Node(*hand2[i]) for i in config.FINGER_IDS]

        for l_node in left_nodes:
            for r_node in right_nodes:
                dist = math.hypot(l_node.x - r_node.x, l_node.y - r_node.y)

                if dist < config.MAX_CONNECTION_DISTANCE:
                    self.connections.append((l_node, r_node, dist))

    def get_connections(self):
        return self.connections
