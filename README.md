# searchEngine
A portable web search engine with keywords recommend system

1.项目开发环境
Linux: Ubuntu18.04
G++: Version 4.8.4
Vim: Version 8.0

2.系统目录结构
src/：存放系统的源文件（*.cpp/*.cc） 。
Include/：存放系统的头文件（*.hpp） 。
bin/：存放系统的可执行程序
conf/myconf.conf：存放系统程序中所需的相关配置信息
data/dict.dat: 存放词典
data/dictIndex.dat: 存放单词所在位置的索引库
data/newripepage.dat：存放网页库
data/newoffset.dat：存放网页的偏移库
data/invertIndex.dat：存放倒排索引库
log/:存放日志文件

3.系统需求
3.1 系统运行过程图
![image](https://user-images.githubusercontent.com/65232041/222167469-d1935e8d-7f40-4d97-8544-adf029ff55e6.png)
