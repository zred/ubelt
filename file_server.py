import os
from flask import Flask, send_from_directory
from collections import deque
import click

app = Flask(__name__)

@app.route('/<path:path>')
def serve_file(path: str) -> None:
    """Serve a file from the specified PATH."""
    directory = os.getcwd()
    return send_from_directory(directory=directory, path=path)

@app.route('/')
def link_files() -> str:
    links = []
    files = [_ for _ in os.listdir('.') if not os.path.isdir(_)]
    for file in files:
        link = f'<a href="/{file}/">{file}</a>'
        links.append(link)
    return '<br>'.join(links)

def serve_files(path: str, port: int) -> None:
    """Serve files from PATH on PORT."""
    os.chdir(path)
    app.run(host='0.0.0.0', port=port)

def tail_file(file: str, n: int) -> None:
    with open(file) as f:
        for line in deque(f, n):
            click.echo(line, nl=False)