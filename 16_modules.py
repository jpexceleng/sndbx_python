# a module is a way to put definitions in a file and use them in a a script;
# definitions from a module can be imported into other modules or into the
# main module.
#
# the module name is the file name with the suffix '.py' appended.
# the module name can be accessed via the global variable '__name__'

# import fib module from modules directory; you would need to prefix all 
# definitions used with 'modules.fibo':
# import modules.fibo

# import fibo and reference using an alias
import modules.fibo as fibo

# import specific definitions from module
from modules.fibo import fib2

# use definitions from module:
print(fibo.fib(1000))
print(fib2(1000))
print(fibo.__name__)