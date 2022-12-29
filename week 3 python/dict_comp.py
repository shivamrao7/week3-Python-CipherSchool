square = {num:num**2 for num in range(1,11)}
print(square)

square = {f"Square of {num} is":num**2 for num in range(1,11)}
print(square)
for k,v in square.items():
    print(f"{k}, {v}")
