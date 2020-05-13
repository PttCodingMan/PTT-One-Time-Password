from time import strftime
import time
import threading
import sys

from PySide2.QtWidgets import QWidget, QVBoxLayout, QApplication
from PySide2.QtCore import Qt, QRectF

from PySide2.QtGui import QColor, QFont, QImage, QPainter, QPen, QPainterPath, QConicalGradient, QGradient, QColor, \
    QPalette, QGuiApplication
from PySide2.QtWidgets import QDialog

from log import Logger
import util
import config


class QRoundProgressBar(QWidget):
    StyleDonut = 1
    StylePie = 2
    StyleLine = 3

    PositionLeft = 180
    PositionTop = 90
    PositionRight = 0
    PositionBottom = -90

    UF_VALUE = 1
    UF_PERCENT = 2
    UF_MAX = 4

    def __init__(self, console):
        super().__init__()
        self.min = 0
        self.max = 100
        self.value = 25

        self.nullPosition = self.PositionTop
        self.barStyle = self.StyleDonut
        self.outlinePenWidth = 1
        self.dataPenWidth = 1
        self.rebuildBrush = False
        self.format = "%p%"
        self.decimals = 1
        self.updateFlags = self.UF_PERCENT
        self.gradientData = []
        self.donutThicknessRatio = 0.75

        self.console = console

    def setRange(self, min, max):
        self.min = min
        self.max = max

        if self.max < self.min:
            self.max, self.min = self.min, self.max

        if self.value < self.min:
            self.value = self.min
        elif self.value > self.max:
            self.value = self.max

        if not self.gradientData:
            self.rebuildBrush = True
        self.update()

    def setMinimun(self, min):
        self.setRange(min, self.max)

    def setMaximun(self, max):
        self.setRange(self.min, max)

    def setValue(self, val):
        if self.value != val:
            if val < self.min:
                self.value = self.min
            elif val > self.max:
                self.value = self.max
            else:
                self.value = val
            self.update()

    def setNullPosition(self, position):
        if position != self.nullPosition:
            self.nullPosition = position
            if not self.gradientData:
                self.rebuildBrush = True
            self.update()

    def setBarStyle(self, style):
        if style != self.barStyle:
            self.barStyle = style
            self.update()

    def setOutlinePenWidth(self, penWidth):
        if penWidth != self.outlinePenWidth:
            self.outlinePenWidth = penWidth
            self.update()

    def setDataPenWidth(self, penWidth):
        if penWidth != self.dataPenWidth:
            self.dataPenWidth = penWidth
            self.update()

    def setDataColors(self, stopPoints):
        if stopPoints != self.gradientData:
            self.gradientData = stopPoints
            self.rebuildBrush = True
            self.update()

    def setFormat(self, format):
        if format != self.format:
            self.format = format
            self.valueFormatChanged()

    def resetFormat(self):
        self.format = ''
        self.valueFormatChanged()

    def setDecimals(self, count):
        if count >= 0 and count != self.decimals:
            self.decimals = count
            self.valueFormatChanged()

    def setDonutThicknessRatio(self, val):
        self.donutThicknessRatio = max(0., min(val, 1.))
        self.update()

    def paintEvent(self, event):
        outerRadius = min(self.width(), self.height())
        baseRect = QRectF(1, 1, outerRadius - 2, outerRadius - 2)

        buffer = QImage(outerRadius, outerRadius, QImage.Format_ARGB32)
        buffer.fill(0)

        p = QPainter(buffer)
        p.setRenderHint(QPainter.Antialiasing)

        # data brush
        self.rebuildDataBrushIfNeeded()

        # background
        self.drawBackground(p, buffer.rect())

        # base circle
        self.drawBase(p, baseRect)

        # data circle
        arcStep = 360.0 / (self.max - self.min) * self.value
        self.drawValue(p, baseRect, self.value, arcStep)

        # center circle
        innerRect, innerRadius = self.calculateInnerRect(baseRect, outerRadius)
        self.drawInnerBackground(p, innerRect)

        # text
        self.drawText(p, innerRect, innerRadius, self.value)

        # finally draw the bar
        p.end()

        painter = QPainter(self)
        painter.drawImage(0, 0, buffer)

    def drawBackground(self, p, baseRect):
        p.fillRect(baseRect, self.palette().window())

    def drawBase(self, p, baseRect):
        bs = self.barStyle
        if bs == self.StyleDonut:
            # p.setPen(QtGui.QPen(self.palette().shadow().color(), self.outlinePenWidth))
            p.setPen(QPen(self.palette().shadow().color(), -1))
            # p.setBrush(self.palette().base())
            p.setBrush(QColor(7, 93, 145))
            p.drawEllipse(baseRect)

        elif bs == self.StylePie:
            p.setPen(QPen(self.palette().base().color(), self.outlinePenWidth))
            p.setBrush(self.palette().base())
            p.drawEllipse(baseRect)
        elif bs == self.StyleLine:
            p.setPen(QPen(self.palette().base().color(), self.outlinePenWidth))
            p.setBrush(Qt.NoBrush)
            p.drawEllipse(
                baseRect.adjusted(self.outlinePenWidth / 2, self.outlinePenWidth / 2, -self.outlinePenWidth / 2,
                                  -self.outlinePenWidth / 2))

    def drawValue(self, p, baseRect, value, arcLength):
        # nothing to draw
        if value == self.min:
            return

        # for Line style
        if self.barStyle == self.StyleLine:
            p.setPen(QPen(self.palette().highlight().color(), self.dataPenWidth))
            p.setBrush(Qt.NoBrush)
            p.drawArc(baseRect.adjusted(self.outlinePenWidth / 2, self.outlinePenWidth / 2, -self.outlinePenWidth / 2,
                                        -self.outlinePenWidth / 2),
                      self.nullPosition * 16,
                      -arcLength * 16)
            return

        # for Pie and Donut styles
        dataPath = QPainterPath()
        dataPath.setFillRule(Qt.WindingFill)

        # pie segment outer
        dataPath.moveTo(baseRect.center())
        dataPath.arcTo(baseRect, self.nullPosition, -arcLength)
        dataPath.lineTo(baseRect.center())

        p.setBrush(self.palette().highlight())
        p.setBrush(QColor(255, 255, 255, 255 * 0.3))

        # pen = QtGui.QPen(self.palette().shadow().color(), self.dataPenWidth)
        pen = QPen(self.palette().shadow().color(), -1)
        p.setPen(pen)
        p.drawPath(dataPath)

    def calculateInnerRect(self, baseRect, outerRadius):
        # for Line style
        if self.barStyle == self.StyleLine:
            innerRadius = outerRadius - self.outlinePenWidth
        else:  # for Pie and Donut styles
            innerRadius = outerRadius * self.donutThicknessRatio

        delta = (outerRadius - innerRadius) / 2.
        innerRect = QRectF(delta, delta, innerRadius, innerRadius)
        return innerRect, innerRadius

    def drawInnerBackground(self, p, innerRect):
        if self.barStyle == self.StyleDonut:
            p.setBrush(self.palette().alternateBase())

            cmod = p.compositionMode()
            p.setCompositionMode(QPainter.CompositionMode_Source)

            p.drawEllipse(innerRect)

            p.setCompositionMode(cmod)

    def drawText(self, p, innerRect, innerRadius, value):
        if not self.format:
            return

        text = self.valueToText(value)

        # !!! to revise
        # f = self.font()
        f = QFont()
        f.setFamily("微軟正黑體")
        # f.setPixelSize(innerRadius * max(0.05, (0.35 - self.decimals * 0.08)))
        f.setPixelSize(60)
        p.setFont(f)

        textRect = innerRect
        p.setPen(self.palette().text().color())
        p.drawText(textRect, Qt.AlignCenter, text)

    def valueToText(self, value):
        textToDraw = self.format

        format_string = '{' + ':.{}f'.format(self.decimals) + '}'

        if self.updateFlags & self.UF_VALUE:
            textToDraw = textToDraw.replace("%v", format_string.format(value))

        if self.updateFlags & self.UF_PERCENT:
            percent = (value - self.min) / (self.max - self.min) * 100.0
            textToDraw = textToDraw.replace("%p", format_string.format(percent))

        if self.updateFlags & self.UF_MAX:
            m = self.max - self.min + 1
            textToDraw = textToDraw.replace("%m", format_string.format(m))

        return textToDraw

    def valueFormatChanged(self):
        self.updateFlags = 0;

        if "%v" in self.format:
            self.updateFlags |= self.UF_VALUE

        if "%p" in self.format:
            self.updateFlags |= self.UF_PERCENT

        if "%m" in self.format:
            self.updateFlags |= self.UF_MAX

        self.update()

    def rebuildDataBrushIfNeeded(self):
        if self.rebuildBrush:
            self.rebuildBrush = False

            dataBrush = QConicalGradient()
            dataBrush.setCenter(0.5, 0.5)
            dataBrush.setCoordinateMode(QGradient.StretchToDeviceMode)

            for pos, color in self.gradientData:
                dataBrush.setColorAt(1.0 - pos, color)

            # angle
            dataBrush.setAngle(self.nullPosition)

            p = self.palette()
            p.setBrush(QPalette.Highlight, dataBrush)
            self.setPalette(p)

    def mouseDoubleClickEvent(self, event):
        clipboard = QGuiApplication.clipboard()
        clipboard.setText(self.format.strip())
        self.console.system_alert('驗證碼已經複製到剪貼簿')


