import bpy

def mergeVertexGroups(targetName, sourceName):

    o = bpy.context.object
    bpy.ops.object.mode_set( mode = 'EDIT' )

    target = o.vertex_groups[targetName]
    source = o.vertex_groups[sourceName]          

    # Deselect all verts and select only current VG    
    bpy.ops.mesh.select_all( action = 'DESELECT' )

    # Set the first vertex group as active:
    o.vertex_groups.active_index = source.index 
    #o.vertex_groups.active = source
    bpy.ops.object.vertex_group_select()
    
    # Set the second vertex group as active:
    o.vertex_groups.active_index = target.index
    #o.vertex_groups.active = target
    bpy.ops.object.vertex_group_select()

    bpy.ops.object.vertex_group_assign()
    
    o.vertex_groups.active_index = source.index
    #o.vertex_groups.active = source    
    bpy.ops.object.vertex_group_remove()

    bpy.ops.object.mode_set( mode = 'OBJECT' )

        
mergeVertexGroups("lowerarm_L", "lowerarm_twist_L")
mergeVertexGroups("lowerarm_R", "lowerarm_twist_R")
mergeVertexGroups("upperarm_L", "upperarm_twist_L")
mergeVertexGroups("upperarm_R", "upperarm_twist_R")
mergeVertexGroups("thigh_L", "thigh_twist_L")
mergeVertexGroups("thigh_R", "thigh_twist_R")
mergeVertexGroups("calf_L", "calf_twist_L")
mergeVertexGroups("calf_R", "calf_twist_R")



map = {'ORG-spine':'pelvis',
 'ORG-spine.001': 'spine01',
 'ORG-spine.002': 'spine02',
 'ORG-spine.003':'spine03',
 'ORG-spine.004': 'neck',
 'ORG-spine.005': 'head',
'ORG-shoulder.L': "clavicle_L",
'ORG-shoulder.R': "clavicle_R",
'ORG-upper_arm.L': "upperarm_L",
'ORG-upper_arm.R': "upperarm_R",
'ORG-forearm.L': 'lowerarm_L',
'ORG-forearm.R': 'lowerarm_R',
'ORG-hand.L': 'hand_L',
'ORG-hand.R': 'hand_R',
'ORG-palm.01.L': 'index00_L',
'ORG-palm.01.R': 'index00_R',
'ORG-f_index.01.L': 'index01_L',
'ORG-f_index.01.R': 'index01_R',
'ORG-f_index.02.L': 'index02_L',
'ORG-f_index.02.R': 'index02_R',
'ORG-f_index.03.L': 'index03_L',
'ORG-f_index.03.R': 'index03_R',
'ORG-palm.02.L': 'middle00_L',
'ORG-palm.02.R': 'middle00_R',
'ORG-f_middle.01.L': 'middle01_L',
'ORG-f_middle.01.R': 'middle01_R',
'ORG-f_middle.02.L': 'middle02_L',
'ORG-f_middle.02.R': 'middle02_R',
'ORG-f_middle.03.L': 'middle03_L',
'ORG-f_middle.03.R': 'middle03_R',
'ORG-palm.03.L': 'ring00_L',
'ORG-palm.03.R': 'ring00_R',
'ORG-f_ring.01.L': 'ring01_L',
'ORG-f_ring.01.R': 'ring01_R',
'ORG-f_ring.02.L': 'ring02_L',
'ORG-f_ring.02.R': 'ring02_R',
'ORG-f_ring.03.L': 'ring03_L',
'ORG-f_ring.03.R': 'ring03_R',
'ORG-palm.04.L': 'pinky00_L',
'ORG-palm.04.R': 'pinky00_R',
'ORG-f_pinky.01.L': 'pinky01_L',
'ORG-f_pinky.01.R': 'pinky01_R',
'ORG-f_pinky.02.L': 'pinky02_L',
'ORG-f_pinky.02.R': 'pinky02_R',
'ORG-f_pinky.03.L': 'pinky03_L',
'ORG-f_pinky.03.R': 'pinky03_R',
'ORG-thumb.01.L': 'thumb01_L',
'ORG-thumb.02.L': 'thumb02_L',
'ORG-thumb.03.L': 'thumb03_L',
'ORG-thumb.01.R': 'thumb01_R',
'ORG-thumb.02.R': 'thumb02_R',
'ORG-thumb.03.R': 'thumb03_R',
'ORG-thigh.R': 'thigh_R',
'ORG-thigh.L': 'thigh_L',
'ORG-shin.L': 'calf_L',
'ORG-shin.R': 'calf_R',
'ORG-foot.L': 'foot_L',
'ORG-foot.R': 'foot_R',
'ORG-toe.L': "toes_L",
'ORG-toe.R': "toes_R",
'ORG-breast.L': 'breast_L',
'ORG-breast.R': 'breast_R'}

#for i in map:
#    print(i + " = " + map[i]);
    
    
armature = bpy.context.object.find_armature()
print(armature)

#bones = armature.data.bones
#bpy.ops.object.mode_set(mode='EDIT')

boneData = {}
bpy.data.objects[armature.name].select = True
bpy.context.scene.objects.active = bpy.data.objects[armature.name]
print(armature.name)
bpy.ops.object.mode_set(mode='EDIT')
for b in bpy.context.object.data.edit_bones:
    if b.name in map:
        print(b.name)
        b.name = map[b.name]
        b.use_deform = True
        
bpy.ops.object.mode_set(mode='OBJECT')

