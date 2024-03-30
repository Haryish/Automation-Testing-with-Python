import logging


class BaseClass:

    def test_LogMaking(self):
        log = logging.getLogger('__name__')
        file = logging.FileHandler("Logs/file.log")
        formattor = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        file.setFormatter(formattor)

        log.addHandler(file)

        return log
