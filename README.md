# tempest-compression-decider-service  
  
this impements a basic API, it trains a decision tree ML model and can decide which compression is best for a given file  
     
This service is responsible for determining the appropriate method of compression to enhance the storage efficiency of uploaded files. This README provides an overview of the service, its functionality, and instructions for setting up and running the service.  
   
# Features  
- Intelligent compression decision  
  - the service uses decision trees, to analyse file characteristics and make informed decisions regarding the compression method to be applied.
- Enhanced storage efficiency
  - by dynamically choosing the optimal compression approach, the service maximizes the storage efficiency
  - reducing storage costs and improving overall performance.  
  
# How to run locally
```bash
uvicorn main:app --reload
```
