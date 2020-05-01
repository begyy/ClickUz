import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ClickUz",
    version="0.1",
    author="Sadullayev Bekhzod",
    author_email="begymrx@gmail.com",
    description="ClickUz",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.5",
    install_requires=['requests', 'django', 'djangorestframework'],
    url="https://github.com/begyy/ClickUz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ]
)
