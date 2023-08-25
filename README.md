# FLASK CRUD API 

### Video Link: https://drive.google.com/file/d/1dGq62ECGZ1aNio89XN35jDAqTHXOiSB8/view?usp=sharing
## Installation

#### 1. USING DOCKER

```bash
  pip install virtualenv
  virtualenv venv
  git clone https://github.com/neel-jotaniya/flask_crud/
  cd .\flask_crud\
  docker build -t flask_crud . 
  docker run -p 8000:8000 flask_crud
```
#### 2. MANUALLY

```bash
  pip install virtualenv
  virtualenv venv
  set CONNECTION_STRING=mongodb+srv://neel:0WuC26YLdrjdApau@cluster0.v58xczy.mongodb.net/
  git clone https://github.com/neel-jotaniya/flask_crud/
  cd .\flask_crud\
  pip install -r requirements.txt
  python ./CRUD/main.py
```

- Then we can access APIs at http://127.0.0.1:8000 
    
