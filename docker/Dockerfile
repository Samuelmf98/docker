FROM jupyter/base-notebook:python-3.8.8

RUN conda install --quiet --yes \
    'pandas' \
    'numpy' \
    'psycopg2' \
    'sqlalchemy' \
    'flask' \
    'gunicorn' \
    'app'

CMD ["jupyter", "lab", "--ServerApp.token=''"]
