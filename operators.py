import bpy
from bpy.props import EnumProperty

def populateSearch(self, context):

    current_nodegroup = context.space_data.edit_tree

    node_groups = []
    for node in current_nodegroup.nodes:
        try:
            if "Group" in node.name:
                node_groups.append((node.name, node.node_tree.name+f" ({node.name})", ""))
        except AttributeError:
            pass
    
    result = tuple(node_groups)
    return result

class NODE_OT_find_node_group(bpy.types.Operator):
    bl_idname = "node.findgroup"
    bl_label = "Find group"
    bl_property = "nodequery"

    # first is identifier, second is name, third is ???. items require 3 fields.
    nodequery: EnumProperty(name="Query", items=(populateSearch))

    # @classmethod
    # def poll(cls, context):
    #     return True if hasattr(context, 'NODE_EDITOR') else False
    
    def execute(self, context):

        current_nodegroup = context.space_data.edit_tree

        print(f"selected: {self.nodequery}")
        bpy.ops.node.select_all(action='DESELECT')
        current_nodegroup.nodes[self.nodequery].select = True
        bpy.ops.node.view_selected()

        return {'FINISHED'}
        
        
    def invoke(self, context, event):
        context.window_manager.invoke_search_popup(self)
        return {'RUNNING_MODAL'}
