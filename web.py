from nodes import Node

FINGER_IDS = [4, 8, 12, 16, 20]

class SpiderWeb:
    def __init__(self):
        self.edges = []

    def update_between_hands(self, hand1, hand2):
        self.edges = []

        left_fingers = []
        right_fingers = []

        for fid in FINGER_IDS:
            lx, ly = hand1[fid]
            rx, ry = hand2[fid]

            left_fingers.append(Node(lx, ly))
            right_fingers.append(Node(rx, ry))

        # ALL left fingers → ALL right fingers
        for lf in left_fingers:
            for rf in right_fingers:
                self.edges.append((lf, rf))

    def get_edges(self):
        return self.edges
