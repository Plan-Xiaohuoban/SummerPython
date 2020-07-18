import matplotlib.pyplot as plt
import numpy as np 

plt.rcParams["font.sans-serif"] = ["SimHei"]  # 用来正常显示中文标签
plt.rcParams["axes.unicode_minus"] = False  # 用来正常显示负号



x = np.linspace(0,20,100)
y1 = np.sin(x)
y2 = np.sin(x / 2)

plt.figure(dpi=100)
plt.plot(x,y1)
plt.plot(x,y2)
plt.legend(["y1","y2"])
plt.title("电压输出曲线")
plt.show()


