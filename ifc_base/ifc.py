import ifcopenshell
import ifcopenshell.geom
import ifcopenshell.util.shape
import multiprocessing

filename = (r'C:\Users\D097\Downloads\SteelFrame.Ifc')
ifc_file = ifcopenshell.open(filename)

settings = ifcopenshell.geom.settings()
iterator = ifcopenshell.geom.iterator(settings, ifc_file, multiprocessing.cpu_count())
if iterator.initialize():
    while True:
        shape = iterator.get()
        matrix = shape.transformation.matrix.data
        faces = shape.geometry.faces
        edges = shape.geometry.edges
        verts = shape.geometry.verts
        materials = shape.geometry.materials
        material_ids = shape.geometry.material_ids

        print(shape.guid)
        print(ifc_file.by_guid(shape.guid))
        matrix = shape.transformation.matrix.data

        # For convenience, you might want the matrix as a nested numpy array, so you can do matrix math.
        matrix = ifcopenshell.util.shape.get_shape_matrix(shape)

        # You can also extract the XYZ location of the matrix.
        location = matrix[:,3][0:3]

        # X Y Z of vertices in flattened list e.g. [v1x, v1y, v1z, v2x, v2y, v2z, ...]
        verts = shape.geometry.verts
        print(verts)

 
        # ... write code to process geometry here ...
        if not iterator.next():
            break