from log import Logger


class Console:
    ptt_id = None
    config = None
    ptt_adapter = None
    log_handler = None
    system_alert_func = None
    otp_form = None
    current_otp = None

    test_mode = False
    test_local = True

    def __init__(self, argv):
        self.logger = Logger('Console', Logger.INFO)

        if '-debug' in argv:
            self.test_mode = True

        if '-test_local' in argv:
            self.test_local = True

        if self.test_mode:
            self.logger.show(Logger.INFO, '測試模式')

        if self.test_local:
            self.logger.show(Logger.INFO, '本機測試模式')

    def system_alert(self, msg):
        if self.system_alert_func is None:
            self.logger.show_value(Logger.INFO, 'system_alert is None', msg)
            return
        self.logger.show_value(Logger.INFO, 'system_alert', msg)
        self.system_alert_func(msg)
