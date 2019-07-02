eng2sp = {"one": "uno", "two": "dos", "three": "tres"}

#for k in eng2sp.keys():   # The order of the k's is not defined
#   print("Got key", k, "which maps to value", eng2sp[k])

for k in eng2sp:  # simpler, .keys implicit
   print("Got key", k)

ks = list(eng2sp.keys())
print(ks)

print(list(eng2sp.values()))

print(list(eng2sp.items()))

for (k,v) in eng2sp.items():
    print("Got",k,"that maps to",v)

print("one" in eng2sp, "six" in eng2sp, "tres" in eng2sp)