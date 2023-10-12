# Spotify ETL Data Engineering project using Python and AWS. 

### Overview 
In this project, An ETL(Extract,Load,Transform) data pipline is built using [Spotify API](https://developer.spotify.com/documentation/web-api) and AWS. Data will be extracted from Spotify API using Python and then transformed into Python objects via AWS Lambda. Later on, data will be load into AWS Analytics Services. 

### Architecture
![img](https://user-images.githubusercontent.com/88946343/273404722-7a7378fb-8478-4501-a271-dc04e76526ae.jpg)

### How does it work? 

EventBrigde Trigger(every day at midnight) => Run Lambda Function(extraction) => Store Raw Data => Trigger Transform Lambda Function => 
Tranform Data and Load => Querry Data using Athena.

### Technology used
- **S3(Simple Storage Service):** Stores data extracting from Spotify API in _.cvs_ format.
- **AWS Lambda:** Hosts and triggers Python script for pulling data and transforming data. There are two lambda functions in this project, the first one runs at midnight every day thanks to _EventBridge_ event to get data and put it into _S3 Bucket_. After this event, the second lambda function fires off and begins tranforming data, then delivers data to another folder in _S3 bucket_..
- **Glue Crawler:** Crawls data and converts into SQL tables after transformed data is coming.
- **Data Catalog:** Repository and stores SQL tables.
- **Athena:** Views tables and excutes SQL queries.

### Install packages

```
pip install -r requirements.txt
```
