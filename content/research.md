+++
title = "Research"
layout = "single"
+++

## Research

Our work sits at the intersection of parallel computing and AI systems. Below are some of the projects we build and contribute to.

- **[UnifyFS](https://github.com/LLNL/UnifyFS):** A specialized burst buffer parallel file system for supercomputers. UnifyFS manages node-local fast storage devices (e.g., SSD and NVMe) and provides a unified view for applications. Applications (e.g., AI workloads and scientific simulations) can use UnifyFS just as they would traditional global file systems, requiring no code changes. UnifyFS was awarded the 2024 [R&D 100 Award](https://software.llnl.gov/news/2024/08/08/rd100/)!

- **[DYAD](https://github.com/flux-framework/dyad):** A data streamer optimized for producer-consumer workloads, enabling consumers to retrieve data directly from producers via RDMA, bypassing costly file system interactions. Like UnifyFS, DYAD can utilize node-local storage devices and has demonstrated significant improvements in I/O bandwidth for AI applications.

- **[Recorder](https://github.com/uiuc-hpc/Recorder):** A comprehensive parallel I/O and tracing library, initially developed for our study on HPC I/O characterization and storage system consistency. Recorder collects detailed information about I/O calls, MPI calls, and their parameters, enabling analysis that existing tracing tools could not provide. It captures near-lossless information across the entire HPC I/O software stack, including POSIX, MPI-IO, HDF5, NetCDF, and PnetCDF.

- **[VerifyIO](https://github.com/uiuc-hpc/Recorder/tree/dev/tools/verifyio):** VerifyIO addresses the challenges posed by user-level parallel file systems that deviate from POSIX semantics to improve performance. These systems often define their consistency semantics informally, complicating correctness verification for applications. VerifyIO provides a formal framework for specifying storage semantics and uses a trace-driven approach (leveraging Recorder traces) to verify correctness.

- **[MPI Standard](https://www.mpi-forum.org) Revision:** While working on VerifyIO, we uncovered several consistency issues in production-level I/O libraries. Further investigation revealed that these issues stemmed from the strict specifications of the MPI Standard, particularly regarding the `MPI_File_sync` call. To address these limitations, we lead an effort within the MPI-I/O working group to revise the MPI Standard, aligning it more closely with the needs of modern I/O libraries and next-generation storage systems.

- **[Pilgrim](https://github.com/pmodels/pilgrim):** Pilgrim traces all MPI calls (over 400 functions per MPI Standard 4.0) along with their parameters and compresses the trace online using a novel pattern-recognition-based algorithm. Compared to state-of-the-art MPI tracing tools, Pilgrim captures more information while using less storage. Most of Pilgrim's features have since been merged into Recorder, which can now be used for both MPI and I/O tracing.
