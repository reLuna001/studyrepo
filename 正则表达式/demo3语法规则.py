# 开发时间：22/9/2022 下午4:07
'''
a,b,c,d,1,2,3......     字符常量，写什么就是什么
\d                       一个数字
\D                      一个非数字字符
\s                       一个空格
\S                       一个非空格
\w                       一个任意字母数字下划线字符
\W                       一个除了字母数字下划线之外的任意字符
[abef]                   a,b,e,f中的任意一个字符
[a-e]                    范围：从a-e中任意一个字符
[^a-e]                   取反：从a-e之外的任意一个字符
[\b]                    退格符号
.                       统配符：除了换行\n之外的任意一个字符（最大，包含的范围最广
'''


'''
下面再在上面的条件下加入数量
*              0或者多个
+              1或者多个
？              0或者1个
{2}              2个
{2,5}           2到5个
{2，}            至少2个
{，5}            最多5个
'''

#组合模式
#\d{6}[a-z]{6}   表示为6个数字之后跟着6个小写字母
#   |        表示为或者
#   （）   表示为一个小组    （abc）{3}表示为abcabcabc


'''
限定模式出现的位置，比如行首，行尾，或者特定的字符之后。
^          表示为在字符串的开头
\A         表示在字符串的开头，并且忽略跨行标记
$          表示在行尾
\Z           字符串行尾，忽略跨行标记
\b          必须在 单词边界   举例：123\b    在abc用于123中
\B          不能在单词的边界
（？=。。。）  匹配目标必须出现在。。。之后的位置   举例：(？=9527)\w
(?!=...)     匹配。。。不出现在之后的位置
(?<=...)     匹配...出现在之前的位置
(?<...)      匹配。。。不出现在之前的位置
(?()|)       条件语句

'''
# text='密码:9527,wode mingzishi '
# import re
# print(re.findall(r'(?<=密码.)\d+',text))



#分组
'''（。。。）       捕获一个组
（？P<Y>....）   捕获的组名为Y
（？：。。。）    不捕获的组
\Y           匹配第Y个匹配到的组
（？P=Y）       匹配名为Y的组
（？#。。。。）    给正则表达式加注释'''
