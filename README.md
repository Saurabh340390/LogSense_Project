# LogSense: Scalable Log Analysis & Anomaly Detection

# Overview

This project focuses on analyzing log files to extract meaningful insights, detect anomalies, and cluster users based on their behavior. It processes a synthetic log file containing success and error logs, making it easier for organizations and developers to understand software usage patterns. Additionally, it provides employers with a way to monitor log data for potential system-wide issues or security threats.
# Technologies Used

    Hadoop (HDFS & MapReduce) – Efficient data storage and preprocessing.
    Python – Data extraction and transformation.
    Apache Spark (PySpark) – Large-scale anomaly detection.
    K-Means Clustering – User behavior analysis and anomaly detection.
    Matplotlib & Seaborn – Data visualization for insights.

# Data Storage and Preprocessing

Log data consists of multiple fields such as timestamps, usernames, ticket IDs, etc., many of which may be redundant or unnecessary for analysis. Since log data grows exponentially with user activity, storing and processing it efficiently is critical. Instead of using Spark for preprocessing, which could be costly, I opted for Hadoop MapReduce to structure the data efficiently.
Processing Pipeline:

    Log Data Collection → Generated a synthetic log file with 1000+ entries.
    Preprocessing with MapReduce → The log data is passed through a MapReduce JAR file to filter and extract relevant details.
    Structured Data Generation → MapReduce outputs a part-r-00000 file, which is converted into CSV format:
        error_ranking.csv → Contains ranked error messages based on frequency.
        user_logs.csv → Captures user activity with counts of success and error logs.

# Anomaly Detection & Visualization

Once the structured data is stored in HDFS, Apache Spark is used to process and flag anomalies. The detection criteria are based on mathematical rules, helping identify unusual patterns such as:

    High error spikes → Possible system-wide failures.
    Users with no information logs → Potential misconfigurations or inactive accounts.
    Rare or critical errors → Potential security threats or software bugs.

For further insights, K-Means clustering is applied to group users based on behavior. The optimal number of clusters is determined using the Elbow Method, ensuring efficient anomaly detection and behavioral segmentation.

#About Me

I am an aspiring software engineer with hands-on experience in algorithms, data structures, and large-scale data processing. My strengths lie in problem-solving and code optimization. I am passionate about AI, Big Data, and scalable software solutions and believe in continuous learning and teamwork.
