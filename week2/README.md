# Week 2: DevOps & CI/CD

## Topics

- Inner and outer development loops
  - "Inner dev loop" is writing code, building the code, and running/testing the code. When you're satisfied with your changes, you'll open a PR to push your changes into the code base. Then begins the next loop...
  - The "outer" loop involves running automated tests on your PR, getting it reviewed and merged. Next, someone will "cut a release" meaning that all the planned improvements for that milestone are in the code base at the commmit at which the release was made. From there, the compiled code might be deployed to a system, an update becomes available for mobile app users, etc. 

    ![](https://lh3.googleusercontent.com/proxy/zc9YiocpMQm6vf2MzRKLMZbtVC-_iq5mDsAJ7itGrJx_TEIkCBSAOZCRlqlGEkO2DvN0gxubykWJ4yzMGs6GClP5SyEzo33wWoh-2VYLQb0YVpXoFw6M46u-UvkikA)
- Continuous Integration
  - Test code, publish code coverage and results
  - Save time, prevent bugs which speeds development cycle
  - On a Pull Request, you can publish the site to a staging environment. Ex: https://github.com/azure/appservice
- Continuous Delivery
  - Promotes a culture of fast-paced deployments
  - Root cause problems
- Automation
  - DevOps: catch-all term for work involving development operations like CI pipelines, release management and deployment, and possibly IT infrastructure.
  - Chat-ops: automation built into the chat functionality on issues and pull requests. Useful in large organizations where you don't want users to have rights to manage issues/PRs directly. 
    - Ex: See Azure Docs repo
  - Git-ops: a software development strategy where the git repository acts as the central source of truth for the project. An example would be defining your IT infrastructure using Terraform, and tagging releases or deployments with the respective commit hash.
    - Ex: See Azure Bicep
- GitHub Actions: an automation framework
  - workflow file
  - jobs
  - steps
  - actions
  - dependent steps

## Learning Materials
  
- GitHub Learning Labs
  - https://lab.github.com/githubtraining/github-actions:-hello-world
  - https://lab.github.com/githubtraining/github-actions:-continuous-integration
  - https://lab.github.com/githubtraining/github-actions:-using-github-script
- General Reading
  - https://azure.microsoft.com/en-us/overview/what-is-devops/#practices

## Exercises

- In your GitHub Pages repo, add 2 workflow files:
  - One that runs every time there's a Pull Request. The workflow should check the spelling on the pull request's changes to your README file
    - https://github.com/marketplace/actions/check-spelling-js-vue-html-markdown-text
  - One that runs every time there's a commit on the repository. The workflow should zip up your project's contents and upload them as an artifact on GitHub.
    - https://github.com/actions/upload-artifact
- Fork the [Python playground app](https://github.com/JasonFreeberg/python-playground) if you haven't already. Add a workflow that creates a Python virtual environment, installs the requirements.txt, and runs some unit tests. This should run on every Pull Request to the master branch, and on every commit on the master branch.

### Extra credit
- Use [this PR commenter action](https://github.com/mshick/add-pr-comment) to comment on Pull Requests to your repository. The comment can introduce the user to the repo, thank them for their contribution, and refer them to the README file.
