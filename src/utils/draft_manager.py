import os

DRAFTS_DIR = os.path.join('data', 'drafts')

def save_draft(filename, content):
    """Save a draft to the drafts folder."""
    os.makedirs(DRAFTS_DIR, exist_ok=True)
    path = os.path.join(DRAFTS_DIR, filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    return path

def load_draft(filename):
    """Load a draft from the drafts folder."""
    path = os.path.join(DRAFTS_DIR, filename)
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def list_drafts():
    """List all draft files."""
    os.makedirs(DRAFTS_DIR, exist_ok=True)
    return [f for f in os.listdir(DRAFTS_DIR) if f.endswith('.md') or f.endswith('.txt')]
