import time
import csv

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By


options = Options()
driver = webdriver.Chrome(executable_path='C:\\Users\\GS75\\Desktop\\chromedr\\chromedriver.exe', chrome_options=options)


LOGIN_URL = 'https://www.dienmayxanh.com/dien-thoai/#c=42&o=9&pi=4'

ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
time.sleep(5)

product_links =[]


def get_product_link(driver):
    number = len(driver.find_elements(By.CLASS_NAME, 'item.ajaxed.__cate_42'))
    print('NUMBER: ', number)
    for i in range(number):
        product_link = (driver.find_elements(By.CLASS_NAME, 'item.ajaxed.__cate_42')[i]).find_element(By.TAG_NAME,'a').get_attribute('href')
        product_links.append(product_link)
    return product_links

driver.get(LOGIN_URL)
product_links = get_product_link(driver)


for link in product_links:
    try:
        driver.get(str(link))
        time.sleep(2)

        name =''
        price = ''

        bluetooth = ''
        thuong_hieu=''
        xuat_xu=''
        ho_tro_the_nho_ngoai=''
        chip_set=''
        toc_do_cpu=''
        kich_thuoc=''
        cong_nghe_man_hinh=''
        jack_tai_nghe=''
        loai_pin=''
        loai_sim=''
        trong_luong=''
        ram=''
        do_phan_giai=''
        rom=''
        kich_thuoc_man_hinh=''

        name_xpath = '/html/body/section[1]/h1'
        price_CN = '/html/body/section[1]/div[3]/div[2]/div[3]/div[2]/div/p[1]'
        try:
            name = driver.find_element(By.XPATH, name_xpath).text
        except:
            print('NO NAME')
        try:
            price = driver.find_element(By.XPATH, price_CN).text
        except:
            print('NO PRICE')
        # print( name,'--', price)
        try:
            driver.find_element(By.CLASS_NAME,'btn-detail.btn-short-spec.not-have-instruction').click()
        except:
            driver.find_element(By.CLASS_NAME,'btn-detail.btn-short-spec').click()
        time.sleep(1)
        ths = driver.find_elements(By.CLASS_NAME,'ctLeft')
        tds = driver.find_elements(By.CLASS_NAME,'ctRight')
        heads=[]
        datas = []
        for th in ths:
            heads.append(th.text)
        for td in tds:
            datas.append(td.text)
        for i in range(len(ths)):
            try:
                if heads[i] == 'Bluetooth':
                    bluetooth=datas[i]

                if heads[i]== 'Chip xử lý (CPU):':
                    chip_set=datas[i]
                # if heads[i]=='Tốc độ CPU':
                #     toc_do_cpu=datas[i]
                if heads[i]=='Màn hình rộng:':
                    kich_thuoc=datas[i]
                if heads[i]== 'Công nghệ màn hình':
                    cong_nghe_man_hinh=datas[i]
                # if heads[i]=='Jack tai nghe':
                #     jack_tai_nghe=datas[i]
                if heads[i]=='Dung lượng pin:':
                    loai_pin=datas[i]
                if heads[i] =='SIM:':
                    loai_sim=datas[i]
                # if heads[i]=='Trọng lượng':
                #     trong_luong=datas[i]
                if heads[i]=='RAM:':
                    ram=datas[i]
                # if heads[i]=='Độ phân giải':
                #     do_phan_giai=datas[i]
                if heads[i]=='Bộ nhớ trong:':
                    rom=datas[i]
                # if heads[i]=='Kích thước màn hình':
                #     kich_thuoc_man_hinh=datas[i]
            except:
                print('cant get tr')
        with open('M:\\pycharm\\crawling_new\\dien_may_xanh.csv', 'a',newline='',encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([name,price,bluetooth,thuong_hieu,xuat_xu,ho_tro_the_nho_ngoai,chip_set,toc_do_cpu,kich_thuoc,cong_nghe_man_hinh,jack_tai_nghe,loai_pin,loai_sim,trong_luong,ram,do_phan_giai,rom,kich_thuoc_man_hinh
                             ])
    except:
        print('can not get link')





