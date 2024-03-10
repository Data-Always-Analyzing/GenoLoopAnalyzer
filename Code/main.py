import subprocess
from Find import Find
import sys

if __name__ == "__main__":
    # 设置Bin_Size
    bin_size = 2000
    # 设置文件输入与输出路径
    datasets = [
        ('', '', '', '',''),
        ]
    # 执行Cython编译以加速运行
    subprocess.run(["python","Code/setup.py","build_ext","--inplace"], capture_output=True, text=True)
    # 查找编译后的文件路径
    path = Find("build").find_so_files()[0]
    # 添加 .So 文件路径至模块导入路径
    sys.path.append(path)
    from Process import Process
    Process(datasets,bin_size, path)