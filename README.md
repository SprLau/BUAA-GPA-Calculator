# 北航绩点计算器

> Last Update: Sat, Jan 29, 2022

该绩点计算器严格遵守[《北京航空航天大学2021-2022学年学生手册》](http://xsc.buaa.edu.cn/info/1074/3256.htm)中公布的计算公式。

----

## 写入成绩

1. 编辑`gradebook.txt`：

   对于每一科成绩，4行为一组：

   * 第一行：课程名称
   * 第二行：分数（百分制以及二级制为分数0～100；五级制为A对应优秀、B对应良好、C对应中等、D对应及格、E对应不及格）
   * 第三行：学分
   * 第四行：课程评分机制（`ord`：百分制；`bin`：两级制；`qua`：五级制）

   **一个例子**：

   ```
   数学分析
   92
   6
   ord
   博雅课程
   A
   0.5
   qua
   科研课堂
   93
   2
   bin
   ```

2. （*非必需）编辑`config.py`：

   按照规则，两级制评分不计入绩点计算；如果需要查看计入两级制评分的绩点结果，将`count_binary = False`修改为：

   ```python
   count_binary = True
   ```



## 计算绩点

### 命令行

打开终端运行：

```bash
python buaa_gpa.py
```

**一个例子**：

```bash
springs@MacBook-Pro BUAA-GPA-Calculator % python buaa_gpa.py
3.893676470588235
springs@MacBook-Pro BUAA-GPA-Calculator %
```

