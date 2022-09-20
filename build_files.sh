# build_files.sh
pip install -r requirements.txt
cd weather/weather/
python3.9 manage.py collectstatic