from my_code import fix_phone_num
import pytest

def test_fix_phone_num():
    assert fix_phone_num("5125558823") == "(512) 555 8823"
    assert fix_phone_num("5554429876") == "(555) 442 9876"
    assert fix_phone_num("3216543333") == "(321) 654 3333"

def test_invalid_length():
    with pytest.raises(ValueError):
        fix_phone_num("555-442-98761")

    with pytest.raises(ValueError):
        fix_phone_num("(3213) 654 3333")

def test_non_digit_characters():
    with pytest.raises(ValueError):
        fix_phone_num("334dfdee45")

    with pytest.raises(ValueError):
        fix_phone_num("abcdefghij")
