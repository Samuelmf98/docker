FROM jupyter/base-notebook:python-3.8.8

WORKDIR /home/jovyan
RUN mkdir samuel


COPY ./  /home/jovyan/samuel   

#../pokedex

#contexto: ../source

 RUN pip install --no-cache-dir -r samuel/requirements.txt

# RUN conda install --quiet --yes \
#     'pandas' \
#     'numpy' \
#     'psycopg2' \
#     'sqlalchemy' \
#     'flask' \
#     'gunicorn' \
#     'app'

CMD ["jupyter", "lab", "--ServerApp.token=''"]

