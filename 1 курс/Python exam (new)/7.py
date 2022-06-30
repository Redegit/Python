fraction = input().split('/')
n, m = int(fraction[0]), int(fraction[1])
l = [n, m]


def simplify_tuple(n, m):
    for i in range(2, n+1):
        if n % i == 0 and m % i == 0:
            n = n // i
            m = m // i
            return simplify_tuple(n, m)
    else:
        return n, m


def simplify_list(__self__):
    n = __self__[0]
    m = __self__[1]
    for i in range(2, n+1):
        if n % i == 0 and m % i == 0:
            __self__[0] = n // i
            __self__[1] = m // i
            simplify_list(__self__)


print(simplify_tuple(n, m))
simplify_list(l)
print(l)
