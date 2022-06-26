def Inmode(e):
  print('This is result -> %s'%e)

Inmode('Hello In-mode')


def Outmode():
  result = 'Hello Out-mode'
  return print(result)

Outmode()


def InAndOutmode(e):
  result = ''
  result += e
  return print(result)

InAndOutmode('Hello In and Out Mode')