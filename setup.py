from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="gAAC",
    version="0.1.0",
    author="HaShaWB",
    author_email="whitebluej@kaist.ac.kr",
    description="AI-powered service that converts natural language to personalized AAC symbols for language-impaired communication",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HaShaWB/generative-AAC",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.9",
    install_requires=requirements,
)