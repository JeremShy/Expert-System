class LogicError(Exception):
    def __init__(self, message):
		super(LogicError, self).__init__(message)
		self.strerror = message;
