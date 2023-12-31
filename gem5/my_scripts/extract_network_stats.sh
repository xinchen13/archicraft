echo > m5out/network_stats.txt
grep "packets_injected::total" m5out/stats.txt | sed 's/system.ruby.network.packets_injected::total\s*/packets_injected = /' >> m5out/network_stats.txt
grep "packets_received::total" m5out/stats.txt | sed 's/system.ruby.network.packets_received::total\s*/packets_received = /' >> m5out/network_stats.txt
grep "average_packet_queueing_latency" m5out/stats.txt | sed 's/system.ruby.network.average_packet_queueing_latency\s*/average_packet_queueing_latency = /' >> m5out/network_stats.txt
grep "average_packet_network_latency" m5out/stats.txt | sed 's/system.ruby.network.average_packet_network_latency\s*/average_packet_network_latency = /' >> m5out/network_stats.txt
grep "average_packet_latency" m5out/stats.txt | sed 's/system.ruby.network.average_packet_latency\s*/average_packet_latency = /' >> m5out/network_stats.txt
grep "flits_injected::total" m5out/stats.txt | sed 's/system.ruby.network.flits_injected::total\s*/flits_injected = /' >> m5out/network_stats.txt
grep "flits_received::total" m5out/stats.txt | sed 's/system.ruby.network.flits_received::total\s*/flits_received = /' >> m5out/network_stats.txt
grep "average_flit_queueing_latency" m5out/stats.txt | sed 's/system.ruby.network.average_flit_queueing_latency\s*/average_flit_queueing_latency = /' >> m5out/network_stats.txt
grep "average_flit_network_latency" m5out/stats.txt | sed 's/system.ruby.network.average_flit_network_latency\s*/average_flit_network_latency = /' >> m5out/network_stats.txt
grep "average_flit_latency" m5out/stats.txt | sed 's/system.ruby.network.average_flit_latency\s*/average_flit_latency = /' >> m5out/network_stats.txt
grep "average_hops" m5out/stats.txt | sed 's/system.ruby.network.average_hops\s*/average_hops = /' >> m5out/network_stats.txt
echo >> m5out/network_stats.txt
cat  m5out/network_stats.txt