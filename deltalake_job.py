import os
import sys
sys.path.append("jars/delta-core_2.11-0.6.1.jar")
import yaml

from urllib.request import urlopen
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from delta.tables import *


if __name__ == "__main__":
	print(sys.argv[1])
	job_config = yaml.load(urlopen(sys.argv[1]))

	#
	spark = (SparkSession.builder
		.appName("s3-deltalake-app")
		.getOrCreate()
		)

	# setup config
	spark.sparkContext._jsc.hadoopConfiguration().set("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
	spark.sparkContext._jsc.hadoopConfiguration().set("fs.AbstractFileSystem.s3a.impl", "org.apache.hadoop.fs.s3a.S3A")
	spark.sparkContext._jsc.hadoopConfiguration().set("spark.delta.logStore.class", "org.apache.spark.sql.delta.storage.S3SingleDriverLogStore")
	spark.sparkContext._jsc.hadoopConfiguration().set("fs.s3a.access.key", job_config['s3']['access_key_id'])
	spark.sparkContext._jsc.hadoopConfiguration().set("fs.s3a.secret.key", job_config['s3']['secret_access_key'])

	# create delta table
	data = spark.range(0, 5)
	data.write.format("delta").save("s3a://test/delta-table")

	# read delta table
	df = spark.read.format("delta").load("s3a://test/delta-table")
	df.printSchema()
	df.show()

	spark.stop()
