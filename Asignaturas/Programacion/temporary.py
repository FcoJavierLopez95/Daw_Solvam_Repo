tiro_a =["libre", "libre", "triple", "libre", "area", "triple", "libre", "triple", "area"]
libre_a =0
area_a =0
triple_a = 0


for i in range (len(tiro_a)):
    if tiro_a[i] == "libre":
        libre_a += 1
    elif tiro_a[i] == "area":
            area_a += 1
    elif tiro_a[i] == "triple":
            triple_a += 1
    print(i)
    print(tiro_a[i])



print("libres" \
":",libre_a)
print("areas:",area_a)
print("triples:",triple_a)