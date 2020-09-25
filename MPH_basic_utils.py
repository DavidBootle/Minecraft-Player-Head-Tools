import bpy

class MPH_OT_delete_faces(bpy.types.Operator):
    """Deletes selected faces"""
    bl_idname = "mph.delete_faces"
    bl_label = "Delete Faces"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        if not context.object:
            return False
        return True if context.object.mode == 'EDIT' else False
    
    def execute(self, context):
        bpy.ops.mesh.delete(type='FACE')
        return {'FINISHED'}

class MPH_OT_prime_cursor(bpy.types.Operator):
    """Center the cursor on the selected objects"""
    bl_idname = "mph.prime_cursor"
    bl_label = "Prime Cursor"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        if not context.object:
            return False
        return True if context.object.mode == 'EDIT' else False
    
    def execute(self, context):
        bpy.ops.view3d.snap_cursor_to_selected()
        return {'FINISHED'}