import cv2
import mediapipe as mp

class HandTracker:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=2,
            min_detection_confidence=0.6,
            min_tracking_confidence=0.6
        )
        self.mp_draw = mp.solutions.drawing_utils

    def find_hands(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb)

        all_hands = []

        if results.multi_hand_landmarks:
            h, w, _ = frame.shape

            for hand in results.multi_hand_landmarks:
                points = []

                for lm in hand.landmark:
                    points.append((
                        int(lm.x * w),
                        int(lm.y * h)
                    ))

                all_hands.append(points)

                self.mp_draw.draw_landmarks(
                    frame,
                    hand,
                    self.mp_hands.HAND_CONNECTIONS
                )

        return frame, all_hands
