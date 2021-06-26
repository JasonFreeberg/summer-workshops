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
  