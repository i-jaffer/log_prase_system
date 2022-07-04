import easygui
import re

ret = None
tag, keyword_header, keyword_tail = '', '', ''
msg = """\
请输入以下信息进行数据提取

例: 待处理数据 [adc] power volt 3.3f
    日志tag: adc
    关键字前部: volt 
    关键字后部: f
"""

ret = easygui.msgbox(msg = "欢迎使用日志提取系统", title = "日志提取系统", ok_button="OK")
if ret == None:
    exit(1)
while (tag == '') or (keyword_header == ''):
    ret = easygui.multenterbox(msg, title = "日志提取系统",
                               fields=["日志tag", '关键字前部', '关键字后部'])
    if ret == None:
        exit(1)
    else:
        tag, keyword_header, keyword_tail = ret[0], ret[1], ret[2]

    if tag == '':
        easygui.msgbox(msg = "tag不能为空,请重新输入", title = "错误")
    if keyword_header == '':
        easygui.msgbox(msg = "关键字前部不能为空,请重新输入", title = "错误")
print('tag:', tag, "keyword_header:", keyword_header, "keyword_tail:", keyword_tail)

# open file
filename = easygui.fileopenbox()
print(filename)
expression = f"^\[{tag}\].*{keyword_header}(\d+.{{0,1}}\d+)v"
print(expression)

fd = open(filename, 'r')
p = re.compile(expression, re.MULTILINE)
#p = re.compile("^\[task\].*volt:(\d+.{0,1}\d+)v", re.MULTILINE)
out = p.findall(fd.read())
fd.close()

out_of_num = [float(i) for i in out]
print(out)
print(out_of_num)
