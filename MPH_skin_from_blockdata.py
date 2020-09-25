import bpy
import base64
import json
import requests
import os

class MPH_OT_skin_from_blockdata(bpy.types.Operator):
    """Assigns a texture based on blockdata found on the clipboard. This will work with any player head. Look at the head in Minecraft and press F3+I, then use this option"""
    bl_idname = 'mph.skin_from_blockdata'
    bl_label = 'Skin From Blockdata'
    bl_description = 'Assigns a texture based on blockdata found on the clipboard. This will work with any player head. Look at the head in Minecraft and press F3+I, then use this option'
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        if not context.active_object:
            return False
        
        test1 = True if 'Inner Skin' in context.active_object.name else False
        test2 = True if 'Outer Skin' in context.active_object.name else False
        test3 = True if 'Value:"' in context.window_manager.clipboard else False

        return ((test1 or test2) and test3)
    
    def execute(self, context):

        # get iteration of the object selected
        iteration = context.active_object.name[10:]

        # get value string out of the big string
        block_info = context.window_manager.clipboard
        start_index = block_info.find('Value:"') + 7

        search_index = start_index
        value_string = ""


        while block_info[search_index] != '"':
            value_string += block_info[search_index]
            search_index += 1

        # decode the value string
        base64_bytes = value_string.encode('ascii')
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
        