x = 3
print(x)
你好 = 666
print(你好)
"""python可以用中文作为变量名"""
x = 3
y  = 5
y = x
print(y)
"""y输出是3，后赋值"""

x = 3
y = 5
x,y = y,x
print(x,y)
"""x,y就换了个值"""
print('i love china.')
print("i love ow")
"""这俩基本无差别，例如里面有 let's go,就多用 ”  """
print('"life is short,you need python"')




"""转义字符,反斜杠在字符前面"""
print('\"life is short,let\'s learn python.\"')

print("i love you,\nbut you.....")
"""换行符演示如上"""



"""转义字符演示下方"""
print("D:\three\two\one\now")
"""结果：     hree    wo 反斜杠 one"""
"""ow"""

print(r"D:\three\two\one\now")
"""这个r说明后面是原始字符串，只能当作原始字符，每个字符没特殊含义，反斜杠不能放到末尾，放到末尾说明还没结束"""
print("D:\\three\\two\\one\\now")
"""也可以多加点杠"""
"""还可以如下"""
poetry = """woyaowanyuanshen
asdasdasdasd
dasdasdasdasdas
dasd
asd
asd
asd
aadsdasdasdasdas
  
  
  """

print(poetry)

520 + 1314
"""1834"""
'520' + '1314'
"""5201314"""

print("我每天爱你三千遍！\n" * 3000)
"""竖着生成三千条hhh"""
