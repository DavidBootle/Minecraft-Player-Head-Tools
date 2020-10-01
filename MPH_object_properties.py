import bpy

from . MPH_set_floor_alignment import MPH_OT_set_floor_alignment

class ObjectProperties(bpy.types.PropertyGroup):

    @classmethod
    def register(cls):

        bpy.types.Object.head_properties = bpy.props.PointerProperty(type = cls)

        cls.floor_alignment = bpy.props.EnumProperty(
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

    @classmethod
    def unregister(cls):
        bpy.types.Object.head_properties = None
        del bpy.types.Object.head_properties