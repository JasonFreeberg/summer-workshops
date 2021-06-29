# Simple Docker app

Open the `Dockerfile` and take a look. This app simply runs the shell script, `hello.sh`. To run this app as a Docker container, you first have to build a Docker image from the `Dockerfile`:

```bash
docker build -t hello-world .
```

Let's break that command down word-by-word:

1. `docker`: This runs connects to the Docker process running on your machine. Try running `docker --help` for a full list of available commands
2. `build`: This tells docker we want to build a new Docker image
3. `-t`: This is the "tag" argument, meaning we want to tag the Docker image with the following name and tag (of the format `name:tag`)
4. `hello-world`: This is the name of the Docker image we're going to create, since we didn't give a name for the tag, it will automatically be tagged `latest` (as in `hello-world:latest`)
5. `.`: The dot (period) literally means "the current directory". You'll see this used in a lot of contexts. Two dots, `..`, means "the parent directory". So when you're in the terminal, `cd ..` moves you up 1 level in the directory.

Once the image is built, you can run it with:

```bash
docker run hello-world:latest
```
