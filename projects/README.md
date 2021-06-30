# Projects

Now that we've covered git, CI/CD, APIs and containers... let's put it to work! The goal for all these projects will be to create a working sample project, and to write documentation so another person can follow along, learn about the topic, and get the sample application running. This will help you document what you did and how you did it, which will be helpful when you're preparing for interviews, because interviewers will want to hear you describe the details. It also pays-it-forward, because I'll be using these in my future mentorship and training materials.

Here's my suggested approach for tackling these projects:

1. Get the thing working. You can't document what you don't know! So first just try to get the application/project working correctly. As you do so, take short notes about what you did, the notes will help on step 3.
2. When you're satisfied with the state of the project, clean up your code (add helpful comments, opt for readable code over optimized code, remove old code that's no longer necessary, etc.)
3. Start writing steps on how someone else can fork your project and get it running. Explain where necessary, imagine that you are writing this for your past self from ~5 weeks ago before this summer's learning sessions :) 

## R Shiny Dashbaord in a Docker container

## Introduction to CI for Data Scientists

- Introduction and explanation of Git, GitHub, GitHub desktop
  - Steps to fork the repository, clone the fork, make a change and commit it back, make a change as a pull request
- Introduction to CI/CD, and GitHub Actions
- Project format:
		- A small library with some data cleaning methods 
		- A notebook
- Writes a workflow to run tests on their library methods, and their notebook!

## Surfacing a Machine Learning Model as a REST API

**Context**: It's more and more common for software to provide recommendations, auto-complete inputs, or project future outcomes using Machine Learning. In a distributed system or large organization, it may make sense to surface a trained ML model to the rest of the application/system with a REST API. In this scenario, a client can POST inputs to the API and recieve recommendations, auto-completion text, or any other inferred output. This pattern is commonly referred to as an "Inference API", since the API returns an _inference_ given the inputs. Some cloud providers (AWS, Azure, GCP) provide services specifically for inferences APIs: [GCP Cloud Inference API for time-series data](https://cloud.google.com/inference), [Azure Machine Learning](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-deploy-and-where?tabs=azcli).

**Goal**: The goal of the project will be to guide a data science or computer science student through process of creating a **simple** Machine Learning model, and exposing it a REST API in a small, **simple** application. 

### Deliverables

1. A Jupyter notebook that trains an ML model on some data
2. A web application that... 
    1. Exposes the ML model as a REST API (takes inputs that match those in the training data, and responds with the predicted value)
    1. Takes some kind of user input
    2. Passes the user input to the REST API and displays the predicted result

## Flask and Vue.js ToDo Application
