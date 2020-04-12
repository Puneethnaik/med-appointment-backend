# echo "Removing previous copy and installing a fresh copy of the code"  
# rm -rf ~/Documents/deployed/med-appointment-backend  
# mkdir ~/Documents/deployed/med-appointment-backend  
# cp -r . ~/Documents/deployed/med-appointment-backend  
# cd ~/Documents/deployed/med-appointment-backend  
echo "Creating virtual environment and installing dependencies"  
virtualenv django_env  
source django_env/bin/activate  
pip3 install django   
pip3 install djangorestframework  
pip3 install gunicorn dj-database-url psycopg2  
pip3 freeze > requirements.txt
rm -r django_env
# cd ~/Documents/deployed/med-appointment-backend
# python3 manage.py migrate  
heroku login  
touch Procfile && echo "web: gunicorn backend.wsgi --log-file -" > Procfile 
touch runtime.txt && echo "python-3.6.10" > runtime.txt  
heroku create backend14557
# git init
# heroku git:remote -a backend14557
# git pull heroku master
# git add .
# git commit -m "first deployment"
# git push heroku master	