from business_rules import (
    calculate_stay_total,
    requires_credit_check,
    gets_welcome_package,
    total_reserved,
    largest_stay,
    format_stay_line,
)

stays = [
    {"guest": "Kessler", "nightly_rate": 110.00, "nights": 2, "corporate": False},
    {"guest": "Lindqvist", "nightly_rate": 150.00, "nights": 2, "corporate": True},
    {"guest": "Moreno", "nightly_rate": 125.00, "nights": 6, "corporate": False},
    {"guest": "Nakata", "nightly_rate": 140.00, "nights": 20, "corporate": False},
    {"guest": "Osei", "nightly_rate": 95.00, "nights": 15, "corporate": True},
    {"guest": "Petrov", "nightly_rate": 200.00, "nights": 5, "corporate": False},
    {"guest": "Quinn", "nightly_rate": 180.00, "nights": 6, "corporate": False},
    {"guest": "Rahman", "nightly_rate": 260.00, "nights": 10, "corporate": True},
]

print("Seabreeze Inn - Stay Report")

for stay in stays:
    total = calculate_stay_total(
        stay["nightly_rate"],
        stay["nights"],
        stay["corporate"],
    )
    credit_check = requires_credit_check(total)
    welcome_package = gets_welcome_package(stay["nights"], total)

    print(
        format_stay_line(
            stay["guest"],
            total,
            credit_check,
            welcome_package,
        )
    )
stay_count = 0
credit_check_count = 0
welcome_package_count = 0

for stay in stays:
    stay_count += 1

    total = calculate_stay_total(
        stay["nightly_rate"],
        stay["nights"],
        stay["corporate"],
    )

    if requires_credit_check(total):
        credit_check_count += 1

    if gets_welcome_package(stay["nights"], total):
        welcome_package_count += 1
total = total_reserved(stays)
average = total / stay_count if stay_count > 0 else 0.0
largest = largest_stay(stays)
print(f"Stays: {stay_count}")
print(f"Total reserved: ${total:.2f}")
print(f"Average stay total: ${average:.2f}")
print(f"Largest stay total: {largest}")
print(f"Credit checks required: {credit_check_count}")
print(f"Welcome packages: {welcome_package_count}")
