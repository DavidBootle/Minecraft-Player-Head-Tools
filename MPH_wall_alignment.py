import bpy

class MPH_OT_set_to_wall(bpy.types.Operator):
    """Sets the head to the correct placement on the wall"""
    bl_idname = "mph.set_to_wall"
    bl_label = "Set to Wall"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        if not context.active_object:
            return False
        test1 = True if 'Inner Skin' in context.active_object.name else False
        test2 = True if 'Outer Skin' in context.active_object.name else False
        return (test1 or test2)

    def execute(self, context):
        # get head iteration
        iteration = context.active_object.name[10:]
        inner_skin_name = 'Inner Skin' + iteration
        outer_skin_name = 'Outer Skin' + iteration

        # get z position
        inner_skin_z = bpy.data.objects[inner_skin_name].location.z
        outer_skin_z = bpy.data.objects[outer_skin_name].location.z

        # get block offset
        inner_skin_offset = inner_skin_z % 1
        outer_skin_offset = outer_skin_z % 1

        # get block position
        inner_skin_block = inner_skin_z - inner_skin_offset
        outer_skin_block = outer_skin_z - outer_skin_offset

        # set z decimal to 0.5
        bpy.data.objects[inner_skin_name].location.z = inner_skin_block + 0.5
        bpy.data.objects[outer_skin_name].location.z = outer_skin_block + 0.5

        return {'FINISHED'}

class MPH_OT_set_to_floor(bpy.types.Operator):
    """Sets the head to the correct placement on the floor."""
    bl_idname = "mph.set_to_floor"
    bl_label = "Set to Floor"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        if not context.active_object:
            return False
        test1 = True if 'Inner Skin' in context.active_object.name else False
        test2 = True if 'Outer Skin' in context.active_object.name else False
        return (test1 or test2)

    def execute(self, context):
        # get head iteration
        iteration = context.active_object.name[10:]
        inner_skin_name = 'Inner Skin' + iteration
        outer_skin_name = 'Outer Skin' + iteration

        # get z position
        inner_skin_z = bpy.data.objects[inner_skin_name].location.z
        outer_skin_z = bpy.data.objects[outer_skin_name].location.z

        # get block offset
        inner_skin_offset = inner_skin_z % 1
        outer_skin_offset = outer_skin_z % 1

        # get block position
        inner_skin_block = inner_skin_z - inner_skin_offset
        outer_skin_block = outer_skin_z - outer_skin_offset

        # set z decimal to 0.5
        bpy.data.objects[inner_skin_name].location.z = inner_skin_block + 0.25
        bpy.data.objects[outer_skin_name].location.z = outer_skin_block + 0.25

        return {'FINISHED'}