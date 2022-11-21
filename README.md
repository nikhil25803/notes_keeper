

<h1 align=center> Notes Keeper </h1>
<h3 align=center> A note keeping API with user authentication and back-population :')</h3>

---

## Tech Stack 💻

  ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
  ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)

---



## What does it exactly do? 🤔
It is an API built using **Fast API**, that keeps your notes. The initial release includes user authentication and back population of data. 

More feature will be added in near future that includes, auto-delete, email reminders, sharing and allowing friends to make changes in your notes, etc.

---

### A demo🧑‍💻
To run and test this API on your local system, follow these steps :

### Fork and clone the repository
Copy the URL of the forked repository and clone it.
```bash
git clone https://github.com/nikhil25803/notes_keeper.git
```

### Change the directory
```bash
cd notes_keeper
```


### Create a virtual environment
```bash
python -m venv env
```
### Activate the virtual environment
> For windows
```bash
env\Scripts\Activate.ps1
```
> For Linux
```bash
source env/scripts/activate
```

### Install the dependencies
```powershell
pip install -r requirements.txt
```

### Run the FastAPI server
```powershell
uvicorn main:app --reload
```

This will create a `NotesDB.db` named database file in your root directory.

### The endpoints
You can find it running on `http://127.0.0.1:8000`

#### **POST** `/user` : To create an user.
```python
# Schema :

{
  "name": "string",
  "email": "string",
  "password": "string"
}

# Response Schema

{
  "name": "string",
  "email": "string",
  "posts": [
    {
      "id": 0,
      "title": "string",
      "description": "string"
    }
  ]
}

```

#### **Get** `/user/{id}` : To get an user details
```python
# Response Schema

{
  "name": "string",
  "email": "string",
  "posts": [
    {
      "id": 0,
      "title": "string",
      "description": "string"
    }
  ]
}

```

#### **POST** `/post`
```python
# Schema

{
  "title": "string",
  "description": "string",
  "user_id": 0
}

# Response Schema
{
  "id": 0,
  "title": "string",
  "description": "string"
}
```
----