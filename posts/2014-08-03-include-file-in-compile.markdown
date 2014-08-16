---
layout: post
title: "头文件是如何参与编译的"
date: 2014-08-03 00:00:00
comments: true
categories: Unix CLI
---

###头文件是如何参与编译的

最近在看C语言的编译与链接的内部实现，这是比较基础的内容，但是又往往很容易被忽视，因为各种IDE尤其是VS的强大集成功能将编译和链接的实现给隐藏了。		

至于编译与链接的具体过程并非本文内容，本文实际要讲的是我在自学时发现的一个有趣内容，头文件的编译参与问题。		

有些文章说过头文件不参与编译，其实严格来说头文件是参与编译的。		
在预编译源文件的时候，凡是遇到#include<XX>的时候，就会把XX的文本内容全部复制到相应的位置。		
然后被编译的源文件其实是 【头文件文本内容】+【源文件文本内容】		

这有点宏定义的感觉~		

--more--

所以，下面这段代码是真的可以用的！

`abc.h`

```c	
1,2,3
```

`main.cpp`	
```c	
#include <iostream>
#include <string>

int main()
{
    int a[] = {
        #include "abc.h"
    };
	    for (int i = 0;i< 3;i++)
    {
        std::cout<<a[i]<<std::endl;
    }
		return 0;
}
```
![示例](http://codeup.org/wp-content/uploads/2012/12/%E5%A4%B4%E6%96%87%E4%BB%B6%E7%BC%96%E8%AF%91-1024x553.png)
