import numpy as np
from scipy.integrate import cumulative_trapezoid
import matplotlib.pyplot as plt
import os

def calculate_distance(data_file=None):
    """
    从速度数据计算距离并绘图
    
    参数:
        data_file (str): 数据文件路径。如果为None，则尝试默认文件名
    """
    try:
        # 1. 确定数据文件路径
        if data_file is None:
            # 尝试可能的文件位置
            possible_paths = [
                'Velocities.txt',
                'data/Velocities.txt',
                'Exp4-数据积分/Velocities.txt',
                'Exp4-数据积分/data/Velocities.txt'
            ]
            
            for path in possible_paths:
                if os.path.exists(path):
                    data_file = path
                    break
            else:
                raise FileNotFoundError("未找到Velocities.txt文件，请检查文件路径")

        # 2. 读取并验证数据
        with open(data_file, 'r') as f:
            first_line = f.readline().strip()
            if not first_line.replace('.','',1).replace(' ','').isdigit():
                raise ValueError("数据文件格式不正确")

        data = np.loadtxt(data_file)
        if data.shape[1] != 2:
            raise ValueError("数据文件应包含两列(时间和速度)")

        t = data[:, 0]  # 时间列
        v = data[:, 1]  # 速度列

        # 3. 计算总距离(使用推荐的trapezoid)
        total_distance = np.trapezoid(v, t)
        print(f"总运行距离: {total_distance:.2f} 米")

        # 4. 计算累积距离
        distance = cumulative_trapezoid(v, t, initial=0)

        # 5. 绘图(测试时不需要显示)
        if __name__ == '__main__':
            plt.figure(figsize=(10, 6))
            plt.plot(t, v, 'b-', label='速度 (m/s)')
            plt.plot(t, distance, 'r--', label='距离 (m)')
            plt.title('速度与距离随时间变化')
            plt.xlabel('时间 (秒)')
            plt.ylabel('速度 (米/秒) / 距离 (米)')
            plt.legend()
            plt.grid(True)
            plt.show()

        return total_distance, distance

    except Exception as e:
        print(f"错误: {str(e)}")
        print(f"当前工作目录: {os.getcwd()}")
        print("请检查:")
        print("1. 文件是否存在")
        print("2. 文件格式是否正确(应包含两列数字)")
        raise  # 重新抛出异常以便测试捕获

def main():
    """命令行入口"""
    calculate_distance()

if __name__ == '__main__':
    main()
