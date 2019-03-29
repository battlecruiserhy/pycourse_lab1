import requests
from PyQt5.QtGui import QPixmap

present_weather = ''
present_temperature = ''
present_aqi = ''
today_temperature = ''
today_weather = ''
tomorrow_temperature = ''
tomorrow_weather = ''
tdafttmr_temperature = ''
tdafttmr_weather = ''

pixmap1 = None
pixmap2 = None
pixmap3 = None
pixmap0 = None


def get_inform(city_str):
    # get information from api
    with open('./key/key.txt', 'r') as f:
        key_str = f.read()
    with open('./data/text.txt', 'w') as f:
        b = requests.get(
            'http://apis.juhe.cn/simpleWeather/query?city=%s&key=%s' % (city_str, key_str))
        f.write(b.text)
    with open('./data/text.txt', 'r') as f:
        text_str = f.read()
    return text_str


def select_inform(target_str, start_index, bias_index, text_str):
    # select required information from the target text
    get_str = ''
    index = text_str.find(target_str, start_index)
    if index != -1:
        index += bias_index
        while text_str[index] != '"':
            get_str += text_str[index]
            index += 1
    return index, get_str


def picture_select(target_str):
    # choose a picture according to the weather
    dict_p = {'晴': './picture/d00', '多云': './picture/d01', '阴': './picture/d02', '阵雨': './picture/d03',
              '雷阵雨': './picture/d04', '雷阵雨伴有冰雹': './picture/d05', '雨夹雪': './picture/d06',
              '小雨': './picture/d07', '中雨': './picture/d08', '大雨': './picture/d09', '暴雨': './picture/d10',
              '大暴雨': './picture/d11', '特大暴雨': './picture/d12', '阵雪': './picture/d13', '小雪': './picture/d14',
              '中雪': './picture/d15', '大雪': './picture/d16', '暴雪': './picture/d17', '雾': './picture/d18',
              '冻雨': './picture/d19', '沙尘暴': './picture/d20', '小到中雨': './picture/d21', '中到大雨': './picture/d22',
              '大到暴雨': './picture/d23', '暴雨到大暴雨': './picture/d24', '大暴雨到特大暴雨': './picture/d25',
              '小到中雪': './picture/d26', '中到大雪': './picture/d27', '大到暴雪': './picture/d28', '浮尘': './picture/d29',
              '扬沙': './picture/d30', '强沙尘暴': './picture/d31', '霾': './picture/d53'}
    index = target_str.find('转')
    if index != -1:
        target_str = target_str[0: index]
    return dict_p[target_str]


def city_choose(city_str):
    # detect whether the input city name is a legal one
    text_str = get_inform(city_str)
    index = text_str.find('"error_code":0')
    if index != -1:
        return 1
    else:
        return 0


def get_init_city():
    # get the initial city name
    with open('./data/init_city.txt', 'r') as f:
        init_city_str = f.read()
        return init_city_str


def set_init_city(init_city_str):
    # change the initial city name
    with open('./data/init_city.txt', 'w') as f:
        f.write(init_city_str)


def aqi_judge(aqi):
    # judge air quality through aqi
    if 0 <= int(aqi) <= 50:
        aqi = '空气优 ' + aqi
    elif 51 <= int(aqi) <= 150:
        aqi = '空气良 ' + aqi
    elif 101 <= int(aqi) <= 100:
        aqi = '轻度污染 ' + aqi
    elif 151 <= int(aqi) <= 200:
        aqi = '中度污染 ' + aqi
    elif 201 <= int(aqi) <= 300:
        aqi = '重度污染 ' + aqi
    else:
        aqi = '严重污染 ' + aqi
    return aqi


def main(city_str):
    # form all the information displayed on the main form
    global present_weather, present_temperature, present_aqi, today_temperature, today_weather, tomorrow_temperature, \
           tomorrow_weather, tdafttmr_temperature, tdafttmr_weather
    global pixmap1, pixmap2, pixmap3, pixmap0

    # value
    text_str = get_inform(city_str)
    # find the value of present's temperature
    flag, present_temperature = select_inform('temperature', 0, 14, text_str)
    # find the value of present's weather
    flag, present_weather = select_inform('info', flag, 7, text_str)
    # find the value of present's aqi
    flag, present_aqi = select_inform('aqi', flag, 6, text_str)
    # find the value of today's temperature
    flag, today_temperature = select_inform('temperature', flag, 14, text_str)
    # find the value of today's weather
    flag, today_weather = select_inform('weather', flag, 10, text_str)
    # find the value of tomorrow's temperature
    flag, tomorrow_temperature = select_inform('temperature', flag, 14, text_str)
    # find the value of tomorrow's weather
    flag, tomorrow_weather = select_inform('weather', flag, 10, text_str)
    # find the value of the day after tomorrow's temperature
    flag, tdafttmr_temperature = select_inform('temperature', flag, 14, text_str)
    # find the value of the day after tomorrow's weather
    flag, tdafttmr_weather = select_inform('weather', flag, 10, text_str)

    # aqi
    present_aqi = aqi_judge(present_aqi)

    # picture
    route = picture_select(today_weather)
    pixmap1 = QPixmap(route)
    route = picture_select(tomorrow_weather)
    pixmap2 = QPixmap(route)
    route = picture_select(tdafttmr_weather)
    pixmap3 = QPixmap(route)
    route = picture_select(present_weather)
    pixmap0 = QPixmap(route)
