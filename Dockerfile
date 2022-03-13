# the base image that we inherit from
FROM python:3.9.5-slim

#best practice: create a user
RUN adduser --disabled-password --gecos '' ml-api-user

WORKDIR /opt/app-fastapi

# copy our project inside the container
ADD ./app-fastapi /opt/app-fastapi/
RUN pip install --upgrade pip
RUN pip install -r /opt/app-fastapi/requirements.txt

RUN chmod +x /opt/app-fastapi/run.sh
RUN chown -R ml-api-user:ml-api-user ./

USER ml-api-user

EXPOSE 8001

CMD ["bash", "./run.sh"]