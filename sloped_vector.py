import math
import element_controller as ec
import cadwork


# ec.rotate_elements()

def create_sloped_vector(angle):
    radius = 1
    angle = math.radians(angle)

    x = radius * math.cos(angle)
    y = 0  # The vector is in the xz-plane
    z = radius * math.sin(angle)

    return x, y, z


if __name__ == '__main__':
    vector = create_sloped_vector(30)
    print(vector)
