name: str = input("Enter your name: ").strip()
quarters_count: int = int(input("Enter the number of quarters: "))
dimes_count: int = int(input("Enter the number of dimes: "))
nickels_count: int = int(input("Enter the number of nickels: "))
pennies_count: int = int(input("Enter the number of pennies: "))

total_cents: int = (
    25 * quarters_count
    + 10 * dimes_count
    + 5 * nickels_count
    + pennies_count
)

print(f"{name}, your total coin value is {total_cents} cents.")