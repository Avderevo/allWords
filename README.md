# Analysis and counting of frequent words of code

This program creates statistics of the most frequent verbs or nouns in variable names, function names, class names.

This version of the project loads the repository from the githab and analyzes the code written on the python.

The result can be obtained in one of three formats:

 - json
 - csv
 - console


### Install modules:

``` 
   $ pip install requirements.txt   
```


### To start, you must specify the required arguments:


1. script name: **main.py**
2. url of the github repository: ***some of githab repository***
3. one of the names of objects: **func, class, variable**
4. part of speech: **verb, noun**
5. format of result: **json, csv, console**



### Example:

```
$ python3 main.py https://github.com/Avderevo/word-statistic func noun json
```

