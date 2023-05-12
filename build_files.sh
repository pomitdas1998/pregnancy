echo "Build start"
python3.11.3 -m pip install -r requirements.txt
python3.11.3 manage.py collectstatic --noinput --clear
echo "Build END"