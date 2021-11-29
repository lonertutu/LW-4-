import enum
import numpy as np
import matplotlib.pyplot as plt
import waveFunctions as b
from scipy.optimize import curve_fit

L = 1.66

# чтение данных ADC для калибровки

samples_20, duration_20, length_20 = b.read("20mmcalibration.txt")
samples_40, duration_40, length_40 = b.read("40mmcalibration.txt")
samples_60, duration_60, length_60 = b.read("60mmcalibration.txt")
samples_80, duration_80, length_80 = b.read("80mmcalibration.txt")
samples_100, duration_100, length_100 = b.read("100mmcalibration.txt")
samples_120, duration_120, length_120 = b.read("120mmcalibration.txt")

# чтение данных ADC при открывании дверцы

samples_wave_40, duration_wave_40, length_wave_40 =  b.read("40mmexp.txt")
samples_wave_80, duration_wave_80, length_wave_80 =  b.read("80mmexp.txt")
samples_wave_120, duration_wave_120, length_wave_120 =  b.read("120mmexp.txt")

y = np.array([20, 40, 60, 80, 100, 120])
x = np.array([np.mean(samples_20), np.mean(samples_40), np.mean(samples_60), np.mean(samples_80), np.mean(samples_100), np.mean(samples_120)]) #среднее значение
coef = np.polyfit(x, y, 3)
x_fit = np.linspace(1200, 2500, 1000)
y_fit = np.polyval(coef, x_fit)

def to_height(x):
    global coef
    return np.polyval(coef, x)

# print(coef, x, y_fit)

fig0 = plt.figure(figsize=(16, 10), dpi=400)
ax0 = plt.axes()
plt.plot(x_fit, y_fit, '#3568e7', linewidth = 3, label = 'Калибровочная функция в диапозоне  [0:2700] отсчетов АЦП')
plt.plot(x, y, 'ro', label = 'Измерения', markersize=10)
plt.ylabel('Уровень воды [мм]', fontsize = 18)
plt.xlabel('Отсчеты АЦП', fontsize = 18)
plt.title('Калибровочный график зависимости показаний АЦП от уровня', loc = 'center', fontsize = 24, wrap = True)
plt.legend(fontsize = 16)
plt.grid()
if 1:
    plt.savefig("level-calibration1.png")



# ---------------------------- график для 40 мм -----------------------------------------

time_40exp = np.linspace(0, duration_wave_40, length_wave_40)
heights_40exp = to_height(samples_wave_40)
for i, h in enumerate(heights_40exp):
    if h < 0:
        i_crop = i
        break

heights_40exp = heights_40exp[0:i_crop]
time_40exp = time_40exp[0:i_crop]

fig1 = plt.figure(figsize=(16, 10), dpi=400)
ax1 = plt.axes()
plt.plot(time_40exp, heights_40exp, 'o')
plt.ylabel('Уровень воды [мм]', fontsize = 18)
plt.xlabel('Время [cек]', fontsize = 18)
plt.title('Уровень воды в кювете после открытия торцевой двери', loc = 'center', fontsize = 24, wrap = True)
plt.grid()
plt.savefig("vel_40exp.png")


# ---------------------------- график для 80 мм -----------------------------------------

time_80exp = np.linspace(0, duration_wave_80, length_wave_80)
heights_80exp = to_height(samples_wave_80)

for i, h in enumerate(heights_80exp):
    if h < 0:
        i_crop = i
        break
heights_80exp = heights_80exp[0:i_crop]
time_80exp = time_80exp[0:i_crop]


fig2 = plt.figure(figsize=(16, 10), dpi=400)
ax2 = plt.axes()
plt.plot(time_80exp, heights_80exp, 'o')
plt.ylabel('Уровень воды [мм]', fontsize = 18)
plt.xlabel('Время [cек]', fontsize = 18)
plt.title('Уровень воды в кювете после открытия торцевой двери', loc = 'center', fontsize = 24, wrap = True)
plt.grid()
#plt.text(11, 90, "L = {} [м]\nt = {} [с]\nV = {} [м/c]".format(L, round(time_80exp[что-то туть], 2), round(L/time_80exp[что-то туть], 2)), size=30, bbox={"boxstyle": "round, pad=0.1", "facecolor": "white"})
plt.savefig("vel_80exp.png")
# ---------------------------- график для 120 мм -----------------------------------------

time_120exp = np.linspace(0, duration_wave_120, length_wave_40)
heights_120exp = to_height(samples_wave_120)
for i, h in enumerate(heights_120exp):
    if h < 0:
        i_crop = i
        break

heights_120exp = heights_120exp[0:i_crop]
time_120exp = time_120exp[0:i_crop]

fig1 = plt.figure(figsize=(16, 10), dpi=400)
ax1 = plt.axes()
plt.plot(time_120exp, heights_120exp, 'o')
plt.ylabel('Уровень воды [мм]', fontsize = 18)
plt.xlabel('Время [cек]', fontsize = 18)
plt.title('Уровень воды в кювете после открытия торцевой двери', loc = 'center', fontsize = 24, wrap = True)
plt.grid()
plt.savefig("vel_120exp.png")

