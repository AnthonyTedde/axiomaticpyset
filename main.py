import itertools
# FA. For all
# EQ. Equivalence <->

################################################################################
# Extensionality
# FA. u(U in X <-> U in Y) <-> X = Y
################################################################################
X = set(range(1, 5)) # {1, 2, 3, 4)
Y = {1, 2, 3, 4, 1, 2, 3, 4}

X == Y # Sets are equals because duplicate information in not recorded.

################################################################################
# Pairing
# FA. a FA. b Ex. c FA. x (x in c <-> x = a or x = b)
################################################################################
# We define a small domain of integer value as the universe.
universe = set(range(1, 1001))
a = 10
b = 500

# Based on the definition of pairing:
{x for x in universe if x == a or x == b}

# OrderedSet
# Start with ordered list:
osl = [x for x in range(4, 16)]
osl = [3, 1, 5, 2, 6, 12]

# In python Orderset Does not exist by default. According to axiomatic set
# theory:
# An ordered set such as (a, b) can be written as {{a}, {a, b}}
# Same logic for (a, b, c): {{a}, {a, b}, {a, b, c}}
oslx = [osl[0:i] for i in range(1, len(osl) + 1)]
os = set(map(frozenset, oslx))

# Get the order of all items in the set:
fs = frozenset.intersection(*os).difference(fs)
os.remove(fs)

os = set(map(frozenset, oslx))
def get_order(v, dif = None):
    val = []
    fs = frozenset.intersection(*v)
    if dif:
        rem = fs.difference(dif)
    else:
        rem = fs
    v.remove(fs)
    val.append(list(rem))
    if len(v):
        val += get_order(v, dif = fs)
    return val

a = get_order(os.copy())



