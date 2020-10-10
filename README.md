# 自学计算机科学

> 本项目参考了[TeachYourselfCS](https://github.com/keithnull/TeachYourselfCS-CN/blob/master/TeachYourselfCS-CN.md)以及[Coding Interview University](https://github.com/jwasham/coding-interview-university)，目标是为了掌握更加系统全面的知识。

我毕业于一所普通大学，信息管理与信息系统专业，但是大学没有好好学习，毕业后经亲戚介绍找了份普通的测试工作。机缘巧合下我接触并自学了Python，并因此找到了一份开发的工作。

我平时看的东西很杂，买了一堆技术书却总是看了前面的几章就换一本，直到现在也没有多少书是完整读完的，而且只熟悉一门Python语言，对很多知识都不太了解。我觉得是时候制定一个系统的学习计划并照做了，整体科目按照[TeachYourselfCS](https://github.com/keithnull/TeachYourselfCS-CN/blob/master/TeachYourselfCS-CN.md)中列出的来，但是书籍以及视频可能会有些个人的选择。
## 科目
| 科目                                      | 为何要学？                                                                             | 书籍及视频                                                                                                                                      |
|-------------------------------------------|----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| **[算法与数据结构](#算法和数据结构)**     | 如果你不懂得如何使用栈、队列、树、图等常见数据结构，遇到有难度的问题时，你将束手无策。 | _[《数据结构与算法：Python语言描述》](https://book.douban.com/subject/26702568/)_                                                                                |
| **[编程](#编程)**                         | 不要做一个“永远没彻底搞懂”诸如递归等概念的程序员。                                     | _[《计算机程序的构造和解释》](https://book.douban.com/subject/1148282/)_                                                                      |
| **[计算机架构](#计算机架构)**             | 如果你对于计算机如何工作没有具体的概念，那么你所做出的所有高级抽象都是空中楼阁。       | _[《深入理解计算机系统》](https://book.douban.com/subject/26912767/)_                                                                           |
| **[数学知识](#数学知识)**                 | 计算机科学基本上是应用数学的一个“跑偏的”分支，因此学习数学将会给你带来竞争优势。       | _[《计算机科学中的数学》](https://book.douban.com/subject/33396340/)_                                                                         |
| **[操作系统](#操作系统)**                 | 你所写的代码，基本上都由操作系统来运行，因此你应当了解其运作的原理。                   | _[《操作系统导论》](https://book.douban.com/subject/33463930/)_                                                                               |
| **[计算机网络](#计算机网络)**             | 互联网已然势不可挡：理解工作原理才能解锁全部潜力。                                     | _[《计算机网络：自顶向下方法》](https://book.douban.com/subject/30280001/)_                                                                   |
| **[数据库](#数据库)**                     | 对于多数重要程序，数据是其核心，然而很少人理解数据库系统的工作原理。                   | _[《Readings in Database Systems》](https://book.douban.com/subject/2256069/) （暂无中译本）_                                                 |
| **[编程语言与编译器](#编程语言与编译器)** | 若你懂得编程语言和编译器如何工作，你就能写出更好的代码，更轻松地学习新的编程语言。     | _[《Crafting Interpreters》](https://craftinginterpreters.com/)_                                                                                    |
| **[分布式系统](#分布式系统)**             | 如今，_多数_ 系统都是分布式的。                                                        | _[《数据密集型应用系统设计》](https://book.douban.com/subject/30329536/)_                                                              |
## 算法与数据结构
- 顺序表（不需要实现，只要理解即可）
  - [x] 两种布局方案：元素内置和外置
  - [x] 基本操作的实现
    - 创建和访问操作
    - 变动操作：加入元素
    - 变动操作：删除元素
  - [x] 各种操作的性质及优缺点
  - [x] 两种实现方式：一体式结构和分离式结构
    - 一体式结构：存储表信息的单元与元素存储区以连续的方式安排在一块 存储区里，几部分数据的整体形成一个完整的表对象
    - 分离式结构：表对象里只保存与整个表有关的信息（容量和元素个数），实际元素存放在另一个独立的元素存储区对象里，通过链接与基本表对象关联
  - [x] 动态顺序表：可以替换元素存储区，且不改变对象
  - [x] 存储区扩充策略：