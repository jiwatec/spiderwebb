import os
os.environ["QT_QPA_PLATFORM"] = "xcb"
import cv2
import config
from camera import start_camera
from hand_tracking import HandTracker
from web import SpiderWeb
from visuals import draw_web

def main():
    cap = start_camera()
    tracker = HandTracker()
    web = SpiderWeb()

    print("Spider Web Ready. Press 'ESC' to exit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        frame, hands = tracker.find_hands(frame)

        if len(hands) == 2:
            web.update_between_hands(hands[0], hands[1])
            draw_web(frame, web)

        cv2.imshow("Spider Web 2.0", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
