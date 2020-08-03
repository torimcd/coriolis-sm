# coriolis-sm
This repository contains updated code examples from "An Introduction to the Coriolis Force" by Stommel & Moore (1989).
Programs were rewritten in Python from the original GW-BASIC. 



RUN THE PROGRAMS IN A JUPYTER NOTEBOOK
--------------------------------------
Standalone Jupyter Notebook files (.ipynb) for each exercise are available in the notebooks directory. These contain full inline explanations including notes from the original text to explain each program.



RUN THE PYTHON CODE FILES
-------------------------
Pythoon code files (.py) for the full set of exercises are available in the code directory. There are comments explaining some of the code but see the notebooks for more verbose explanations. 

The coriolis_tools module contains the subroutines that are shared among multiple exercises, in the spirit of how the original program was designed. Programs that use tools from this module will fail unless it is in the same directory that the program is run from.



RUN THE ORIGINAL PROGRAMS IN GW-BASIC
----------------------------------

The original GW-BASIC programs (.bas files) can be found in the GW-BASIC directory. These programs can be run in the PC-BASIC emulator (https://robhagemans.github.io/pcbasic/) which is available for Windows, OSX, and Linux. 

CORIOLIS.bas is the full program containing all of the exercises from the book as described in section 1.2 of Stommel and Moore (1989).
Individual exercises are also provided and contain all of the subroutines that they require individually. 

ALong with each individual exercise is a text file documenting in plain language the algorithm used - ie, what they programmed in BASIC. These are the notes I used to rewrite the programs in Python, and can be used to extend the programs to other languages as desired.

To run the programs in PCBASIC, copy the .bas file to your home directory. On Windows this is usually C:\Users\YourName. On OSX and Linux this is ~
Refer to the documentation (https://robhagemans.github.io/pcbasic/doc/1.2/#mounting) in case your system is configured differently or you installed PC-BASIC to a different location.

Load the program into memory by typing LOAD "FILENAME" into the PC-BASIC terminal, where filename is the name of the .bas file you want to run. Then type RUN to start the program.
