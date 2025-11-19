## AWS DATA SCIENCE AND ENGINEERING UPSKILL 

# RESOURCE 1: https://www.youtube.com/watch?v=6G0bLDIcO7Y

# NOTES
## TYPES OF DATA
- Structured Data[ organized ina predefined maner, searchable, stored in a tabular formats, fields are descrete and defined] eg. msql, postgres, amazon redshift.
- Unstructured Data[Lacks predefined organized maner, not easily searchabble, wide variety of data types and formats] eg. text documents, audio files, video files, social media posts, emails. 

- Semi structured Data types[elements of both structured and unstructured data, does not neatly fit tabular format, has some organizational properties, uses tags or markers to structure data] eg. xml files, json, nosql database html.

# PROPERTIES OF DATA [3 V's]
- Volume[Scale or quantity being generated, stored or processed, 
 itrequires storage. 
    Chalenges: storage management, processing power, Data integration 
    ]
- Velocity [speed of data generation, transmitted and processed. 
 Challenges: real-time processing, latency
 ]
- Variety[defined by the diversity of data, source and formats.
    Challenges: Data integration, Data Quality, Interoperability.
    ]


# DATA WAREHOUSE
- A centralized repo that stores structured data from multiple sources
Components 
- Schema-on-write
- Stores structured data
- fast query performance 
- ensures data integrity and consistency. 

# SNOW FLAKE

# DATA LAKE
- A centralized repo to store data, both structured and unstructured at any scale.
- its schema-on-read
- stores all data types
- Highly scalable
- Allows for data exploration and experimentation

# services to create a data lake
- s3
- Apache Hadoop
- ms data lakehouse


# Datalake House
- Combines data lakes and data warehouse to provide a unified data platform
- Real-time dta analytics
- minimizes data movements and duplication
- schema-on-read and schema-one-ewrite

# DATA MESH
- it decentralizes the approach to manage and access large-scale data in an organization
- it aims to address some of the limitations of traditional centralizd data architecture models by treating data as a product and forstering domain-oriented data ownership.

- Creates a central repo so that data can be used for various purposes in teams like finance, sales, operations.
Challenges: 
- siloed data
- slow responsne

# DATA MESH PRINCIPLES
- Data ownership
- Data as a product 
- Self serve platform 
- Federal decision making model.

# ORCHESTRATIONS IN DATA ENGINEERING
- Refers to the automated coordination and management or complex data workflows of complex data workflows and processes. eg. aws step functions, apeche airflow

# COMMON DATA FORMATS
- CSV
- JSON
- XML
- APACHE PARQUET[used in data lakes]

# common data sources
- Databases
- Data warehousee
- Data lakes
- Flat files [csv files]


# DATA MODELING
- Conceptual Data Model
- Logical Data Model
- Physical Data Model

# DATA LINEAGE
- involes tracking the flow of dta through and org systems and processes

# Schema Evolution
- The process of managing changes to the schema of a database or data structure over time

# Data Sampling
- A statistical technique used to select a subset of data from a larger dataset
- Population and sample 
- Sampling Frame
- Sampleing Error
- Sample Size

# Data Skewness
Refers to the asymemerty in the distribution of data values around the mean

Data Validataion[ Ensures data is acurate, consistent and meets predefined criteria or rules.] 
- Data Profiling[It analysis and understand the characteristics, structure and quality of data within a dataset. 
]

## AWS GLUE
- Fully managed ETL service 
- A spark ETL engine
- Consists of a Central Metadata Repo- Glue Data Catalog
- Flexible Scheduler

## GLUE DATA CATALOG
 - Persistent Metadata Store[
    - Its a managed service that lets you store, annotate, and share metadata which can be used to query and transform data.
 ]
 NOTE: the metadata information is Data Location, Schema, Data Types, Data Classification.

 ## AWS Glue Tables
- The metadata definition that represents your data. The data resides in its original store. This is just a representation of the schema.

## AWS GLUE CRAWLERS
 A Crawler is a program that connects to a data store (source or target), progresses through a prioritized list of classifiers to determine the schema for your data, and then creates metadata tables in the AWS Glue Data Catalog