# pyasdm
ASDM backend for the VIPER framework.

Note that some code is generated from the ASDM model by templates kept
in the almasw code repo. Changes made here may be lost if not also
made in the appropriate template. Generated code is clearly marked
as generated in the code. The generated code is ugly and not very
readable. To improve that, and to make it easy to update the copy of
the generated code here, all of the code in this module has been 
run through the python [black formatter](https://pypi.org/project/black/).

## build instructions
A virtual python environment is recommended.
```
python3 -m pip install build
python3 -m build
```
pyasdm can then installed from the resulting build (wheel or tar file) found in the dist directory.
