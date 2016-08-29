import subprocess # for running subprocesses like we are in the command line

def launch_notebook( filepath ):
    """ Launch a python notebook for the user. To make their life easier. """
    raise NotImplementedError

## This might be a problem as we won't know which editor to open...
## Also the opening process will be diffenent for different systems.
## Even finding the "default" way to open a .py file for editing might be
## different across systems.
##
## SOLUTION: Just open default .txt editor and say "it's a good thing you're working barebones. No crutches."
##
def launch_python_script( filepath ):
    """ Launch an editor for the named python script. """
    raise NotImplementedError
