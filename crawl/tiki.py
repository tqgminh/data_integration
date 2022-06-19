import time
import csv

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By


options = Options()
driver = webdriver.Chrome(executable_path='C:\\Users\\GS75\\Desktop\\chromedr\\chromedriver.exe', chrome_options=options)


LOGIN_URL = 'https://tiki.vn/dien-thoai-may-tinh-bang/c1789?page='

ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
time.sleep(5)


# name_list = []
# new_price_list = []
# old_price_list = []
# kich_thuoc_man_hinh_list = []
# cong_nghe_man_hinh_list = []
# camera_sau_list = []
# camera_truoc_list = []
# chipset_list = []
# dung_luong_ram_list = []
# bo_nho_trong_list = []
# pin_list = []
# the_sim_list = []
# he_dieu_hanh_list = []
# do_phan_giai_man_hinh_list = []
# tinh_nang_man_hinh_list = []
# loai_cpu_list = []
# trong_luong_list = []
# bluetooth_list = []
# tan_so_quet_list = []


ITEM_CN = 'item-product'

product_links = []


def get_product_link(driver):
    number = len(driver.find_elements(By.CLASS_NAME, 'product-item'))
    print('NUMBER: ', number)
    for i in range(number):
        product_link = (driver.find_elements(By.CLASS_NAME, 'product-item')[i]).get_attribute('href')
        product_links.append(product_link)
    return product_links
#
#
# def get_tskt(driver):
#     # GET NAME AND PRICE
#     name_xpath = '/html/body/div[2]/main/div/div[1]/div[2]/div[1]/h1'
#     new_price_xpath ='/html/body/div[2]/main/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]'
#     old_price_xpath ='/html/body/div[2]/main/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]'
#
#     try:
#         name =driver.find_element(By.XPATH, name_xpath).text
#     except:
#         name =''
#     try:
#         new_price = driver.find_element(By.XPATH, new_price_xpath).text
#     except:
#         new_price=''
#     try:
#         old_price = driver.find_element(By.XPATH, old_price_xpath).text
#     except:
#         old_price =''
#
#     print(name,old_price,new_price)
#
#     # GET DETAILS
#     kich_thuoc= ''
#     trong_luong_san_pham=''
#     phien_ban_cpu=''
#     so_nhan_cpu =''
#     toc_do_cpu=''
#     ram =''
#     kich_thuoc_man_hinh=''
#     cong_nghe_man_hinh=''
#     do_phan_giai=''
#     chuan_man_hinh=''
#     tan_so_quet=''
#     chat_lieu_mat_kinh=''
#     gpu=''
#     bo_nho_trong=''
#
#     tskt = driver.find_element(By.CLASS_NAME,'re-link.js--open-modal').click()
#     time.sleep(2)
#     TR_XPATH = '//*[@id="tskt"]/tbody/tr'
#
#     try:
#         trs = tskt.find_elements(By.XPATH,TR_XPATH)
#         for tr in trs:
#             ths = tr.find_elements(By.TAG_NAME, 'th')
#             if ths[0].text == 'Kích thước màn hình':
#                 kich_thuoc_man_hinh= (ths[1].text)
#             if ths[0].text == 'Công nghệ màn hình':
#                 cong_nghe_man_hinh=(ths[1].text)
#             if ths[0].text == 'Camera sau':
#                 camera_sau=(ths[1].text)
#             if ths[0].text == 'Camera trước':
#                 camera_truoc=(ths[1].text)
#             if ths[0].text == 'Chipset':
#                 chipset=(ths[1].text)
#             if ths[0].text == 'Dung lượng RAM':
#                 dung_luong_ram=(ths[1].text)
#             if ths[0].text == 'Bộ nhớ trong':
#                 bo_nho_trong=(ths[1].text)
#             if ths[0].text == 'Pin':
#                 pin=(ths[1].text)
#             if ths[0].text == 'Thẻ SIM':
#                 the_sim=(ths[1].text)
#             if ths[0].text == 'Hệ điều hành':
#                 he_dieu_hanh=(ths[1].text)
#             if ths[0].text == 'Tính năng màn hình':
#                 tinh_nang_man_hinh=(ths[1].text)
#             if ths[0].text == 'Loại CPU':
#                 loai_cpu=(ths[1].text)
#             if ths[0].text == 'Trọng lượng':
#                 trong_luong=(ths[1].text)
#             if ths[0].text == 'Bluetooth':
#                 bluetooth=(ths[1].text)
#             if ths[0].text == 'Tần số quét':
#                 tan_so_quet=(ths[1].text)
#
#     except:
#         'CAN NOT GET DETAILS'
#
#     # WRITE INTO .CSV FILE
#     with open('C:\\Users\\GS75\\PycharmProjects\\crawling_new\\phone.csv', 'a',newline='',encoding='utf-8') as f:
#         writer = csv.writer(f)
#         writer.writerow([(name),new_price,old_price,kich_thuoc_man_hinh,cong_nghe_man_hinh,camera_sau,camera_truoc,chipset,dung_luong_ram,bo_nho_trong,pin,the_sim,he_dieu_hanh,tinh_nang_man_hinh,loai_cpu,trong_luong,bluetooth,tan_so_quet])


