def get_valid_count():
    while True:
        try:
            count = int(input("How many Fibonacci numbers do you want to print (1-20, or 0 to exit)? "))
        except ValueError:
            print("Please enter a whole number between 0 and 20.")
            continue

        if 0 <= count <= 20:
            return count

        print("Please enter a whole number between 0 and 20.")


def build_fibonacci(count):
    sequence = []
    a, b = 0, 1

    for _ in range(count):
        sequence.append(a)
        a, b = b, a + b

    return sequence


def validate_fibonacci(sequence):
    if not sequence:
        return False

    if len(sequence) == 1:
        return sequence[0] == 0

    for index in range(2, len(sequence)):
        if sequence[index] != sequence[index - 1] + sequence[index - 2]:
            return False

    return True


def main():
    while True:
        count = get_valid_count()
        if count == 0:
            print("Goodbye!")
            break

        fib_sequence = build_fibonacci(count)

        if not validate_fibonacci(fib_sequence):
            raise ValueError("Fibonacci sequence validation failed.")

        print(" ".join(str(num) for num in fib_sequence))


if __name__ == "__main__":
    main()
