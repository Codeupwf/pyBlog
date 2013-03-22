
# Codeup-Blog

Codeup-Blog 是[Codeup][3]在学习Python过程中，借鉴[MartianZ][1]和[YANG Yang][2]同学的博客系统，进行融合加工，并增加了我自己的理解以及修改。

[1]: https://github.com/MartianZ "MartianZ"
[2]: http://yangyangin "YANG Yang"
[3]: https://github.com/Codeupwf "Codeup"

### 依赖：

	python 2.6 +
	pip

	pip install flask
	pip install markdown
	pip install PyRSS2Gen

	同时注意根目录下的requirements.txt文件，此文件同样包含依赖的组件。
	主要有uWSGI和pygments

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

目前本博客架设在OpenShift上，详细架设方式请参考[YANG Yang][1]的博文介绍

[1]: http://yangyang.in/article/2013-01-26-setting-a-py27-environment-on-openshift-diy-app-type "在 OpenShift 平台上自定义 Python 2.7 运行环境"
