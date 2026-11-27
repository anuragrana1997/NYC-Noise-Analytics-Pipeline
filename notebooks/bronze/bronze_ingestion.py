# Databricks notebook source
import pyspark.sql.functions as F

source_path = '/Volumes/nyc_noise/bronze/raw_files'

df = spark.read.json(source_path)
bronze_df = (
    df.withColumn(
        "ingestion_date",
        F.current_timestamp()
    )
    .withColumn(
        "source_file",
        F.col("_metadata.file_path")
    )
)

(
    bronze_df.write
    .format("delta")
    .mode("append")
    .saveAsTable("nyc_noise.bronze.raw_complaints")
)

print("Bronze Ingestion Complete")