# KLC Datasets

* The Kellogg Linux Cluster ([KLC](https://www.kellogg.northwestern.edu/research-support/computing/kellogg-linux-cluster.aspx)) is a cluster of Linux servers that is available to Kellogg faculty and students.

* KLC is part of [Quest](https://www.it.northwestern.edu/departments/it-services-support/research/computing/quest/index.html) Northwestern's High-Performance Computing (HPC) cluster.


![Data Workflow](images/data-pipeline-klc.png)

* With KLC, the data exist as files on disk -- there is no generic way (like SQL) to load and query the data. Instead, we need to write code to load the data into memory, and then query it. This offers a huge amount of flexibility, but it requires some programming.
* KLC nodes have a lot of RAM, so you can usually load big chunks of data into memory with no issues (caveat: shared resource means you still have to be careful).
* KLC nodes have many cores, so you can do parallel processing of data where possible (you are allowed up to 24 cores at one time).
* What kinds of program you write depends on the *format* of the data files. There is no single format. Some are text-based (CSV, JSON, XML), some are binary (Parquet, Avro, ORC).
* [There is a KRS github project](https://github.com/rs-kellogg/edgar2data) that provides a good example for how to process EDGAR documents (plain text + XML) to extract relevant information.

```{image} ./images/data-formats.png
    :alt: data-formats
    :width: 500px
    :align: center
```
