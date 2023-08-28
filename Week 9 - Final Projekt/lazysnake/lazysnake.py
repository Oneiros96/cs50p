import sys, os, subprocess, click

@click.command()
@click.option("-n", "--name", "name", default="new_project",
              help="Specify a name for the new projekt")
@click.option("-p", "--path", "path", default=".",
              help="Desired path where the project folder should be created")
@click.option("-t", "--type", "type", default="standart",
              help="Currently supported: standart, flask")
def main(name, path, type):
    path = create_root(f"{path}/{name}")
    basics(path)
    match type:
        case "standart":
            standart(path)
        case "flask":
            flask(path)
    git(path)
    sys.exit()

def create_root(in_path):
    """
    Try's to create the project Folder and will append (0) to it if an existing folder has the same Name.
    Exit's the programm when provided with an anvalid path.
    """
    x = 0
    path = in_path
    while True:
        try:
            os.makedirs(path)
            return path
        except FileNotFoundError:
            print("Invalid Path")
            sys.exit()
        except FileExistsError:
            path = in_path + f"({x})"
            x += 1
            pass

def basics(path):
    with open(f"{path}/README.md", "w"):
        pass
    with open(f"{path}/requirements.txt", "w"):
        pass
    with open(f"{path}/.gitignore", "w") as f:
        f.write('.venv\n.ignored\n')

def standart(path):
        with open(f"{path}/main.py", "w"):
            pass

def flask(path):
    with open(f"{path}/app.py", "w") as f:
        f.write('from flask import Flask, redirect, render_template\n\n')
        f.write('app = FLask(__name__)\n\n')
        f.write('@app.route("/", methods=["GET"])\ndef index():\n')
        f.write('   return render_template("index.html")')

    os.mkdir(f"{path}/static")
    with open(f"{path}/static/styles.css", "w"):
        pass

    os.mkdir(f"{path}/templates")
    with open(f"{path}/templates/index.html", "w") as f:
        f.write('{% extends "layout.html" %}\n\n')
        f.write('{% block title %}\n\n{% endblock %}\n\n')
        f.write('{% block main %}\n\n{% endblock %}\n\n')
        f.write('{% block script %}\n\n{% endblock %}\n')

    with open(f"{path}/templates/layout.html", "w") as f:
        f.write('<!doctype html>\n\n<html lang="en">\n')
        f.write('   <head>\n')
        f.write('       <!-- CSS -->\n      <link href="/static/styles.css" rel="stylesheet">\n\n')
        f.write('       <title>{% block title %}{% endblock %}</title>\n\n')
        f.write('   </head>\n   <body>\n')
        f.write('       <main>\n        {% block main %} {% endblock %}\n       </main>\n')
        f.write('       {% block script %} {% endblock %}\n')
        f.write('   </body>\n</html>\n')

def git(path):
    os.chdir(path)
    subprocess.run(['git', 'init'])
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', 'Initial commit'])




if __name__ == "__main__":
    main()

