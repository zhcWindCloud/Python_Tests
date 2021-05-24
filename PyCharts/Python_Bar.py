"""
@Time    : 2021/5/16 12:47
@Author  : ZHC
@FileName: Python_Bar.py
@Software: PyCharm
"""

# 导入柱状图-Bar
import pyecharts
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType
from pyecharts.options import AnimationOpts

AnimationOpts()
print(pyecharts.__version__)

bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
bar.set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"),
                    toolbox_opts=opts.ToolboxOpts(), legend_opts=opts.LegendOpts(is_show=True),
                    )
bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar.add_yaxis("商家A", y_axis=[5, 20, 36, 10, 75, 90])
bar.add_yaxis("商家B", [45, 45, 48, 54, 48, 48, 48])
# render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# 也可以传入路径参数，如 bar.render("mycharts.html")
bar.render("myBarCharts.html")
