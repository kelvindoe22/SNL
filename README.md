# Stem & Leaf parser? 

Stem and Leaf parser with Python.  
Help parse a stem and leaf plot into a dataset in an R file.  
You can use this on an already created R file and it'll will append to the next line.


## How to use
First you must have python install

```sh
python SNL.py  "stem & leaf plot file: compulsory" "name of r file: compulsory"
"name of dataset: optional `data` by default"
```

### Example 1
How example 1 was made
```sh
python SNL.py examples/data.txt examples/example1.r
```

### Example 2
How example 2 was made
```sh
python SNL.py examples/data.txt examples/example2.r students
```