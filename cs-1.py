

mileage = float(input("Enter vehicle mileage (km/litre): "))
fuel_price = float(input("Enter fuel price per litre (Rs): "))
n = int(input("Enter number of routes: "))

lowest_cost = float('inf')
best_route = ""

for i in range(1, n + 1):
    distance = float(input(f"Enter distance of Route {i} (km): "))

    fuel = distance / mileage
    cost = fuel * fuel_price

    print("\nRoute", i)
    print("Distance:", distance, "km")
    print("Fuel Required:", round(fuel, 2), "litres")
    print("Fuel Cost: Rs.", round(cost, 2))

    if cost < lowest_cost:
        lowest_cost = cost
        best_route = "Route " + str(i)

print("\n--- Best Route ---")
print("Most economical route:", best_route)
print("Lowest fuel cost: Rs.", round(lowest_cost, 2))
