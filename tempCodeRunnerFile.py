laptop = {
    "brand": "Apple",
    "model": "MacBook Pro",
    "processor": "M1 Pro",
    "ram": 16
}

print(laptop.get("processor"))
laptop.update(
    {"storage":512,
     "ram":32,
    }
)

for key in laptop.keys():
    print(key)

for value in laptop.values():
    print(value)

for key,value in laptop.items():
    print(key,":",value)

remove=laptop.pop("ram")
print(remove)
laptop.setdefault("gpu",["integrated" ])
