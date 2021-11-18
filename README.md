# DVC - CASE 1
Here you have the data for testing DVC on your local machine. Please follow the instructions below:
### STEPS
<ol><li>Download this repo (manually or by <code>svn export --force httsp://github.com/tomasrene/dvc-case1/trunk ./</code>)</li>
<li>Create a virtual environment (for example with <code>python3 -m venv venv</code>)</li>
<li>Initialize the virtual environment (for example with <code>source venv/bin/activate</code>)</li>
<li>Install the requirements (for example with <code>python3 -m pip install -r requirements.txt</code>)</li>
<li>Initialize a git repo (<code>git init</code>)</li>
<li>Initialize a dvc repo (<code>dvc init</code>)</li>
<li>Add the .csv files to DVC (<code>dvc add data_train.csv data_test.csv</code>)</li>
<li>Follow the instructions that DVC provided (<code>git add .gitignore data_train.csv.dvc data_test.csv.dvc</code>)</li>
<li>Add the .py files to git (<code>git add train_model.py test_model.py</code>)</li>
<li>Commit changes to git (<code>git commit -m "First commit"</code>)</li>
</ol>
<br>
<p><b>Congrats!</b> You've initialized a DVC repo linked to a GIT repo (if you want, you can add a git remote origin to start pushing to a repo).
  Now you can go on with the rest of the tutorial to learn the funcionalities that DVC provides.</p>

