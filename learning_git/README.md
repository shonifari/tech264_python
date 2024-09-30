# Basic Git understanding

Go to your folder of choice: 

```bash
cd /OneDrive/Documents/Github/tech264-test-git
```

## Initialise the repository: 

```bash
git init
```

## Add file to stage:
```bash
git add <file_path>
```

## Commit changes: 

```bash
git commit -m "<Commit message>"
```

## Check the changes

```bash
git log
```

## Switching branch or restoring files
The git checkout command is quite versatile in Git. Here are its primary uses:

* Switching Branches: You can use git checkout to switch between different branches in your repository. 
This will switch to the main branch.
```bash
git checkout main
```

* Creating New Branches: You can create and switch to a new branch in one step with git checkout -b new-branch .
```bash
git checkout -b new-branch
```
* Restoring Files: If you want to discard changes in your working directory and revert to the last committed state, you can use:
```bash
 git checkout -- <file>
```
* Checking Out Commits: You can also view a specific commit using hash: 
```bash
 git checkout <commit-hash> 
```


```bash
git checkout HEAD~1 -- README.md
```


## This command adds a remote repository to your local Git repository.
```bash
git remote add origin <github account>
```


## This command renames your current branch to main.
The -M flag is used to forcefully rename the branch.
```bash
git branch -M main
```


## This command pushes your local main branch to the remote repository named origin.
The -u flag sets the upstream tracking reference, meaning your local main branch will be linked to the remote main branch. This makes future pushes and pulls easier, as you won’t need to specify the branch name each time.
```bash
git push -u origin main
```

## Danger: If the sensitive file is still accessible in a previous commit
 
SOLUTION:
* Option 1: Remove previous commits with that file (e.g. use 'git reset' DANGEROUS - YOU COULD LOSE WORK)
```bash
git reset
```
* Option 2: 
  > 1. Remove GitHub repo (Now safe!)
  > 2. Remove sensitive from your local file
  > 3. Remove .git folder from your local repo