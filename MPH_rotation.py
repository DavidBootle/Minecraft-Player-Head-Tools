import bpy
from math import radians

class MPH_OT_adjust_rotation(bpy.types.Operator):
    """Adjusts the rotation of the head by the specified amount"""
    bl_idname = "mph.adjust_rotation"
    bl_label = "Adjust Rotation"
    bl_options = {'REGISTER', 'UNDO'}

    rotation: bpy.props.FloatProperty(default = 0.0)

    @classmethod
    def poll(cls, context):
        if not context.active_object:
            return False
        test1 = True if 'Inner Skin' in context.active_object.name else False
        test2 = True if 'Outer Skin' in context.active_object.name else False
        test3 = True if context.object.mode == 'OBJECT' else False
        return ((test1 or test2) and test3)

    def execute(self, context):
        # get head iteration
        iteration = context.active_object.name[10:]

        inner_skin = bpy.data.objects['Inner Skin' + str(iteration)]
        outer_skin = bpy.data.objects['Outer Skin' + str(iteration)]

        inner_skin.rotation_euler.z += radians(self.rotation)
        outer_skin.rotation_euler.z += radians(self.rotation)

        return {'FINISHED'}

class MPH_OT_rotate_0(bpy.types.Operator):
    """Rotates selected head to 0 degrees"""
    bl_idname = "mph.rotate_0"
    bl_label = "Rotate to 0"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        if not context.active_object:
            return False
        test1 = True if 'Inner Skin' in context.active_object.name else False
        test2 = True if 'Outer Skin' in context.active_object.name else False
        test3 = True if context.object.mode == 'OBJECT' else False
        return ((test1 or test2) and test3)
    
    def execute(self, context):
        # get head iteration
        iteration = context.active_object.name[10:]

        inner_skin = bpy.data.objects['Inner Skin' + str(iteration)]
        outer_skin = bpy.data.objects['Outer Skin' + str(iteration)]

        inner_skin.rotation_euler.z = radians(0)
        outer_skin.rotation_euler.z = radians(0)

        return {'FINISHED'}

class MPH_OT_rotate_90(bpy.types.Operator):
    """Rotates selected head to 90 degrees"""
    bl_idname = "mph.rotate_90"
    bl_label = "Rotate to 90"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        if not context.active_object:
            return False
        test1 = True if 'Inner Skin' in context.active_object.name else False
        test2 = True if 'Outer Skin' in context.active_object.name else False
        test3 = True if context.object.mode == 'OBJECT' else False
        return ((test1 or test2) and test3)
    
    def execute(self, context):
        # get head iteration
        iteration = context.active_object.name[10:]

        inner_skin = bpy.data.objects['Inner Skin' + str(iteration)]
        outer_skin = bpy.data.objects['Outer Skin' + str(iteration)]

        inner_skin.rotation_euler.z = radians(90)
        outer_skin.rotation_euler.z = radians(90)

        return {'FINISHED'}

class MPH_OT_rotate_180(bpy.types.Operator):
    """Rotates selected head to 180 degrees"""
    bl_idname = "mph.rotate_180"
    bl_label = "Rotate to 180"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        if not context.active_object:
            return False
        test1 = True if 'Inner Skin' in context.active_object.name else False
        test2 = True if 'Outer Skin' in context.active_object.name else False
        test3 = True if context.object.mode == 'OBJECT' else False
        return ((test1 or test2) and test3)
    
    def execute(self, context):
        # get head iteration
        iteration = context.active_object.name[10:]

        inner_skin = bpy.data.objects['Inner Skin' + str(iteration)]
        outer_skin = bpy.data.objects['Outer Skin' + str(iteration)]

        inner_skin.rotation_euler.z = radians(180)
        outer_skin.rotation_euler.z = radians(180)

        return {'FINISHED'}

class MPH_OT_rotate_270(bpy.types.Operator):
    """Rotates selected head to 270 degrees"""
    bl_idname = "mph.rotate_270"
    bl_label = "Rotate to 270"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        if not context.active_object:
            return False
        test1 = True if 'Inner Skin' in context.active_object.name else False
        test2 = True if 'Outer Skin' in context.active_object.name else False
        test3 = True if context.object.mode == 'OBJECT' else False
        return ((test1 or test2) and test3)
    
    def execute(self, context):
        # get head iteration
        iteration = context.active_object.name[10:]

        inner_skin = bpy.data.objects['Inner Skin' + str(iteration)]
        outer_skin = bpy.data.objects['Outer Skin' + str(iteration)]

        inner_skin.rotation_euler.z = radians(270)
        outer_skin.rotation_euler.z = radians(270)

        return {'FINISHED'}