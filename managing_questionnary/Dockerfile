FROM ubuntu:latest
LABEL author="Thibault KOLLEN"
RUN apt-get update -y && apt-get install -y python3-pip python-dev
COPY ./requirements.txt /managing_todo_list/requirements.txt
WORKDIR /managing_todo_list
RUN pip install -r requirements.txt
COPY . /managing_quetionnary
ENTRYPOINT [ "python" ]
CMD ["webapp.py"]