class Form(QDialog):
    def __init__(self, console):
        super(type(self), self).__init__()

        self.bar = QRoundProgressBar(console)
        self.bar.setFixedSize(300, 300)

        self.bar.setDataPenWidth(0)
        self.bar.setOutlinePenWidth(0)
        self.bar.setDonutThicknessRatio(0.92)
        self.bar.setDecimals(0)
        self.bar.setNullPosition(90)
        self.bar.setBarStyle(QRoundProgressBar.StyleDonut)
        self.bar.setDataColors([(0., QColor.fromRgb(65, 105, 225))])

        self.bar.setRange(0, 29)

        self.setWindowTitle(f'{console.ptt_id} 驗證碼')

        lay = QVBoxLayout()
        lay.addWidget(self.bar)
        self.setLayout(lay)

        self.console = console
        self.timer_thread = None
        self.call_close = False
        self.logger = Logger('Progress', Logger.INFO)
        self.setWindowIcon(util.load_icon(config.icon_small))

        self.update_otp()

    def update_otp(self):

        data = self.console.current_otp
        self.logger.show_value(Logger.INFO, 'update_otp', data)

        current_data = f'{data}'
        self.bar.setFormat(current_data)

        if self.timer_thread is None:
            self.timer_thread = threading.Thread(target=self.timer)
            self.timer_thread.daemon = True
            self.timer_thread.start()

    def timer(self):

        self.logger.show(Logger.INFO, '啟動計時器')

        while not self.call_close:
            current_sec = int(strftime("%S")) % 30

            self.logger.show_value(Logger.INFO, 'current_sec', current_sec)

            for value in range(current_sec, 30):
                self.bar.setValue(value)

                self.logger.show_value(Logger.TRACE, 'value', value)

                temp_sec = value
                if self.call_close:
                    break
                while temp_sec == value:
                    time.sleep(0.05)
                    temp_sec = int(strftime("%S")) % 30
                    # self.logger.show_value(Logger.INFO, 'temp_sec', temp_sec)

    def close_form(self):
        self.call_close = True
        time.sleep(0.5)
        self.hide()

    def closeEvent(self, event):
        self.logger.show(Logger.INFO, '直接關閉')
        self.console.system_alert('背景執行中')


def update_thread():
    for i in range(10):
        print('===================================')
        dlg.update_otp('12345' + str(i))
        sleep_time = 30 - (int(strftime("%S")) % 30)
        print(f'sleep {sleep_time}')
        time.sleep(sleep_time)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = Form()
    dlg.show()

    thread = threading.Thread(target=update_thread)
    thread.daemon = True
    thread.start()

    sys.exit(app.exec_())
