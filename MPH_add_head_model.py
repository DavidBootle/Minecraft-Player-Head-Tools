import bpy
import bmesh

class MPH_OT_add_head_model(bpy.types.Operator):
    """Creates a new player head object"""
    bl_idname = "mph.add_head_model"
    bl_label = "New Player Head"
    bl_description = "Creates a new player head object"
    bl_options = {'REGISTER', 'UNDO'}

    iteration = 0
    
    @classmethod
    def poll(cls, context):
        # it's ok if there is not selected object. Using this statement stops the next statement from raising an error
        if not context.object:
            return True
        return True if context.object.mode == 'OBJECT' else False

    def execute(self, context):
        scene = context.scene
        iteration = MPH_OT_add_head_model.iteration

        cursor_pos = context.scene.cursor.location

        # create collection
        col = bpy.data.collections.new("Player Head" + str(iteration))

        root_col = bpy.context.scene.collection
        root_col.children.link(col)

        # create inner skin cube
        mesh = bpy.data.meshes.new('Inner Skin' + str(iteration))
        inner_skin = bpy.data.objects.new('Inner Skin' + str(iteration), mesh)

        col.objects.link(inner_skin)
        bpy.ops.object.select_all(action='DESELECT')
        if not inner_skin.select_get():
            inner_skin.select_set(True)
        
        inner_skin.location = cursor_pos

        bm = bmesh.new()
        bmesh.ops.create_cube(bm, size=0.5, calc_uvs=False)
        bm.to_mesh(mesh)
        bm.free()

        # create inner skin uv
        bpy.context.view_layer.objects.active = inner_skin
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.select_all(action = 'SELECT')
        bpy.ops.uv.cube_project()
        bpy.ops.object.editmode_toggle()

        uv_layer = bpy.context.object.data.uv_layers.active.data
        self.createInnerUV(uv_layer)

        # create outer skin cube
        mesh = bpy.data.meshes.new('Outer Skin' + str(iteration))
        outer_skin = bpy.data.objects.new('Outer Skin' + str(iteration), mesh)

        col.objects.link(outer_skin)
        bpy.ops.object.select_all(action='DESELECT')
        if not outer_skin.select_get():
            outer_skin.select_set(True)

        outer_skin.location = cursor_pos
        
        bm = bmesh.new()
        bmesh.ops.create_cube(bm, size=0.5208, calc_uvs=False)
        bm.to_mesh(mesh)
        bm.free()

        # create outer skin uv
        bpy.context.view_layer.objects.active = outer_skin
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.select_all(action = 'SELECT')
        bpy.ops.uv.cube_project()
        bpy.ops.object.editmode_toggle()

        uv_layer = bpy.context.object.data.uv_layers.active.data
        self.createOuterUV(uv_layer)

        # select both objects
        bpy.ops.object.select_all(action='DESELECT')
        if not inner_skin.select_get():
            inner_skin.select_set(True)
        if not outer_skin.select_get():
            outer_skin.select_set(True)
        
        # setup materials
        mat = bpy.data.materials.new('Player Head' + str(iteration))
        mat.use_nodes = True
        mat.blend_method = 'CLIP'
        nodes = mat.node_tree.nodes

        node_image = nodes.new('ShaderNodeTexImage')
        node_image.interpolation = 'Closest'
        node_image.label = 'Minecraft Skin'
        node_image.name = 'Minecraft Skin'

        node_principled = nodes.get('Principled BSDF')
        node_principled.inputs[7].default_value = 1.0 # set roughness to 1

        links = mat.node_tree.links
        links.new(node_image.outputs[0], node_principled.inputs[0]) # link image color output to color input
        links.new(node_image.outputs[1], node_principled.inputs[18]) # link image alpha to alpha

        if inner_skin.data.materials:
            inner_skin.data.materials[0] = mat
        else:
            inner_skin.data.materials.append(mat)
        
        if outer_skin.data.materials:
            outer_skin.data.materials[0] = mat
        else:
            outer_skin.data.materials.append(mat)
        
        # set head rotation
        inner_skin.head_properties.cardinal_rotation = 'EAST'
        outer_skin.head_properties.cardinal_rotation = 'EAST'

        # finish
        self.report({'INFO'}, "Player head created")

        MPH_OT_add_head_model.iteration += 1
        return {'FINISHED'}
    
    def createInnerUV(self, uv_layer):
        # polgyon 0 : back of the head
        uv_layer[0].uv = (0.5, 0.75)
        uv_layer[1].uv = (0.5, 0.875)
        uv_layer[2].uv = (0.375, 0.875)
        uv_layer[3].uv = (0.375, 0.75)

        # polygon 1 : right side of face
        uv_layer[4].uv = (0.375, 0.75)
        uv_layer[5].uv = (0.375, 0.875)
        uv_layer[6].uv = (0.25, 0.875)
        uv_layer[7].uv = (0.25, 0.75)

        # polygon 2 : face
        uv_layer[8].uv = (0.25, 0.75)
        uv_layer[9].uv = (0.25, 0.875)
        uv_layer[10].uv = (0.125, 0.875)
        uv_layer[11].uv = (0.125, 0.75)

        # polygon 3: left side of face
        uv_layer[12].uv = (0.125, 0.75)
        uv_layer[13].uv = (0.125, 0.875)
        uv_layer[14].uv = (0.0, 0.875)
        uv_layer[15].uv = (0.0, 0.75)

        # polygon 4: top of head
        uv_layer[16].uv = (0.375, 1.0)
        uv_layer[17].uv = (0.375, 0.875)
        uv_layer[18].uv = (0.25, 0.875)
        uv_layer[19].uv = (0.25, 1.0)

        # polygon 5: bottom of head
        uv_layer[20].uv = (0.25, 0.875)
        uv_layer[21].uv = (0.25, 1.0)
        uv_layer[22].uv = (0.125, 1.0)
        uv_layer[23].uv = (0.125, 0.875)
    
    def createOuterUV(self, uv_layer):
        # polgyon 0 : back of the head
        uv_layer[0].uv = (1.0, 0.75)
        uv_layer[1].uv = (1.0, 0.875)
        uv_layer[2].uv = (0.875, 0.875)
        uv_layer[3].uv = (0.875, 0.75)

        # polygon 1 : right side of face
        uv_layer[4].uv = (0.875, 0.75)
        uv_layer[5].uv = (0.875, 0.875)
        uv_layer[6].uv = (0.75, 0.875)
        uv_layer[7].uv = (0.75, 0.75)

        # polygon 2 : face
        uv_layer[8].uv = (0.75, 0.75)
        uv_layer[9].uv = (0.75, 0.875)
        uv_layer[10].uv = (0.625, 0.875)
        uv_layer[11].uv = (0.625, 0.75)

        # polygon 3: left side of face
        uv_layer[12].uv = (0.625, 0.75)
        uv_layer[13].uv = (0.625, 0.875)
        uv_layer[14].uv = (0.5, 0.875)
        uv_layer[15].uv = (0.5, 0.75)

        # polygon 4: top of head
        uv_layer[16].uv = (0.875, 1.0)
        uv_layer[17].uv = (0.875, 0.875)
        uv_layer[18].uv = (0.75, 0.875)
        uv_layer[19].uv = (0.75, 1.0)

        # polygon 5: bottom of head
        uv_layer[20].uv = (0.75, 0.875)
        uv_layer[21].uv = (0.75, 1.0)
        uv_layer[22].uv = (0.625, 1.0)
        uv_layer[23].uv = (0.625, 0.875)