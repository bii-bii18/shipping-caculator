# shipping_calculator.py

def calculate_shipping_cost(weight, distance):
    rate_per_kg = 2.0  # Example rate per kilogram
    cost = weight * distance * rate_per_kg
    return cost

print("Shipping cost:", calculate_shipping_cost(5, 100))
