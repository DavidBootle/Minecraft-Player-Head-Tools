import bpy

class PanelSettings(bpy.types.PropertyGroup):
    
   rotate_to_match_floor_alignment: bpy.props.BoolProperty(
      name='rotate_to_match_floor_alignment',
      description='Whether the head should rotate the correct direction when setting a directional floor alignment',
      default=False
   )