
from pyspark.sql import functions as f
from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
from pyspark.sql.types import StructType as struct, IntegerType, StringType as String,TimestampType as Timestamp,StructField, DoubleType,DateType

sc = SparkContext('local')
spark = SparkSession(sc)

#specify schema
schema =           struct(
                [
                    StructField("clicks", IntegerType(), True),
                    StructField("quantity", IntegerType(), True),
                    StructField("datetime", Timestamp(), True),
                    StructField("impressions", IntegerType(), True),
                    StructField("total_price", DoubleType(), True)
                ]
            )

#agregates the csv data to sum every 5 minutes
csv_sdf = spark.readStream \
          .format('csv') \
          .option('header',True) \
          .schema(schema) \
          .load("/home/spark-stuff/stream_processing_wkld/data/csv_files/")

tumblingWindows = csv_sdf.withWatermark("datetime", "5 minutes") \
                .groupBy(
                f.window(f.col("datetime"), "5 minutes")).agg(f.sum("clicks").alias("aggregate_clicks"), 
                f.sum("impressions").alias("aggregate_impressions"), 
                f.sum("quantity").alias("aggregate_quantity"), 
                f.sum("total_price").alias("aggregate_tprice"))
        


#write aggregates to pq file
ready_data = tumblingWindows.writeStream.option("checkpointLocation","checkpoints1")\
        .option("header", "true")\
        .outputMode("append")\
        .format("parquet")\
        .start("/home/spark-stuff/stream_processing_wkld/data/parquet_files/")\
    .awaitTermination()

#print final aggregated data
import pandas as pd
pdf = pd.read_parquet('data/parquet_files', engine='pyarrow')

pdf.head()
