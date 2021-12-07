import logging


def set_logger(name, mode="debug", write_log=False, full_path="./debug.log", write_mode="a"):
    """
        Make Log-File and PrettyPrints. Write mode can be either 'a' (append) or 'w' ((over)write).

        Usage:
            self.log = set_logger(name="log1", mode="info")
            self.log.error("This is wrong")

        Args:
            write_mode:
            full_path:
            write_log:
            name:
            mode:
        """

    if mode == "debug":
        level = logging.DEBUG
    elif mode == "info":
        level = logging.INFO
    elif mode == "warn":
        level = logging.WARN
    elif mode == "error":
        level = logging.ERROR
    else:
        level = logging.INFO

    # create logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)

    # create format
    log_format = '[%(name)s][%(asctime)s][%(levelname)-5s][l:%(lineno)d][%(module)s.%(funcName)s()] %(message)s'
    formatter = logging.Formatter(log_format)

    # add format to console handler
    console_handler.setFormatter(formatter)

    # add console handler to logger
    logger.addHandler(console_handler)

    # write log in file
    if write_log is True:
        # create FileHandler
        file_handler = logging.FileHandler(full_path, mode=write_mode)  # write mode is a, w
        file_handler.setLevel(level)

        # add format to console handler
        file_handler.setFormatter(formatter)

        # add Handler to logger
        logger.addHandler(file_handler)

    return logger