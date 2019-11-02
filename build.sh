echo "commit message is $1"

pip freeze > requirements.txt
github_changelog_generator
git status
git add .
git commit -m "$1"
git push