# -- coding: utf-8 --
# @ModuleName:setup.py
# @Author:wanwan
# @Time:2021/2/14 15:28

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pytest_encode", # Replace with your own username
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=['pytest_encode'],
    python_requires='>=3.6',
    #需要安装的依赖
    install_requires=['pytest'],
    #入口模块或者入口函数
    entry_points={
        'pytest11': ['pytest-encode = pytest_encode',]
    },
    zip_safe=False

)

