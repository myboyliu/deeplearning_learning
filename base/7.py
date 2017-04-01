#-*- encoding=utf8 -*-

import os,sys

if __name__=="__main__":

    print("__file__=%s" % __file__ )

    print("os.path.realpath(__file__)=%s" % os.path.realpath(__file__))

    print("os.path.dirname(os.path.realpath(__file__))=%s" % os.path.dirname(os.path.realpath(__file__)))

    print("os.path.split(os.path.realpath(__file__))=%s" % os.path.split(os.path.realpath(__file__))[0])

    print("os.path.abspath(__file__)=%s" % os.path.abspath(__file__))

    print( "os.getcwd()=%s" % os.getcwd())

    print("sys.path[0]=%s" % sys.path[0])

    print("sys.argv[0]=%s" % sys.argv[0])

    # 获取当前文件__file__的路径

    print("os.path.realpath(__file__)=%s" % os.path.realpath(__file__))

    # 获取当前文件__file__的所在目录

    print("os.path.dirname(os.path.realpath(__file__))=%s" % os.path.dirname(os.path.realpath(__file__)))
    # 获取当前文件__file__的所在目录

    print("os.path.split(os.path.realpath(__file__))=%s" % os.path.split(os.path.realpath(__file__))[0])

    dir = os.path.dirname(os.path.realpath(__file__))
    parent_dir = os.path.dirname(dir)
    print(parent_dir)