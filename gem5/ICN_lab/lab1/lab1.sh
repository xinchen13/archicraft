#!/bin/bash

# init
value=0.02
echo "average packet latency" > m5out/uniform_random.txt

# 循环开始
for ((i=0; i<=48; i++))
do
    # 在这里执行你的指令，可以使用 $value 变量
    ./build/Garnet_standalone/gem5.opt configs/example/garnet_synth_traffic.py \
    --network=garnet \
    --num-cpus=64 \
    --num-dirs=64 \
    --topology=Mesh_XY \
    --mesh-rows=8 \
    --sim-cycles=1000000 \
    --inj-vnet=0 \
    --injectionrate=$value \
    --synthetic=uniform_random

    grep "average_packet_latency" m5out/stats.txt | awk '{print $2}' >> m5out/uniform_random.txt

    # grep "average_packet_latency" m5out/stats.txt | sed 's/system.ruby.network.average_packet_latency\s*/average_packet_latency = /' >> m5out/uniform_random.txt
 
    # 递增变量 value，使用 bc 进行浮点数运算
    value=$(echo "$value + 0.02" | bc)
done
