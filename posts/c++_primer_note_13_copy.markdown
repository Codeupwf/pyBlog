---
layout: post
title: "C++Primer 笔记 13章 复制控制"
date: 2010-09-06 20:02:17
comments: true
categories: C++,复制,笔记
---

### C++Primer 笔记 13章 复制控制

#### 13章 复制控制

#####复制构造函数：

复制构造函数就是接受单个类类型引用形参（通常用const修饰）的构造函数。该构造函数一般不应设置为`explicit`

e.g.:

```c++
class EXP
{
    public:
        EXP(); //default constructor
        EXP(const EXP&) //copy constructor
        //...
}
```
    复制构造函数的难点在于意识到需要复制构造函数

--more--

#####禁止复制：

为了防止复制，类必须显式声明其复制构造函数为private。一般来说，最好显示或者隐式定义默认构造函数和复制构造函数，如果定义了复制构造函数，那也必须定义默认构造函数。

#####三法则：

一般而言，如果类需要复制构造函数，那也会需要赋值操作符。实际上，应将这两个操作看做一个单元，如果需要其中一个，那我们几乎肯定需要另一个。

析构函数通常用于释放在构造函数或在对象生命期内获取到的资源。      
析构函数与复制构造函数或赋值操作符之间的一个重要区别是不管类是否定义了自己的析构函数，编译器都自动执行类中非 
static 数据成员的析构函数。

三法则：如果类需要**析构函数**，则它也需要**复制构造函数**和**赋值操作符**

#####实现：

编写自己的复制构造函数时，必须显式复制需要复制的所有成员对象，显式定义的复制构造函数不会进行任何的自动复制操作。

#####自身赋值：

在将自身对象赋值给自己时，赋值操作符的正确工作非常重要。        
保证自身赋值正确性的通用方法是显式检查对自身的赋值。在赋值操作符重载中如果有操作数的删除，如果不进行检查，可能会出现先删除，然后又将已经删除掉的数据赋值给操作数的情况，导致数据丢失。

#####智能指针

定义智能指针的通用技术是采用一个**使用计数**。智能指针类将一个计数器与类指向的对象相关联。使用计数跟踪该类有多少个对象共享同一指针。使用计数为 0 时，删除对象。使用计数有时也称为**引用计数**。 

每次创建类的新对象时，初始化指针并将使用计数置为 1。当对象作为另一
对象的副本而创建时，复制构造函数复制指针并增加与之相应的使用计数的值。
对一个对象进行赋值时，赋值操作符减少左操作数所指对象的使用计数的值（如
果使用计数减至 0，则删除对象），并增加右操作数所指对象的使用计数的值。
最后，调用析构函数时，析构函数减少使用计数的值，如果计数减至 0，则删除
基础对象。 

让智能指针负责删除共享对象，可以避免悬垂指针的出现。

```c++
int obj; 
HasPtr p1(&obj, 42); 
HasPtr p2(p1); // p1 and p2 both point to same int object
HasPtr p3(p1); // p1, p2, and p3 all point to same int object 

// private class for use by HasPtr only 
class U_Ptr{
    friend class HasPtr;
    int *ip;
    size_t use;
    U_Ptr(int *p):ip(p),use(1){}
    ~U_Ptr(){delete ip;}
};//这是一个计数类的示例。

/* smart pointer class: takes ownership of the dynamically allocated 
* object to which it is bound 
* User code must dynamically allocate an object to initialize a HasPtr 
* and must not delete that object; the HasPtr class will delete it 
*/ 
class HasPtr { 
public: 
    // HasPtr owns the pointer; pmust have been dynamically allocated 
    HasPtr(int *p, int i): ptr(new U_Ptr(p)), val(i) { } 
    // copy members and increment the use count 
    HasPtr(const HasPtr &orig): 
    ptr(orig.ptr), val(orig.val) { ++ptr->use; } 
    HasPtr& operator=(const HasPtr&); 
    // if use count goes to zero, delete the U_Ptr object 
    ~HasPtr() { if (--ptr->use == 0) delete ptr; } 
private: 
    U_Ptr *ptr; // points to use-counted U_Ptr class 
    int val; 
}; 

HasPtr& HasPtr::operator=(const HasPtr &rhs) 
{ 
    ++rhs.ptr->use; // increment use count on rhs first 
    if (--ptr->use == 0) 
    delete ptr; // if use count goes to 0 on this object, 
    delete it 
    ptr = rhs.ptr; // copy the U_Ptr object 
    val = rhs.val; // copy the int member 
    return *this; 
} 
```

在这里，首先将右操作数中的使用计数加 1，然后将左操作数对象的使用计
数减 1 并检查这个使用计数。像析构函数中那样，如果这是指向 U_Ptr 对象的
最后一个对象，就删除该对象，这会依次撤销 int 基础对象。将左操作数中的
当前值减 1（可能撤销该对象）之后，再将指针从 rhs 复制到这个对象。赋值
照常返回对这个对象的引用

    这个赋值操作符在减少左操作数的使用计数之前使 rhs 的使用计数加 1，从而防止自身赋值。
