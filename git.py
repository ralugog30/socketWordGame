from git import Repo

# Path to your existing git repository
repo_path = '/path/to/your/repository'

# Initialize the repository object
repo = Repo(repo_path)

# Add files to the staging area
file_paths = ['file1.py', 'file2.py']  # List of file paths you want to commit
repo.index.add(file_paths)

# Commit changes
commit_message = 'Your commit message here'
repo.index.commit(commit_message)

# Optionally, push changes to remote repository
# If you want to push changes to a remote branch
# repo.remotes.origin.push()
