# allWords

This program creates statistics of the most frequent verbs or nouns in variable names, function names, class names.
This version of the project loads the repository from the githab and analyzes the code written on the python.

## Requirements:

- python 3.5+
- NLTK
- AST

## Install:

```
$ pip3 install git+https://github.com/Avderevo/allWords  

```
Or clone project
and install the modules from the requirements.
```
$ git clone https://github.com/Avderevo/allWords
```
Then go to the project directory.

```
$ cd allWords
$ pip3 install requirements.txt
```


### :point_right: To run the project, the NLT module requires the installation of the library:exclamation:

```
$ python3
>>> import nltk
>>> nltk.download('averaged_perceptron_tagger')
```
# Use






###  To start, you must specify the required arguments:


1. script name: **main.py**
2. url of the github repository: ***some of githab repository***
3. one of the names of objects: **func, class, variable**
4. part of speech: **verb, noun**
5. format of result: **json, csv, console**



### Example:

```
$ python3 main.py https://github.com/Avderevo/word-statistic func noun json
```

