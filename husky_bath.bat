@echo "Add, Commit, Push to remote Husky repo"
CALL git add .
set /p CommitMessage=What Should We Tell Others Who Own Husky?
CALL git commit -m %CommitMessage%
@echo "Husky just took a bath"