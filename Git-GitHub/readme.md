[![N|Solid](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQmnqxlkRu175fCZAGTd0O5Wi94y2-sQDRCUg&s)](#)

# Git & GitHub Guide

## Introduction
Git is a version control system that helps developers track and manage changes to code. GitHub is a cloud-based platform that enables collaboration and code sharing using Git.

---

## Installation
### Windows:
```sh
Download and install from https://git-scm.com/
```
### Linux:
```sh
sudo apt update
sudo apt install git
```
### macOS:
```sh
brew install git
```

Verify installation:
```sh
git --version
```

---

## Basic Git Commands
### 1. Configuration
```sh
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
git config --global core.editor "vim"
```
### 2. Initialize a Repository
```sh
git init
```
### 3. Cloning a Repository
```sh
git clone <repository-url>
```
### 4. Staging and Committing Changes
```sh
git add <file>  # Stage a file
git add .       # Stage all changes
git commit -m "Commit message"
```
### 5. Viewing Status and Logs
```sh
git status
git log
```
### 6. Branching
```sh
git branch            # List branches
git branch <name>     # Create a branch
git checkout <name>   # Switch to branch
git checkout -b <name>  # Create and switch to new branch
```
### 7. Merging and Rebasing
```sh
git merge <branch>
git rebase <branch>
```
### 8. Pushing Changes
```sh
git push origin <branch>
```
### 9. Pulling Changes
```sh
git pull origin <branch>
```
### 10. Stashing Changes
```sh
git stash  # Save changes temporarily
git stash pop  # Apply stashed changes
```

---

## Working with GitHub
### 1. Authenticating with GitHub
```sh
git remote add origin <repository-url>
git push -u origin main
```
### 2. Forking a Repository
- Navigate to a GitHub repository.
- Click **Fork** (top-right corner).

### 3. Creating a Pull Request
- Push changes to a forked repo.
- Go to **Pull Requests** on GitHub.
- Click **New Pull Request**.

### 4. Resolving Merge Conflicts
```sh
git merge <branch>
# Edit conflicting files
# Add and commit changes
git push origin <branch>
```

---

## Best Practices
- **Use Meaningful Commit Messages**: Clearly describe what the commit does.
- **Commit Often but Meaningfully**: Don't push unfinished or unrelated work in one commit.
- **Use Branches**: Work on new features and bug fixes in separate branches.
- **Pull Before Pushing**: Always run `git pull` before pushing to avoid conflicts.
- **Use `.gitignore`**: Exclude unnecessary files (e.g., `node_modules`, `*.log`).
- **Review Before Merging**: Use pull requests for code reviews.

---

## Summary Table
| Command | Description |
|---------|-------------|
| `git init` | Initialize a repository |
| `git clone <repo>` | Clone a repository |
| `git add <file>` | Stage a file |
| `git commit -m "msg"` | Commit changes |
| `git push origin <branch>` | Push changes to GitHub |
| `git pull origin <branch>` | Pull latest changes |
| `git branch <name>` | Create a new branch |
| `git checkout <name>` | Switch branch |
| `git merge <branch>` | Merge branches |
| `git stash` | Stash changes |

---

## Conclusion
Git and GitHub are essential tools for version control and collaboration. Following best practices will help maintain a clean and efficient workflow.
