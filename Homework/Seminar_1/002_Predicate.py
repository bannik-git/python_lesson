x, y, z = [True, False], [True, False], [True, False]

print(f"X \tY \tZ \t¬(X ⋁ Y ⋁ Z) \t¬X ⋀ ¬Y ⋀ ¬Z  \tРезультат")

for i in x:
    for j in y:
        for k in z:
            print(f"{i} \t{j} \t{k} \t{not(i or j or k)} \t        {not(i) and not(j) and not(k)} \t        {not(i or j or k) == (not(i) and not(j) and not(k))}")

