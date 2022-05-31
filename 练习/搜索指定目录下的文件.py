#编写一个程序文件，用于搜索指定目录下的文件。
import os,sys
def findfile(start, name):
    for root, dirs, files in os.walk(start):
        #print ('relpath= %s, dirs=%s, files = %s' %(root, dirs, files))
        for filename in files:
            if name in filename:
                full_path = os.path.join(start, filename)
                #full_path = os.sep.join([root,filename])    
                print(os.path.normpath(os.path.abspath(full_path))) #规范path字符串形式
if __name__ == '__main__':#如果函数不是被调用则运行
    findfile(".", "回文")
