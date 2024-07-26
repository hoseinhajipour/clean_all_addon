bl_info = {
    "name": "Clean All",
    "blender": (2, 80, 0),
    "category": "Object",
}

import bpy

class OBJECT_OT_clean_all(bpy.types.Operator):
    bl_idname = "object.clean_all"
    bl_label = "Clean All"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        selected_objects = context.selected_objects
        
        for obj in selected_objects:
            # Remove shape keys
            if obj.data.shape_keys:
                for key in obj.data.shape_keys.key_blocks:
                    obj.shape_key_remove(key)
            
            # Remove armature modifiers
            for mod in obj.modifiers:
                if mod.type == 'ARMATURE':
                    obj.modifiers.remove(mod)
                    
            # Remove vertex groups
            obj.vertex_groups.clear()
            
        self.report({'INFO'}, "Cleaned all shape keys, armature modifiers, and vertex groups")
        return {'FINISHED'}

class OBJECT_PT_clean_all_panel(bpy.types.Panel):
    bl_label = "Clean All"
    bl_idname = "OBJECT_PT_clean_all_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Clean All'

    def draw(self, context):
        layout = self.layout
        layout.operator(OBJECT_OT_clean_all.bl_idname)

def register():
    bpy.utils.register_class(OBJECT_OT_clean_all)
    bpy.utils.register_class(OBJECT_PT_clean_all_panel)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_clean_all)
    bpy.utils.unregister_class(OBJECT_PT_clean_all_panel)

if __name__ == "__main__":
    register()
