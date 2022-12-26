# 基本数据类型
## 整数类型
## 浮点数类型
## 复数类型
## 更多的数学函数
# 逻辑值
* 逻辑值仅包括true false
* 用来配合 if while 等语句做条件来判断
## 判断与真值
## 逻辑运算
and和or是双目运算，由两个逻辑类型真值进行运算
not是单目运算，作用于一个逻辑类型真值
优先级
* not > and > or
## 各种类型对应的真值
整数、浮点数和复数类型
* 0是false 所有非0都是true

字符串类型
* 空串 是 false 非空串是true

所有序列类型（包括字符串）
* 空序列是 false 非空序列都是true

空值none
* false

# 字符串
## 字符串常见操作
* len函数
* slice操作
* 删除空格
  
    str.strip:去掉字符串前后的所有空格，内部的空格不受影响
  
    str.lstrip:去掉字符串前部的所有空格
  
    str.restrip:去掉字符串后部的所有空格


* 判断字母数字
  
    str.isalpha:判断字符串是否全部由字母构成
  
    str.isdigit:判断字符串是否全部由数字构成
  
    str.isalnum:判断字符串是否仅包含字母和数字，而不含特殊字符

split 分割

join 合并

upper lower swapcase 大小写相关

ljust center rjust 排版左中右对齐

replace 替换子串

# 可变类型 不可变类型
## 不可变类型：一旦创建就无法修改数据值的数据类型

整型 浮点数 复数 字符串 逻辑值 元组

## 可变类型：可以随时改变的数据类型

列表 字典 集合
