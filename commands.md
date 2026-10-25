# Terminal Record: [Seabreeze Inn]

## 1. Building the project
cd
cd
deactivate
c
cd ~/Documents/ism3232_midterm
pwd
ls la
ll
ls
la -la
ls -la
touch business_rules.py main.py commands.md readme.md requirements.txt .gitignore tests/
touch tests
cd ~/tests
cd ~/Documents/ism3232_midterm/tests
mkdir tests
cd ~/tests
cd ~/Documents/ism3232_midterm/tests
touch __init__.py test_business_rules.py
python3 -m venv .venv
cd
cd .
cd .
cd ~/Documents/ism3232_midterm
python3 -m venv .venv
source .venv/bin/activate
which python3
pip list
pip install pytest ruff
pip list
pip freeze > requirements.txt
echo '.venv/' > .gitignore
echo '__pycache__/' >> .gitignore
echo '*.pyc' >> .gitignore
git remote -v
git add .
git commit -m "Complete ISM3232 Midterm project"
git push
git push --set-upstream origin main
## 2. The virtual environment
/Users/ashleymarte/Documents/ism3232_midterm/.venv/bin/python3
The output shows that the virtual environment is active because the Python executable is located inside the project's `.venv` folder.
## 3. The project structure
The original ism3232 folder is on my computer but not in my GitHub repository because my GitHub repository tracks only the files inside my ism3232_midterm project folder.
## 4. Every function and test
business_rules.py defines 8 functions, and tests/test_business_rules.py defines 14 test functions.
## 5. Which files print
Only `main.py` prints output because it displays the stay report, while `business_rules.py` only contains business logic and returns values without printing anything.
## 6. The commit history
2bce7c0 (HEAD -> main) Initial commit
There was 1 commit in the history at that point.