for i in range(2,10):
    main_page ='https://tiki.vn/dien-thoai-may-tinh-bang/c1795?page=' + str(i)

    driver.get(main_page)
    driver.get(main_page)
    time.sleep(2)
    product_links = get_product_link(driver)
    # print(len(product_links))

for link in product_links:
    driver.get(str(link))
    time.sleep(2)
    table = driver.find_element(By.CLASS_NAME, 'content.has-table')
    trs = table.find_elements(By.TAG_NAME, 'tr')

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

    name_xpath = '/html/body/div[1]/div[1]/main/div[3]/div[1]/div[3]/div[1]/h1'
    price_CN = 'product-price__current-price'
    try:
        name = driver.find_element(By.XPATH, name_xpath).text
    except:
        print('NO NAME')
    try:
        price = driver.find_element(By.CLASS_NAME, price_CN).text
    except:
        print('NO PRICE')
    print( name,'--', price)
    for tr in trs:
        try:
            th = tr.find_elements(By.TAG_NAME, 'td')[0].text
            td = tr.find_elements(By.TAG_NAME, 'td')[1].text

            if th == 'Bluetooth':
                bluetooth=td
            if th == 'Thương hiệu':
                thuong_hieu = td
            if th ==  'Xuất xứ thương hiệu':
                xuat_xu=td
            if th == 'Hỗ trợ thẻ nhớ ngoài':
                ho_tro_the_nho_ngoai=td
            if th== 'Chip set':
                chip_set=td
            if th=='Tốc độ CPU':
                toc_do_cpu=td
            if th=='Kích thước':
                kich_thuoc=td
            if th== 'Loại/ Công nghệ màn hình':
                cong_nghe_man_hinh=td
            if th=='Jack tai nghe':
                jack_tai_nghe=td
            if th=='Loại pin':
                loai_pin=td
            if th =='Loại Sim':
                loai_sim=td
            if th=='Trọng lượng':
                trong_luong=td
            if th=='RAM':
                ram=td
            if th=='Độ phân giải':
                do_phan_giai=td
            if th=='ROM':
                rom=td
            if th=='Kích thước màn hình':
                kich_thuoc_man_hinh=td
        except:
            print('cant get tr')
    with open('M:\\pycharm\\crawling_new\\tiki_data.csv', 'a',newline='',encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([name,price,bluetooth,thuong_hieu,xuat_xu,ho_tro_the_nho_ngoai,chip_set,toc_do_cpu,kich_thuoc,cong_nghe_man_hinh,jack_tai_nghe,loai_pin,loai_sim,trong_luong,ram,do_phan_giai,rom,kich_thuoc_man_hinh
                         ])





