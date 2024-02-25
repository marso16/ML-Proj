Iteration 1

In this iteration we have tried to train a model to classify a network traffic as malicious or not, in order to help identify attacks in a network traffic log.

Technical Description:

We have built 2 models, using Logistic Regression and Autoencoder.

Autoencoder:

Autoencoder helps to classify the traffic but it also further helps with detecting traffic anomalies by reconstructing the data. If the difference between the original and reconstructed log is significantly higher than usual, it indicates an anomaly.

Logistic Regression:

Well suited for binary classification, and it helps classifying the traffic as attack or benign

Attack Types:

The models cover the below attack types:
DDos, Port Scan, Bot, infiltration, webattack|Brute force, Web attack|XSS, Web attack|SQL Injection, FTP-Patator, SSH-Patator, DoS slowris, DoS slowhttptest, DoS Hulk, DoS GoldenEye, Hearbleed

Network Environment:
Online server

Performance goals:

Desired Accuracy >= 90%
Cost of misclassification: 
FPR: tolerable up to 2% with the presence of a SOC team.


