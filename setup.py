from setuptools import setup 

with open("requirements.txt") as f: 
    requirements = f.read().splitlines()

setup(
    name="pretend-api",
    version="1.0.0",
    description="A Python API wrapper for Pretend api",
    author="Resent",
    url="https://github.com/evictbot/pretend.api",
    install_requires=requirements,
    python_requires='>=3.8.0',
    project_urls = {
        "Documentation": "https://api.pretend.cc/docs"
    }
)
