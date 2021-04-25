# coding: utf-8

class LexerError(RuntimeError):
    def __init__(error_str):
        super(LexerError, self).__init__(error_str)


class SyntaxParseError(RuntimeError):
    def __init__(error_str):
        super(LexerError, self).__init__(error_str)