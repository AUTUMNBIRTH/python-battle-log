import datetime

def show_header():
    """打印控制台战术抬头"""
    print("=" * 45)
    print("   🛡️  ANNA TACTICAL COMMAND CONSOLE v1.0  🛡️   ")
    print("=" * 45)

def record_daily_log():
    """录入每日战报数据"""
    print("\n[!] 开始录入今日战术数据：")
    
    # 1. 数据采集
    weight = float(input("请输入当前体重 (kg): "))
    steps = int(input("请输入今日行走步数: "))
    
    # 2. 战术状态计算
    step_target = 10000
    completion_rate = (steps / step_target) * 100
    
    status = "🟢 达标" if steps >= 8000 else "🔴 需补充巡航"
    
    # 3. 格式化战报文本
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_content = f"""
========================================
[战报时间]: {now}
[体重数据]: {weight} kg
[巡航步数]: {steps} 步 (目标完成度: {completion_rate:.1f}%)
[战术评估]: {status}
========================================
"""
    print(log_content)
    
    # 4. 数据持久化（写入本地文件）
    with open("daily_command_log.txt", "a", encoding="utf-8") as f:
        f.write(log_content)
    
    print("[✓] 战报已成功持久化写入 daily_command_log.txt！")

# --- 主程序入口 ---
if __name__ == "__main__":
    show_header()
    record_daily_log()