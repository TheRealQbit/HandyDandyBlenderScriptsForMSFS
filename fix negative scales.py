import bpy

def fix_negative_scale(obj):
    """Check and fix negative scale of an object while preserving its transformation."""
    scale = obj.scale
    if scale.x < 0 or scale.y < 0 or scale.z < 0:
        # Store the object's world matrix
        obj_matrix = obj.matrix_world.copy()

        # Apply the inverse of the object's world matrix to reset its transformation
        obj.matrix_world.invert()

        # Fix negative scale by taking the absolute values of the scale components
        obj.scale = (abs(scale.x), abs(scale.y), abs(scale.z))

        # Apply the original world matrix back to the object
        obj.matrix_world = obj_matrix

        print(f"Fixed negative scale for object '{obj.name}'.")

# Select all objects in the scene
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')

# Loop through selected objects and check/fix negative scale
for obj in bpy.context.selected_objects:
    fix_negative_scale(obj)
