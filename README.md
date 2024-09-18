
# FastAPI Assignment

## Prerequisite
- have python 3.10.7 installed
- use virtualenv is preferred

## Project Description
- A note can consist of 0 or many tags.
- A note has title, description and tags.
- A tag has name.
- A note can be added, edited, retrieved and deleted.

## Tasks
- install requirements into python environment
- create note_app
- create note model
- create tag model
- create note serializers
- create note views
    - To get list of all notes
    - To create a note
    - To allow modification to the existing note
- create tag views
    - To get list of all tags
    - To get a tag and its corresponding notes where it is used


    ## Requirements
    This project uses a postgresql, which you need to have docker install in your machine.
    postresql was used in the project, for image you can check at command.yaml or docker-compose.yaml for more details
    ```html
    - docker compose up -d postgres
    ```
    I am also using plutonkit(Personal project I developed for project management).

    ## Information
    Serving at: http://127.0.0.1:8000
    API docs: http://127.0.0.1:8000/docs

    The shell command how to run this application can check at command.yaml(command inventory from plutonkit)

    ## Unit test

    You need to run the docker for postresql before performing the unit test. please check the `command.yaml` for available command you can use.


    ## How to run the application
    I am using plutonkit, this library was personally developed by me that helps to organize my application cycles

    Install the neccessary library using this command
    ```html
    - plutonkit cmd  pip_install
    ```
    or
    ```html
    - pip install -r requirements.txt
    ```

    Start running the docker first using this command, therefore postresql image will be install
    ```html
    - plutonkit cmd  run_pg_docker
    ```
    Seed the data
    ```html
    - plutonkit cmd  run_pg_migrate
    ```

    Running the actual application, please use this command
    ```html
    - plutonkit cmd  start
    ```

    If you can struggles in using plutonkit command, please check the command.yaml for more details.
