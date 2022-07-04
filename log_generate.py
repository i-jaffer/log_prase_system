import random
import os

init_str = '''
 \ | /
- RT -     Thread Operating System
 / | \     3.1.1 build Nov 19 2018
 2006 - 2018 Copyright by rt-thread team
msh >
'''

filename = str(input("请输入需要操作的文件:"))

filesize = 0
if (os.path.exists(filename)):
    filesize = os.path.getsize(filename)
if (filesize == 0):
    fd = open(filename, 'a')
    fd.write(init_str)
    fd.close()
else :
    fd = open(filename)
    # read log content
    print("read log content:")
    print(fd.read())
    fd.close()

fd = open(filename, 'a')
# write random log
for i in range(random.randint(0, 100)):
    fd.write("[task] adapter volt:" + str(random.randint(0, 100)) + '.' + str(random.randint(0, 10)) + 'v')
    fd.write("\n")
fd.close()