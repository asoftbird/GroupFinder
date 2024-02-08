# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8 compliant>

bl_info = {
    "name": "GroupFinder",
    "description": "Find node groups by name",
    "author": "asoftbird (https://titmou.se/)",
    "version": (1, 0, 0),
    "blender": (3, 3, 0),
    "category": "Interface",
    }

import json

def load_json(file):
    data = ""
    with open(file, "r") as jsonfile:
        data = json.load(jsonfile)
        return data

if "bpy" in locals():
    import importlib
    importlib.reload(ui)
    importlib.reload(operators)
else:
    import bpy

    from . import (
        ui,
        operators,
    )

classes = (
    ui.GroupFinder,
    operators.NODE_OT_find_node_group

)

addon_keymaps = []

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    