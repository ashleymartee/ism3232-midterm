
from business_rules import (
    calculate_room_cost,
    get_stay_discount,
    calculate_stay_total,
    requires_credit_check,
    gets_welcome_package,
    total_reserved,
    largest_stay,
    format_stay_line,
)


def test_calculate_room_cost():
    assert round(calculate_room_cost(100.00, 3), 2) == 300.00


def test_no_discount_below_four_nights():
    assert get_stay_discount(3) == 0.0


def test_standard_discount_at_four_nights():
    assert get_stay_discount(4) == 0.06


def test_standard_discount_at_thirteen_nights():
    assert get_stay_discount(13) == 0.06


def test_long_stay_discount_at_fourteen_nights():
    assert get_stay_discount(14) == 0.18


def test_corporate_guest_gets_discount_below_four_nights():
    assert get_stay_discount(3, corporate=True) == 0.06


def test_corporate_changes_discount_answer():
    assert get_stay_discount(2, corporate=True) != get_stay_discount(2)


def test_long_stay_discount_overrides_corporate_discount():
    assert get_stay_discount(14, corporate=True) == 0.18


def test_cleaning_fee_does_not_apply_above_fee_limit():
    assert round(calculate_stay_total(200.00, 2), 2) == 400.00


def test_credit_check_below_two_thousand():
    assert requires_credit_check(1999.99) is False


def test_credit_check_at_two_thousand():
    assert requires_credit_check(2000.00) is True


def test_credit_check_above_two_thousand():
    assert requires_credit_check(2000.01) is True


def test_welcome_package_when_both_conditions_are_met():
    assert gets_welcome_package(6, 1000.00) is True


def test_no_welcome_package_at_five_nights():
    assert gets_welcome_package(5, 1200.00) is False


def test_welcome_package_at_six_nights():
    assert gets_welcome_package(6, 1000.00) is True


def test_no_welcome_package_below_total_limit():
    assert gets_welcome_package(6, 999.99) is False


def test_welcome_package_above_total_limit():
    assert gets_welcome_package(6, 1000.01) is True


def test_total_reserved_for_short_list():
    stays = [
        {"guest": "A", "nightly_rate": 100.00, "nights": 2},
        {"guest": "B", "nightly_rate": 200.00, "nights": 2},
    ]
    assert round(total_reserved(stays), 2) == 640.00


def test_largest_stay_returns_guest_with_largest_total():
    stays = [
        {"guest": "A", "nightly_rate": 100.00, "nights": 2},
        {"guest": "B", "nightly_rate": 200.00, "nights": 2},
    ]
    assert largest_stay(stays) == "B"


def test_largest_stay_keeps_first_guest_in_a_tie():
    stays = [
        {"guest": "A", "nightly_rate": 100.00, "nights": 2},
        {"guest": "B", "nightly_rate": 100.00, "nights": 2},
    ]
    assert largest_stay(stays) == "A"


def test_largest_stay_returns_empty_string_for_empty_list():
    assert largest_stay([]) == ""


def test_format_stay_line():
    result = format_stay_line("Kessler", 260.00, False, False)
    assert result == (
        "Kessler: $260.00 | credit check: no | welcome package: no"
    )
