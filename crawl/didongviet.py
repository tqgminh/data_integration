import time
import csv

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By


options = Options()
driver = webdriver.Chrome(executable_path='C:\\Users\\GS75\\Desktop\\chromedr\\chromedriver.exe', chrome_options=options)


LOGIN_URL = 'https://didongviet.vn/dien-thoai'

ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
time.sleep(5)

product_links =[]


def get_more_product(driver):
    for i in range(50):
        time.sleep(1)
        try:
            driver.find_elements(By.CLASS_NAME,'more_product')[0].click()
        except:
            print('can not get more product')


def get_product_link(driver):
    number = len(driver.find_elements(By.CLASS_NAME, 'item.product.product-item'))
    print('NUMBER: ', number)
    for i in range(number):
        product_link = (driver.find_elements(By.CLASS_NAME, 'item.product.product-item')[i]).find_element(By.TAG_NAME,'a').get_attribute('href')
        # print(product_link)
        product_links.append(product_link)
    return product_links

driver.get(LOGIN_URL)
get_more_product(driver)
product_links = get_product_link(driver)


for link in product_links:
    try:
        driver.get(str(link))
        time.sleep(1)

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

        name_CN = 'heading-title'

        try:
            name = driver.find_element(By.CLASS_NAME, name_CN).text
        except:
            print('NO NAME')
        try:
            price = driver.find_element(By.CLASS_NAME, 'price-wrapper ').text
            print(price)
        except:
            print('NO PRICE')
        # print( name,'--', price)
        # try:
        #     driver.find_element(By.CLASS_NAME,'btn-detail.btn-short-spec.not-have-instruction').click()
        # except:
        #     driver.find_element(By.CLASS_NAME,'btn-detail.btn-short-spec').click()
        # time.sleep(1)
        table = driver.find_element(By.CLASS_NAME,'data.table.additional-attributes')
        # ths = driver.find_elements(By.CLASS_NAME,'ctLeft')
        # tds = driver.find_elements(By.CLASS_NAME,'ctRight')
        # heads=[]
        # datas = []
        # for th in ths:
        #     heads.append(th.text)
        # for td in tds:
        #     datas.append(td.text)
        # for i in range(len(ths)):
        rows = table.find_elements(By.TAG_NAME,'li')
        for row in rows:
            th = row.find_element(By.TAG_NAME,'p').text
            td = row.find_element(By.TAG_NAME,'span').text
            # print(td,th)
            try:
                if th == 'Bluetooth':
                    bluetooth = td
                if th == 'Th????ng hi???u':
                    thuong_hieu = td
                if th == 'Xu???t x??? th????ng hi???u':
                    xuat_xu = td
                if th == 'H??? tr??? th??? nh??? ngo??i':
                    ho_tro_the_nho_ngoai = td
                if th == 'Chipset (h??ng SX CPU)':
                    chip_set = td
                if th == 'T???c ????? CPU':
                    toc_do_cpu = td
                if th == 'M??n h??nh r???ng':
                    kich_thuoc = td
                if th == 'C??ng ngh??? m??n h??nh':
                    cong_nghe_man_hinh = td
                if th == 'Jack tai nghe':
                    jack_tai_nghe = td
                if th == 'Dung l?????ng pin':
                    loai_pin = td
                if th == 'SIM':
                    loai_sim = td
                if th == 'Tr???ng l?????ng':
                    trong_luong = td
                if th == 'RAM':
                    ram = td
                if th == '????? ph??n gi???i':
                    do_phan_giai = td
                if th == 'B??? nh??? trong':
                    rom = td
                if th == 'K??ch th?????c m??n h??nh':
                    kich_thuoc_man_hinh = td
            # try:
            #     if heads[i] == 'Bluetooth':
            #         bluetooth=datas[i]
            #
            #     if heads[i]== 'Chip x??? l?? (CPU):':
            #         chip_set=datas[i]
            #     # if heads[i]=='T???c ????? CPU':
            #     #     toc_do_cpu=datas[i]
            #     if heads[i]=='M??n h??nh r???ng:':
            #         kich_thuoc=datas[i]
            #     if heads[i]== 'C??ng ngh??? m??n h??nh':
            #         cong_nghe_man_hinh=datas[i]
            #     # if heads[i]=='Jack tai nghe':
            #     #     jack_tai_nghe=datas[i]
            #     if heads[i]=='Dung l?????ng pin:':
            #         loai_pin=datas[i]
            #     if heads[i] =='SIM:':
            #         loai_sim=datas[i]
            #     # if heads[i]=='Tr???ng l?????ng':
            #     #     trong_luong=datas[i]
            #     if heads[i]=='RAM:':
            #         ram=datas[i]
            #     # if heads[i]=='????? ph??n gi???i':
            #     #     do_phan_giai=datas[i]
            #     if heads[i]=='B??? nh??? trong:':
            #         rom=datas[i]
            #     # if heads[i]=='K??ch th?????c m??n h??nh':
            #     #     kich_thuoc_man_hinh=datas[i]
            except:
                print('cant get tr')
        with open('C:\\Users\\GS75\\PycharmProjects\\Tich_hop_du_lieu\\data_integration\\data\\didongviet.csv', 'a',newline='',encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([name,price,bluetooth,thuong_hieu,xuat_xu,ho_tro_the_nho_ngoai,chip_set,toc_do_cpu,kich_thuoc,cong_nghe_man_hinh,loai_pin,loai_sim,trong_luong,ram,do_phan_giai,rom
                             ])
    except:
        print('can not get link')





