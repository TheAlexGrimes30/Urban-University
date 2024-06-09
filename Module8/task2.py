class InvalidDataException(Exception):
    pass


class ProcessingException(Exception):
    pass


def process_data(data):
    if not isinstance(data, (int, float, str)):
        raise InvalidDataException("Invalid data type provided")
    if not data:
        raise ProcessingException("Empty string provided")
    if isinstance(data, (int, float)):
        return data ** 2
    return data


def handle_data(data):
    try:
        result = process_data(data)
        return result
    except InvalidDataException as e:
        print(f"InvalidDataException caught: {e}")
        raise
    except ProcessingException as e:
        print(f"ProcessingException caught: {e}")
        raise
    finally:
        print("Execution of handle_data is complete")


def main():
    test_data = [42, 3.14, 'hello', '', [], {}]

    for data in test_data:
        try:
            result = handle_data(data)
            print(f"Processed result: {result}")
        except InvalidDataException as e:
            print(f"Exception handled in main: {e}")
        except ProcessingException as e:
            print(f"Exception handled in main: {e}")


if __name__ == "__main__":
    main()
