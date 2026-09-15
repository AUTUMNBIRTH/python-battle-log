#记录一周步数
step_list = [13000,19000,7000,19000]
print("--- 检查超过1.5w步的暴走日 ---")
for step in step_list:
    if step >= 15000:
        print(f"找到高消耗日：{step}步！")



bmr = 1800 #基础消耗
walk_steps = 19000
burn_from_walk = walk_steps * 0.055 #粗略估算步数消耗
toal_burn = bmr + burn_from_walk

food_intake = 1500 #估算摄入
calorie_gap = toal_burn - food_intake

print(f"今日预估总消耗：{toal_burn:.0f}kcal")
print(f"今日战术热量缺口：{calorie_gap:.0f}kcal!")

#命令行交互
hero = input("请输入你今晚 ow 最想玩的英雄：")
print(f"战术部署：今晚使用【{hero}】在赛场上大杀四方！")