CALL heroku plugins:install heroku-builds
CALL heroku builds:cancel
CALL git add .
CALL git commit -m "test"
CALL git push heroku master
CALL heroku ps:scale web=1
CALL heroku open
@echo "Husky is awake"