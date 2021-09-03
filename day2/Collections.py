#* Phase 1 - No collection, go write your own ... every time
## languages like C and Pascal didn't have Data Structures built-in

#* Phase 2 - Collection through library code
#% C++, Java, C#
#% C++ - STL (Standard Template Library)     -> vector, list, map, set, ...
#% Java - JCF (Java Collection Frameworks)   -> ArrayList, HashMap, HashSet, ...
#% C# - .NET CF (.NET Collection Frameworks) -> List, Dictionary, Set, ...

#* Phase 3 - Collections built-in at language syntax 
#! Python, Javascript, Dart ..
#! Python 
#! list -> []
#! tuple -> ()     
#! set -> {}
#! dictionary -> {k:v} 

myself = ("Nitin Gopi", 30, "married", True)
print(myself)
print(myself[0])
print(myself[1])
print(myself[2])
print(myself[3])
# myself[4] = "Python, AWS" # type error -> 'tuple' object does not support item assignment
# myself[0] = "chotu" # type error -> 'tuple' object does not support item assignment
print(myself[4]) # Type error -> tuple index out of range
print((()))
