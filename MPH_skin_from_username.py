import bpy
import requests
import json
import base64

class MPH_OT_skin_from_username(bpy.types.Operator):
    """Assigns the proper texture using a Minecraft username"""
    bl_idname="mph.skin_from_username"
    bl_label = "Skin From Username"
    bl_options = {'REGISTER', 'UNDO'}

    username: bpy.props.StringProperty(
        name = "Username",
        description = "The Minecraft username belonging to the head",
        maxlen = 16
    )

    @classmethod
    def poll(cls, context):
        if not context.active_object:
            return False

        test1 = True if 'Inner Skin' in context.active_object.name else False
        test2 = True if 'Outer Skin' in context.active_object.name else False

        return (test1 or test2)

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
    
    def draw(self, context):
        row = self.layout.row()
        row.prop(self, "username")
    
    def execute(self, context):
        # get head iteration
        iteration = context.active_object.name[10:]

        # get uuid from username
        r = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{self.username}', allow_redirects=True)
        if len(r.content) == 0:
            self.report({'ERROR'}, "Invalid username")
            return {'CANCELLED'}
        response = json.loads(r.content)
        uuid = response['id']

        # get value data from uuid
        r = requests.get(f'https://sessionserver.mojang.com/session/minecraft/profile/{uuid}', allow_redirects=True)
        response = json.loads(r.content)
        value = response["properties"][0]["value"]

        # get url from value data
        base64_bytes = value.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        message = message_bytes.decode('ascii')

        message = message.replace('\n', '')
        message = message.replace('\r', '')

        # get the file url by decoding the json
        skin_data = json.loads(message)
        skin_url = skin_data['textures']['SKIN']['url']

        # download the file to the blender temp folder
        filename = 'SkinTexture' + str(iteration) + '.png'
        r = requests.get(skin_url, allow_redirects=True)
        full_path = bpy.app.tempdir + filename
        open(full_path, 'wb').write(r.content)

        # set material texture
        mat = context.active_object.data.materials[0]
        node_image = mat.node_tree.nodes['Minecraft Skin']
        bpy.ops.image.open(filepath=full_path, directory=bpy.app.tempdir, files=[{"name": filename}], relative_path=True, show_multiview=False)
        node_image.image = bpy.data.images[filename]
        bpy.data.images[filename].pack()

        return {'FINISHED'}