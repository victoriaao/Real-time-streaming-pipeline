#!/usr/bin/env python
# coding: utf-8

from pyspark.sql import functions as f
from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession


sc = SparkContext('local')
spark = SparkSession(sc)


#streaming json data to path
json_sdf = spark.readStream.json("/home/spark-stuff/stream_processing_wkld/data/json_files/")


#flatten data structure
flat_df = json_sdf.select("analytics.*", "datetime", "sales.*")


#send json stream to csv folder
write_to = flat_df.writeStream.option("checkpointLocation","checkpoints")\
        .option("header", "true")\
        .outputMode("append")\
        .format("csv")\
        .start("/home/spark-stuff/stream_processing_wkld/data/csv_files/")\
    .awaitTermination()




