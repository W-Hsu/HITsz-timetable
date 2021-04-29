# coding=utf-8

class LackArgumentError(RuntimeError):
    def __init__(self, error_str):
        super(LackArgumentError, self).__init__(error_str)


class CrawlerError(RuntimeError):
    def __init__(self, error_str):
        super(CrawlerError, self).__init__(error_str)


class ExcelParserError(RuntimeError):
    def __init__(self, error_str):
        super(SyntaxParseError, self).__init__(error_str)
