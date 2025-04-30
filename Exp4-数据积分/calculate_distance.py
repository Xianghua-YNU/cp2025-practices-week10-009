import numpy as np
from scipy.integrate import cumulative_trapezoid
import matplotlib.pyplot as plt
import os

def main():
    try:
        # 1. 获取数据文件路径（更智能的路径查找）
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        # 尝试可能的文件位置
        possible_paths = [
            os.path.join(current_dir, 'Velocities.txt'),  # 同级目录
            os.path.join(current_dir, '../Velocities.txt'),  # 上级目录
            os.path.join(current_dir, '../../Velocities.txt')  # 上上级目录
        ]
        
        data_file = None
        for path in possible_paths:
            if os.path.exists(path):
                data_file = path
                break
        
        if data_file is None:
            raise FileNotFoundError("未找到Velocities.txt文件")

        # 2. 读取数据
        data = np.loadtxt(data_file)
        t = data[:, 0]  # 时间列
        v = data[:, 1]  # 速度列

        # 3. 计算总距离（使用推荐的trapezoid替代trapz）
        total_distance = np.trapezoid(v, t)
        print(f"总运行距离: {total_distance:.2f} 米")

        # 4. 计算累积距离
        distance = cumulative_trapezoid(v, t, initial=0)

        # 5. 绘制图表（测试时不显示）
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

    except FileNotFoundError:
        print(f"错误：找不到数据文件")
        print("请确保Velocities.txt文件位于以下位置之一：")
        print("\n".join(f"- {path}" for path in possible_paths))
    except Exception as e:
        print(f"发生错误: {str(e)}")

if __name__ == '__main__':
    main()
