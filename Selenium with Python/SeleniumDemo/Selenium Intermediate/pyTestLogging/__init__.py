import logging

log = logging.getLogger('__name__')
file = logging.FileHandler("Logs/file.log")
formatd = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
file.setFormatter(formatd)
#
# log.addHandler(file)
# log.setLevel(logging.DEBUG)
#
# log.debug("Debugged this test case")
# log.info("Requires Info on this case")
# log.warning("Requires to Resolve the warning on this case")
# log.error("Test case failed")
# log.critical("Test case failed and critical")