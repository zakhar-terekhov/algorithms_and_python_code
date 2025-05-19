import unicodedata


mystery = "\U0001f4a9"
symbol_name = unicodedata.name(
    mystery
)  # возвращает имя символа Unicode в верхнем регистре
symbol = unicodedata.lookup(symbol_name)  # преобразует название в символ Unicode
pop_bytes = mystery.encode("utf-8")  # закодировать строку
pop_string = pop_bytes.decode("utf-8")  # декодировать строку в символ Unicode
