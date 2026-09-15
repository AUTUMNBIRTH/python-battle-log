#1. 列表嵌套字典（战队英雄库数据）
hero_list = [
    {"name":"死神","win_rate":80.0,"kd":5.0},
    {"name":"麦克雷","win_rate":20.0,"kd":3.0},
    {"name":"艾姆雷","win_rate":65.0,"kd":4.2},
    {"name":"安娜","win_rate":90.0,"kd":3.5}
]

#2. 定义战术分析函数
def analyze_team(heroes):
    total_win_rate = 0
    best_hero = heroes[0] #假定第一个是 mvp

    # 遍历列表中的每一个字典
    for h in heroes:
        total_win_rate += h["win_rate"]
        #寻找胜率最高的 mvp 
        if h["win_rate"] > best_hero["win_rate"]:
            best_hero = h

    avg_win_rate = total_win_rate / len(heroes)
    return avg_win_rate, best_hero["name"]
#3. 调用函数并接受返回值
avg_rate,mvp = analyze_team(hero_list)

print("=== OW 战术小队综合分析 ===")
print(f"英雄池平均胜率:{avg_rate:.1f}%")
print(f"战术核心 MVP 英雄:【{mvp}】")

#4.自动写入战报
with open("team_log.txt","w",encoding="utf-8") as f:
    f.write(f"平均胜率:{avg_rate:.1f}%\nMVP:{mvp}\n")

print("分析完毕，战报已写入 team_log.txt!")