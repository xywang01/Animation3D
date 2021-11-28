import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="animation3d",
    version="0.0.1",
    author="WXY",
    author_email="",
    description="A package that uses Matplotlib to create 3D/2D animations of human movement data.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xywang01/Animation3D",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'matplotlib',
        'numpy'
    ]
)
