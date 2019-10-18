files="analytics/google/google_tag_manager.py analytics/google/google_analytics.py"

for f in $files
do
    mypy $f --ignore-missing-imports
done
