import os

def save_draft(content, filename):
    with open(os.path.join('data/drafts', filename), 'w') as f:
        f.write(content)
