# KDC Datasets

*  The [Kellogg Data Center](https://www.kellogg.northwestern.edu/research-support/computing/kellogg-data-center.aspx) is a Microsoft SQL Server relational database management system that is currently available to Kellogg faculty and students.

![Data Workflow](images/data-pipeline-sql-server.png)

```{warning}
KDC (Kellogg Data Center) will be retired this Summer. At that time, the acronym "KDC" will take on a new meaning, and will refer to the The <span style="color:purple">*Kellogg Data Cloud*</span>.
```

```{image} ./images/sql-server-2-aws.png
    :alt: sql-server-2-aws
    :width: 500px
    :align: center
```


*  The [Kellogg Data Cloud](https://nu-sso.awsapps.com/start/#/) is a cloud-based data storage and compute environment. Currently we are focused on using Amazon Web Services (AWS) for storage and compute, though we may expand to other cloud providers in the future. We will focus on using [AWS Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html) for querying data in the Kellogg Data Cloud.

![Data Workflow](images/data-pipeline-aws.png)

```{admonition} How does this change things?
:class: tip
Accessing data will be similar, but the underlying infrastructure will be different. The Kellogg Data Cloud is a cloud-based data storage and compute environment. The cloud environment will offer many advantages in scalability, computating resources, and cost.
```

* There are many similarities between these two systems, including the ability to use SQL clients and ODBC-based connections from software like R, Python, and Stata. The cloud-based version has the advantage of being able to handle larger datasets, and allowing us to take advantage of the many tools available in the cloud.

* Example: firing up an EC2 instance with GPUs for machine learning
