import bpy

class GroupFinder(bpy.types.Menu):
    bl_label = "GroupFinder"
    bl_idname = "WINDOW_MT_GroupFinder"

    def draw(self, context):
        layout = self.layout

        layout.operator("node.findgroup", text="Query")

def draw_item(self, context):
    layout = self.layout
    layout.menu(GroupFinder.bl_idname)