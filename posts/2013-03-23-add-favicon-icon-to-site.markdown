---
layout: post
title: "为自己的网站添加图标Icon"
date: 2013-03-23 23:40:07
comments: true
categories: Web
---

### 为自己的网站添加图标

我这里说的图标是指网站在收藏夹或者标签页中标题左侧的小图标。	
至于图标的制作这里就不说了，随便找东西搞一下就可以。

图标的尺寸最好是16*16或者32*32 256色，个人推荐16*16，因为太大了没有用。	

添加图标的方式有两种：

1. 直接将图标文件存为favicon.ico，然后上传到网站所在服务器的根目录下。通常即为与index.html放在一起。

2. 在页面的`<HEAD>`标签之间增加link指向，举例如下：

		<head>
			<link rel="Shortcut" href="http://example.com/favicon.ico">
		</head>

	其中的`href`可以指向任何ico文件，也可以使用本站的相对路径。	
	使用这个方法可以为不同的页面指定不同的图标文件。
