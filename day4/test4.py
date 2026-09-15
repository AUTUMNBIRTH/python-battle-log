#1.定义评估函数
def evalulate_hero(hero_name,win_rate,kd_ratio):
    if win_rate >= 55 and kd_ratio >= 2.0:
        status = "上分密码"
    else:
        status = "练枪英雄"
    return f"【{hero_name}】胜率:{win_rate}%,KD:{kd_ratio} -> 战术判定: {status}"

print("=== OW 战术档案录入系统 ===")

#2.循环录入
while True:
    hero = input("\n请输入英雄名称(输入 q 退出):")
    if hero.lower() == 'q':
        print("战术档案录入完毕,准备出征!")
        break
    # 获取数据并转换类型
    win_rate = float(input("请输入胜率(例如 58.5):"))
    kd = float(input("请输入 kd 比(例如 2.3):"))

    # 调用函数获取评估成果
    result = evalulate_hero(hero,win_rate,kd)
    print(result)

    #.用 with 追加写入本地日志文件
    with open ("ow_log.txt","a",encoding="utf-8") as f:
        f.write(result + "\n")
        print("已保存至 ow_log.txt!")