# Real-Time-Retail-Transaction-Pipeline-Using-Kafka-Spark-and-MongoDB
Data Engineering Project (Intermediate Level)

Project Title: Building a Real-Time Retail Transaction Pipeline Using Kafka, Spark, and MongoDB

Project Objectives Summary
The project aims to streamline DulexMall data workflows by building a seamless pipeline for ingesting, processing, and storing data. Interns will develop a real-time system using Kafka, Spark, and MongoDB and managed with Docker and Docker Compose. 

The project focuses on delivering actionable insights, enabling scalable infrastructure, and providing hands-on experience with cutting-edge data engineering tools while fostering collaboration through GitHub version control

Project Learning Opportunities
• Docker 
• API 
• Streaming Pipeline Development 
• Real Time Analytics 
• Error Handling .

Learning Skills 
• Streaming Data Pipelines 
• Data Transformation(ETL) 
• Programming/Scripting (Python,Bash)

Business Introduction
DulexMall. operates in the fast-paced retail industry, where real-time access to transactional insights is critical for optimizing operations,
inventory management, and customer engagement. Our success is fueled by the ability to swiftly analyze sales patterns, detect demand
fluctuations, and tailor customer experiences across our omnichannel platforms.

However, we currently face a major challenge with fragmented and delayed data processing workflows, which limits our
ability to react to live sales trends and inventory changes.

To address this, we are launching a data engineering initiative to build a seamless real-time retail transaction streaming pipeline using
Kafka for data ingestion, Apache Spark for real-time processing, and MongoDB for scalable storage of transactional records.

Additionally, we are integrating Docker and Docker Compose to streamline the deployment and management of our infrastructure, ensuring scalability, reliability, and faster collaboration across development teams.

Business problem
Inefficient Data Processing:
Slow and cumbersome data processing can lead to delays in generating insights, resulting in missed opportunities to engage with consumers effectively.

Disparate Datasets:
When data is stored in silos or is not integrated, it becomes challenging to obtain a holistic view of consumer behaviour. This fragmentation can
lead to inconsistent messaging and ineffective marketing campaigns

Limited Real-Time Analysis:
The inability to analyze data in real-time restricts the agency's capacity to respond quickly to market changes or consumer purchase. 
This lag can result in lost leads and diminished competitive advantage.

Inability to Scale:
As the volume of data grows, the current fragmented system may struggle to keep up, making it difficult for the agency to scale its
operations.

Rationale for the Project

Real-Time Data Ingestion: To develop a robust pipeline that continuously collects and streams
data from API using Kafka, ensuring minimal latency in data availability.

Data Processing and Analysis: To implement Apache Spark Streaming for real-time data
processing tasks, including text preprocessing, language detection, and sentiment analysis, using
machine learning models.

Data Storage and Security: To securely store processed data in a MongoDB NoSQL database,
ensuring data integrity and accessibility for future analysis.

Insight Generation: To enable organizations to derive actionable insights from real-time data,
facilitating informed decision-making in areas such as marketing, product development, and
customer engagement.

Aim of Objectives
Real-time Data Collection:
Establish a reliable mechanism to continuously fetch data from Reddit using the Reddit API and stream them into a Kafka topic

Efficient Data Processing:
Utilize Apache Spark Streaming to process the incoming data streams in real-time.

Data Storage:
Integrate MongoDB for persistent storage, enabling historical trend analysis and cross-platform correlation

Scalability:
Design the pipeline to be scalable, allowing for the handling of varying data volumes and ensuring system performance.

Tech Stack
GitHub:
Manages version control and collaboration for code, documentation, and project tracking, ensuring that all team members are aligned and can contribute effectively.

Spark: 
Utilized for processing large datasets in real-time, allowing for fast and scalable data transformations and analytics.
Python: 
Used for scripting data extraction, cleaning, and transformation processes, enabling efficient handling of data from various sources.

Kafka: 
Serves as the messaging system for building a real-time streaming data pipeline, facilitating the ingestion of data from Reddit.

MongoDB:
A NoSQL database that stores unstructured data, providing flexibility in managing diverse data formats during the ETL process.

Docker: 
Leveraged to containerize applications and services, ensuring consistent environments across development, testing, and production.

Draw.io: 
Utilized to create diagrams that outline data flow, architecture, and ETL process design, providing a visual representation of the system for better understanding and communication

Project Enhancement
To enhance project delivery and ensure a scalable, maintainable architecture, the following
components will be integrated into the data engineering workflow:
API Integration:
A dedicated RESTful API will serve as the primary data source for streaming structured retail transaction data. This API delivers JSON-formatted records in
real time, including transaction details such as store, customer, product, and payment information, which will feed directly into the Kafka ingestion layer.
API URI:
a. Docs: https://retails-api.amdari.io/docs:To check for the documentation
b. ReDoc: https://retails-api.amdari.io/redoc : To check for the documentation
c. Stream: https://retails-api.amdari.io/stream: API Endpoint for data stream..... (used)

GitHub:
GitHub will be used for version control and collaborative development. It enables seamless coordination among team members, ensuring codebase integrity, transparent change tracking, and efficient issue management through pull requests and code reviews.

Docker:
Docker will be used to containerize all core services including Kafka, Apache Spark, MongoDB, and the API client. This ensures consistent runtime environments across development and deployment stages, enhances portability, and simplifies service orchestration using Docker Compose. It also streamlines onboarding and supports scalable, modular deployment of the entire data pipeline.

Data Pipeline Architecture (view in file)
Resources:
Install Java 11jdk 
kafka installation using Docker & Docker-Compose 
Install Apache Spark 
Setup MongoDB connection, with Docker-compose
