# CACS_Dave-nagri

Hindi-English Code-Switching Project

Description about the system - 
Dave-nagri is a Hindi-English code-switching model that makes use of the BERT system to classify the input into five classes - English 'en', Hindi 'hi', NER'ne', Universal 'univ':4 and Acronym 'acro'. 

The Project is built on Python 3.7.4. 



1) Download the BERT repository from here - https://drive.google.com/drive/folders/1zuntQrIixY4ngV86te_wT2UwAinNO1gI?usp=sharing
2) Save the download in the directory - 'bert-uncased-multilingual-tensorflow'
3) setup.sh: run this file to install the necessary libraries for this project
4) train.sh: run this file from the src directory.  This file will run the train.py file and save the trained model in the outputs directory as
train_model.h5.
5) train.py: This file trains on the 'tweets_train.conll' dataset in the Data directory. This file also uses the weights from the 'bert-uncased-multilingual-tensorflow' directory for model training. The file first pre-processes the data by extracting the input column (in our case, first column), and taking the 7th column of LID tokens as the output one. It then maps the data to their respective IDs as per the BERT specifications and further utilizes the time-dense distributed layer architecture to produce classifications. 
6) predict.sh: run this file from the src directory!  This will run the predict.py file and save the predicted LID labels for the sentences in tweets_dev.conll and tweets_test.conll as a CSV file in the outputs directory (dev.csv, test.csv)
7) predict.py: this file takes the tweets_dev.conll and tweets_test.conll files and isolates the second column and the second to last column.  We detokenize each sentence so that we can feed each sentence into our model for prediction. This file creates two CSV files (dev.csv and test.csv) in the outputs directory where each file has a column for the sentences' tokens, a column for their corresponding gold LID labels, and a column for the predicted LID labels.
8) evaluate.sh: run this file from the src directory!  This will run the evaluate.py file and save the accuracy score for the predicted LID labels for the dev and test data in the outputs directory as results.tsv.
9) evaluate.py: this file takes the gold LID labels and predicted LID labels saved in the dev.csv and test.csv files and calculates the accuracy score for each dataset.  This is done by calculating how many true positives (TPs) there are for each LID label ('hi', 'en', 'acro', 'ne', 'univ') divided by the length of the vocabulary of the dataset.  This file creates a TSV file in the outputs directory that saves the accuracy score for the dev and test datasets.
10) **The output accuracies are as follows -**

**dev-set = 0.74**
**test-set = 0.71**





