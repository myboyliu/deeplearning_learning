# 6.py


def p(c):
    print(c)

p('a')


def get_unit_code(c):
    return c.encode('utf-8')

print(get_unit_code('我'))


def do_pass():
    pass


def p_default(log=1):

    print(log)

p_default("a")
p_default()
