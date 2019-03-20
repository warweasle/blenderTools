import bpy
from bpy import context

# move every bone by 1.0 units on the Y.
obj = context.object

bpy.ops.object.mode_set(mode='EDIT')

for bone in obj.data.edit_bones:
    bone.head.y += 1.0
    bone.tail.y += 1.0

bpy.ops.object.mode_set(mode='OBJECT')

####################################

import bpy

name_list = [
    # old name - new name
    ['lowerarm_L','forearm.L'],
    ['lowerarm_R','forearm.R'],
    ['upperarm_L','upper_arm.L'],
    ['upperarm_R','upper_arm.R'],
]

v_groups = bpy.context.active_object.vertex_groups
for n in name_list:
    if n[0] in v_groups:
        v_groups[n[0]].name = n[1]
        
#########################################
# Note that matching names this way is case-sensitive, for an insensitive match use -
########################################

v_groups = bpy.context.active_object.vertex_groups
for n in name_list:
    for vn in v_groups:
        if vn.name.lower() == n[0].lower():
            vn.name = n[1]
