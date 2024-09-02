from setuptools import find_packages,setup
from typing import List

trigger='-e .'

def get_requirements(file_path: str) -> List[str]:
    requiremetns=[]

    with open(file_path) as file:
        requiremetns=file.readlines()
        requiremetns=[req.replace('\n','') for req in requiremetns]

        if trigger in requiremetns:
            requiremetns.remove(trigger)

    return requiremetns

setup(
    name='Krish',
    version='0.0.1',
    author='leson207',
    author_email='sonthaile2002@gmail',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)

# use "pip install -e ." before "pip install requirements.txt"