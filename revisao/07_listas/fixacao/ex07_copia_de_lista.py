import copy

a = [1, 2, 3]
b = a
print(f"A id: {id(a)}, B id: {id(b)}")

print("\nCORRIGINDO 1º FORMA")
b = a.copy()
print(f"A id: {id(a)}, B id: {id(b)}")

print("\nCORRIGINDO 2º FORMA")
b = list(a)
print(f"A id: {id(a)}, B id: {id(b)}")

print("\nCORRIGINDO 3º FORMA")
b = copy.deepcopy(a)
print(f"A id: {id(a)}, B id: {id(b)}")
