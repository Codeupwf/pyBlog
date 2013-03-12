---
layout: post
title: "Markdown语法学习 Part1"
date: 2013-03-11 00:59:17
comments: true
categories: Markdown
---

#### 一、段落和换行

段落由一个或多个连续的文本组成，由段落前后的一个或多个空行分割开。

段落内文本的换行由上一行末尾的两个以上空格以及回车组成。

#### 二、标题

底线标 `===` 表示 `<h1>`   
底线标 `---` 表示 `<h2>`  
ps:底标线要是连续的符号

行首插入1到6个  `#` 表示 `<h1>` 到 `<h6>`

#### 三、引用

区块引用使用行首的 >角括号表示，可以再引用块中每行都加角括号或者只在整个段落的第一行最前加上角括号
e.g.

	A First Level Header
	====================
	A Second Level Header
	---------------------

	Now is the time for all good men to come to
	the aid of their country. This is just a
	regular paragraph.

	The quick brown fox jumped over the lazy
	dog's back.
	### Header 3

	> This is a blockquote.
	> 
	> This is the second paragraph in the blockquote.
	>
	> ## This is an H2 in a blockquote


输出 HTML 为：

	<h1>A First Level Header</h1>
	<h2>A Second Level Header</h2>
	<p>Now is the time for all good men to come to
	the aid of their country. This is just a
	regular paragraph.</p>
	<p>The quick brown fox jumped over the lazy
	dog's back.</p>
	<h3>Header 3</h3>
	<blockquote>
	<p>This is a blockquote.</p>
	<p>This is the second paragraph in the blockquote.</p>
	<h2>This is an H2 in a blockquote</h2>
	</blockquote>

#### 四、强调

在要被强调的内容前后增加`*`和`_`。

`*XX*`

会被翻译成

`<em>XX</em>`

`_XX_`

会被翻译成

`<strong>XX</strong>`

当连续两个`*`包括内容时会被翻译成`<strong></strong>`

e.g. 

`**XX**`

会被翻译成

`<strong>XX</strong>`

#### 五、列表

1）无序列表使用星号、加号、减号在行首标记并与内容中间有一个空格

	* Candy
	* Gum
	* Booze

和

	+ Candy
	+ Gum
	+ Booze

以及

	- Candy
	- Gum
	- Booze

都会被翻译为

	<ul>
	<li>Candy</li>
	<li>Gum</li>
	<li>Booze</li>
	</ul>

2）有序列表使用数字加一个英文句点在行首，并与内容中间一个空格

	1. Red
	2. Green
	3. Blue

会被翻译为

	<ol>
	<li>Red</li>
	<li>Green</li>
	<li>Blue</li>
	</ol>

列表中包含多个段落时段落开始都必须缩进4空格或1制表符

ps：行首只要出现【数字\-句点\-空白】，就会翻译成项目列表，要避免这种情况需要在句点前加上反斜杠【\\】

	1986. What a great season

前面的【1986\-句点\-空白】会被翻译成列表项。  
正确的写法是：

	1986\. what a great season

#### 六、代码区块

首先需要说明的是代码区和代码块是不一样的。

+ 代码区是用`<pre><code></code></pre>`标签包起来的内容
+ 代码块是用`<code></code>`标签包起来的内容

先说代码区：

Markdown中建立代码区非常简单，只需要简单的在代码前缩进4个空格或1个制表符即可。

	这是普通段落

		这是一段代码区

会被翻译为：

	<p>这是普通段落</p>

	<pre><code>这是一段代码区
	</code></pre>

一个代码区块会一直持续到没有缩进的那一行（或是文件结尾）。

再来说说代码块：

代码块与代码区类似，不过代码区无法与普通段落在一行中显示，而代码块可以与普通段落混杂显示。	
Markdown中建立代码块只需要在代码前后添加`` ` ``（即数字键1左侧那个点，又叫反引号）即可。

#### 七、分割线

你可以在一行中用三个以上的星号、减号、底线来建立一个分隔线，行内不能有其他东西。你也可以在星号或是减号中间插入空格。下面每种写法都可以建立分隔线：

	***
	* * *
	---
	- - -
	___
	_ _ _


