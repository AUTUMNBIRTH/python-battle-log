#1.战术变量定义
name = "安娜"
weight = 92.4
steps = 19000

#2.格式化输出（f-string)
print(f"【战术战报】统帅:{name}")
print(f"今早空腹体重：{weight}kg")
print(f"今日计划巡航步数：{steps}步")

today_steps = 19000

if today_steps >= 18000:
    print("判定：今日属于高消耗远征，今晚准许畅玩ow！")
elif today_steps >= 12000:
    print("判定：今日属于基础巡航，代谢引擎运转正常。")
else:
    print("判定：今日属于战术休整日，注意控制盐分摄入。")


#记录近期的体重战果
weight_history = {
    "Day 1":94.1,
    "Day 2":93.1,
    "Day 3":92.8,
    "Day 4":92.4,
}

print("--- 体重暴落战报遍历 ---")
for day,record in weight_history.items():
    print(f"{day}的体重防线是：{record}kg")

#用with 打开/新建一个txt文件，完事后管家会自动关闭文件
with open("battle_log.txt","w",encoding="utf-8") as f:
    f.write("安娜战术日志:92.4开个突破大捷,python 破冰成功！\n")

print("文件写入完毕，去左侧文件树看看是不是多了一个 battle_log.txt!")
