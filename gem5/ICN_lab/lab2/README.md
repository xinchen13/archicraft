# Topology Comparison
- compare a Mesh (called `Mesh_XY` in Garnet), `Flattened-Butterfly`, and a `hierarchical ring` topology for network performance
- design space exploration: run a suite of simulations for of these three topologies and plot the results

sample run command
```sh
./build/Garnet_standalone/gem5.opt configs/example/garnet_synth_traffic.py \
--network=garnet \
--num-cpus=16 \
--num-dirs=16 \
--topology=Mesh_XY \
--mesh-rows=4 \
--sim-cycles=5000000 \
--inj-vnet=0 \
--router-latency=2 \
--injectionrate=0.02 \
--synthetic=uniform_random \
--link-width-bits=32
```

- all packets are 64-bits wide: the number of flits in every packet = (packet_size / link width)
- run Uniform Random (--synthetic=uniform_random), Tornado (--
synthetic=tornado) and Neighbor (--synthetic=neighbor) traffic for all the designs
- the details of each traffic pattern can be seen in `src/cpu/testers/garnet_synthetic_traffic/GarnetSyntheticTraffic.cc`
- start at a (packet) injection rate of 0.02, and keep incrementing in intervals of 0.02 till the network saturates
- for each (configuration, traffic pattern) pair, plot the average packet latency vs. injection rate for all three topologies on the same graph: Mesh, Flattened Butterfly and Hierarchical ring