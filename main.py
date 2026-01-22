import cv2
from hand_tracking import HandTracker
from web import SpiderWeb
from visuals import draw_web

cap = cv2.VideoCapture(0)

tracker = HandTracker()
web = SpiderWeb()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame, hands = tracker.find_hands(frame)

    # Only create web when TWO hands are visible
    if len(hands) == 2:
        web.update_between_hands(hands[0], hands[1])
        draw_web(frame, web)

    cv2.imshow("Spider Web", frame)

    # ESC to quit
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
