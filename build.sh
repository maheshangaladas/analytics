set -e

echo "commit message is $1"

for f in $(find ./{analytics,tests} -type f -name "*.py" -print); do
		if [ "$f" != "__init__.py" ]
		then
		isort "$f"
		black -l 79 "$f"
		flake8 --ignore E501 "$f"
		fi
done

pytest

source env/bin/activate
pip freeze > requirements.txt
deactivate

github_changelog_generator

git status
git add .
git commit -m "$1"
git push
