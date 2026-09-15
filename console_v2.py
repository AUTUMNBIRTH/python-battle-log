import datetime
import os

def show_header():
    """打印控制台战术抬头"""
    print("\n" + "=" * 45)
    print("   🛡️  ANNA TACTICAL COMMAND CONSOLE v2.0  🛡️   ")
    print("=" * 45)

def get_valid_float(prompt):
    """鲁棒性输入校验：浮点数"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ [错误]: 请输入有效的数字（如 92.4）！")

def get_valid_int(prompt):
    """鲁棒性输入校验：整数"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ [错误]: 请输入有效的整数步数（如 9000）！")

def record_daily_log():
    """录入每日战报数据"""
    print("\n[!] 开始录入今日战术数据：")
    
    weight = get_valid_float("请输入当前体重 (kg): ")
    steps = get_valid_int("请输入今日行走步数: ")
    
    step_target = 10000
    completion_rate = (steps / step_target) * 100
    status = "🟢 达标" if steps >= 8000 else "🔴 需补充巡航"
    
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_content = f"""========================================
[战报时间]: {now}
[体重数据]: {weight} kg
[巡航步数]: {steps} 步 (目标完成度: {completion_rate:.1f}%)
[战术评估]: {status}
========================================
"""
    print("\n" + log_content)
    
    with open("daily_command_log.txt", "a", encoding="utf-8") as f:
        f.write(log_content + "\n")
    print("[✓] 战报已成功持久化写入 daily_command_log.txt！")

def view_history_logs():
    """查看历史战报日志"""
    print("\n[!] 正在调取历史战报档案...")
    if not os.path.exists("daily_command_log.txt"):
        print("⚠️ 暂无历史日志文件，请先录入战报！")
        return
    
    with open("daily_command_log.txt", "r", encoding="utf-8") as f:
        logs = f.read()
        print(logs if logs.strip() else "⚠️ 日志文件为空！")

def main_menu():
    """控制台主菜单循环"""
    while True:
        show_header()
        print("1. 录入今日战术数据")
        print("2. 查看历史战报档案")
        print("3. 退出战术控制台")
        
        choice = input("\n请选择战术动作 (1/2/3): ").strip()
        
        if choice == "1":
            record_daily_log()
        elif choice == "2":
            view_history_logs()
        elif choice == "3":
            print("\n[!] 战术控制台已安全关机，指挥官请休息！")
            break
        else:
            print("❌ 无效指令，请输入 1、2 或 3！")

if __name__ == "__main__":
    main_menu()