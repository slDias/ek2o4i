# Load Balancer

Finds the most economic manner to host tasks

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


### Prerequisites

What things you need to install the software:

* [Python 3](https://www.python.org/downloads/)


### Installing

A step by step series of examples that tell you how to get a development env running

Clone this repository to your local machine

```
git clone https://github.com/slDias/ek2o4i.git
```

Open a terminal on the cloned directory and run the `load_balancer/core.py` providing the input file

```
python load_balancer/core.py input.txt
```

The proccess will generate an `output.txt` file on the current working directory

## Running the tests

The tests were written using python's builtin testing library `unittest`. To run, use the command:

```
python -m unittest discover
```
