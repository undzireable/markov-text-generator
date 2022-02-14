def load_text(filename):
    with open(filename, encoding='utf8') as f:
        return f.read().lower()