import os 

class Find:
    """
    参数：
        directory (String) : 传入当前文件夹目录

    返回：
        (String) 已找到 .so 文件的目录
    """
    def __init__(self,directory):
        self.directory = directory

    def find_so_files(self,):
        for root, dirs, files in os.walk(self.directory):
            for file in files:
                if file.endswith('.so'):
                    return(os.path.split(os.path.join(root, file)))