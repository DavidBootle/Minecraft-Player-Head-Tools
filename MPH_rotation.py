import bpy
from math import radians, degrees

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

        if context.active_object.head_properties.cardinal_rotation == 'NONE':
            pass
        else:
            rotation = round(degrees(inner_skin.rotation_euler.z))
            
            # clamp values
            while rotation < 0:
                rotation += 360
            while rotation > 360:
                rotation -= 360
            
            # check if aligned cardinally
            if rotation == 0:
                inner_skin.head_properties.cardinal_rotation = 'EAST'
                outer_skin.head_properties.cardinal_rotation = 'EAST'
            elif rotation == 90:
                inner_skin.head_properties.cardinal_rotation = 'SOUTH'
                outer_skin.head_properties.cardinal_rotation = 'SOUTH'
            elif rotation == 180:
                inner_skin.head_properties.cardinal_rotation = 'WEST'
                outer_skin.head_properties.cardinal_rotation = 'WEST'
            elif rotation == 270:
                inner_skin.head_properties.cardinal_rotation = 'NORTH'
                outer_skin.head_properties.cardinal_rotation = 'NORTH'
            else:
                inner_skin.head_properties.cardinal_rotation = 'OTHER'
                outer_skin.head_properties.cardinal_rotation = 'OTHER'

        return {'FINISHED'}

class MPH_OT_set_rotation(bpy.types.Operator):
    """Sets the rotation of the head to the specified amount"""
    bl_idname = 'mph.set_rotation'
    bl_label = 'Set Rotation'
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

        inner_skin.rotation_euler.z = radians(self.rotation)

class MPH_OT_set_cardinal_rotation(bpy.types.Operator):
    """Sets the cardinal rotation of the head to the cardinal_rotation property"""
    bl_idname = 'mph.set_cardinal_rotation'
    bl_label = 'Set Cardinal Rotation'
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

        if 'Inner Skin' in context.active_object.name:
            obj_name = 'Inner Skin' + iteration
            update_obj = bpy.data.objects['Outer Skin' + iteration]
        if 'Outer Skin' in context.active_object.name:
            obj_name = 'Outer Skin' + iteration
            update_obj = bpy.data.objects['Inner Skin' + iteration]
        
        obj = bpy.data.objects[obj_name]

        rotation = obj.head_properties.cardinal_rotation
        if rotation != 'NONE':
            if rotation == 'EAST':
                rotation_amount = 0
            elif rotation == 'SOUTH':
                rotation_amount = 90
            elif rotation == 'WEST':
                rotation_amount = 180
            elif rotation == 'NORTH':
                rotation_amount = 270
            elif rotation == 'OTHER':
                rotation_amount = degrees(obj.rotation_euler.z)
            else:
                return {'CANCELLED'}
            
            obj.lock_rotation = (True, True, True)
            obj.rotation_euler.z = radians(rotation_amount)
        else:
            obj.lock_rotation = (False, False, False)
        
        if update_obj.head_properties.cardinal_rotation != rotation:
            bpy.context.view_layer.objects.active = update_obj
            update_obj.head_properties.cardinal_rotation = rotation
        else:
            bpy.context.view_layer.objects.active = update_obj
        return {'FINISHED'}