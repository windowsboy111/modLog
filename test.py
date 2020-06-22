import logging
logger = logging.Logger()
logger.debug('hi')
def wow(message):
    print("wow " + message)
logger.lvl(name='hi',fn=wow)
# => alternate
"""\
@logger.lvl(name='hi')
def wow(messsage):
    print("wow" + message)
""" # <= alternate
logger.set_default_lvl('wow')
logger.hi('this is nice') # pylint: disable=no-member # pylint has a bug that treats methods added with logger.lvl() do not exist.
print(logger.get())