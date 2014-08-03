
# Codeup-Blog

Codeup-Blog 是[Codeup][3]在学习Python过程中，借鉴[MartianZ][1]和[YANG Yang][2]同学的博客系统，进行融合加工，并增加了我自己的理解以及修改，系统的主要构架是MartianZ同学的，我做的修改主要是使用了不同的组件，并且增加了代码亮显的功能。

[1]: https://github.com/MartianZ "MartianZ"
[2]: http://yangyang.in "YANG Yang"
[3]: https://github.com/Codeupwf "Codeup"

### 依赖：

	主要依赖的是python相关，
	apt-get install python
	apt-get install python-pip

	注意根目录下的requirements.txt文件，此文件包含依赖的组件。
	主要有uWSGI和pygments、Flask等。
	可以通过pip install -r requirements.txt来批量安装.
	(注意有些组件的安装依赖c编译器，请保证服务器上有相关编译器。)

### 使用：

1. 将Markdown放在posts文件夹下，保证每个Markdown文件的开头有下面的标志区域

		---
		layout: post
		title: "Markdown语法学习 Part1"
		date: 2013-03-11 00:59:17
		comments: true
		categories: Markdown
		---

2. 执行start_exe.sh

目前本博客架设在OpenShift上，详细架设方式请参考[YANG Yang][4]的博文介绍

[4]: http://yangyang.in/2014/01/25/%E5%9C%A8-openshift-%E5%B9%B3%E5%8F%B0%E4%B8%8A%E8%87%AA%E5%AE%9A%E4%B9%89-python-27-%E8%BF%90%E8%A1%8C%E7%8E%AF%E5%A2%83/ "在 OpenShift 平台上自定义 Python 2.7 运行环境"

### 样例

我的博客[WangFu][5]。

[5]: http://blog.wangfu.info "Wang Fu"
