import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
with open('requirements.txt') as f:
    install_requires = f.read().splitlines()
setuptools.setup(
    name="pangsitpy",
    version="0.0.8",
    author="Dali Kewara",
    license="MIT",
    author_email="dalikewara@gmail.com",
    description="Pangsit(py) is my starter pack framework represented in Python to deal with learning computing such as Machine/Deep Learning, Data Science, etc.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dalikewara/pangsitpy",
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    keywords = ['python', 'machine learning', 'deep learning', 'data science', 'framework'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)
