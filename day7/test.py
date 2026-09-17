#python进阶综合练习，涵盖：正则匹配，生成器，集合去重，格式化输出
import re 
from collections import Counter

#模拟一段服务器的运行日志
LOG_DATA = '''
2026-09-18 10:00:01 [INFO] User '秋生' logged in successfully from 192.168.1.10
2026-09-18 10:00:05 [ERROR] Failed login attempt from 192.168.1.50
2026-09-18 10:01:12 [WARNING] Memory usage high: 85%
2026-09-18 10:02:20 [INFO] User '莉莉丝' except query 'SELECT * FROM magic'
2026-09-18 10:03:00 [ERROR] Database connection lost from 192.168.1.50
2026-09-18 10:04:15 [INFO] User '秋生' updated profile
'''

#1. 生成器函数：逐行解析日志，节省内存
def parse_log_lines(log_data):
    #正则表达式捕获：时间、日志级别、详细消息
    pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \[(\w+)\] (.+)"
    for line in log_data.strip().split('\n'):
        match = re.match(pattern,line)
        if match:
            timestamp,level,message = match.groups()
            yield {"time":timestamp,"level":level,"msg":message}

#2. 统计与分析逻辑
def analyze_logs(log_text):
    level_counter = Counter()
    ip_set = set() #使用集合去重，记录所有出现过的IP

    #提取IP的正则表达式
    ip_pattern = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"

    print("=== 开始解析日志数据 ===")

    #使用for循环遍历生成器
    for log in parse_log_lines(log_text):
        level_counter[log["level"]] += 1

        #查找消息中的IP地址

        ips = re.findall(ip_pattern,log["msg"])
        for ip in ips:
            ip_set.add(ip)

    return level_counter,ip_set

#3. 结果打印与解包
def main():
    #统计日志级别和涉及的IP
    counts,unique_ips = analyze_logs(LOG_DATA)

    print("\n--- 分析报告结果 ---")

    #字典与Counter的遍历
    print("【日志级别统计】")
    for level,count in counts.items():
        print(f"  - {level}: {count} 次")

    #集合遍历与lambda排序展示
    print("\n【涉及的独立IP地址列表】")
    sorted_ips = sorted(list(unique_ips),key=lambda x: [int(b) for b in x.split(".")])
    for ip in sorted_ips:
        print(f"  - IP: {ip}")

if __name__ == "__main__":
    main()
