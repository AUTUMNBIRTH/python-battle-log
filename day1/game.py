3 < 4
"""true"""
5 < 3 
"""false"""


counts = 3
while counts > 0:
    temp = input("guess maths:")
    guess = int(temp)

    if guess == 8:
        print("666666")
        print("nb")
        break
    else:
        if guess < 8:
            print("笑了")
        else:
            print("打了，fw")
    counts = counts - 1
"""必须并列"""

print("game over")

"""循环语句还有while"""

counts = 3
while counts > 0:
    print("asdasdasda")
    counts = counts - 1
"""运行了三次"""
import random
random.randint(1,10)
"""random演示"""
import random

counts = 3
answer = random.randint(1,10)
while counts > 0:
    temp = input("guess maths:")
    guess = int(temp)

    if guess == answer:
        print("666666")
        print("nb")
        break
    else:
        if guess < answer:
            print("笑了")
        else:
            print("打了，fw")
    counts = counts - 1
print("game over")

"""攻击随机数"""
x = random.getstate()
print(x)

random.randint(1,10)
random.randint(1,10)
random.randint(1,10)
random.randint(1,10)
random.randint(1,10)
random.randint(1,10)
random.randint(1,10)
random.randint(1,10)


random.setstate(x)
random.randint(1,10)
random.randint(1,10)
random.randint(1,10)
random.randint(1,10)
random.randint(1,10)
random.randint(1,10)
random.randint(1,10)
random.randint(1,10)
"""结果会得到和之前一样的结果！"""


import random
answer = random.randint(1,10)
counts = 3
while counts > 0:
    temp = input("mathes = ")
    guess = int(temp)
    if guess == answer:
        print("66666")
        break
    else:
        if guess < answer:
            print("笑了")
            print("once again")
        else:
            print("打了")
            print("fw")
        counts = counts - 1
        
print("game over!!!")