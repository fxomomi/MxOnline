## Markdown语法
1. `# 一级标题`、`## 二级标题`...
2. `1. 第一点`、`- 这一点` 
3. `**加粗** or __加粗__`、`*斜体* or _斜体_`、`~~删除线~~`
4. __\`单行代码\`__
5. `tab or 4space 多行代码`
***
## 5.xadmin后台管理系统
### Theme主题功能:
    # 注册BaseSetting,任一一个adminx.py文件中即可
    from xadmin import views
    xadmin.site.register(views.BaseAdminView, BaseSetting)

    class BaseSetting(object):
        enable_themes = True    
        use_bootwatch = True
### 修改页眉、页脚、菜单样式
    # 注册GlobalSetting
    xadmin.site.register(views.CommAdminView, GlobalSetting)

    class GlobalSetting(object):
        site_title = "Momi后台管理系统" # 左上角页眉
        site_footer = "Momi在线网" # 页脚
        menu_style = "accordion" # 菜单样式（收起）
### 修改App显示名称
    # apps.py文件,增加verbose_name字段:
    class OperationConfig(AppConfig):
        name = 'Operation'
        verbose_name = u"用户操作"
    # 在__init__.py中引入:
        default_app_config = "Operation.apps.OperationConfig"