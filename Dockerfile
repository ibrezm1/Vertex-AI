FROM tensorflow/tensorflow:2.9.1
#docker pull tensorflow/tensorflow:2.9.1
# docker run -v /path/on/host:/path/in/container
# docker exec -it test bash 

WORKDIR /app

COPY . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt 

#RUN usermod -u 1000 docker
RUN chmod a+rwx -R /app

CMD gunicorn --bind 0.0.0.0:5005 --timeout=150 app:app -w 5 \
                --access-logfile /tmp/access.log --error-logfile /tmp/general.log

EXPOSE 5005