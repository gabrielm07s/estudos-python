num = int(input("Tabuada de: "))

print("=" * 21)
print(f"|| {f'TABUADA DO {num}':^15} ||")
print("=" * 21)

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
