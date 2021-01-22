
from setuptools import setup, find_packages
import re

# https://stackoverflow.com/questions/17791481/creating-a-version-attribute-for-python-packages-without-getting-into-troubl/41110107
def get_property(prop, project):
    result = re.search(r'{}\s*=\s*[\'"]([^\'"]*)[\'"]'.format(prop), open(project + '/__init__.py').read())
    return result.group(1)

project_name = 'greetings'
setup(
    name = "Greetings",
    #version = "0.1.0",
    version = get_property('__version__', project_name),
    packages = find_packages(exclude=['*test']),
    install_requires = ['argparse'],
    entry_points={
        'console_scripts': [
            'greet = greetings.command:process'
        ]}
    )



