# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "MC Player Head Tools",
    "author" : "David Bootle",
    "description" : "An addon meant to work with Mineways and MCPrep that adds tools for creating and managing custom player heads in blender",
    "blender" : (2, 80, 0),
    "version" : (1,0,1),
    "location" : "VIEW_3D",
    "warning" : "",
    "category" : "Generic"
}

import bpy

# import operators
from . MPH_add_head_model import MPH_OT_add_head_model
from . MPH_skin_from_blockdata import MPH_OT_skin_from_blockdata
from . MPH_skin_from_username import MPH_OT_skin_from_username
from . MPH_skin_from_file import MPH_OT_skin_from_file
from . MPH_basic_utils import MPH_OT_delete_faces, MPH_OT_prime_cursor
from . MPH_rotation import MPH_OT_rotate_0, MPH_OT_rotate_90, MPH_OT_rotate_180, MPH_OT_rotate_270, MPH_OT_rotate_plus_30, MPH_OT_rotate_minus_30, MPH_OT_rotate_plus_45, MPH_OT_rotate_minus_45
from . MPH_wall_alignment import MPH_OT_set_to_wall, MPH_OT_set_to_floor
from . MPH_set_floor_alignment import MPH_OT_set_floor_alignment
from . MPH_head_settings import HeadSettings

# import panels
from . MPH_app_panel import MPH_PT_panel

classes = (
    MPH_OT_add_head_model,
    MPH_OT_skin_from_blockdata,
    MPH_PT_panel,
    MPH_OT_skin_from_username,
    MPH_OT_skin_from_file,
    MPH_OT_delete_faces,
    MPH_OT_prime_cursor,
    MPH_OT_rotate_0,
    MPH_OT_rotate_90,
    MPH_OT_rotate_180,
    MPH_OT_rotate_270,
    MPH_OT_rotate_plus_30,
    MPH_OT_rotate_plus_45,
    MPH_OT_rotate_minus_30,
    MPH_OT_rotate_minus_45,
    MPH_OT_set_to_wall,
    MPH_OT_set_floor_alignment,
    MPH_OT_set_to_floor,
    HeadSettings
)

def register():
    for class_obj in classes:
        bpy.utils.register_class(class_obj)
    bpy.types.Scene.mc_player_heads = bpy.props.PointerProperty(type=HeadSettings)

def unregister():
    for class_obj in classes:
        bpy.utils.unregister_class(class_obj)
    del bpy.types.Scene.mc_player_heads