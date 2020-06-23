#!/bin/bash
JOB_HOME=spark-s3-deltalake
OPT_JARS=jars/hadoop-aws-2.8.5.jar,jars/aws-java-sdk-core-1.10.6.jar,jars/aws-java-sdk-s3-1.10.6.jar
arg1='file://'"${HOME}"'/'"${JOB_HOME}"'/job_config.yml'
sp_job=deltalake_job.py

$SPARK_HOME/bin/spark-submit --jars $OPT_JARS $sp_job $arg1
