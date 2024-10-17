#Join multiple sets using |

set1 = {"a", "b", "c", "d"}
set2 = {1, 2, 3}
set3 = {"@","@", "@"}
set4 = {"!", "#", "$"}

myset = set1 | set2 | set3 | set4
print(myset)