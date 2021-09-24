# Test-task from Wargaming TF-IDF

#### How to install and run

* Build project
`docker-compose up`
* First setting for project

if you have error `Permission denied` in docker, try to run docker with root privileges `sudo` in Linux OS

````bash
docker exec -it wargaming-test-task_web_1 sh
flask start create_db
````
* So you can to see how the project is working, just open in browser `127.0.0.1:5000`