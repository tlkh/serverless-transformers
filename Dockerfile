FROM 3.8.6-slim-buster
LABEL maintainer="Timothy Liu <timothy_liu@mymail.sutd.edu.sg>"
USER root
ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app

RUN python3 -m pip install --no-cache-dir torch==1.7.0+cpu -f https://download.pytorch.org/whl/torch_stable.html

COPY requirements.txt /app/requirements.txt

RUN python3 -m pip install --no-cache-dir -r requirements.txt

COPY . /app/requirements.txt

RUN python3 cache_model.py

EXPOSE 5000

CMD gunicorn --workers=1 --timeout=300 --bind 0.0.0.0:5000 wsgi:app
