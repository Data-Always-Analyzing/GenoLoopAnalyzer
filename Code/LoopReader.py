import pandas as pd
import sys
from Loop_C import Loop

#from Loop_O import Loop
class LoopReader:
    def __init__(self,path):
        sys.path.append(path)
        
        
    """
    提供读取和解析循环数据文件的功能。

    方法:
        read_loops: 静态方法，从指定的文件路径读取循环数据，并返回Loop对象的列表。
    """

    @staticmethod
    def read_loops(file_path):
        """
        从文件中读取循环数据，返回Loop对象列表。

        参数:
            file_path (str): 包含循环数据的文件路径。

        返回:
            list[Loop]: 从文件中读取并解析得到的Loop对象列表。
        """
        loops = []  # 初始化空列表用于存储Loop对象
        # 使用pandas读取文件，假设文件格式遵循特定的列结构
        df = pd.read_csv(file_path, header=None, sep=r'\s+')
        # 为数据帧指定列名，便于通过列名访问数据
        df.columns = ['chromosome1', 'start1', 'end1', 'chromosome2', 'start2', 'end2', 'dot', 'number']
        
        for _, row in df.iterrows():
            # 对每一行数据，根据起始和结束位置创建Loop对象并添加到列表中
            loop = Loop(row['start1'], row['end1'], row['start2'], row['end2'])
            loops.append(loop)
        
        return loops  # 返回包含所有Loop对象的列表