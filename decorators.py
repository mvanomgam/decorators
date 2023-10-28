import logging

########################################################

# First set up a logger to use logging instead of printing:

# logger will be created if it does not exist.
logger = logging.getLogger(__name__)

# set the log level on the logger
logger.setLevel(logging.INFO)

# create a formatter for the logger to format the output
formatter = logging.Formatter('%(message)s ')

########################################################
# This part is optional and only neccessary when results must be logged to a file.

# create a file handler to specify the file that will be logged to.
file_handler = logging.FileHandler('decorators.log')

# add the formatter to the file handler and set the level to be logged to the log file.
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.INFO)

# add the file handler to the logger 
logger.addHandler(file_handler)

########################################################

# set up a stream handler to display code results
stream_handler = logging.StreamHandler()

# add the formatter to the stream handler
stream_handler.setFormatter(formatter)

# add the stream handler to the logger
logger.addHandler(stream_handler)

########################################################

logger.info("\n-------------------------------------\n")

# a decorator takes another function as an arguement

# 1. function decorators

def decorator(func):
  def wrapper ():
    print('Do something before ...')
    func()
    print('Do something after ...')
  return wrapper

def name():
  print('Mvano')

# call the decorator and store the output in a funcation variable.
myName = decorator(name)
# then call the function variable 
myName()

logger.info("\n-------------------------------------\n")

def decorator(func):
  def wrapper ():
    print('Do something before ...')
    func()
    print('Do something after ...')
  return wrapper

# instead of calling the decorator and store the output in a funcation variable, use @ symbol:

@decorator
def name():
  print('Cecilia')

# then call the actual function instead of the function variable 
name()

logger.info("\n-------------------------------------\n")

def decorator(func):
  def wrapper (*args, **kwargs):
    print('Do something before ...')
    result = func(*args, **kwargs)
    print('Do something after ...')
    return f"Return the result: {result}"
  return wrapper

# instead of calling the decorator and store the out in a funcation variable, use @ symbol:

@decorator
def add(x, y):
  return x + y

# then call the actual function instead of the function variable 
logger.info(add(5, 10))

logger.info("\n-------------------------------------\n")

# identity and name of the function arguement 
logger.info(help(add))
logger.info(add.__name__)

# the above function is incorrectly identified by python and it can be fixed as follows:

import functools

# add a decorator on the func input

logger.info("\n-------------------------------------\n")

def decorator(func):
  @functools.wraps(func)
  def wrapper (*args, **kwargs):
    print('Do something before ...')
    result = func(*args, **kwargs)
    print('Do something after ...')
    return f"Return the result: {result}"
  return wrapper

# instead of calling the decorator and store the out in a funcation variable, use @ symbol:

@decorator
def add(x, y):
  return x + y

# then call the actual function instead of the function variable 
logger.info(add(5, 5))

logger.info("\n-------------------------------------\n")

# identity and name of the function
logger.info(help(add))
logger.info(add.__name__)

logger.info("\n-------------------------------------\n")

# example: a function that repeats something a number of times:

def repeat(numTimes):
  def repeatDecorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
      for _ in range(numTimes):
        Result = func(*args, **kwargs)
      return Result # wrapper result
    return wrapper # repeatDecorator result
  return repeatDecorator # repeat function result 

@repeat(numTimes=5)
def great(name):
  logger.info(f"Hello {name}!")

# call the function 
great('Mvano')

logger.info("\n-------------------------------------\n")

# identity and name of the function
logger.info(help(great))
logger.info(great.__name__)

########################################################

logger.info("\n-------------------------------------\n")

def debuger(func):
  @functools.wraps(func)
  def wrapper (*args, **kwargs):
    # extract the args, kwargs and the name
    args_repr = [repr(a) for a in args]
    kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
    signature = ", ".join(args_repr + kwargs_repr)
    
    # print the name and executes the function 
    print(f"Calling {func.__name__} ({signature})")
    Result = func(*args, **kwargs)
    print(f"{func.__name__!r} ({signature})) returned {signature!r}")
    return Result
  return wrapper

def decorator(func):
  @functools.wraps(func)
  def wrapper (*args, **kwargs):
    print('Start executing func ...')
    result = func(*args, **kwargs)
    print('End executing func ...')
    return f"Return the result: {result}"
  return wrapper

@debuger
@decorator
def hello(name):
  greeting = f"Hello {name}"
  print(greeting)
  return greeting

# the debuger function will be executed first and then inside the debuger function the decorator will be executed
# the hello function will be executed inside the decorator
hello("Mvano")
########################################################

# 2. class decorators
# used to maintain or update a state

logger.info("\n-------------------------------------\n")

class CountCalls:
  def __init__(self, func):
    self.func = func
    self.numCalls = 0
  
  # implement the class decorator 
  
  def __call__(self, *args, **kwargs):
    print("Hi there!")

# create an instance of the class
countCalls = CountCalls(None)

# execute the instance as a function
countCalls()

@CountCalls
def hello():
  logger.info("Hello")
  
logger.info("\n-------------------------------------\n")

class CountCalls:
  def __init__(self, func):
    self.func = func
    self.numCalls = 0
  
  # implement the class decorator 
  
  def __call__(self, *args, **kwargs):
    self.numCalls += 1
    print(f"This is executed {self.numCalls} times")
    return self.func(*args, **kwargs)

@CountCalls
def hello():
  logger.info("Hello")
  
hello()
hello()
hello()
hello()
hello()

logger.info("\n-------------------------------------\n")