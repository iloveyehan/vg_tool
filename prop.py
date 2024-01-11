import bpy
class Mirror_Settings(bpy.types.PropertyGroup):
    mirror_method: bpy.props.EnumProperty(
        name="镜像方法",
        description="左右对称时最近点效果好，不对称时面插值",
        items=(("NEAREST", "最近点", "最近的顶点"),
               ("POLYINTERP_NEAREST", "面插值", "最近的面插值"),
               ))
    left_right: bpy.props.EnumProperty(
            name="对称方向",
            description="选择对称方向",
            items=(("-x", "", "使用右边权重",'BACK', 1),
                   ("+x", "", "使用左边权重",'FORWARD', 2),
                   )

    )
            # 此处图标名'FILE_TICK'和'FILE_NEW'应替换为有效的Blender图标名称
    is_center: bpy.props.BoolProperty(name='对称',
                                                  description="中间骨对称，左右骨镜像")

    is_multiple:bpy.props.BoolProperty(name='多个',
                                                  description="多个顶点组")