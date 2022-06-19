import time
import csv

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By


options = Options()
driver = webdriver.Chrome(executable_path='C:\\Users\\GS75\\Desktop\\chromedr\\chromedriver.exe', chrome_options=options)


LOGIN_URL = 'https://viettelstore.vn/dien-thoai'
# driver.get(LOGIN_URL)
driver.get(LOGIN_URL)


ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
time.sleep(5)


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


def show_more_product(driver):
    # time.sleep(2)
    # more_product_xpath ='/html/body/div[2]/div/div[4]/div[2]/div[3]/div/div/a'
    more_product_id = 'div_Danh_Sach_San_Pham_loadMore_btn'
    try:
        driver.find_element(By.ID,more_product_id).find_element(By.TAG_NAME,'a').click()
    except:
        # driver.find_element(By.ID, more_product_id).find_element(By.TAG_NAME, 'a').click()
        print('NO MORE PRODUCT')
    try:
        driver.find_element(By.ID, more_product_id).find_element(By.TAG_NAME, 'a').click()
    except:
        print('NO MORE PRODUCT again')


def get_product_link(driver):
    links = []
    link_CN ='item.ProductList3Col_item'
    number_product = len(driver.find_elements(By.CLASS_NAME,link_CN))
    for i in range(number_product):
        link = driver.find_elements(By.CLASS_NAME,link_CN)[i].find_element(By.TAG_NAME,'a').get_attribute('href')
        links.append(link)
    print(len(links))
    return links


def get_detals(driver):
    name_xpath = '/html/body/div[3]/div[1]/div/div[1]/ul/li[2]/div/div/div[1]/div[1]/h1'
    new_price  = '/html/body/div[3]/div[1]/div/div[1]/ul/li[2]/div/div/div[1]/div[1]/div[1]/span[1]'

    name =''
    kich_thuoc_man_hinh =''
    cong_nghe_man_hinh=''
    camera_sau=''
    camera_truoc=''
    loai_sim=''
    bo_nho_trong=''
    pin=''
    ram=''
    chip_set=''
    bluetooth=''


    try:
        name = driver.find_element(By.XPATH,name_xpath).text
    except:
        print('no name')
    try:
        new_price = driver.find_element(By.XPATH,new_price).text
    except:
        print('no new price')
    driver.execute_script("window.scrollTo(0, 3000)")
    # try:
    #     driver.find_elements(By.CLASS_NAME, 'glyphicon.glyphicon-menu-down')[1].click()
    # except:
    #     print('can not get table')
    # driver.execute_script("window.scrollTo(0, 3000)")
    table = driver.find_elements(By.CLASS_NAME,'digital ')[0].find_element(By.TAG_NAME,'table')
    trs   = table.find_elements(By.TAG_NAME,'tr')
    # pop = driver.find_elements(By.ID, 'pop-digital')
    # driver.execute_script("pop.scrollTo(0, 3000)")

    for tr in trs:
        th=''
        td=''

        try:
            th = tr.find_elements(By.TAG_NAME, 'td')[0].text
            td = tr.find_elements(By.TAG_NAME, 'td')[1].text
            # print(th, td)
        except:
            # print('no')
            x=0
        hdh =''
        if th == 'Hệ điều hành:':
            hdh = td
            # driver.execute_script("window.scrollTo(0, 1000)")
        if th == 'CPU:':
            chip_set = td
            # driver.execute_script("window.scrollTo(0, 1000)")
        if th == 'Màn hình:':
            cong_nghe_man_hinh = td
            # driver.execute_script("window.scrollTo(0, 1000)")
        if th =='Camera sau:':
            camera_sau=td
            # driver.execute_script("window.scrollTo(0, 1000)")
        if th =='Camera trước:':
            camera_truoc = td
            # driver.execute_script("window.scrollTo(0, 1000)")
        if th == 'Hỗ trợ đa sim:':
            loai_sim = td

        if th == 'Dung lượng pin':
            pin = td

        if th == 'RAM:':
            ram = td

        if th == 'Độ phân giải':
            do_phan_giai = td

        if th == 'Bộ nhớ trong:':
            bo_nho_trong = td

        if th == 'Pin:':
            pin = td
            # driver.execute_script("window.scrollTo(0, 1000)")
    # except:
    #     print('cant get tr')
    with open('M:\\pycharm\\crawling_new\\viettel_store.csv', 'a',newline='',encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([name,new_price,cong_nghe_man_hinh,camera_sau,camera_truoc,chip_set,ram,bo_nho_trong,pin,loai_sim,hdh])

for i in range(4):
    show_more_product(driver)
    time.sleep(2)

links = get_product_link(driver)


for link in links:
    try:
        driver.get(link)
    except:
        x=0
    try:
        get_detals(driver)
    except:
        print('can not get details')





driver.close()

