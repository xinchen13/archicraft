# roadmap-4-digital-ic

## Universal
`EECS basics` 电路, C/C++, 信号处理, 通信, 计算机体系结构

`Verilog` hdlbits, 牛客网. 实现常用模块: api, iic, uart, fifo, sramfifo
- Clifford E. Cummings关于reset/状态机/fifo的文章

`tools` synopsys的vcs, verdi, dc, spyglass(有时间看中后端相关), 参考芯王国

`script language` python, makefile, shell, perl

`verification` SystemVerilog, uvm了解, 设计也要懂简单的验证

`protocols` axi, apb: Arm提供的AMBA Specification

`toy projects` ahb2apb, apb_uart


## Architecture
`reference`
- 计算机组成与设计——软硬件接口
- 计算机体系结构量化研究方法
- 超标量处理器设计

`courses` EECS151, CS61c

`simulator` gem5: 尝试使用, 通过复现论文来入门

`open sourse projects` nemu(模拟器), tinyriscv, Nuclei E203

`projects` 一生一芯(乱序多发射超标量)

### NoC
`reference`
- On-Chip Networks (2nd Edition): 了解NoC的基本概念和原理

`papers` 加深对NoC研究的问题的理解:通过 abstraction + introduction + motivationn + background 搞懂文章究竟在解决什么问题, 其次才是了解方法细节

- Pitstop: Enabling a virtual network free network-on-chip (HPCA’21)
