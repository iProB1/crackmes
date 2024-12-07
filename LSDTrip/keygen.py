def generate_key():
    target = 895
    length = 4
    newline_ascii = 10

    valid_ascii = list(range(48, 58)) + list(range(65, 91)) + list(range(97, 123))

    for c1 in valid_ascii:
        for c2 in valid_ascii:
            for c3 in valid_ascii:
                for c4 in valid_ascii:
                    v1 = (1 * c1) + (2 * c2) + (3 * c3) + (4 * c4)
                    if v1 == target:
                        return ''.join(chr(c) for c in [c1, c2, c3, c4]) + chr(newline_ascii)

password = generate_key()
print("Password:", repr(password)) 
