# KDC Datasets


```{warning}
For the next few months, "KDC" can mean one of two things:
- Kellogg Data Center (Microsft SQL Server)
- Kellogg Data Cloud (Amazon Web Services)
```

The Kellogg Data Center will be retired this Summer. At that time, the acronym "KDC" will take on a single meaning, and will refer simply to the <span style="color:purple">*Kellogg Data Cloud*</span>.
```

```{admonition} How does this change things?
Accessing data will be similar, but the underlying infrastructure will be different. The Kellogg Data Cloud is a cloud-based data storage and compute environment. The cloud environment will offer many advantages in scalability, computating resources, and cost.

The one extra step is authenticating yourself with Duo Mobile to AWS, using netid and password. Email [Kellogg Research Support](mailto:rs@kellogg.northwestern.edu) for assistance.
```

## Kellogg Data Center

*  The [Kellogg Data Center](https://www.kellogg.northwestern.edu/research-support/computing/kellogg-data-center.aspx) is a Microsoft SQL Server relational database management system that is currently available to Kellogg faculty and students.

![Data Workflow](images/data-pipeline-sql-server.png)
- KDC is accessible from a *SQL* client. This could be a dedicated SQL client, such as [Datagrip](https://www.jetbrains.com/datagrip/) or [Microsoft SSMS](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver16) or many, many other choices
- It could also be a programmatic connection via [ODBC](https://en.wikipedia.org/wiki/Open_Database_Connectivity), with implementations available in most programming languages (Python, R, Stata, etc).

* Here is a snapshot of Datagrip with a connection set up to the Kellogg Data Center:

```{image} ./images/kdc-ssms-snapshot.png
    :alt: datagrip-snapshot
    :width: 700px
    :align: center
```

* Here is an example of how to set SQL Server connection parameters for Datagrip:

```{image} ./images/kdc-connection-settings-datagrip.png
    :alt: datarip-connection-settings
    :width: 400px
    :align: center
```

## Kellogg Data Cloud

```{note}
The [Kellogg Data Cloud](https://nu-sso.awsapps.com/start/#/) is a cloud-based data storage and compute environment.  We are currently focused on using Amazon Web Services (AWS), though we will probably expand to other cloud providers in the future. Within AWS, we will primarily rely on [AWS Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html) for querying data, though other application and software tools are also available.

![Data Workflow](images/data-pipeline-aws.png)
```

```{admonition} Athena Marketing Copy
> [Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html) carries out queries simultaneously, so even queries on very large datasets can be obtained within seconds. Due to Athena’s distributed, serverless architecture, it can support large numbers of users and queries, and computing resources like CPU and RAM are seamlessly provisioned.
```

* Like Microsoft SQL Server, AWS Athena allows for the use of SQL clients and ODBC-based connections from software. Here is an [ODBC example notebook](https://github.com/rs-kellogg/data-the-right-way/blob/main/comscore-project/comscore-odbc.ipynb) for Python. R and Stata can also be used to directly connect to Athena.
* Athena has an advantage over KLC of being able to handle larger datasets.
* The Athena web-based query console removes need to install and connect through a 3rd party tool such as Datagrip. However, you can still use tools if that is your preferred mode.

* Here is an example of how to set AWS Athena connection parameters for Datagrip:

```{image} ./images/aws-connection-settings-datagrip.png
    :alt: datarip-connection-settings
    :width: 400px
    :align: center
```


```{admonition} Benefits of moving to the cloud
Moving data to the cloud unlocks a huge toolset for data processing, including handling of very large scale datasets, image processing, text processing, and GPUs for deep learning.
* Example: firing up an EC2 instance with GPUs for machine learning [AWS Deep Learning AMIs](https://aws.amazon.com/releasenotes/aws-deep-learning-ami-catalog/)
* Example: Running Apache Spark to handle very large scale data workloads.
* Example: Sagemaker notebooks for rapid spinnning up of machine learning environments, including GPUs

![Data Workflow](images/aws-console-home.png)
```


