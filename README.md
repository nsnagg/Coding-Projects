How to push code to GitHub
Many DevOps professionals only want to know the Git commands necessary to push their existing project to GitHub.

To save those readers from going through the entire example, here are the Git commands used in this tutorial. These commands assume a push to a GitHub repo named existing-website, owned by a GitHub user named cameronmcnz:


git init
git add .
git commit -m "Add existing project files to Git"
git remote add origin https://github.com/cameronmcnz/example-website.git
git push -u -f origin master


Updating a remote GitHub repo
To push an existing project to GitHub, you must first create a GitHub repository. To do this, simply click the green “Create repository” button in GitHub’s online console and provide a repository name.

For this example, we will name the repository example-website.

GitHub repo for existing project
You must create a GitHub repo to manage your existing project’s files.

Obtain the repo’s GitHub URL
After you create the repository, click the green “Code” button. This reveals the GitHub URL for HTTPS connections.

Copy this value for use in a future step.

find GitHub URL
The GitHub URL is used to push the existing project to GitHub.

Initialize Git in the existing project
If the existing project does not already use Git, issue a git init command in the root folder. After the repository is initialized, add all of the project files to the Git index and perform a commit:

git add .
git commit -m "Add existing project files prior to the push to GitHub."
Add a remote reference for GitHub
To let your existing project synchronize with GitHub, issue a git remote add command to configure a reference from you local Git installation to the repository on GitHub. Note that the last segment of the git remote add command is your project’s GitHub URL.

git remote add origin https://github.com/cameronmcnz/example-website.git
Push the first commit to GitHub
Once you’ve added the remote reference, you are ready to push your existing project to GitHub.

Simply issue a git push command with the name of the current branch along with the -u and -f switches.

Note that older Git repositories create a master branch by default, while newer ones use main. Amend the git push command accordingly.

git push -u -f origin master
The -u switch makes the remote GitHub repo the default for your existing project. The -f switch forces Git to overwrite any files that already exist on GitHub with your existing project’s files.

Verify the GitHub push
To verify that the existing project was pushed to GitHub successfully, log into the GitHub website and browse the repository. All of the files from your existing project should be visible on GitHub.

And that’s how easy it is to push an existing project to a Git or GitHub repository
