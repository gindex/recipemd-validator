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
