---
layout: post
title: "C++Primer 笔记 12章 类"
date: 2010-09-04 19:02:17
comments: true
categories: C++,类,笔记
---

### C++Primer 笔记 12章 类

#### 12章 类

#####类的初始化：    

+ const成员的值必须在初始化列表中初始化，无法在构造函数的函数体重进行赋值。
+ 引用类型的成员也必须在初始化列表中初始化。
+ 没有默认构造函数的类类型成员也要在初始化列表中初始化。

#####构造函数的执行过程：

首先默认构造所有成员，使用初始化列表初始化成员变量，然后执行构造函数的函数体。
    
    所以那些无法进行赋值，或无法由系统自己初始化的成员必须在初始化列表中进行初始化。  
    初始化const和引用类型数据成员的唯一机会就是在构造函数的初始化列表中。

#####static成员的初始化

类中的static成员一般不能在类的定义体（一般就是声明）中初始化，相反的，static数据成员通常在定义时才初始化（通常在cpp中）。        
例外的是，用常量表达式初始化是可以在定义体中进行的，比如整型的const static数据成员可以再类的定义体中初始化。

```c++
class Account {
    public:
        static double rate() {return interestRate;}
        static const int interestRate = 30;
}
```
#####构造函数的隐式转化

类的构造函数有时会做自动转换。     
例如某函数Fun的形参是一个class对象，此class类型有一个只有一个string类型形参的构造函数，那么 Fun("This is a string!")是合法的。

执行过程如下：     

1. 首先调用class的只有一个string形参的构造函数和参数“This is a string!”来生成一个class临时对象。
2. 然后调用Fun函数，并将class临时对象作为参数传入。
3. 调用Fun函数后，将class临时对象销毁。

实际上，这与函数的本意是不相符的，我们应该尽量避免这种情况的发生。       
为此，我们可以使用`explicit`关键字来声明某构造函数不可用于隐式转换。使用explicit后将无法在任何情况下使用隐式转换，需要慎重使用。

```c++
class EXP {
    public:
        explicit EXP(const std::string &Name);
}
```