import subprocess # imports the Popen below
# The subprocess module allows you to spawn new processes, 
# connect to their input/output/error pipes, and obtain their return codes. 
# https://docs.python.org/3/library/subprocess.html
import sys
# This module provides access to some variables used 
# or maintained by the interpreter and to functions that
# interact strongly with the interpreter.

def dump(url): # this tool will allow us to easily get backups from a PostgreSQL database.
    return subprocess.Popen(['pg_dump',url], stout=subprocess.PIP)
    # utilizing subprocess.PIPE to capture Stdout into a file-like object 
    # and prevent it from being written to the terminal when we run 
    # this code.
    except OSError as err:
    print(f"Error: {err}")
    sys.exit(1)
# The subprocess.Popen can raise an OSError so we're going to wrap
# that call in a try block, print the error message, 
# and use sys.exit to set the error code.

#REPL
#(pgbackup) $ PYTHONPATH=./src python
# >>> from pgbackup import pgdump
# >>> dump = pgdump.dump('postgres://demo:password@54.245.63.9:80/sample')
# >>> f = open('dump.sql', 'w+b')
# >>> f.write(dump.stdout.read())
# >>> f.close()
