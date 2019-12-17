# gtcrypto
Using data visualization to explain statistical characterization of bitcoin transaction data.

Built for explaining results of the paper :
Bitcoin Transaction Forecasting with Deep Network Representation Learning", Wenqi Wei(Georgia Tech), Qi Zhang(IBM Research), Ling Liu(Georgia Tech). under submission

Data used : https://senseable2015-6.mit.edu/bitcoin/

Requires:
Cassandra database setup - Table formats are present in cqls/create_tables. Data can be written using write_to_db.py. The sample files required are stored in data/ folder.

main.py - Starts a Flask web app, to allow searching for node data

graph_visuals.ipynb - Code for generating temporal graph and k-step directed graph representation.
