# a simple tutorial for Garnet

run and modify Garnet as a stand-alone in gem5. Garnet models the interconnection network in gem5. It is cyclic accurate, implements the micro-architecture of on-chip router, and uses gem5 ruby memory system for topology and routing

### Garnet source file 
Garnet is written in C++ and uses python to pass the configuration parameters to the C++ objects. All the files are available in `src/mem/ruby/network/garnet/`. In this folder, the NoC and the router micro-architecture is implemented

### Compile and first run
to run Garnet as a stand-alone, compile it with the following command

```sh
scons build/Garnet_standalone/gem5.debug PROTOCOL=Garnet_standalone -j9
```

run gem5 using the `garnet_synth_traffic.py` configuration file with default configuration parameters

```sh
./build/Garnet_standalone/gem5.debug configs/example/garnet_synth_traffic.py 
```

### Configuration parameters
in general, all the configurations can be found in `config/` folder

most of the configuration parameters related to Garnet can be found in the following files and folders


- `configs/common/Options.py`: general configration parameters (i.e. number CPUs, directories, memory size, ... etc.)  
- `configs/network/Network.py`: network configuration parameters (i.e. router & link latency, routing algorithm, topology... etc.) 
- `configs/topologies/`: topologies are defined here
- `configs/example/garnet_synth_traffic.py`: template file, include configuration parameters related to a single run (i.e. traffic pattern type, injection rate, number of simulation cycles, ... etc.)


change any default value of any configuration parameter directly in the related configuration file or change it from command line as follows: `./build/Garnet_standalone/gem5.debug configs/example/garnet_synth_traffic.py [--configuration_name=value]`, e.g.

```sh
./build/Garnet_standalone/gem5.debug configs/example/garnet_synth_traffic.py \
--ruby --ruby-clock=1GHz \
--sys-clock=1GHz \
--mem-type=SimpleMemory \
--num-cpus=16 \
--num-dirs=16 \
--synthetic=bit_complement --injectionrate=0.200 --sim-cycles=100000 --num-packets-max=30000 --inj-vnet=2 \
--network=garnet --topology=Mesh_XY --mesh-rows=4 --vcs-per-vnet=2 --link-latency=1 --router-latency=1 \
--routing-algorithm=1
```

some parameters:

- [--num-cpus=16] number of CPU = 16
- [--num-dirs=16] number of cache directories = 16
- [--network=garnet] configure the network as garnet network
- [--topology=Mesh_XY] use `Mesh_XY.py` topology in `configs/topologies/`
- [--mesh-rows=4] number of rows in the network layout
- [--sim-cycles=100000] run simulation for 100000 cycles
- [--synthetic=bit_complement] traffic pattern
- [--injectionrate=0.200] injection rate
- [--vcs-per-vnet=2] number of VCs per vitrual network