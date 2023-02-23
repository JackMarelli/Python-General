import pygame, math

def load_image(image_path):
    return pygame.image.load(image_path).convert_alpha()

def point_inside_polygon(point, polygon):
    x, y = point
    n = len(polygon)
    inside = False

    p1x, p1y = polygon[0]
    for i in range(n + 1):
        p2x, p2y = polygon[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x < max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside


def point_inside_circle(point, circle):
    x, y = point
    center_x, center_y = circle[0], circle[1]
    distance = math.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)
    return distance <= circle[2]