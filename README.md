# spark-s3-deltalake
Integrate S3 with DeltaLake

# Pre-requisites:
  * Spark disturbution version >= 2.4.5 (pre-built with user provided Apache Hadoop)
  * Apache Hadoop version >= 2.8.5
    - Extract hadoop distribution and setup HADOOP_HOME environment variable
    - Add hadoop bin in the PATH environment variable
    - Add export SPARK_DIST_CLASSPATH=$(hadoop classpath) in $SPARK_HOME/conf/spark-env.sh
  * delta-core_2.11-0.6.1.jar
  * hadoop-aws-2.8.5.jar
  * aws-java-sdk-core-1.10.6.jar
  * aws-java-sdk-s3-1.10.6.jar

# Run the spark job
```sh
sh run_deltalake_job.sh
```

