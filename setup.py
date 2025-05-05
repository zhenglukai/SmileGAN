import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SmileGAN",
    version="0.1.4",
    author="zhijian.yang",
    author_email="zhijianyang@outlook.com",
    description="A python implementation of Smile-GAN for semisupervised clustering",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zhenglukai/SmileGAN",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    install_requires=[         
        'numpy>=1.22.3',
        'tqdm>=4.50.2',
        'torch>=1.10.2',
        'scikit-learn>=0.24.2',
        'scipy>=1.8.0',
        'pandas>=1.4.2'
    ]
)

