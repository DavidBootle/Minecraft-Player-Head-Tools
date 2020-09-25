import bpy

class MPH_OT_skin_from_file(bpy.types.Operator):
    """Upload a Minecraft skin file"""
    bl_idname="mph.skin_from_file"
    bl_label="Skin From File"
    bl_options={'REGISTER', 'UNDO'}

    filepath: bpy.props.StringProperty(subtype='FILE_PATH')

    @classmethod
    def poll(cls, context):
        if not context.active_object:
            return False
        test1 = True if 'Inner Skin' in context.active_object.name else False
        test2 = True if 'Outer Skin' in context.active_object.name else False
        return (test1 or test2)

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}
    
    def draw(self, context):
        row = self.layout.row()
        row.prop(self, "skinFile")

    def execute(self, context):
        # get head iteration
        iteration = context.active_object.name[10:]

        # set material texture

        mat = context.active_object.data.materials[0]
        node_image = mat.node_tree.nodes['Minecraft Skin']

        # ready file
        full_path = self.filepath
        path_index = full_path.rfind('/')
        if path_index == -1:
            path_index = full_path.rfind('\\')
        if path_index == -1:
            self.report({'ERROR'}, "Invalid file path")
            return {'CANCELLED'}
        path_index += 1
        directory = full_path[:path_index ]
        filename = full_path[path_index:]

        bpy.ops.image.open(filepath=full_path, directory=directory, files=[{"name": filename}], relative_path=True, show_multiview=False)
        node_image.image = bpy.data.images[filename]
        bpy.data.images[filename].pack()

        return {'FINISHED'}