# GenoLoopAnalyzer
## 项目简介
GenoLoopAnalyzer 是一个为基因组数据中的环结构分析而设计的创新工具。该工具利用 Python 和 Cython 提供了一个平台，以发现和比较环结构，帮助深入了解基因组的组织和功能。

**环结构识别：** 使用算法识别基因组数据中的环结构，提供不同区域环的起始和结束位置的重要信息。

**Cython 优化：** 对于工具的关键组件，采用 Cython 将 Python 代码编译成 C 代码，为大规模基因组数据分析提供显著的性能改进。

**数据比较与可视化：**  支持不同数据集之间的基因组环结构比较分析，并通过如Venn图这样的视觉表示形式简洁地展示重叠和区别。

**灵活的数据处理：**  能够处理广泛的基因组数据格式，得益于多功能的循环数据读取器和可自定义的处理参数。
## 文件结构
    GenoLoopAnalyzer
    ├── Code
    │   ├── Find.py
    │   ├── LoopReader.py
    │   ├── Loop_C.c
    │   ├── Loop_C.pyx
    │   ├── Loop_O.py
    │   ├── Process.py
    │   ├── __pycache__
    │   │   ├── Find.cpython-312.pyc
    │   │   ├── LoopReader.cpython-312.pyc
    │   │   ├── Loop_O.cpython-312.pyc
    │   │   └── Process.cpython-312.pyc
    │   ├── main.py
    │   └── setup.py
    ├── Data
    │   └── 说明.md
    ├── Output
    │   └── 说明.md
    └── README.md

## 使用说明
### 执行
1. 在 Terminal (终端) 中，使用 `git clone git@github.com:Data-Always-Analyzing/GenoLoopAnalyzer.git` 命令下载本项目的存储库。
2. 在 Terminal (终端) 中，使用 `cd GenoLoopAnalyzer` 命令进入本项目目录。
3. 在 Terminal (终端) 中，使用 `cd Env` 命令 进入本项目中的 `Env` 目录。
4. 在 Terminal (终端) 中，使用 `conda env create -f environment.yml` 创建虚拟环境并安装所需的依赖。
5. 在 Terminal (终端) 中，使用 `Conda activate Venn` 激活 Conda 虚拟环境。
6. 在 Terminal (终端) 中，使用 `cd ../Code` 命令，进入本项目中的 `Code` 目录。
7. 使用任何文本编辑器，编辑 `Code` 目录中的 `main.py` 文件。在`main.py` 文件中，修改 `bin_size = 2000` 中 `2000` 这个数字。值应当取决于具体的使用需求，通常情况下应在 `1E3 至 9.9E4` 之间。
8. 使用任何文本编辑器，编辑 `Code` 目录中的 `main.py` 文件。在 `main.py` 文件中，修改 `datasets = [('', '', '', '',''),]`。在单引号中分别设置为：`[('输入路径/文件1', '输入路径/文件2', '输出路径/文件名.png', '数据名称1', '数据名称2'),]` 。 其中 `数据名称1` 与 `数据名称2` 会出现在最终的输出文件中。
9. 保存并退出文本编辑器。
10. 在 Terminal (终端) 中，使用 `python Code/main.py` 开始运行。
### 备注
1. 由于使用了 Cython 编译加速运行，如果出现无法使用情况，在 `Code` 目录中保存有 `Loop_O.py` 未使用 Cython 编译运行的版本。在 LoopReader.py 中进行替换，在  LoopReader.py 中有详细的替换指导注释内容。
2. 如果有多个文件需要比对，`datasets = [('', '', '', '', ''), ]`可扩充为 `datasets = [('', '', '', '', ''), ('', '', '', '', ''),]` 如果有更多需要，可以继续扩充。
3. 请务必确认在进入项目的 ***根目录*** 且激活对应的 ***Conda*** 环境后再运行。

