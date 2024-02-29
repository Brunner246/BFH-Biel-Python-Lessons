from typing import List

import cadwork
import element_controller as ec
import geometry_controller as gc


def get_element_orientation_and_position(element_id: int):
    point1 = gc.get_p1(element_id)
    x_direction = gc.get_xl(element_id)
    y_direction = gc.get_yl(element_id)
    return point1, x_direction, y_direction


def transform_element(element_id: int, point1_new: cadwork.point_3d, x_direction_new: cadwork.point_3d,
                      y_direction_new: cadwork.point_3d):
    point1_old, x_direction_old, y_direction_old = get_element_orientation_and_position(element_id)
    ec.apply_transformation_coordinate([element_id],
                                       point1_old,
                                       x_direction_old,
                                       y_direction_old,
                                       point1_new,
                                       x_direction_new,
                                       y_direction_new)


if __name__ == '__main__':
    element_ids: List[int] = ec.get_user_element_ids()

    x_direction_new = cadwork.point_3d(1., 0., 0.)
    y_direction_new = cadwork.point_3d(0., 1., 0.)

    for element_id in element_ids:
        point1_new = gc.get_p1(element_id) # or set your preferred position
        transform_element(element_id, point1_new, x_direction_new, y_direction_new)
