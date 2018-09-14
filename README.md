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
The program can store the results in formatst:
- json
- csv
or outputting the result to the console
 
# Use


###  To start, you must specify the required arguments:
```
usage: allwords [-h] [-d DIR_PATH] [-t TOP_SIZE] [--repo REPO_URL]
                [-c {noun,verb}] [-n {var,func,class}] [-o {console,file}]
                [--format {json,csv}] [--ext EXTENSION]
```
### Arguments:
```
optional arguments:
  -h, --help            show this help message and exit
  
  -d DIR_PATH, --dirs DIR_PATH
                        The path to the local project.
                        
  -t TOP_SIZE, --top TOP_SIZE
                        The size of the top verbs, default is 10.
                        
  --repo REPO_URL       URL of the project repository.
  
  -c {noun,verb}, --category {noun,verb}
                        Select a "noun" if you want statistics of nouns.Or
                        "verb" if statistics verbs. "verb" are by default.
                        
  -n {var,func,class}, --name {var,func,class}
                        Choose: "verb" - if you keep verbs."noun" - if you
                        want nouns."class" - if you want statistics on classe
                        names
                        
  -o {console,file}, --output {console,file}
                        Report output method.Possible value: console - output
                        result script to console, file - output result script
                        to file.
                        
  --format {json,csv}   Report output format.Possible value: json - save
                        report in json format, csv - save report in csv
                        format.
```
### Example:

Outputting the result to the console.
```
$ allwords --repo https://github.com/Avderevo/IZORM  -c noun  -n func -o console

  Top 10 nouns:
  field      --- 5
  arg        --- 4
  filter     --- 3
  update     --- 3
  order      --- 3
  args       --- 2
  name       --- 2
  connect    --- 2
  list       --- 2
  cursor     --- 2

```
Save to file:
```
$ allwords --repo https://github.com/Avderevo/IZORM  -c verb  -n func -o file --format json

The result file is saved to the directory "/tmp/words_statistic_qvygrjc1"

```
