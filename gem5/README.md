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

使用Scons编译gem5, Scons根据`SConstruct`文件来进行编译. 通过命令行可以指定编译参数，比如示例中为:

```python
python3 `which scons` build/X86/gem5.opt -j9
```

编译完成后会得到一个gem5的可执行文件`build/X86/gem5.opt`

gem5 binary types：
- `debug`: debug symbols, no optimization, slow
- `opt`: most optimization, debug symbols, faster
- `fast`: all optimization, no debug symbols, fastest and much smaller

## Configure gem5
set up a configuration script to model a system 

编译gem5得到的binary文件以一个python脚本为参数，来构建系统，为系统模块指定参数和运行simulation

### SimObjects
gem5的模块化设计是通过SimObject类型实现的，大多数组件都是SimObjects: CPUs, caches, memory controllers, buses等等

gem5 exports all of these objects from their C++ implementation to python

基于此，就能够使用python脚本实现SimObject的创建，参数设置和模块交互，基本步骤如下:

1. import the `m5` library and all SimObjects compiled
2. 例化system设置时钟域，时钟频率和电压域
3. 配置存储器(大小、时序), 创建CPU，总线，cache，I/O
4. 设置仿真运行的客户程序与仿真process
5. 例化system与simulation并执行
6. 在命令行运行simulation: 如`build/X86/gem5.opt configs/tutorial/part1/simple.py`

### gem5 ports
gem5使用了端口抽象(封装)，每个memory对象都有两种类型的端口: `request ports`和`response ports`, 在连接时将request port连接到response port(利用等号赋值的方式连接，与顺序无关)

### full system vs syscall emulation
gem5 有两种运行模式: `syscall emulation(SE)`and`full system(FS)`modes
- FS: 仿真(emulate)整个硬件系统并且运行一个未修改过的内核，类似运行虚拟机
- SE: 主要关注CPU和memory系统，仿真Linux系统调用，只能建模user-mode代码

### baseCPUs
gem5 提供的CPU以`{ISA}{Type}CPU`的方式命名. 例如, 一个RISCV Minor CPU为RiscvMinorCPU
- Valid ISAs: Riscv, Arm, X86, Sparc, Power, Mips
- Valid CPU types: AtomicSimpleCPU, O3CPU, TimingSimpleCPu, KvmCPU, MinorCPU

## Add cache to the configuration script
### Classic cache and Ruby
gem5有两套完全不同的子系统来对系统的cache进行建模，取决于是否修改cache coherence protocal/cache coherence protocal对系统性能影响, 作者画了个饼以后会将两者合并:)
- calssic: 简单且不够灵活的MOESI一致性协议
- Ruby: 能够细致地建模cache coherence

cache的SimObject声明在`src/mem/cache/Cache.py`中，其中定义了我们可以设置的参数. 许多cache的参数没有默认值，需要在`m5.instantiate()`前指定

## gem5 statistics and output
除了simulation脚本的输出，在`m5out/`下还有三个输出文件: 
- `config.ini`: 包括每个创建的SimObject以及对应的参数值，用于确认系统及其参数
- `config.json`: 内容与`config.ini`一致，json格式
- `stats.txt`: simulation记录的所有gem5数据的文本表示，首先包含总的执行数据，接着是SimObject的数据，值得关注的数据有sim_seconds(simulated time for the simulation), sim_insts(the number of instructions committed by the CPU), host_inst_rate(the performance of gem5).

## default configuration scripts
所有关于gem5的配置脚本都在`configs/`, 一些有用的:
- `boot/`: 与FS mode有关的rcS文件
- `common/`: 一些helper脚本和函数帮助创建simulation
- `dram/`: 测试DRAM的脚本
- `example/`: 开箱即用的gem5配置脚本，尤其是`se.py`和`fs.py`
- `network/`: HeteroGarnet网络的配置脚本
- `ruby/`: Ruby和缓存一致性协议的配置脚本