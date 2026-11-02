# Problem 9: Electricity Bill with Progressive Tiers

# (a) Create a function to calculate electricity bill
def electricity_bill(kwh):

    # Check negative input
    if kwh < 0:
        return None

    # Calculate consumption for each tier
    tier1 = min(kwh, 50)
    tier2 = min(max(kwh - 50, 0), 150)
    tier3 = max(kwh - 200, 0)

    # Calculate electricity cost
    cost = (tier1 * 480) + (tier2 * 610) + (tier3 * 730)

    # Add service fee and 10% VAT
    total = (cost + 2000) * 1.10

    return round(total)


# (b) Print electricity bill table
print("========== ELECTRICITY BILL ==========")

for kwh in [0, 35, 50, 120, 200, 350]:

    bill = electricity_bill(kwh)
    usd = bill / 4100

    print(f"{kwh} kWh -> {bill:,} riel (≈ {usd:.2f} USD)")


# (c) Ask user for monthly consumption
print("\n========== MONTHLY CONSUMPTION ==========")

user_kwh = float(input("Enter your monthly consumption (kWh): "))

bill = electricity_bill(user_kwh)

if bill is None:
    print("Invalid input! Consumption cannot be negative.")
else:
    usd = bill / 4100
    print(f"Your electricity bill is {bill:,} riel.")
    print(f"Your electricity bill is approximately {usd:.2f} USD.")