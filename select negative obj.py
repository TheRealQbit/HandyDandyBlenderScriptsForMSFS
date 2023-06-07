import bpy

def select_negative_scale(obj):
    """Check and fix negative scale of an object."""
    scale = obj.scale
    if scale.x > 0 and scale.y > 0 and scale.z > 0:
        obj.select_set(False)
        
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')

# Loop through selected objects and check/fix negative scale
for obj in bpy.context.selected_objects:
    select_negative_scale(obj)
