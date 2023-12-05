def trim_and_repeat(input_string, offset=0, repetitions=1):
    # Обрезаем строку с учетом сдвига (offset)
    trimmed_string = input_string[offset:]

    # Повторяем строку нужное количество раз
    repeated_string = trimmed_string * repetitions

    return repeated_string

# Пример использования
original_string = "Hello, World!"
result = trim_and_repeat(original_string, offset=2, repetitions=3)

print("Исходная строка:", original_string)
print("Результат:", result)
