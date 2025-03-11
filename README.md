# Hadoop-Apache_Project
Project : Log Analysis and Anomaly Detection Using Hadoop-MapReduce, and Apache Spark
About project :
Well various company utilizes server that run a special service. A service which logs events to the system log.
However, logging is not enough. This data is crucial for company as well as developer's.
company : wishes to secure, and optimize their operation by system monitoring.
developer's : They wish to know how thier software is used and how they can improve it.
Hence, these critical information requires proper storage and processing and eventually a good visulization and 
anomaly detection of the processed data.
Here are two crucial framework of this project : Apache Spark and hadoop.
# Data storage and preprocessing.
The log data contains multiple fields like timestamps, username, ticket ID, etc. Which might be unnecessary.
This log data can be huge as it generates with every action and hence forth might be costlier or not memory-
efficient if utilize spark. hence I prefer the MapReduce of hadoop to preprocess the data efficently. 
With preprocessing the raw log data is converted to a meaningful and structured data. The proccess is as such:
log-data collection (in our case synthetic log-data) ----> Passed to MapReduce jar file ----> part--r-00000 file generated
this file --converted--> CSV file (error ranking, user_data)
# Anomaly Detection and Visulaziation of Data.
The result is stored in hdfs and processed using Apache Spark.
There are certain criteria that helps to figure out the anomalies type and eventually flag it.
This criteria utilizes the past data, error ratio, etc. More about criteria in Rules.txt file.

# About Myself : 
I am aspiring software engineer who has hands on experience in implementing algorithms and data structures. 
My greatest strength is problem-solving and I have talent for optimizing code efficiently. I am passionate about 
AI, Big Data, and building scalable solutions, and I value continuous learning and teamwork.
