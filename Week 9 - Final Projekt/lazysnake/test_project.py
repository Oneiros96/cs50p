import os, shutil
from project import create_root, basics, flask, standart, git

def test_create_root():
    # new project folder created
    path = "new_project"
    create_root(path)
    assert os.path.exists(path) == True

    # altes project endind if folder already exists
    create_root(path)
    assert os.path.exists(f"{path}(0)") == True
    os.rmdir(path)
    os.rmdir(f"{path}(0)")

def test_basics():
    # setup testdirectory
    os.mkdir("test")
    basics("test")
    # tests
    assert os.path.exists("test/README.md") == True
    assert os.path.exists("test/requirements.txt") == True
    assert os.path.exists("test/.gitignore") == True
    with open("test/.gitignore", "r") as f:
        assert f.read() == ".venv\n.ignored\n"
    # clean up
    shutil.rmtree("./test")


def test_flask():
    # setup testdirectory
    os.mkdir("test")
    flask("test")
    # tests
    assert os.path.exists("test/app.py") == True
    assert os.path.exists("test/static/styles.css") == True
    assert os.path.exists("test/templates/layout.html") == True
    assert os.path.exists("test/templates/index.html") == True
    # clean up
    shutil.rmtree("./test")

def test_standart():
    os.mkdir("test")
    standart("test")
    assert os.path.exists("test/main.py") == True
    shutil.rmtree("./test")



