from setuptools import setup

with open("Readme.md", "r") as fh:
    long_description = fh.read()

setup(
    name='vk_poster',
    version='0.1.0',    
    description='Package for VK wall posting',
    url='https://github.com/snussik/vk_poster.git',
    author='snussik',
    author_email='snussik@snussik.com',
    package_dir={"":"src"},
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='BSD 2-clause',
    packages=['vk_poster'],
    install_requires=['vk_api'],

    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",     
        'Programming Language :: Python :: 3.8',
    ],
)