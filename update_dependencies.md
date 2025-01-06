# devcontainer

Edit `devcontainer.json`.

# Python packages

In dev container:

```bash
pip install --requirement requirements.in pip-tools  # warning: unpinned dependency
# Consider --allow-unsafe and --generate-hashes
pip-compile --upgrade --strip-extras --newline LF --quiet --output-file=requirements.txt requirements.in
```
