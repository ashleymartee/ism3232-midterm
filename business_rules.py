
STANDARD_DISCOUNT = 0.06
LONG_STAY_DISCOUNT = 0.18
STANDARD_DISCOUNT_NIGHTS = 4
LONG_STAY_NIGHTS = 14
CLEANING_FEE = 40.00
CLEANING_FEE_LIMIT = 300.00
CREDIT_CHECK_LIMIT = 2000.00
WELCOME_PACKAGE_NIGHTS = 5
WELCOME_PACKAGE_LIMIT = 1000.00


def calculate_room_cost(nightly_rate: float, nights: int) -> float:
    """Calculate the room cost before discounts and fees."""
    return nightly_rate * nights


def get_stay_discount(nights: int, corporate: bool = False) -> float:
    """Return the discount rate for a stay."""
    if nights >= LONG_STAY_NIGHTS:
        return LONG_STAY_DISCOUNT
    if nights >= STANDARD_DISCOUNT_NIGHTS or corporate:
        return STANDARD_DISCOUNT
    return 0.0


def calculate_stay_total(
    nightly_rate: float, nights: int, corporate: bool = False
) -> float:
    """Calculate the total stay cost after discount and cleaning fee."""
    cost = calculate_room_cost(nightly_rate, nights)
    cost *= 1 - get_stay_discount(nights, corporate)
    if cost <= CLEANING_FEE_LIMIT:
        cost += CLEANING_FEE
    return cost


def requires_credit_check(total: float) -> bool:
    """Return whether the total requires a credit check."""
    return total >= CREDIT_CHECK_LIMIT


def gets_welcome_package(nights: int, total: float) -> bool:
    """Return whether the stay qualifies for a welcome package."""
    return nights > WELCOME_PACKAGE_NIGHTS and total >= WELCOME_PACKAGE_LIMIT


def total_reserved(stays: list) -> float:
    """Calculate the combined total for all stays using a loop."""
    total = 0.0
    for stay in stays:
        total += calculate_stay_total(
            stay["nightly_rate"],
            stay["nights"],
            stay.get("corporate", False),
        )
    return total


def largest_stay(stays: list) -> str:
    """Return the guest name for the largest stay using a loop."""
    largest_total = -1.0
    guest_name = ""
    for stay in stays:
        total = calculate_stay_total(
            stay["nightly_rate"],
            stay["nights"],
            stay.get("corporate", False),
        )
        if total > largest_total:
            largest_total = total
            guest_name = stay["guest"]
    return guest_name


def format_stay_line(
    guest: str, total: float, credit_check: bool, welcome_package: bool
) -> str:
    """Format the stay details as one readable line."""
    credit = "yes" if credit_check else "no"
    welcome = "yes" if welcome_package else "no"
    return (
        f"{guest}: ${total:.2f} | credit check: {credit} "
        f"| welcome package: {welcome}"
    )
