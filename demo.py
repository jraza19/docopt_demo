# author: Tiffany Timbers
# modified by: Javairia Raza
# date: 2020-11-19

"""This script prints out docopt args.
Usage: docopt.py <arg1> --arg2=<arg2> [--arg3=<arg3>] [--arg4=<arg4>]

Options:
<arg>             Takes any value (this is a required positional argument)
--arg2=<arg2>     Takes any value (this is a required argument)
[--arg3=<arg3>]   Takes any value (this is an optional argument)
[--arg4=<arg4>]   Takes any value (this is an optional argument)
"""

from docopt import docopt
opt = docopt(__doc__)

def main(opt):
      return print(opt), print(type(opt)), print(opt["--arg4"])
    
if __name__ == "__main__":
      main(opt)
 
