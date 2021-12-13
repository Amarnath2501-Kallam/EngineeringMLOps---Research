# Machine Learning As A Service - MLaaS

**End-To-End MLOps Delivery & Excellence** 

MLOps is a systematic approach to building, deploying, and monitoring machine learning (ML) solutions. It is an engineering discipline that can be applied to various industries and use cases. It brings together data engineering, ML, and DevOps in a streamlined fashion. it is modular and flexible and can be used to build proofs of concept or to operationalize ML solutions in any business or industry

**This workflow is segmented into two modules :**
  * MLOps pipeline (build, deploy, and monitor) – the upper layer
  * Drivers: Data, code, artifacts, middleware, and infrastructure – mid and lower layers

<img width="1000" alt="Screenshot 2021-12-10 at 15 39 38" src="https://user-images.githubusercontent.com/61119710/145600614-cde8cd98-cf40-4c30-98f5-e61cd51c1add.png">

# Data preprocessing

Raw data cannot be directly passed to the ML model for training purposes. We have to refine preprocess the data before training the ML model. To further analyze the imported data, we will perform a series of steps to preprocess the data into a suitable shape for the ML training. We start by assessing the quality of the data into a suitable shape for the ML training. We start by assessing the quality of the data to check for accuracy, completeness,reliability,relevance,and timeliness. After that we calibrate the required data which is ideal for ML training. Lastly, we will analyze the correlations and time series, and filter out irrelevant data for training ML models.

# Machine learning Pipelines

<img width="949" alt="Screenshot 2021-12-13 at 12 17 10" src="https://user-images.githubusercontent.com/61119710/145810798-1008de88-0cbe-446b-8a01-7ee69ca75603.png">

As shown in the figure a comprehensive ML pipeline consists of the following steps
  * Data ingestion
  * Model training
  * Model testing
  * Model packaging
  * Model registering
  
  We will implement all these steps of the pipeline using the Azure ML service.

# Model evaluation and interpretability metrics

Acquiring data and training ML models is a good start toward creating bussiness value. After training models, it is vital to measure the models performance and understand why and how a model is performing in a certain way. Hence, model evaluation and interpretability are essential parts of thr MLOps workflow. They enable us to understand and validate the ML models to determine the bussiness value they will produce. As there are several types of ML models there are numerous evaluation techniques as well.

<img width="742" alt="Screenshot 2021-12-13 at 00 52 22" src="https://user-images.githubusercontent.com/61119710/145736946-281dff80-d1c5-4f55-b111-20373c564783.png">


# Key Principles for Deploying ML System

Machine Learning is implemented with specific goals and priorities to improve the state of the art in the field, whereas the aim of ML in production is to optimize, automate, or augment a scenario or a business. some of the key principles for deploying the ML system 

<img width="1017" alt="Screenshot 2021-12-13 at 00 50 57" src="https://user-images.githubusercontent.com/61119710/145736879-90a573da-d972-4570-99ff-4df31b6b8bed.png">

# Building Robust CI-CD Pipelines

Automation is the primary reason for the CI/CD in the MLOps workflow. The goal of enabling continuous delivery to the ML service is to maintain data and source code versions of the models, enable triggers to perform necessary jobs in parallel, build artifact, release deployments for production.

<img width="1176" alt="Screenshot 2021-12-13 at 00 44 42" src="https://user-images.githubusercontent.com/61119710/145737166-13edf686-b731-4671-879b-c0510b64658c.png">

# APIs and Microservices

APIs and Microservices are powerful tools that help to enable your ML models to become useful in production or legacy systems for serving the models or communicating with other components of the system. Using APIs and Microservices, you can design a robust and scalable ML solution to carter to your business needs.

**Working of an API**



# Monitoring ML System

In a dynamically changing world the environment and data in which the ML model is deploymed to perform a task or make a prediction is continually evolving, and it is essential to consider this change. Drift is related to changes in the environment and refers to the degradation of predictive ML models performance and the relationship between the variables degrading. 

<img width="1114" alt="Screenshot 2021-12-13 at 01 08 35" src="https://user-images.githubusercontent.com/61119710/145737686-9b3d9b82-03dc-4d5a-9682-6fcb788b973b.png">


