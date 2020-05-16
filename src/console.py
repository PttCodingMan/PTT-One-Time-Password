from log import Logger


class Console:
    ptt_id = None
    config = None
    ptt_adapter = None
    log_handler = None
    system_alert_func = None
    otp_form = None
    current_otp = None

    test_mode = True

    def __init__(self):
        logger = Logger('Console', Logger.INFO)
        if self.test_mode:
            logger.show(Logger.INFO, '測試模式')

    def system_alert(self, msg):
        if self.system_alert_func is None:
            return
        self.system_alert_func(msg)
