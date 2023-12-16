# eecs-it-yourself

## 数字电路设计基础
数字集成电路设计

#### Verilog
- 基础语法: hdlbits, 牛客网
- 实现常用模块(进阶): api, iic, uart, fifo, sramfifo
- Clifford E. Cummings关于reset/状态机/fifo的文章

#### tools
- synopsys的vcs, verdi, dc, spyglass(有时间看中后端相关), 参考芯王国
- cadence

#### script language 
python, makefile, shell, perl

#### verification 
SystemVerilog, uvm了解, 设计也要懂简单的验证

#### protocols
axi, apb: Arm提供的AMBA Specification

#### toy projects
ahb2apb, apb_uart


## Architecture
#### reading materials
- 计算机组成与设计——软硬件接口
- 计算机体系结构量化研究方法
- 超标量处理器设计

#### courses 
- 体系结构: EECS151, CS61c

#### simulator 
- gem5: 尝试使用, 通过复现论文来入门
- 开源项目: NEMU, 了解模拟器的功能，并实现一个简单的模拟器

#### rtl design
- 开源项目: tinyriscv, Nuclei E203
- 一生一芯(乱序多发射超标量)
    1. 计算机系统结构基础，能够参加体系结构研究或参与高性能处理器开发
    2. 处理器设计，数字集成电路前后端流程与设计经验
    3. 体系结构模拟器


#### NoC
- 熟练使用体系结构模拟器进行建模
- 深入理解高性能体系结构的建模，Cache一致性与NoC

参考书: On-Chip Networks (2nd Edition)

`papers`: 加深对NoC研究的问题的理解:通过 abstraction + introduction + motivationn + background 搞懂文章究竟在解决什么问题, 其次才是了解方法细节

- The adaptive bubble router (JPDC’01)
- A case for bufferless routing in on-chip networks (ISCA’09)
- Ariadne: Agnostic reconfiguration in a disconnected network environment (ICPACT’11)
- DBAR: An Efficient Routing Algorithm to Support Multiple Concurrent Applications in Networks-on-Chip (ISCA’11)
- Static Bubble: A Framework for Deadlock-free Irregular On-chip Topologies (HPCA’17)
- Footprint: Regulating Routing Adaptiveness in Networks-on-Chip (ISCA’17)
- Pitstop: Enabling a virtual network free network-on-chip (HPCA’21)

`projects`: 使用gem5复现Pitstop(HPCA’21)



## other
了解编译器相关：硬件DSA编译器，IR，算法映射，llvm，B站lazyparser

CPU：cache，总线协议（SoC最重要的三部分，高性能CPU，高速接口，总线），vx达坦科技

手画格雷码计数器的电路图

了解DFT

https://github.com/shinezyy/micro-arch-training

岗位整理
