---
layout: post
title: "Unix系统下CTRL-Z和CTRL-C的区别"
date: 2014-08-22 23:38:32
comments: true
categories: Unix,CMD
---

###Unix系统下CTRL-Z和CTRL-C的区别

平时在命令行下执行命令的时候，都是习惯用CTRL-Z或者CTRL-C来退出当前执行的命令，比如正在Ping XXX的时候想要退出等。
只知道通过CTRL-Z和CTRL-C都能实现退出当前执行命令的功能，但是两者的区别却并不清楚，今天查了下资料才搞清楚。

####首先是相同点：     
CTRL-Z和CTRL-C都是中断命令，都能够中断当前正在执行的命令。

####然后是不同点：     
+ **CTRL-C**：CTRL-C是强制中断命令，执行此命令后，原正在执行的命令被强制结束，进程退出。   
+ **CTRL-Z**：CTRL-Z是中断并挂起命令，执行此命令后，原正在执行的命令被中断并挂起在后台，进程未退出。后续可以通过`fg`或者`bg`命令恢复指令，`fg`继续前台执行，`bg`继续后台执行。  

--more--

####举例： 
当你正在使用Vim编辑某个脚本时，需要查看下系统某个目录下的文件名称，可以通过先CTRL-Z到命令行环境，`ls`查看完之后再`fg`恢复Vim环境继续编辑脚本。

[示例图片][p1]

[p1]:http://ww3.sinaimg.cn/mw690/6b995d17gw1ejlw707sc5g20i00c5b2a.gif
