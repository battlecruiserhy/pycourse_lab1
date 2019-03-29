import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont, QIcon
from Weather import Ui_Form
from Query import Ui_Query_Form
import modify

flag = 0
city_str = ''


class MyUiForm(QtWidgets.QWidget, Ui_Form):
    # main ui
    def __init__(self):
        init_city = modify.get_init_city()
        modify.main(init_city)
        super(MyUiForm, self).__init__()
        self.setupUi(self)
        # Icon and title
        self.setWindowTitle('天气')
        self.setWindowIcon(QIcon('./picture/d0'))
        # date label's text
        self.label_date_1.setText("今天·")
        self.label_date_2.setText("明天·")
        self.label_date_3.setText("后天·")
        # data label's text
        self.label_weather_1.setText(modify.today_weather)
        self.label_weather_2.setText(modify.tomorrow_weather)
        self.label_weather_3.setText(modify.tdafttmr_weather)
        self.label_tempeture_1.setText(modify.today_temperature.replace('\\', ''))
        self.label_tempeture_2.setText(modify.tomorrow_temperature.replace('\\', ''))
        self.label_tempeture_3.setText(modify.tdafttmr_temperature.replace('\\', ''))
        self.label_tempeture_0.setText(modify.present_temperature)
        self.label_tempeture_0.setFont(QFont("Roman times", 36, QFont.Bold))
        self.label_weather_0.setText(modify.present_weather)
        self.label_weather_0.setFont(QFont("Roman times", 16, QFont.Normal))
        self.label_api_0.setText(modify.present_aqi)
        self.label_api_0.setFont(QFont("Roman times", 16, QFont.Normal))
        self.label_location.setText(init_city)
        self.label_location.setFont(QFont("Roman times", 12, QFont.Normal))
        # picture
        self.label_picture_1.setPixmap(modify.pixmap1)
        self.label_picture_1.setScaledContents(True)
        self.label_picture_2.setPixmap(modify.pixmap2)
        self.label_picture_2.setScaledContents(True)
        self.label_picture_3.setPixmap(modify.pixmap3)
        self.label_picture_3.setScaledContents(True)
        self.label_picture_0.setPixmap(modify.pixmap0)
        self.label_picture_0.setScaledContents(True)

    def button_click_input(self):
        # set the text of the button back to '·' and close the form
        self.button_change_init_location.setText('·')
        self.close()

    def change_init_city(self):
        # change the initial city and set the text of the button to 'D'
        if city_str != '':
            modify.set_init_city(city_str)
            self.button_change_init_location.setText('D')

    def data_update(self):
        # update data if the new input city is a legal one
        if flag == 1:
            self.show()
            # data label's text
            self.label_weather_1.setText(modify.today_weather)
            self.label_weather_2.setText(modify.tomorrow_weather)
            self.label_weather_3.setText(modify.tdafttmr_weather)
            self.label_tempeture_1.setText(modify.today_temperature.replace('\\', ''))
            self.label_tempeture_2.setText(modify.tomorrow_temperature.replace('\\', ''))
            self.label_tempeture_3.setText(modify.tdafttmr_temperature.replace('\\', ''))
            self.label_tempeture_0.setText(modify.present_temperature)
            self.label_tempeture_0.setFont(QFont("Roman times", 36, QFont.Bold))
            self.label_weather_0.setText(modify.present_weather)
            self.label_weather_0.setFont(QFont("Roman times", 16, QFont.Normal))
            self.label_api_0.setText(modify.present_aqi)
            self.label_api_0.setFont(QFont("Roman times", 16, QFont.Normal))
            self.label_location.setText(city_str)
            self.label_location.setFont(QFont("Roman times", 12, QFont.Normal))
            # picture
            self.label_picture_1.setPixmap(modify.pixmap1)
            self.label_picture_1.setScaledContents(True)
            self.label_picture_2.setPixmap(modify.pixmap2)
            self.label_picture_2.setScaledContents(True)
            self.label_picture_3.setPixmap(modify.pixmap3)
            self.label_picture_3.setScaledContents(True)
            self.label_picture_0.setPixmap(modify.pixmap0)
            self.label_picture_0.setScaledContents(True)


class MyQueryForm(QtWidgets.QWidget, Ui_Query_Form):
    # query ui for changing the target city
    def __init__(self):
        super(MyQueryForm, self).__init__()
        self.setupUi(self)
        # Icon and title
        self.setWindowTitle('切换城市')
        self.setWindowIcon(QIcon('./picture/d0'))

    def show_query(self):
        self.show()
        self.label_2.setText('')

    def button_click_confirm(self):
        # receive a new city name
        global city_str, flag
        city_str = self.textEdit.toPlainText()
        flag = modify.city_choose(city_str)
        self.textEdit.setText('')
        if flag == 0:
            # wrong city name
            self.label_2.setText("暂不支持该城市或api当日使用次数已达上限")
        else:
            # correct city name
            self.close()
            modify.main(city_str)
            # change city name from id to real name
            text_str = modify.get_inform(city_str)
            index, city_str = modify.select_inform('city', 0, 7, text_str)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_ui_form = MyUiForm()
    my_query_form = MyQueryForm()
    my_ui_form.show()
    my_ui_form.button_changeLocation.clicked.connect(my_ui_form.button_click_input)
    my_ui_form.button_changeLocation.clicked.connect(my_query_form.show_query)
    my_ui_form.button_change_init_location.clicked.connect(my_ui_form.change_init_city)
    my_query_form.pushButton.clicked.connect(my_ui_form.data_update)
    sys.exit(app.exec_())
