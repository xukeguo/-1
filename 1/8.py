#欢迎使用Python脚本编辑器！我的一小步，人类一大步！
#@File    :   8.py
#@Time    :   2022/04/20 15:09:15
#@Author  :   flow-laic 
#@Email   :
from email import header
import demo
demo.f()
import math
print(dir(math)) #查看模块的方法
import builtins
print(dir(builtins)) #查看内建模块的方法 
#查看模块的方法

import builtins
print(dir(builtins))#查看内建模块的方法
import os
os.system('/System/Applications/Calculator.app/Contents/MacOS/Calculator')
os.system('/Applications/WeChat.app/Contents/MacOS/WeChat')
os.getlogin()#返回当前登录用户名
os.system('dir')
os.aborter()#终止当前进程
os.system()#执行命令
os.access()#检查文件是否可访问
os.chdir()#改变当前工作目录
os.chmod()#修改文件的权限
os.chown()#修改文件的所有者
os.close()#关闭文件 
os.closerange()#关闭所有文件
os.dup()#复制文件句柄
os.dup2()#复制文件句柄
os.fchdir()#通过文件句柄改变当前工作目录
os.fchmod()#修改文件的权限
os.fchown()#修改文件的所有者
os.fdatasync()#同步文件数据
os.fstat()#返回文件状态
os.fsync()#同步文件数据
os.ftruncate()#截断文件
os.getcwd()#返回当前工作目录
os.getcwdu()#返回当前工作目录
os.getegid()#返回当前进程的用户组ID
os.geteuid()#返回当前进程的用户ID
os.getgid()#返回当前进程的组ID
os.getgroups()#返回当前进程的组列表
os.getlogin()#返回当前登录用户名
os.getpgid()#返回一个进程组的ID
os.getpgrp()#返回当前进程组ID
os.getpid()#返回当前进程ID
os.getppid()#返回当前进程的父进程ID
os.getresuid()#返回当前进程的运行时用户ID
os.getresgid()#返回当前进程的运行时组ID
os.getrlimit()#返回进程的资源限制
os.initgroups()#初始化组
os.isatty()#检查文件是否是一个终端设备
os.kill()#结束进程
os.killpg()#结束进程组
os.lchown()#修改文件的所有者
os.link()#创建硬链接
os.listdir()#返回指定目录下的文件和目录名
os.lseek()#设置文件指针位置
os.lstat()#返回文件状态
os.major()#返回设备的主设备号
os.makedev()#创建一个设备号
os.minor()#返回设备的次设备号
os.mkdir()#创建目录
os.mknod()#创建一个名字符设备文件（包括字符、块设备、管道）
os.open()#打开一个文件，用于读写
os.openpty()#打开一个新的伪终端
os.pathconf()#返回相关文件的系统配置信息
os.pipe()#创建一个管道
os.popen()#打开一个命令行程序，用于读写
os.read()#从文件读取数据
os.readlink()#返回软链接所指向的文件
os.remove()#删除一个文件
os.rename()#重命名文件或目录
os.renames()#递归地对目录进行更名
os.rmdir()#删除目录
os.setegid()#设置进程的用户组ID
os.seteuid()#设置进程的用户ID
os.setgid()#设置进程的组ID
os.setgroups()#设置进程的组列表
os.setpgid()#设置进程组ID
os.setpgrp()#设置进程组ID
os.system()#执行系统命令
os.symlink()#创建软链接
os.tcgetpgrp()#返回一个进程组的ID
os.tcsetpgrp()#设置一个进程组的ID
os.tempnam()#返回一个指定目录的临时文件名
os.tmpfile()#返回一个打开的模式为(w+b)的文件对象
os.tmpnam()#返回一个打开的模式为(w+b)的文件对象
os.ttyname()#返回一个文件的终端设备名
os.unlink()#删除文件
os.utime()#设置访问和修改时间
os.wait()#等待子进程结束
os.wait3()#等待子进程结束，并返回一个元组
os.wait4()#等待子进程结束，并返回一个元组
os.write()#向文件写入数据
os.dup()#复制文件描述符
os.dup2()#复制文件描述符
os.fstat()#返回一个文件的状态
os.lstat()#返回文件状态，和stat()相同，但是没有软链接
os.mkfifo()#创建命名管道，在UNIX中也可以创建特殊的管道文件
os.openpty()#打开一个新的伪终端
os.pipe()#创建一个管道
os.popen()#打开一个命令行程序，用于读写
os.read()#从文件读取数据
os.write()#向文件写入数据
os.fdopen()#打开一个文件描述符，用于读写

import os
#path1=os.path.abspath('text.txt')# 返回当前目录的绝对路径
#path2=os.path.split(path1)# 将一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
#print(path1)
lis=os.listdir('/Users/xkg/Documents/GitHub')# 返回指定的文件夹包含的文件或文件夹的名字的列表')
print(lis)
#os.path.isdir()# 如果path是一个存在的目录返回true，否则返回false
#os.path.isfile()# 如果path是一个存在的文件，返回true。否则返回false
#os.path.exists()# 如果path存在，返回true。否则返回false
#os.path.getsize()# 返回文件大小，如果文件不存在则返回错误
#os.path.getatime()# 返回最后一次进入文件系统的时间
#os.path.getmtime()# 返回最后一次修改文件的时间
#os.path.getctime()# 返回文件系统上的文件创建时间
#os.path.getsize()# 返回文件大小，如果文件不存在则返回错误
#os.path.isabs()# 如果path是绝对路径，返回true。否则返回false
#os.path.isfile()# 如果path是一个存在的文件，则返回true。否则返回false
path3=os.getcwd()# 返回当前工作目录
lis2=os.listdir(path3)# 返回指定的文件夹包含的文件或文件夹的名字的列表
print(lis2)
for file in lis2:
    if file.endswith('.py'):
        print(file)
#os.path.join()# 将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
# os.path.normpath()# 当path以//或C:开头时，返回正确的路径，其他情况下不做转换
# os.path.realpath()# 返回path的真实路径，规范化路径名，并解析或查看规范化路径的符号链接
# os.path.relpath()# 返回path相对于other的相对路径
# os.path.split()# 将path分割成目录和文件名二元组返回
# os.path.splitext()# 将path分割成目录和扩展名两元组返回
# os.path.splitdrive()# 将path分割成目录和文件路径二元组返回
# os.path.basename()# 返回path最后的文件名  
#os.path.dirname()# 返回path的目录。其实就是把最后一个目录分隔符'\'或斜杠'/'去掉
#os.path.commonprefix()# 返回path列表中第一个出现的目录前缀
#os.path.expanduser()# 将path中包含的"~"和"~user"转换成用户目录
#os.path.expandvars()# 将path中包含的"$name"转换成环境变量
#os.path.isabs()# 如果path是绝对路径，返回true。否则返回false

a1=os.path.splitdrive('/Applications/WeChat.app/Contents/MacOS/WeChat')# 将path分割成目录和文件路径二元组返回
print(a1)
a2=os.path.splitext('/Applications/WeChat.app/Contents/MacOS/WeChat')# 将path分割成目录和扩展名两元组返回
import os.path
print (os.path.abspath( 'demol3.py'))# 返回path规范化的绝对路径
print (os.path.exists ('demol3.py'), os. path. exists (' demo18. py'))# 如果path存在，返回true。否则返回false
print (os.path.join('E:\\Python','demo13.py'))
print (os.path.split('E:\\vipython\\chap15\\demo13.py'))#windows下的路径分割
print (os.path.splitdrive('E:/vipython/chap15/demo13.py'))#mac下的路径分割
print (os.path.splitext ( 'demol3.py'))