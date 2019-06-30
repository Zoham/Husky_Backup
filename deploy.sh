git add *
git commit -m "test"
git push heroku master
heroku ps:scale web=1
heroku open
