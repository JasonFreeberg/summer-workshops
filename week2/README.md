# Week 2: DevOps & CI/CD

## Topics

- Continuous Integration
  - Test code, publish code coverage and results
  - Save time, prevent bugs which speeds development cycle
  - On a Pull Request, you can publish the site to a staging environment. Ex: https://github.com/azure/appservice
- Continuous Delivery
  - Promotes a culture of fast-paced deployments
  - Root cause problems
- Automation
  - DevOps (catch-all term)
  - Chat-ops (PR review, build automation)
  - Git-ops (infrastructure as code)
- GitHub Actions concepts
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
