import bpy

def fix_negative_scale(obj):
    """Check and fix negative scale of an object."""
    scale = obj.scale
    if scale.x < 0 or scale.y < 0 or scale.z < 0:
        obj.scale = (abs(scale.x), abs(scale.y), abs(scale.z))
        print(f"Fixed negative scale for object '{obj.name}'.")

# Select all objects in the scene
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')

# Loop through selected objects and check/fix negative scale
for obj in bpy.context.selected_objects:
    fix_negative_scale(obj)
