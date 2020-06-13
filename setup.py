from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name="django-settings-json",
    version="1.0.2",
    author="Andre Pereira",
    author_email="django-settings-json@aper.com.br",
    description="Django Settings JSON is a small package for helping you have environment variables when you can't use them directly from your operational system.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/andrebr/django-settings-json",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)
