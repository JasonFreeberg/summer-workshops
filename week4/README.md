# Docker and Containers

## Topics

- Why Docker?
  - Deploying code consistently and reliably to different environments is tough. 
  - Hope is to have dev, staging, test, and production all as similar as possible to prevent any problems as a change goes through these environments and avoid the *"works on my machine!"* problem.
  - When apps are written in Python, Java, and Node... it becomes an operational nightmare for an IT/infrastracture/Ops team to deploy all those different types.
- What is Docker?
  - A standard unit of software. If your app is in Java or Python, it runs the same in a Docker container. Instead of `java -jar app.jar` and `python main.py` you have `docker run...`.
  - Isolates the app from its environment and any dependencies the app may have on the environment. As long as the target env (local box, server, Kubernetes) can run Docker, it can run your app.
- The `Dockerfile`
  - Should contain the steps to build and run your application. So anyone can pull your project from GitHub, and if it has a Dockerfile they can run it if they have Docker installed. (They don't have to go install Ruby or Go if your app uses those)
- Very common in the cloud
  - Not every cloud has services to run Python apps, Java apps, Go apps, and Ruby apps... but they all have a service to run Docker images!
- How Docker works in practice
  - Add Dockerfile
  - Build and run locally
  - Publish to a registry
  - Server or cloud service pulls the image and runs it

## Learning Materials

1. [Getting Started Guide from Docker](https://docs.docker.com/get-started/). Only parts 1 through 4 are necessary at this point.
    - Looks like Microsoft has an identical guide here: https://docs.microsoft.com/en-us/visualstudio/docker/tutorials/docker-tutorial
3. YouTube Videos. These are from the context of .NET, which is a framework built on top of C#. You can ignore the .NET specifics, but their explanations and reasoning about Docker containers is in plain English.
    1. https://www.youtube.com/watch?v=vmnvOITMoIg&ab_channel=dotNET
    2. https://www.youtube.com/watch?v=k2sskhYEPkI&ab_channel=dotNET
    3. https://www.youtube.com/watch?v=d7D0h9i-QCw&ab_channel=dotNET
  
## Exercises
  
1. If you haven't already, fork the python-playground sample repo. In your fork, add a `Dockerfile` that creates a virtual environment, installs the packages, and runs the application. Remember, your Dockerfile will need to copy the application code and requirements.txt file!
2. Create an account on  [DockerHub](https://hub.docker.com/) and push a Docker image to it (any image, as long as it runs!). This will require you to run `docker push`. Once the image is pushed, try to pull the image and run it (using `docker pull`).
  - Note: This is covered in Part 4 of the "Getting Started Guide from Docker" above.
4. If you accomplished exercises 1 and 2, write a GitHub Actions workflow that builds your Docker iamge every time there's a PR on the main branch.
5. Finally, write a GitHub Actions workflow that builds your Docker image and pushes it to GitHub Continer Registrty every time there's a **push** on the main branch. If you can do this one, then you're really cooking with peanut oil! Here is a doc article to get you started:
    - https://docs.github.com/en/actions/guides/publishing-docker-images#publishing-images-to-github-packages
