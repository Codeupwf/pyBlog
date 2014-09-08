---
layout: post
title: "Unix 下的文件连接"
date: 2013-12-01 00:39:11
comments: true
categories: Unix CLI
---

### Unix 下的文件连接

#### 实例
今天因为某些原因，需要通过命令行来用sublime打开某个隐藏文件，但是sublime的命令并不在usr/bin目录下，所以无法使用简洁的命令行来打开某个文件。
后来查了一些资料，发现sublime text 2的命令行工具在这：

	/Applications/Sublime\ Text\ 2.app/Contents/SharedSupport/bin/subl

如果你不嫌麻烦的话，可以每次都用这个命令来打开文件

	/Applications/Sublime\ Text\ 2.app/Contents/SharedSupport/bin/subl XXX

其实我们可以通过Unix自带的文件连接功能，在`usr/bin`目录下创建一个`subl`的软连接文件，这样我们就可以直接通过命令行输入`subl XXX`来实现使用Sublime打开指定文件的目的。

先把创建软连接的命令写在这里：
	
	ln -s /Applications/Sublime\ Text\ 2.app/Contents/SharedSupport/bin/subl /usr/bin/subl

这样，我们就在`/usr/bin`目录下创建了一个`subl`文件，这个文件是一个指向`/Applications/Sublime\ Text\ 2.app/Contents/SharedSupport/bin/subl`的软连接。

	Codeup-Mac:bin Codeup$ ls -l grep subl
	-rwxr-xr-x  3 root  wheel  30096 10 24 20:09 grep
	lrwxr-xr-x  1 root  wheel     64 12  1 00:13 subl -> /Applications/Sublime Text
--more--

#### 文件连接

我们再回过头来解释一下创建文件连接的命令`ln`。

	ln [-Ffhinsv] source_file target_file
	-f 建立时，将同档案名删除。
	-i 删除前进行询问。
	-s 建立从 source_file到target_file的软连接。
	无可选参数 建立从source_file到target_file的硬链接。

我们主要关注最后两种情况：

1. ln -s a b 创建指向a的软连接文件b 软连接类似快捷方式的概念，文件内容实际只有一个指向源文件的链接。删除源文件后会导致软连接文件指向不存在的文件。软连接又叫*符号连接*。
2. ln a b    创建指向a的硬链接文件b 硬连接类似C++中的智能指针的概念，是对某个文件的计数引用。对硬连接文件的修改，会导致源文件的变化，所有对此文件的硬连接文件都会变化。当删除一个硬连接文件时，文件并不会真的删除，只有所有指向此文件的硬连接都被删除后，文件才会被删除（真的与智能指针的概念很类似）。

关于符号连接的更详细内容，参见[Wiki][1]     
ps: Mac系统下的替身，其实就是一种硬连接。

   [1]: http://zh.wikipedia.org/wiki/%E7%AC%A6%E5%8F%B7%E9%93%BE%E6%8E%A5 "符号链接"