#定义计算战术缺口的函数
def calc_gap(steps,intake=1500):
    burn = 1800 + steps * 0.055
    return burn - intake
#直接调用函数
today_gap = calc_gap(19000)
print(f"--- 函数测试：今日战术缺口为{today_gap:.0f}kcal ---")

#巡航远征倒计时
countdown = 3
while countdown > 0:
    print(f"战术准备中... 距离出发还有{countdown}秒！")
    countdown = countdown - 1
print("时间到！远征部队立刻出发！")


#OW 英雄战绩库
hero_stats = {"艾姆雷":"80%胜率","安娜":"100%胜率"}

#新增/修改数据
hero_stats["雾子"] = "90%胜率"

print("--- 当前OW英雄战术档案 ---")
for name,win_rate in hero_stats.items():
    print(f"英雄【{name}】:{win_rate}")


#模拟用户输入的杂乱文本
raw_input = "    overwatch2   "
clean_name = raw_input.strip().upper()  #去首尾空格并转大写

print(f"原始输入：‘{raw_input}'")
print(f"清洗后战术指令:'{clean_name}'")