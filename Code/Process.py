from tqdm import tqdm
from LoopReader import LoopReader
from matplotlib_venn import venn2

import matplotlib.pyplot as plt


class Process:
    def __init__(self,datasets,bin_size,path):
        """
        参数：
            datasets (List) : ["比较文件 1","比较文件 2","输出文件.png","比较数据 1 的名称","比较数据 2 的名称"]
            bin_size (int) : 应设置为 几千 至 几十千
            path (String) : Cython编译后生成的.so文件路径
        """
        self.datasets = datasets
        self.bin_size = bin_size
        self.path = path
        self.Processrocess()
    
    def compare_loops(self,loops1, loops2, bin_size):
        """比较两组循环数据，返回重叠和唯一的循环数量"""
        overlapping_loops = 0
        unique_loops1 = 0
        unique_loops2 = 0

        # 使用tqdm显示第一个循环的进度
        for loop1 in tqdm(loops1, desc="Comparing dataset 1"):
            if any(loop1.is_overlapping(loop2, bin_size) for loop2 in loops2):
                overlapping_loops += 1
            else:
                unique_loops1 += 1

        # 使用tqdm显示第二个循环的进度
        for loop2 in tqdm(loops2, desc="Comparing dataset 2"):
            if not any(loop2.is_overlapping(loop1, bin_size) for loop1 in loops1):
                unique_loops2 += 1

        return overlapping_loops, unique_loops1, unique_loops2

    def Processrocess(self,):
        """
        主函数，执行循环数据的读取、比较和结果展示
        """
        for dataset in self.datasets:
            # 读取并处理数据集1
            loops1 = LoopReader(self.path).read_loops(dataset[0])
            # 读取并处理数据集2
            loops2 = LoopReader(self.path).read_loops(dataset[1])

            # 比较两个数据集中的循环
            overlapping_loops, unique_dataset1, unique_dataset2 = self.compare_loops(loops1, loops2, self.bin_size)
            print(f"Overlapping loops: {overlapping_loops}")
            print(f"Unique in dataset 1: {unique_dataset1}")
            print(f"Unique in dataset 2: {unique_dataset2}")

            # 生成并保存Venn图
            venn2(subsets=(unique_dataset1, unique_dataset2, overlapping_loops), set_labels=(dataset[3], dataset[4]))
            plt.savefig(dataset[2])  # 保存图形到指定路径
            plt.clf()  # 清除当前图形，防止图形间的重叠