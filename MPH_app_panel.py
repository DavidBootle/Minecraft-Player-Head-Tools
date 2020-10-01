import bpy

class MPH_PT_panel(bpy.types.Panel):
    bl_idname = "MPH_PT_panel"
    bl_label = "MC Player Head Tools"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "MC Head Tools"

    def headIsSelected(self, context):
        if not context.active_object:
            return False
        test1 = True if 'Inner Skin' in context.active_object.name else False
        test2 = True if 'Outer Skin' in context.active_object.name else False
        return (test1 or test2)

    def draw(self, context):
        layout = self.layout
        obj = context.object

        # Head creation tools
        col = layout.column()
        col.label(text="Create player head")
        col.operator("mph.add_head_model", text="New Player Head")

        col.label(text="Texture assignment")
        col.operator('mph.skin_from_blockdata', text="Skin From Blockdata")
        col.operator('mph.skin_from_username', text="Skin From Username")
        col.operator('mph.skin_from_file', text="Skin From File")

        col.label(text="Editing tools")
        col.operator('mph.prime_cursor', text="Prime Cursor")
        col.operator("mph.delete_faces", text="Delete Faces")

        col.label(text="Rotation")
        row = col.row(align=True)
        row.operator('mph.rotate_0', text="0°")
        row.operator('mph.rotate_90', text="90°")
        row.operator('mph.rotate_180', text="180°")
        row.operator('mph.rotate_270', text="270°")
        row = col.row(align=True)
        row.operator('mph.rotate_minus_45', text="<< 45°")
        row.operator('mph.rotate_minus_30', text="<< 30°")
        row.operator('mph.rotate_plus_30', text="30° >>")
        row.operator('mph.rotate_plus_45', text="45° >>")

        col.label(text="Alignment")
        if self.headIsSelected(context):
            box = col.box()
            box_col = box.column(align = True)
            box_col.label(text = 'Floor Alignment')
            box_col.prop(context.active_object.head_properties, 'floor_alignment', expand=True)
        row = col.row(align=True)
        row.operator('mph.set_to_wall', text="Set to Wall")
        row.operator('mph.set_to_floor', text="Set to Floor")