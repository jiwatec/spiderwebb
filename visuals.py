import cv2

def draw_web(frame, web):
    for a, b in web.get_edges():
        cv2.line(
            frame,
            (a.x, a.y),
            (b.x, b.y),
            (220, 220, 255),
            1
        )
