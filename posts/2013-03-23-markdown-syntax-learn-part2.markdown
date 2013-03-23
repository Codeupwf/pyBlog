---
layout: post
title: "Markdown语法学习 Part2"
date: 2013-03-23 22:29:19
comments: true
categories: Markdown
---

#### 八、链接

作为文章中很重要的一部分，链接是不可或缺的。	
Markdown支持两种形式的链接语法：*行内式*和*参考式*。	

不管用哪种方式，链接文字均用\[方括号\]来标记

1. *行内式*：
	要建立一个行内式的链接，只要在方块括号后面紧接着圆括号并插入网址链接即可，如果你还想要加上链接的 title 文字，只要在网址后面，用双引号把 title 文字包起来即可。	

		This is [an example](http://example.com/ "Title") inline link.	
		[This link](http://example.net/) has no title attribute.

	会产生：

		<p>This is <a href="http://example.com/" title="Title">an example</a> inline link.</p>
		<p><a href="http://example.net/">This link</a> has no title attribute.</p>

	其中的链接可以是绝对路径，也可以是相对路径。

2. *参考式*：
	参考式的链接是在链接文字的括号后面再接上另一个方括号，而在第二个方括号里面要填入用以辨识链接的标记：

		This is [an example][id] reference-style link.

	接着，在文章的任意处，你可以吧这个标记的链接内容定义出来：

		[id]: http://example.com/  "Optional Title Here"

	链接内容定义的形式为：
	* 方括号（前面可以选择性地加上至多三个空格来缩进），里面输入链接文字
	* 接着一个冒号
	* 接着一个以上的空格或制表符
	* 接着链接的网址
	* 选择性地接着 title 内容，可以用单引号、双引号或是括弧包着

	链接网址也可以用尖括号包起来：

		[id]: <http://example.com/>  "Optional Title Here"

	或者你也可以把title属性放到下一行，加一些缩进：

		[id]: http://example.com/longish/path/to/resource/here
			"Optional Title Here"

	链接识别标记可以有字母、数字、空白和标点符号，但是并不区分大小写。	
	*隐式链接标记*功能可以省略链接识别标记，这种情况下链接识别标记会视为就是链接内容，要用隐式链接标记只要在链接文字后面加上一个空的方括号。	
	比如，要让“Google”链接到 google.com 你可以简化书写如下：

		[Google][]

	然后定义链接内容：

		[Google]: htttp://google.com

	链接定义可以放在文件的任何位置，但是建议放置于段落结束后或文章结束后。在查找定义链接时从当前位置开始使用向下查询到的第一个匹配定义。

#### 九、图片

Markdown使用一种与链接极为类似的语法来标记图片，同样也分为*行内式*与*参考式*。

1. 行内式语法类似于如下：

		![Alt text](/path/to/img.jpg)
		![Alt text](/path/to/img.jpg "Optional title")

	详细叙述如下：

	* 一个惊叹号`!`
	* 接着一个方括号，里面放上图片的替代文字
	* 接着一个圆括号，里面放上图片的网址，最后还可以加上选择性的标题文字

2. 参考式的图片语法规则类似于如下：

		![Alt Text][id]

	其中\[id\]是图片参考的名称，图片参考的定义方式与链接参考标记

		[id]: url/to/image "Optional title attribute"

	到目前为止Markdown没有办法指定图片的宽高，如果必须的话请使用`<img>`标签。

#### 十、自动链接

Markdown支持以比较简短的自动链接形式来处理网址和电子邮件信箱，只要是用尖括号包起来，Markdown就会自动将其转换为链接，例如：

	<http://example.com/>

Markdown会转为：

	<a href="http://example.com/">http://example.com/</a>

邮件地址的自动链接转换类似，不过会先做一个编码转换，把文字字符转成 16 进位码的 HTML 实体，这样的格式可以糊弄一些不好的邮址收集机器人，例如：

	<address@example.com>

Markdown会转为：

	<a href="&#x6D;&#x61;i&#x6C;&#x74;&#x6F;:&#x61;&#x64;&#x64;&#x72;&#x65;
	&#115;&#115;&#64;&#101;&#120;&#x61;&#109;&#x70;&#x6C;e&#x2E;&#99;&#111;
	&#109;">&#x61;&#x64;&#x64;&#x72;&#x65;&#115;&#115;&#64;&#101;&#120;&#x61;
	&#109;&#x70;&#x6C;e&#x2E;&#99;&#111;&#109;</a>

这段文字其实就是一个可以点击的`[address@example.com]`的链接。

#### 十一、反斜杠

Markdown中的反斜杠实际就是转义字符，可以使有语法意义的字符不起作用。	
Markdown支持以下特殊字符的转义操作：

	\   反斜线
	`   反引号
	*   星号
	_   底线
	{}  花括号
	[]  方括号
	()  括弧
	<>	尖括号
	#   井字号
	+   加号
	-   减号
	.   英文句点
	!   惊叹号



##### 本文参考GitCafe上的[Markdown语法说明][1]。

[1]: https://gitcafe.com/riku/Markdown-Syntax-CN/ "Markdown语法说明"