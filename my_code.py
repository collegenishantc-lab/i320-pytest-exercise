def fix_phone_num(phone_num_to_fix):

    digits = ""

    for c in phone_num_to_fix:
        if c.isdigit():
            digits += c

    if len(digits) != 10:
        raise ValueError("Phone number must contain 10 digits")

    area = digits[0:3]
    middle = digits[3:6]
    last = digits[6:]

    return f"({area}) {middle} {last}"
