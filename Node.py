import cadwork
import element_controller as ec
import attribute_controller as ac
import visualization_controller as vc

if __name__ == '__main__':
    # point1 = cadwork.point_3d(100, 0, 1000)
    # node1 = ec.create_node(point1)
    # ac.set_name([node1], "Node1")
    # vc.set_color([node1], 10)
    element_id = ec.get_active_identifiable_element_ids()
    print(ac.get_name(*element_id))
    print(vc.get_color(*element_id))



