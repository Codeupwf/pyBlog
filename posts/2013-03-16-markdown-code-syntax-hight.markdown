---
layout: post
title: "Markdown + Pygments实现代码高亮"
date: 2013-03-16 13:30:46
comments: true
categories: Markdown
---
#####一、示例

如下Markdown源码（注意不要再用缩进进行代码块标记了）	

	```c
	#include <stdio.h>
	int main(int argc,char *argv[])
	{
	    int n;
	    scanf("%d",&n);
	    if ( n>4 ) {
	        printf("HH");
	    } else {
	        printf("hello");
	    }
	    return 0;
	}
	```

会被高亮显示为如下：
```c
#include <stdio.h>
int main(int argc,char *argv[])
{
    int n;
    scanf("%d",&n);
    if ( n>4 ) {
        printf("HH");
    } else {
        printf("hello");
    }
    return 0;
}
```
--more--
#####二、详细说明

以前用wordpress写博客的时候，使用的是SyntaxHighlighter插件实现的代码高亮。	
现在换成python自建博客了，原来的插件就不能用了。研究了两天后终于搞清楚了怎么用markdown包自带功能进行代码高亮了。

用到的是Markdown模块的两个个扩展`codehilite`和`fenced_code`，默认包含在了Markdown模块中，`codehilite`依赖`pygments`模块实现的，需要先安装[`pygments`][3]。

源码如下：
```python
import markdown
......
ret['content'] = Markup(markdown.markdown(content,extensions=['codehilite(guess_lang=False)','fenced_code']))
```

+ [codehilite扩展][1]使用pygments实现了高亮操作，附带参数`guess_lang=False`是为了在不标示代码类型时不让pygments猜测语言类型并高亮。	
+ [fenced_code扩展][2]实现了强制边界控制，只有在三个`` ` ``反引号之间的内容才会被当做代码进行解析。



[1]: http://pythonhosted.org/Markdown/extensions/code_hilite.html "codehilite"
[2]: http://pythonhosted.org/Markdown/extensions/fenced_code_blocks.html "fenced_code"
[3]: http://pygments.org/ "Pygments"