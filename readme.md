## Overview

This is a container for making a ```TexGen-11.0``` and ```python3.8``` environment. So the container can take a python script (that can use TexGen libraries and functions) as an input and produces the output.  

## Table of Contents
1. How to install Apptainer
2. How to build the container
3. How to run the container to execute various commands of TexGen and Python
4. How to convert back and forth between the ```.sif``` and ```.simg``` format
5. Some limitations

## 1. How to install Apptainer/Singularity (Linux/Mac/Windows)
Follow the instructions here based on your operating system.

https://docs.sylabs.io/guides/3.0/user-guide/installation.html


## 2. How to build the container
The basic mode creates a single container file in binary (```.sif```) after building. The definition file (```.def```) contains the script to build this container. 

```
apptainer build texgen_python_env.sif script_texgen_python.def
```

## 3. How to run the container to execute various commands of TexGen and Python
This container is set to run one command by default:
A python environment capable of importing TexGen libraries 
```
apptainer run texgen_python_env.sif [arg1] [arg2] ...
```

### An example
A sample file has been added to the ```tests``` folder. Go to that folder.
```
cd ./tests/single_yarn_voxel_abaqus/ 
```
Run the container with the python script inside this test folder.
```
apptainer run ../../texgen_python_env.sif simple.py
```
Once done, it will generate various files related to the abaqus model

## 4. How to convert back and forth between the ```.sif``` and ```.simg``` format
Often it is needed to switch between the sandbox mode (```.simg```) and the binary (```.sif```) mode for performing some tasks without rebuilding the whole container again.

```.sif```: is a container which is compressed and cannot be opened directly and the changes made will be lost, also cannot install packages.

```.simg```: is a container which basically creates a folder which can be navigated (it has the same structure as the linux machine). Easy to edit and test things, install things. But is it bulkier than the ```.sif``` container.

### (a) Convert ```.sif``` to ```.simg```
Feel free to change the names while converting to avoid overwriting.
```
apptainer build --sandbox texgen_python_env.simg texgen_python_env.sif
apptainer shell --writable texgen_python_env.simg
```

### (a) Convert ```.simg``` to ```.sif```
Feel free to change the names while converting to avoid overwriting.
```
apptainer build texgen_python_env.sif texgen_python_env.simg
apptainer shell texgen_python_env.sif
```

## 5. Some limitations
* Currently, the python that is used inside the container is ```python3.8``` whereas the recommended one for ```TexGen``` is ```python2.7```. However, there are some problems in making it work. So some functionalities might give errors.
* Do not forget to add ```from TexGen.Core import *``` to the python code in order to use ```TexGen``` functionalities.

