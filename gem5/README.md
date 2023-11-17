# gem5
gem5的简单上手教程

## Introduction
- a modular discrete event driven computer system simulator platform
- gem5’s components can be rearranged, parameterized, extended or replaced easily
- primarily in C++ and python
- designed for use in computer architecture research

入门资料: 官方documentation

#### WHY Simulator
<img src="./pictures/pic1.png" width="500" />

<img src="./pictures/pic2.png" width="500" />

## Build gem5
compile gem5 separately for every ISA that you want to simulate

使用Scons编译gem5, Scons根据`SConstruct`文件来进行编译

通过命令行可以指定编译参数，比如示例中为`python3 `which scons` build/X86/gem5.opt -j0`

编译完成后会得到一个gem5的可执行文件`build/X86/gem5.opt`

gem5 binary types：
- `debug`: debug symbols, no optimization, slow
- `opt`: most optimization, debug symbols, faster
- `fast`: all optimization, no debug symbols, fastest and much smaller

## Configure gem5
