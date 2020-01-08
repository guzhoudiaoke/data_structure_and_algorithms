import math


def evaluate(exp):
    if exp is None or len(exp) == 0:
        return 0

    ops = []
    vals = []

    for s in exp.split():
        if s == '(':
            pass
        elif s in ('+', '-', '*', '/', 'sqrt'):
            ops.append(s)
        elif s == ')':
            op = ops.pop()
            v = vals.pop()
            if op == '+':
                v = vals.pop() + v
            elif op == '-':
                v = vals.pop() - v
            elif op == '*':
                v = vals.pop() * v
            elif op == '/':
                v = vals.pop() / v
            elif op == 'sqrt':
                v = math.sqrt(v)

            vals.append(v)
        else:
            print(s)
            vals.append(float(s))

    return vals.pop()


def test_evaluate():
    print(evaluate('( 1 + ( ( 2 + 3 ) * ( 4 * 5 ) ) )'))
    print(evaluate('( ( 1 + sqrt ( 5.0 ) ) / 2.0 )'))


if __name__ == '__main__':
    test_evaluate()
