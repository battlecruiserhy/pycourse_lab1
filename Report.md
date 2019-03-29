# 实验报告
## 1. 功能说明
* 功能：显示当下的具体天气状况（温度，天气，空气质量），以及今天、明天、后天的大致天气状况（天气，温度范围）
* 使用说明：初次启动程序时默认显示合肥市的天气状况。单击主窗体左上角的“+”按钮，进入“切换城市”界面，在文本框中输入目标城市的城市名或城市编号，单击“确定”按钮，若输入正确则切换回主窗体并显示目标城市天气状况，若输入错误或当日api调用次数已达上限则会显示“暂不支持该城市或api当日使用次数已达上限”的提示，此时请重新输入或关闭程序。若切换回主窗体，可点击主窗体右上角的“·”按钮更改默认显示的城市，若成功更改则该按钮变为“D”，表示更改完成（Done）
* 演示截图：见同级目录下的“演示截图.pdf”
## 2. 代码阐释
### modify.py
* `def get_inform(city_str):` 通过调用“聚合数据”的“天气预报”接口获得程序所需信息（key以文件的形式保存在key文件夹下），写入data文件夹下的text.txt文件中，并将信息以字符串的方式返回
* `def select_inform(target_str, start_index, bias_index, text_str):` 根据传入的参数，从目标字符串中截出需要的子串
* `def picture_select(target_str):` 根据传入的天气字符串返回对应的天气图例
* `def city_choose(city_str):` 判断调用“聚合数据”的接口返回的信息是否正常，即判断输入城市是否错误以及当日api调用次数是否已达上限
* `def get_init_city():` 从data文件夹下的init_city.txt文件中读出程序启动时默认的目标城市
* `def set_init_city(init_city_str):` 根据传入的参数，通过修改init_city.txt，更改默认的目标城市
* `def aqi_judge(aqi):` 根据传入的参数，确定当前空气质量并返回
* `def main(city_str):` 通过调用上述函数，获取所需信息，并定义为全局变量，方便其他程序调用
### ins.py
* `class MyUiForm(QtWidgets.QWidget, Ui_Form):` 主窗体类，其函数分别为：
    > `def __init__(self):` 调用modify.py中的函数获得所有所需信息，通过主窗体显示
    
    > `def button_click_input(self):` 将设置默认城市按钮的标志切换回“·”，并且关闭主窗体
    
    > `def change_init_city(self):` 调用modify.py中的函数来修改默认城市，并将设置默认城市按钮的标志改为“D”，以标志切换成功
    
    > `def data_update(self):` 若更改的目标城市合法，则更新主窗体中的信息
* `class MyQueryForm(QtWidgets.QWidget, Ui_Query_Form):` “切换城市”窗体类，其函数分别为：
    > `def __init__(self):` 设置窗体内显示的信息
    
    > `def show_query(self):` 窗体出现，并初始化提示标签
    
    > `def button_click_confirm(self):` 从文本框中获取目标城市的名字或编号，并调用modify.py中的函数对其是否合法加以判断，根据判断结果修改目标城市或报错
* `if __name__ == '__main__':` 主函数，将上述窗体实例化
### Weather.py
* 主窗体程序，使用QTDesigner编辑，并由PyUIC自动生成
### Query.py
* “切换城市”窗体程序，使用QTDesigner编辑，并由PyUIC自动生成
## 3. 收获总结
* Python与Pycharm相辅相成，给人以十分顺畅的编程体验。由于在下选择的题目虽大致符合要求，但较为简单、代码量小，难以有更深刻的体验，这是一开始未曾考虑到的。以后编程在之前，应当先对编程难度、代码量先进行估计，形成一个全盘的方案后，才能开始施工