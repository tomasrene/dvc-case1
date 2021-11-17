# DVC - CASE 1
Here you have the data for testing DVC on your local machine. Please follow the instructions below:
### STEPS
<ol><li>Download this repo (manually or by svn export)</li>
<li>Create a virtual environment (for example with python3 -m venv venv)</li>
<li>Initialize the virtual environment (for example with source venv/bin/activate)</li>
<li>Install the requirements (for example with python3 -m pip install -r requirements.txt</li>
<li>Initialize a git repo (git init)</li>
<li>Initialize a dvc repo (dvc init)</li>
<li>Add the .csv files to DVC (dvc add data_train.csv data_test.csv)</li>
<li>Follow the instructions that DVC provided (git add .dvcignore data_train.csv.dvc data_test.csv.dvc)</li>
<li>Add the .py files to git (git add train_model.py test_model.py)</li>
<li>Commit changes to git (git commit -m "First commit")</li>
</ol>
<br>
<p><b>Congrats!</b> You've initialized a DVC repo linked to a GIT repo (if you want, you can add a git remote origin to start pushing to a repo).\
  Now you can go on with the rest of the tutorial to learn the funcionalities that DVC provides.</p>

