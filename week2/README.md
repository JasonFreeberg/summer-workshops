# Week 2: DevOps & CI/CD

## Topics

- Continuous Integration
  - Test code, publish code coverage and results
  - Save time
  - Prevent problems
  - Speed development cycle
- Continuous Delivery
  - Promotes a culture of fast-paced deployments
  - Root cause problems
- Automation
  - DevOps (catch-all term)
  - Chat-ops (PR review, build automation)
  - Git-ops (infrastructure as code)

## Learning Materials
  
- https://lab.github.com/githubtraining/github-actions:-hello-world
- https://lab.github.com/githubtraining/github-actions:-continuous-integration
- https://lab.github.com/githubtraining/github-actions:-using-github-script
- https://azure.microsoft.com/en-us/overview/what-is-devops/#practices

## Exercises

- In your GitHub Pages repo, add 2 workflow files:
  - One that runs every time there's a Pull Request. The workflow should check the spelling on the pull request's contents
    - https://github.com/marketplace/actions/check-spelling-js-vue-html-markdown-text
  - One that runs every time there's a commit on the repository. The workflow should zip up your project's contents and upload them as an artifact.
    - https://github.com/actions/upload-artifact
- TODO: Fork a Python same repo and add a workflow that creates a Python virtual environment, installs the requirements.txt, and runs some unit tests.

