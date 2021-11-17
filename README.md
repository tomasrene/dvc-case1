#DVC SHOWCASE // CASE 1
Here you have the data for testing DVC on your local machine. Please follow the instructions below:
###STEPS
1. git clone this repo
2. Create a virtual environment (for example with python3 -m venv venv)
3. Initialize the virtual environment (for example with source venv/bin/activate)
4. Install the requirements (for example with python3 -m pip install -r requirements.txt
5. Initialize a git repo (git init)
6. Initialize a dvc repo (dvc init)
7. Add the .csv files to DVC (dvc add data_train.csv data_test.csv)
8. Follow the instructions that DVC provided (git add .dvcignore data_train.csv.dvc data_test.csv.dvc)
9. Add the .py files to git (git add train_model.py test_model.py)
10. Commit changes to git (git commit -m "First commit")

Congrats! You've initialized a DVC repo linked to a GIT repo (if you want, you can add a git remote origin to start pushing to a repo).
Now you can go on with the rest of the tutorial to learn the funcionalities that DVC provides.

