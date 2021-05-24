"""
@Time    : 2021/5/23 22:48
@Author  : ZHC
@FileName: Python_Line.py
@Software: PyCharm
"""
from pyecharts import options as opts
from pyecharts.charts import Line
from pyecharts.globals import ThemeType
from pyecharts.options import TooltipOpts

from PyCharts.SqlConn import GetDBData


def GetLineHtml(name):
    data = GetDBData(username=name)
    if data[0]:
        line = Line(init_opts=opts.InitOpts(theme=ThemeType.LIGHT, width="100%",
                                            # 图表画布高度，css 长度单位。
                                            height="600px", ))

        line.set_global_opts(title_opts=opts.TitleOpts(title="{0}大学四年来的成绩总览".format(name)),
                             tooltip_opts=TooltipOpts(trigger='axis'),
                             toolbox_opts=opts.ToolboxOpts(), legend_opts=opts.LegendOpts(is_show=True),
                             datazoom_opts=opts.DataZoomOpts())
        line.add_xaxis(data[0])
        line.add_yaxis(series_name="总分数", y_axis=data[1])
        line.add_yaxis(series_name="绩点", y_axis=data[2])
        line.add_yaxis(series_name="学分", y_axis=data[3])
        line.render(r"E:\{0}大学四年来的成绩总览.html".format(name))
    else:
        print("数据库找不到相关{0}的信息".format(name))
if __name__ == '__main__':
    name = input("请输入要生成Html的姓名:")
    GetLineHtml(name)