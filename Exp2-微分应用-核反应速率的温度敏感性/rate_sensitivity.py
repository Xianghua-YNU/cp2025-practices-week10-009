import numpy as np
import matplotlib.pyplot as plt

def q3a(T):
    """
    计算 3-alpha 反应速率中与温度相关的部分 q / (rho^2 Y^3)
    输入: T - 温度 (K)
    返回: 速率因子 (erg * cm^6 / (g^3 * s))
    """
    # TODO: 在此实现3-α反应速率计算
    # 提示：
    # 1. 将温度转换为以 10^8 K 为单位
    # 2. 注意处理温度为零的特殊情况
    # 3. 使用公式：q_{3α} = 5.09×10^11 ρ^2 Y^3 T_8^(-3) exp(-44.027/T_8)
    T = np.asarray(T)  # 统一转换为数组处理
    T8 = T / 1e8
    
    # 创建掩码标识有效温度（T != 0）
    valid = (T != 0)
    
    # 初始化结果数组
    factor = np.zeros_like(T)
    
    # 只对有效温度进行计算
    with np.errstate(divide='ignore', invalid='ignore'):
        T8_valid = T8[valid]
        calc = 5.09e11 * (T8_valid**-3) * np.exp(-44.027 / T8_valid)
        factor[valid] = calc
    
    # 处理可能的异常值
    factor = np.nan_to_num(factor, nan=0.0, posinf=0.0, neginf=0.0)
    
    # 返回标量结果（如果输入是标量）
    return factor.item() if np.isscalar(T) else factor 
def plot_rate(filename="rate_vs_temp.png"):
    """绘制速率因子随温度变化的 log-log 图"""
    # TODO: 在此实现绘图函数
    # 提示：
    # 1. 使用 np.logspace 生成温度数据点
    # 2. 计算对应的速率值
    # 3. 使用 plt.loglog 绘制双对数图
    # 4. 添加适当的标签和标题
    T_values = np.logspace(8, 10, 400)  # 生成从1e8到1e10的温度点
    rates = q3a(T_values)
    plt.figure()
    plt.loglog(T_values, rates)
    plt.xlabel('Temperature (K)')
    plt.ylabel('Rate Factor (erg cm$^6$/(g$^3$ s))')
    plt.title('3-alpha Reaction Rate Factor vs. Temperature')
    plt.grid(True)
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
    for T in temperatures_K:
        q = q3a(T)
        if q == 0:
            nu = np.nan
        else:
            T_perturbed = T * (1 + h)
            q_p = q3a(T_perturbed)
            nu = (q_p - q) / (q * h)
        print(f"{T:12.1e}    :   {nu:.3f}")

    # 调用绘图函数
    plot_rate()
 
    # TODO: 调用绘图函数展示结果
