import cv2
import config

def interpolate_color(dist, max_dist):
    ratio = min(dist / max_dist, 1.0)
    b = int(config.COLOR_WEB_CLOSE[0] * (1 - ratio) + config.COLOR_WEB_FAR[0] * ratio)
    g = int(config.COLOR_WEB_CLOSE[1] * (1 - ratio) + config.COLOR_WEB_FAR[1] * ratio)
    r = int(config.COLOR_WEB_CLOSE[2] * (1 - ratio) + config.COLOR_WEB_FAR[2] * ratio)
    return (b, g, r)

def draw_web(frame, web):
    connections = web.get_connections()

    for node_a, node_b, dist in connections:
        color = interpolate_color(dist, config.MAX_CONNECTION_DISTANCE)
        thickness = 2 if dist < 150 else 1

        cv2.line(
            frame,
            node_a.tuple(), 
            node_b.tuple(), 
            color, 
            thickness, 
            lineType=cv2.LINE_AA
        )

    if connections:
        active_nodes = set()
        for a, b, _ in connections:
            active_nodes.add(a)
            active_nodes.add(b)
        for node in active_nodes:
            cv2.circle(frame, node.tuple(), 6, config.COLOR_NODE_GLOW, -1, cv2.LINE_AA)
            cv2.circle(frame, node.tuple(), 3, config.COLOR_NODE_CORE, -1, cv2.LINE_AA)
