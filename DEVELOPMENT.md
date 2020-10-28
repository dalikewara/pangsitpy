# Development

### Publish to PyPi

```bash
python setup.py sdist bdist_wheel
```

```bash
twine upload dist/*
```