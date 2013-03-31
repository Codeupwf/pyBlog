---
layout: post
title: "Vim个人用配置"
date: 2013-03-31 23:15:58
comments: true
categories: Vim
---

### Vim 个人用配置

	"语法高亮
	if has("syntax")
	  syntax on
	endif
	"显示行号
	set nu

	"修改默认注释颜色
	hi Comment ctermfg=DarkCyan

	"允许退格键删除
	set backspace=2
	"S启用鼠标
	set mouse=a
	set selection=exclusive
	set selectmode=mouse,key

	"侦测文件类型
	filetype on
	"载入文件类型插件
	filetype plugin on
	"为特定文件类型载入相关缩进文件
	filetype indent on

	"设置高亮搜索
	set hlsearch
	"在搜索时，输入的词句的逐字符高亮
	set incsearch

	"按C语言格式缩进
	set cindent
	"设置Tab长度为4格
	set tabstop=4
	"设置自动缩进长度为4格
	set shiftwidth=4
	"继承前一行的缩进方式，特别适用于多行注释
	set autoindent
	"显示括号匹配
	set showmatch
	"括号匹配显示时间为1(单位是十分之一秒)
	set matchtime=1

	"增强模式中的命令行自动完成操作
	set wildmenu
	"不要生成swap文件，当buffer被丢弃的时候隐藏它
	setlocal noswapfile
	set bufhidden=hide


### 存放位置

将以上内容保存为`.vimrc`文件，并保存在`~/`目录下，即用户根目录下。		
我的存放位置如下：
![my config file][p1]

[p1]: https://lh6.googleusercontent.com/-ld9j4KknEHI/UVhY4uIZKnI/AAAAAAAAAmk/WtqKYe3-Fiw/s684/vimrc.png "my vim config file .vimrc"