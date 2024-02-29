import cadwork
import geometry_controller as gc
import element_controller as ec

elements = ec.get_active_identifiable_element_ids()

for element in elements:
    facets = gc.get_element_facets(element)

    for facet_index in range(facets.count()):
        face = facets.at(facet_index)
        print(face)
        for face_index in range(face.count()):
            vertex = face.at(face_index)
            print(vertex)
