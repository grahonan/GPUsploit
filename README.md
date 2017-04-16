# GPUsploit

The goal of GPUsploit is to discover buffer overflow bugs by statically analyzing CUDA source code. 

### Our contribution

There are many approaches to static buffer overflow detection, but one common approach requires programmers to add special annotations to their code [1]. GPUsploit doesn't require any such additions to CUDA source code, but does require a JSON-encoded graph of control flow and memory access. 

![dependencies](http://i.imgur.com/ByTtK0H.png "dependencies")
*Figure 1. Software dependencies for GPUsploit*

In this initial version of GPUsploit, we focus on the highest level of the pyramid depicted in Figure 1. Future work includes integrating GPUsploit with existing CUDA tokenizers and control flow analysis tools.


Created for CIS 601 at the University of Pennsylvania.

### Resources

In [2], the author demonstrates both a stack overflow and heap overflow with CUDA code. This source code formed the basis for much of our work. 

### References

[1] Larochelle, David, and David Evans. "Statically Detecting Likely Buffer Overflow Vulnerabilities." ACM Digital Library. USENIX Association, 13 Aug. 2001. Web. 16 Apr. 2017.

[2] A. Miele  "Buffer Overflow Vulnerabilities in CUDA: A Preliminary Analysis" Journal of ComputerVirology and Hacking Techniques, vol. 12, no. 2, pp. 113-120, May 2016.
