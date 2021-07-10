from core import getpath
import os, shutil

def clear_tmp():
    dic = getpath.tmp()

    for the_file in os.listdir(dic):
        file_path = os.path.join(dic, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)