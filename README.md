# recipemd-validator

Out-of-the-box [RecipeMD](https://recipemd.org/index.html) validation hook for [pre-commit](https://pre-commit.com/).

### Usage

Add this to your `.pre-commit-config.yaml`:
```yaml
  - repo: git://github.com/gindex/recipemd-validator
    rev: v0.0.1
    hooks:
      - id: validate-recipemd
```

### Without pre-commit

If you want to use this package without pre-commit, install it using ``pip install "git+git://github.com/gindex/recipemd-validator"`` and put the following in your ``.git/hooks/pre-commit.sh``:

```sh
#!/bin/sh

if [[ !  -z "$(git diff --cached --name-only --diff-filter=ACM | grep .md$)" ]]; then
    set -e
    git diff --cached --name-only --diff-filter=ACM | grep .md$ | xargs -n 1 recipemd-validator
fi
```
