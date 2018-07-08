# RaportGenerator
Generate raport of unit tests for C/C++ projects

# Requirements
## System
* Ctags [link to repo](https://github.com/universal-ctags/ctags)
## Python requirements:
* XlsxWriter

# How to use it
## short description
```
RaportGenerator.py [-h] [-s] [-r]

Generate test reports

optional arguments:
  -h, --help         show this help message and exit
  -s, --single-file  analyze single file
  -r, --recurrent    resolve included files recurrently, only #include "" is
                     recognised
```

## detailed description

you can analyze all files ( .C .cpp .c .h .hpp) from specified directory, or by passing argument '-s' only one of them

Recurrent analyse means that if file a.c includes file a.h and in that file exists function that has implementation, 
then this function will apear in report for file a.c, becouse raport page is generated for every compilation unit
