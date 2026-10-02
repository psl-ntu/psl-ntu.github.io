+++
title = "Research"
layout = "single"
+++

## Research

Our research sits at the intersection of high-performance computing, storage, and
AI systems. The projects below fall into three themes that build on one another,
and some are still in progress.

### Parallel I/O, Storage & File Systems

Much of our storage work began with a basic question: what consistency and semantics do HPC applications actually need? In [File System Semantics Requirements of HPC Applications](https://doi.org/10.1145/3431379.3460637), we studied real applications and found that most of them do not depend on the strict POSIX guarantees that file systems work hard to provide. We built on this in a later [TPDS paper](https://doi.org/10.1109/TPDS.2024.3391058) that gives formal definitions for the full range of consistency models parallel file systems use, and compares them side by side so the performance cost of each guarantee is explicit instead of guessed at.

Those findings shape the systems we build. [UnifyFS](https://github.com/LLNL/UnifyFS) is a burst-buffer file system that manages node-local SSD/NVMe and presents a unified view, so applications run without any code changes (the work received a 2024 [R&D 100 Award](https://software.llnl.gov/news/2024/08/08/rd100/)). [TangramFS](https://github.com/wangvsa/TangramFS) takes the idea further and lets applications pick the consistency model they need rather than pay for guarantees they never use.

Relaxing POSIX also makes correctness harder to reason about, so we build the tools to check it. [VerifyIO](https://github.com/uiuc-hpc/Recorder/tree/dev/tools/verifyio) uses the formal semantics above, together with execution traces, to verify whether a program actually follows the consistency rules of the file system it runs on. That work surfaced consistency problems that trace back to the MPI Standard itself, which is why we now help lead an [MPI Standard revision](https://www.mpi-forum.org) in the MPI-I/O working group. And to evaluate systems like these without the original application, which is often closed-source or too large to run end to end, [FBench](https://arxiv.org/abs/2606.30197) regenerates runnable proxy benchmarks from traces.

We also optimize I/O at runtime, not just at design time. [SmartIO](https://doi.org/10.1145/3731599.3767509) measures live I/O behavior with Recorder, predicts good configurations online, and applies them through auto-tuning, so the storage stack adapts to a workload instead of relying on one static setting.

### Systems for AI & Agentic Workflows

We work on the systems that run modern AI, starting with the data path. [DYAD](https://github.com/flux-framework/dyad) speeds up producer-consumer data movement in deep-learning training by streaming data directly between processes over RDMA and node-local storage, instead of routing everything through the global file system. Our study of [storage penalties in DL training](https://github.com/psl-ntu/nccl_io_bench) explains why that helps: when collective communication and parallel I/O share the same network fabric, they compete for it, and node-local staging removes both the DataLoader stalls and the all-reduce interference.

On the compute side, [HieraSparse](https://github.com/psl-ntu/HieraSparse) targets LLM inference. It maps a hierarchical, semi-structured sparsity pattern in the attention KV cache onto GPU sparse tensor cores, so that sparsity turns into real speedups in both the prefill and decode phases. We are continuing this line of work in two directions *(ongoing)*: building on HieraSparse to raise the quality of the sparse approximation, so we keep more accuracy at the same sparsity level, and developing complementary methods that compress the KV cache more aggressively, so longer contexts fit in less GPU memory.

**Ephemeris** *(ongoing)* tackles the I/O bottleneck in large-scale AI-for-Science training, where a small model is swept over a very large dataset for many epochs. Compute scales with node count but the shared file system does not, so it saturates and extra nodes stop helping. Ephemeris is a clairvoyant, multi-tier prefetching system that manages node-local SSD and DRAM as a cache and buffer over the file system. Because the SGD sampling sequence is fixed by its random seed, the whole access pattern is known before training starts, which lets Ephemeris compute an exact prefetch schedule and a provable capacity-versus-scale frontier: how much SSD and DRAM each node needs to keep GPUs from stalling. The goal is to push the zero-stall ceiling two to five times beyond today's systems.

Higher up the stack, we work on making agentic AI systems for auto-discovery and AI-for-science scale *(ongoing)*. As these pipelines grow, they run many interacting agents whose work is dynamic and hard to predict, which puts pressure on the orchestration and scheduling layers beneath them. We are building an orchestration layer for these workloads and studying exploration-aware scheduling, where the system accounts for how agents branch and explore instead of treating every task as fixed and independent. A recurring theme is algorithm-system co-design: shaping the exploration algorithm and the systems that run it together, so that scheduling, memory, and data-movement decisions reflect what the agents are actually trying to discover.

### Performance Tracing & Analysis

Everything above depends on being able to see what a system is actually doing, cheaply enough to leave the tracing on all the time. [Recorder](https://github.com/uiuc-hpc/Recorder) captures near-lossless traces across the whole I/O stack, including POSIX, MPI-IO, HDF5, NetCDF, and PnetCDF, recording calls and their parameters in far more detail than earlier tools. [Pilgrim](https://github.com/pmodels/pilgrim) does the same for MPI, tracing over 400 functions and compressing them online with a pattern-recognition algorithm so it captures more information in less space; most of its features have since been merged into Recorder.

These traces are the foundation for much of our other work. Our semantics and consistency studies, VerifyIO, FBench, and SmartIO all run on top of them.
