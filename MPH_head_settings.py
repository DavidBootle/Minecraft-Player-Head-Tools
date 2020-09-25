import bpy

from . MPH_set_floor_alignment import MPH_OT_set_floor_alignment

class HeadSettings(bpy.types.PropertyGroup):
    floor_alignment: bpy.props.EnumProperty(
        items = [
            ('NONE', 'None', 'Not aligned', 0),
            ('CENTER', 'Center', 'In the center of the block', 1),
            ('NORTH', 'North', 'Placed on the -Y side of the block', 2),
            ('EAST', 'East', 'Placed on the +X side of the block', 3),
            ('SOUTH', 'South', 'Placed on the +Y side of the block', 4),
            ('WEST', 'West', 'Placed on the -X side of the block', 5)
        ],
        name = 'Floor Alignment',
        description = 'Where the block is aligned relative to the floor',
        default = 'NONE',
        update = MPH_OT_set_floor_alignment.execute
    )