# Дан набор слов, разделённых точкой с запятой (;). Набор заканчивается двоеточием (:). Определить, сколько в нём слов, заканчивающихся буквой а
string = "Сердце;Змея;Инфекция;;Машина;Собака;Каша:"
i = 0
k = 0
for i in range(len(string)-1):
    if string[i] == "а" and string[i+1] == ";" or string[i+1] == ":":
        k = k+1
print(k)
