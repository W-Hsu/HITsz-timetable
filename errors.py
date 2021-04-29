# coding: utf-8

class CrawlerError(RuntimeError):
    def __init__(self, error_str):
        super(CrawlerError, self).__init__(error_str)


class LexerError(RuntimeError):
    def __init__(self, error_str):
        super(LexerError, self).__init__(error_str)


class SyntaxParseError(RuntimeError):
    def __init__(self, error_str):
        super(SyntaxParseError, self).__init__(error_str)