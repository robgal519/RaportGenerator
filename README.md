# RaportGenerator
Generate report of unit tests for C/C++ projects

# Requirements
## System
* Ctags [link to repo](https://github.com/universal-ctags/ctags)
( on windows unpack binaries and put ctag.exe in this project directory)
## Python requirements:
* XlsxWriter

# How run this on windows ?

1. make sure that you have installed python 3.6 or higher [python](https://www.python.org/)
2. make sure that you have git installed ( not necessary ) [git](https://git-scm.com/)
3. download this project ( and unpack if needed )
4. make sure that ctags.exe is in project directory ( RaportGenerator )
5. open CMD ( i know scary ... ) 
6. install virtualenv (`py -m pip install virtualenv`)
7. generate venv (`py -m virtualenv venv`)
9. get into venv (`venv\Scripts\activate`)
10. get to project directory ( 'cd' and 'dir' commands will be helpful )
11. type `py -m pip install -r requirements.txt`
12. use the script by typing `RaportGenerator.py -h`
    
# How to use it on superior Linux system

1. python is always pre-installed, but make sure that you have python3
2. git is always pre-installed so use it to download this repo
3. for convenience you can put this script in venv ( we keep our system clean and tidy)
4. install virtualenv ( pip install virtuelenv)
5. create venv (`virtualenv venv`)
6. get into venv (`source venv/bin/activate`)
7. install requirements ( `pip install -r requirements.txt`)
8. use the script by typing `RaportGenerator.py -h`

There is no need for using venv, and if you don't want to you can go straight to installing requirements, but those will be installed globally, abut every responsible user should keep its system tidy 

# How to use it
## short description
```
RaportGenerator.py [-h] [-s] [-r]

Generate test reports

optional arguments:
  -h, --help         show this help message and exit
  -s, --single-file  analyse single file
  -r, --recurrent    resolve included files recurrently, only #include "" is
                     recognised
```

## detailed description

you can analyse all files ( .C .cpp .c .h .hpp) from specified directory, or by passing argument '-s' only one of them

Recurrent analyse means that if file a.c includes file a.h and in that file exists function that has implementation, 
then this function will appear in report for file a.c, because report page is generated for every compilation unit
