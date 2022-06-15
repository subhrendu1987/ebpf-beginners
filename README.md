# Notes From Subhrendu
## ebpf Installation in Ubuntu 22.04 (Do not worry if some packages are unavailable)
  * `sudo apt install python3 ipython3 python3-pip`
  * `sudo apt install bpfcc-introspection bpftrace bpfcc-tools`
  * `sudo pip3 install pyebpf bpfcc`

  

## Useful Repos for eBPF sources and examples
  * [iovisor] (https://github.com/iovisor/bcc.git)
  * [cilium] (https://github.com/cilium/ebpf)
  * [Docs] (https://www.kernel.org/doc/html/latest/userspace-api/ebpf/syscall.html)
# Notes from Liz Rice (Original maintainer of the repo)
## The Beginner's Guide to eBPF
Notes from Liz Rice

_New report "What is eBPF?" now available for [download from Isovalent](https://isovalent.com/ebpf/) or with your subscription to [O'Reilly's learning platform](https://www.oreilly.com/library/view/what-is-ebpf/9781492097266/)_

Several presentations and repos that help you get started with eBPF programming

* The Beginners Guide to eBPF Programming as seen at [eBPF Summit 2020](https://ebpf.io/summit-2020/) 
  * ebpf.py in this repo is the code I write during that talk
  * [slides](https://speakerdeck.com/lizrice/liz-rice-beginners-guide-to-ebpf)
  * [YouTube](https://youtu.be/lrSExTfS-iQ)
  * You'll find more Python code examples in [this gist](https://gist.github.com/lizrice/47ad44a15cce912502f8667a403f5649)

* The Beginners Guide to eBPF Programming in Go 
  * This example using `libbpfgo` library is [here](https://github.com/lizrice/libbpfgo-beginners).
  * [YouTube](https://youtu.be/uBqRv8bDroc) 

* At [eBPF Summit 2021](https://ebpf.io/summit-2021) I wrote an eBPF load balancer from scratch - this is all in C
  * [Load balancer code](https://github.com/lizrice/lb-from-scratch)
  * [YouTube](https://youtu.be/L3_AOFSNKK8)

* For Cloud Native eBPF Day I've written some examples showing some of the ways eBPF programs can get involved with networking 
  * [Slides](https://speakerdeck.com/lizrice/beginners-guide-to-ebpf-programming-for-networking)
  * [Code](https://github.com/lizrice/ebpf-networking)
  * YouTube link coming soon
 
* eBPF Superpowers presentation at DockerCon 
  * [Slides](https://speakerdeck.com/lizrice/ebpf-superpowers)
  * [YouTube](https://youtu.be/4SiWL5tULnQ) 

* Packet counting example added for [O'Reilly Superstream "What's next for Infrastructure and Operations?"](https://learning.oreilly.com/live-events/infrastructure-ops-superstream-series-whats-next-for-infrastructure-and-operations/0636920054193/0636920054192/)
  * Examples: ebpf.py & packet.py 
