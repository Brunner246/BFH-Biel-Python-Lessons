import dataclasses
from typing import List

import cadwork
import element_controller as ec
import attribute_controller as ac


@dataclasses.dataclass
class WallCover:
    name: str = ""
    width: float = 0.0
    thickness: float = 0.0
    length: float = 0.0
    color: int = 1
    position: cadwork.point_3d = cadwork.point_3d
    x_direction: cadwork.point_3d = cadwork.point_3d
    z_direction: cadwork.point_3d = cadwork.point_3d


def create_wall_cover(wall_data: WallCover) -> int:
    wall_cover: int = ec.create_rectangular_panel_vectors(wall_data.width,
                                                          wall_data.thickness,
                                                          wall_data.length,
                                                          wall_data.position,
                                                          wall_data.x_direction,
                                                          wall_data.z_direction)
    set_elements_name([wall_cover], wall_data.name)
    return wall_cover


def set_elements_name(elements: List[int], name: str):
    ac.set_name(elements, name)


if __name__ == '__main__':
    wall_cover_data: WallCover = WallCover()
    wall_cover_data.name = "WallCover1"
    wall_cover_data.width = 2700
    wall_cover_data.thickness = 260
    wall_cover_data.length = 8500
    wall_cover_data.position = cadwork.point_3d(0.0, 0.0, wall_cover_data.width * .5)
    wall_cover_data.x_direction = cadwork.point_3d(1.0, 0.0, 0.0)
    wall_cover_data.z_direction = cadwork.point_3d(0.0, 1.0, 0.0)

    create_wall_cover(wall_cover_data)
