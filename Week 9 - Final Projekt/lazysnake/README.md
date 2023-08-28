# Lazysnake

Welcome to Lazysnake, a Python script to automate the creation of new Projectfolders and basic file layout.

## Features

- creates the root folder for a new Project
- creates requirements.txt, readme.md and .gitignore files
- initializes a git repository for the created project
- additional files and folders may be created, dependent on the selected project type

## Usage
Run `python lazysnake.py` to create a basic project, named new_project in the folder of the lazysnake.py file. You can modifiy it's behavior by passing the following commandline arguments to the programm:
- -n or --name desired_name to specify a custom name
- -p or --path desired_path to specify a custom path
- -t or --type desired_type to specify the type of your project currently supported: "standart" and "flask


## Project types and content

### standart
basic Python project
```
/new_project
    /.git
    main.py
    readme.md
    requirements.txt
    .gitignore # by default contains .venv and .ignored
```

### Flask
basic Flask webapp
```
/new_project
    /.git
    /static
        styles.css
    /template
        layout.html # contains basic html and jinja2 to be extended by templates
        index.html # contains basic jinja2 structure for a template
    readme.md
    requirements.txt
    .gitignore # by default contains .venv and .ignored
    app.py # contains basic code to setup a flask app and render index.html at route /