## Prerequisites for containers
Need to have the singularity/apptainer (both are same now). 

https://docs.sylabs.io/guides/3.0/user-guide/installation.html

## Software dependencies
In this case, the software dependencies are downloaded into local storage to avoid repeatitive downloading every time the container is built.

**SWIG-4.0.2** 

https://sourceforge.net/projects/swig/files/swig/swig-4.0.2/swig-4.0.2.tar.gz/download

**TexGen-3.11.0**

https://github.com/louisepb/TexGen/archive/refs/tags/3.11.0.zip

**Miniconda3: (Python3.8)**

https://repo.anaconda.com/miniconda/Miniconda3-py38_4.12.0-Linux-x86_64.sh 

## Building the container

There are two modes that you can build into
(1) Sandbox mode : creates the folders that you can navigate/modify. For the initial testing. Ideal for debugging
(2) Binary mode : creates a .sif file changes to which cannot be saved after the container is closed. Ideal for production

The .def contains the script used to build this container

## Sandbox mode 
Build:
```
apptainer build --sandbox texgen_python_env.simg script_texgen_python.def
```
Run container shell after building:
```
apptainer shell --writable texgen_python_env.simg 
```
## Binary mode
Build:
```
apptainer build texgen_python_env.sif script_texgen_python.def
```
Run container shell after building:
```
apptainer shell texgen_python_env.sif 
```

## Running the container
This container is set to run one command by default:
A python environment capable of importing TexGen libraries 
```
apptainer run texgen_python_env.sif [arg1] [arg2] ...
```
