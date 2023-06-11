import bpy

# Deselect all objects
bpy.ops.object.select_all(action='DESELECT')

# Create a list to store the empty objects
empty_objects = []

# Iterate through all objects in the scene
for obj in bpy.context.scene.objects:
    if obj.type == 'MESH':
        # Check if the object has 0 faces, 0 vertices, or 0 edges
        if len(obj.data.polygons) == 0 or len(obj.data.vertices) == 0 or len(obj.data.edges) == 0:
            # Select the object
            obj.select_set(True)

            # Unparent the child objects
            for child in obj.children:
                # Get the child object's world matrix
                child_matrix = child.matrix_world.copy()

                # Unparent the child object
                child.parent = None

                # Apply the child object's world matrix to preserve its transformation
                child.matrix_world = child_matrix

            # Add the empty object to the list
            empty_objects.append(obj)

# Delete the empty objects
bpy.ops.object.delete()

# Remove the deleted objects from the list
empty_objects.clear()