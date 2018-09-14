from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='allWords',
    entry_points={'console_scripts': [
        'allwords = allwords.wordstat:get_arg',
    ]},
    version='0.1',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Avderevo/allWords',
    description='This application counts parts of speech in the names inside your code',
    classifiers=[
        'Development Status :: 1 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5.2',
    ],
    keywords='word statistics, verb, noun',
    author='Yury Avdeev',
    author_email='avdevman@gmail.com',
    license='MIT',
    python_requires='>=3.5.2',
    zip_safe=False
)