
class Loop:
    """
    表示基因组中的一个循环结构的类。

    属性:
        start1 (int): 第一个区域的起始位置。
        end1 (int): 第一个区域的结束位置。
        start2 (int): 第二个区域的起始位置。
        end2 (int): 第二个区域的结束位置。
    """

    def __init__(self, start1, end1, start2, end2):
        """
        初始化Loop对象。

        参数:
            start1 (int): 第一个区域的起始位置。
            end1 (int): 第一个区域的结束位置。
            start2 (int): 第二个区域的起始位置。
            end2 (int): 第二个区域的结束位置。
        """
        self.start1 = start1
        self.end1 = end1
        self.start2 = start2
        self.end2 = end2

    def is_overlapping(self, other, bin_size):
        """
        判断两个循环是否重叠。

        参数:
            other (Loop): 另一个Loop对象用于与当前Loop比较。
            bin_size (int): 定义重叠时允许的最大距离差。

        返回:
            bool: 如果两个循环重叠，则返回True；否则返回False。
        """
        # 重叠的条件是任一端的起始或结束位置之间的距离小于或等于bin_size
        return abs(self.start1 - other.start1) <= bin_size and abs(self.end1 - other.end1) <= bin_size or \
               abs(self.start2 - other.start2) <= bin_size and abs(self.end2 - other.end2) <= bin_size


