import logging

class TerminalColors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    OK = '\033[92m' # Green
    ERROR = '\033[31;1m' #Red
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    GREY = "\033[38;21m"
    YELLOW = "\033[33;21m"

class LoggingFormater(logging.Formatter):
    """Logging Formatter to add colors and count warning / errors"""
    
    formatInfo = "%(asctime)s  [     INFO ]  %(message)s"
    formatWarning = "%(asctime)s  [  WARNING ]  %(message)s (%(filename)s:%(lineno)d)"
    formatError = "%(asctime)s  [    ERROR ]  %(message)s (%(filename)s:%(lineno)d)"
    formatCritical = "%(asctime)s  [ CRITICAL ]  %(message)s (%(filename)s:%(lineno)d)"

    FORMATS = {
        logging.DEBUG: TerminalColors.GREY + formatInfo + TerminalColors.ENDC,
        logging.INFO: TerminalColors.OK + formatInfo + TerminalColors.ENDC,
        logging.WARNING: TerminalColors.YELLOW + formatWarning + TerminalColors.ENDC,
        logging.ERROR: TerminalColors.ERROR + formatError + TerminalColors.ENDC,
        logging.CRITICAL: TerminalColors.ERROR + formatCritical + TerminalColors.ENDC
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)