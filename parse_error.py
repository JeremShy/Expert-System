class ParseException(Exception):
    def __init__(self, message):
		super(ParseException, self).__init__(message)
		self.strerror = message;
