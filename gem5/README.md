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
set up a configuration script to model a system 

编译gem5得到的binary文件以一个python脚本为参数，来构建系统，为系统模块指定参数和运行simulation

在`configs/examples`中有一些配置脚本的示例参考

#### SimObjects
gem5的模块化设计是通过SimObject类型实现的，大多数组件都是SimObjects: CPUs, caches, memory controllers, buses, etc.

gem5 exports all of these objects from their C++ implementation to python

基于此，就能够使用python脚本实现SimObject的创建，参数设置和模块交互，基本步骤如下:

1. import the `m5` library and all SimObjects compiled
2. 例化system设置时钟域，时钟频率和电压域
3. 配置存储器(大小、时序), 创建CPU，总线，cache，I/O
4. 设置仿真运行的客户程序与仿真process
5. 例化system与simulation并执行
6. 在命令行运行simulation: 如`build/X86/gem5.opt configs/tutorial/part1/simple.py`

#### gem5 ports
gem5使用了端口抽象(封装)，每个memory对象都有两种类型的端口: `request ports`和`response ports`, 在连接时将request port连接到response port(利用等号赋值的方式连接，与顺序无关)

#### full system vs syscall emulation
gem5 有两种运行模式: `syscall emulation(SE)`and`full system(FS)`modes
- FS: 仿真(emulate)整个硬件系统并且运行一个未修改过的内核，类似运行虚拟机
- SE: 主要关注CPU和memory系统，仿真Linux系统调用，只能建模user-mode代码

#### baseCPUs
gem5 提供的CPU以`{ISA}{Type}CPU`的方式命名. 例如, 一个RISCV Minor CPU为RiscvMinorCPU
- Valid ISAs: Riscv, Arm, X86, Sparc, Power, Mips
- Valid CPU types: AtomicSimpleCPU, O3CPU, TimingSimpleCPu, KvmCPU, MinorCPU