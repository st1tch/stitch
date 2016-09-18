import z3

def main():
    s = z3.Solver()
    x, y, z = z3.Ints('x y z')

    s.add(x*x + y*y == z*z)
    s.add(x > 0, y > 0, z > 0)
    s.add(z < 100)

    # get the all the models
    models = []
    while True:
        if s.check() == z3.unsat:
            break
        m = s.model()
        models.append((m[x].as_long(), m[y].as_long(), m[z].as_long()))
        s.add(z3.Not(z3.And(x==m[x], y==m[y], z==m[z])))

    i = 1
    models.sort()
    for (xval, yval, zval) in models:
        print("{}: x = {}, y = {}, z = {}".format(i, xval, yval, zval))
        i += 1

if __name__ == '__main__':
    main()
