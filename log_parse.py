import easygui
import re
import matplotlib.pyplot as plt

ret = None
tag, keyword_header, keyword_tail = '', '', ''
msg = """\
请输入以下信息进行数据提取

例: 待处理数据 [adc] power volt 3.3f
    日志tag: adc
    关键字前部: volt 
    关键字后部: f
"""

def get_key_information(filename, regular_expression):
    # 使用正则表达式提取信息，并将提取到的数据返回
    fd = open(filename, 'r')
    p = re.compile(regular_expression, re.MULTILINE)
    #p = re.compile("^\[task\].*volt:(\d+.{0,1}\d+)v", re.MULTILINE)
    result = p.findall(fd.read())
    fd.close()
    return result

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

# get ket information for regular expression
result = get_key_information(filename, expression)

# str to float
result_of_num = [float(i) for i in result]
print(result)
print(result_of_num)

#plt.plot([i for i in range(len(result))], out_of_num)
plt.plot(result_of_num)
plt.show()