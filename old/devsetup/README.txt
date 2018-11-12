1. Install Docker https://docs.docker.com

2. Install PyCharm Professional https://www.jetbrains.com/pycharm/download

3. Run PyCharm and connect to our Git (Bitbucket) project

4. Open terminal and paste in the following command: mkdir /tmp/dev_doc_tmp

5.
  a. Inside PyCharm, select File:Open from the menu, then navigate to the location of the cloned Sixgill project and open it
  b. Inside PyCharm, select File:Open from the menu, then navigate to the location of the Dockerfile (sixgill/docker/devsetup/Dockerfile) and open it
  
6.
  a. Inside PyCharm, select Run:Edit Configurations from the menu and create a new Run Configuration for a Dockerfile
  b. Click the ... button on the right side of the configuration entry for 'Dockerfile' and select sixgill/docker/devsetup/Dockerfile
  c. Input a name as the "Image tag"
  d. Make sure the "Run built image" box is un-checked (set to False)
  e. Click the ... button on the right side of the configuration entry for 'Bind mounts' and create a new mapping from the local project on the host machine to the                    
     docker container. The host path should be the location of the cloned Sixgill project, and the container path
     should be set to: /opt/project.
     The bind mount string should be something like: /Users/barak/PycharmProjects/sixgill:/opt/project
  f. Create another mapping from /tmp/dev_doc_tmp on your host machine to /tmp/dev_doc_tmp inside the docker container.
     The bind mount string should be something like: /tmp/dev_doc_tmp:/tmp/dev_doc_tmp
  g. Save the configuration and run it to build an image from the Dockerfile you previously opened in PyCharm

7.
  a. Inside PyCharm, open the preferences menu and navigate to the Project Interpreter settings for your current project
  b. Click the gear icon and select add, then choose Docker from the provided options. 
  c. In the Image name field, use the dropdown menu to select the image you built from the Dockerfile. 
  d. Click "OK" to add the new interpreter, then configure the same path mapping (bind mount) as before: the local path
     should be the location of the cloned Sixgill project, and the remote path should be set to: /opt/project
  e. Then, add another mapping as per the instructions in 6f: /tmp/dev_doc_tmp:/tmp/dev_doc_tmp
  f. Wait until PyCharm completes updating skeletons for the docker

8. Running a script
  a. In the run configuration, on the Python interpreter drop-down select the in-docker interpreter defined in #6.
  b.
    i.  In case of a scrapy running configuration make sure the script path field holds path to scrapy's cmdline.py is
        points to this file *in the Docker* (/usr/local/lib/python2.7/site-packages/scrapy/cmdline.py).
    ii. Also in the running configuraton, make sure the docker container settings include the previously defined mapping
        from /tmp/dev_doc_tmp:/tmp/dev_doc_tmp. If the mapping is not present, it must be added.
9. Running a flask app in a docker container
  a. In the case that you experience slow response times when running a flask app inside the docker, navigate to the
     app.py file in question and add threaded=True as an argument to app.run(). For example, app.run(host='0.0.0.0')
     would become app.run(host='0.0.0.0', threaded=True)








