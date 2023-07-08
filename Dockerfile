FROM python:3.10.0

WORKDIR /flask_crud

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./CRUD ./CRUD 

ENV CONNECTION_STRING=mongodb+srv://neel:0WuC26YLdrjdApau@cluster0.v58xczy.mongodb.net/

CMD [ "python", "./CRUD/main.py" ]