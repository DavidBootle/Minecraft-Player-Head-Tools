import bpy

class MPH_OT_set_floor_alignment(bpy.types.Operator):
    """Sets the floor alignment for the current head based on the alignment selection in the MC Heads panel"""
    bl_idname = 'mph.set_floor_alignment'
    bl_label = 'Set Floor Alignment'
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        if not context.active_object:
            return False
        test1 = True if 'Inner Skin' in context.active_object.name else False
        test2 = True if 'Outer Skin' in context.active_object.name else False
        return (test1 or test2)
    
    def execute(self, context):
        alignment = context.scene.mc_player_heads.floor_alignment

        # if the alignment is set to none, just keep position and update enum select. No use running all this code for no reason
        if alignment == 'NONE':
            inner_skin['floor_alignment'] = 'NONE'
            outer_skin['floor_alignment'] = 'NONE'
            return {'FINISHED'}

        # get head iteration
        iteration = context.active_object.name[10:]

        inner_skin_name = 'Inner Skin' + iteration
        outer_skin_name = 'Outer Skin' + iteration

        inner_skin = bpy.data.objects[inner_skin_name]
        outer_skin = bpy.data.objects[outer_skin_name]

        # get z position
        head_x = inner_skin.location.x
        head_y = outer_skin.location.y

        # get block offset
        head_offset_x = head_x % 1
        head_offset_y = head_y % 1

        # get block position
        head_block_x = head_x - head_offset_x
        head_block_y = head_y - head_offset_y

        if alignment == 'CENTER':
            # set x and y to center of the block (0.5)
            x_offset = 0.5
            y_offset = 0.5
            inner_skin.location.x = head_block_x + x_offset
            inner_skin.location.y = head_block_y + y_offset
            outer_skin.location.x = head_block_x + x_offset
            outer_skin.location.y = head_block_y + y_offset
            inner_skin['floor_alignment'] = 'CENTER'
            outer_skin['floor_alignment'] = 'CENTER'
        elif alignment == 'NORTH':
            # set y to 0.25 and x to 0.5
            x_offset = 0.5
            y_offset = 0.25
            inner_skin.location.x = head_block_x + x_offset
            inner_skin.location.y = head_block_y + y_offset
            outer_skin.location.x = head_block_x + x_offset
            outer_skin.location.y = head_block_y + y_offset
            inner_skin['floor_alignment'] = 'NORTH'
            outer_skin['floor_alignment'] = 'NORTH'
        elif alignment == 'EAST':
            # set y to 0.5 and x to 0.75
            x_offset = 0.75
            y_offset = 0.5
            inner_skin.location.x = head_block_x + x_offset
            inner_skin.location.y = head_block_y + y_offset
            outer_skin.location.x = head_block_x + x_offset
            outer_skin.location.y = head_block_y + y_offset
            inner_skin['floor_alignment'] = 'EAST'
            outer_skin['floor_alignment'] = 'EAST'
        elif alignment == 'SOUTH':
            # set y to 0.75 and x to 0.5
            x_offset = 0.5
            y_offset = 0.75
            inner_skin.location.x = head_block_x + x_offset
            inner_skin.location.y = head_block_y + y_offset
            outer_skin.location.x = head_block_x + x_offset
            outer_skin.location.y = head_block_y + y_offset
            inner_skin['floor_alignment'] = 'SOUTH'
            outer_skin['floor_alignment'] = 'SOUTH'
        elif alignment == 'WEST':
            # set y to 0.5 and x to 0.25
            x_offset = 0.25
            y_offset = 0.5
            inner_skin.location.x = head_block_x + x_offset
            inner_skin.location.y = head_block_y + y_offset
            outer_skin.location.x = head_block_x + x_offset
            outer_skin.location.y = head_block_y + y_offset
            inner_skin['floor_alignment'] = 'WEST'
            outer_skin['floor_alignment'] = 'WEST'
        else:
            return {'CANCELLED'}
        
        return {'FINISHED'}