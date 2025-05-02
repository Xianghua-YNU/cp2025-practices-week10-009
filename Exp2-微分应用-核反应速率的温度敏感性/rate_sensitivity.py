import numpy as np
import matplotlib.pyplot as plt
def q3a(T):
    """
    计算 3-alpha 反应速率中与温度相关的部分 q / (rho^2 Y^3)
    输入: T - 温度 (K)
    返回: 速率因子 (erg * cm^6 / (g^3 * s))
    """
    T8 = T / 1e8
    if T <= 0 or T8 == 0:
        return 0.0
    return 5.09e11 * (T8)**(-3) * np.exp(-44.027 / T8)

def plot_rate(filename="rate_vs_temp.png"):
    """绘制速率因子随温度变化的 log-log 图"""
    # TODO: 在此实现绘图函数
    # 提示：
    # 1. 使用 np.logspace 生成温度数据点
    # 2. 计算对应的速率值
    # 3. 使用 plt.loglog 绘制双对数图
    # 4. 添加适当的标签和标题
    T_values = np.logspace(np.log10(1e8), np.log10(5e9), 100)
    q_values = [q3a(T) for T in T_values]
    plt.figure(figsize=(10, 6))
    plt.loglog(T_values, q_values)
    plt.xlabel('温度 T (K)')
    plt.ylabel(r'$q_{3\alpha} / (\rho^2 V^3)$')
    plt.title('3α反应速率与温度的关系')
    plt.grid(True, which="both", linestyle="--")
    plt.savefig(filename)
    plt.close()

if __name__ == "__main__":
    # 计算并打印 nu 值
    print("   温度 T (K)    :   ν (敏感性指数)")
    print("--------------------------------------")

    temperatures_K = [1.0e8, 2.5e8, 5.0e8, 1.0e9, 2.5e9, 5.0e9]
    h = 1.0e-8  # 扰动因子

    # TODO: 实现温度敏感性指数的计算
    # 提示：
    # 1. 对每个温度点计算 q3a
    # 2. 使用前向差分计算导数
    # 3. 计算敏感性指数 nu
    # 4. 注意处理特殊情况（如 q = 0）
    for T0 in temperatures_K:
        q0 = q3a(T0)
        if q0 == 0:
            v = 0.0
        else:
            T_perturbed = T0 * (1 + h)
            q1 = q3a(T_perturbed)
            v = (q1 - q0) / (h * q0)
        
        # 格式化温度字符串
        T_str = "{0:.1e}".format(T0)
        parts = T_str.split('e')
        exp_part = parts[1].lstrip('0+').lstrip('0')
        if not exp_part:
            exp_part = '0'
        formatted_T = f"{parts[0]}e{exp_part}"
        print(f"{formatted_T} K : {v:.3f}")

    plot_rate()
 
    # TODO: 调用绘图函数展示结果
