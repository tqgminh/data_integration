import time
import csv

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By


options = Options()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
driver = webdriver.Chrome(executable_path='C:\\Users\\GS75\\Desktop\\chromedr\\chromedriver.exe', chrome_options=options)
driver.maximize_window()


LOGIN_URL = 'https://cellphones.com.vn/mobile.html'
driver.get(LOGIN_URL)
driver.get(LOGIN_URL)


ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
time.sleep(5)


name_list = []
new_price_list = []
old_price_list = []
kich_thuoc_man_hinh_list = []
cong_nghe_man_hinh_list = []
camera_sau_list = []
camera_truoc_list = []
chipset_list = []
dung_luong_ram_list = []
bo_nho_trong_list = []
pin_list = []
the_sim_list = []
he_dieu_hanh_list = []
do_phan_giai_man_hinh_list = []
tinh_nang_man_hinh_list = []
loai_cpu_list = []
trong_luong_list = []
bluetooth_list = []
tan_so_quet_list = []


ITEM_CN = 'item-product'


def get_tskt(driver):
    # CHECK ADS
    try:
        id = "ins-editable-button-1580496494"
        driver.find_element(By.ID, id).click()
        time.sleep(2)
    except:
        time.sleep(2)

    # GET NAME AND PRICE
    name_xpath = 'box-name__box-product-name'
    new_price_xpath ='special-price'
    old_price_xpath ='old-price'

    try:
        name =driver.find_element(By.CLASS_NAME, name_xpath).text
    except:
        name =''
    try:
        new_price = driver.find_element(By.CLASS_NAME, new_price_xpath).text
    except:
        new_price=''
    try:
        old_price = driver.find_element(By.CLASS_NAME, old_price_xpath).text
    except:
        old_price =''

    # GET DETAILS
    kich_thuoc_man_hinh = ''
    cong_nghe_man_hinh = ''
    camera_sau = ''
    camera_truoc = ''
    chipset = ''
    dung_luong_ram = ''
    bo_nho_trong = ''
    pin = ''
    the_sim = ''
    he_dieu_hanh = ''
    tinh_nang_man_hinh = ''
    loai_cpu = ''
    trong_luong = ''
    bluetooth = ''
    tan_so_quet = ''

    tskt = driver.find_element(By.ID,'tskt')
    TR_XPATH = '//*[@id="tskt"]/tbody/tr'

    try:
        trs = tskt.find_elements(By.XPATH,TR_XPATH)
        for tr in trs:
            ths = tr.find_elements(By.TAG_NAME, 'th')
            if ths[0].text == 'Kích thước màn hình':
                kich_thuoc_man_hinh= (ths[1].text)
            if ths[0].text == 'Công nghệ màn hình':
                cong_nghe_man_hinh=(ths[1].text)
            if ths[0].text == 'Camera sau':
                camera_sau=(ths[1].text)
            if ths[0].text == 'Camera trước':
                camera_truoc=(ths[1].text)
            if ths[0].text == 'Chipset':
                chipset=(ths[1].text)
            if ths[0].text == 'Dung lượng RAM':
                dung_luong_ram=(ths[1].text)
            if ths[0].text == 'Bộ nhớ trong':
                bo_nho_trong=(ths[1].text)
            if ths[0].text == 'Pin':
                pin=(ths[1].text)
            if ths[0].text == 'Thẻ SIM':
                the_sim=(ths[1].text)
            if ths[0].text == 'Hệ điều hành':
                he_dieu_hanh=(ths[1].text)
            if ths[0].text == 'Tính năng màn hình':
                tinh_nang_man_hinh=(ths[1].text)
            if ths[0].text == 'Loại CPU':
                loai_cpu=(ths[1].text)
            if ths[0].text == 'Trọng lượng':
                trong_luong=(ths[1].text)
            if ths[0].text == 'Bluetooth':
                bluetooth=(ths[1].text)
            if ths[0].text == 'Tần số quét':
                tan_so_quet=(ths[1].text)

    except:
        'CAN NOT GET DETAILS'

    # WRITE INTO .CSV FILE
    with open('C:\\Users\\GS75\\PycharmProjects\\crawling_new\\phone.csv', 'a',newline='',encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([(name),new_price,old_price,kich_thuoc_man_hinh,cong_nghe_man_hinh,camera_sau,camera_truoc,chipset,dung_luong_ram,bo_nho_trong,pin,the_sim,he_dieu_hanh,tinh_nang_man_hinh,loai_cpu,trong_luong,bluetooth,tan_so_quet])

    try:
        id = "ins-editable-button-1580496494"
        driver.find_element(By.ID,id).click()
    except:
        print('NO ADS')


# GET MORE PRODUCT
for i in range(100):
    try:
        try:
            id = "ins-editable-button-1580496494"
            driver.find_element(By.ID, id).click()
        except:
            'NO ADS '

        more_product = driver.find_elements(By.CLASS_NAME,'fas.fa-chevron-down')[8]
        more_product.click()
        time.sleep(7)
    except:
        print('NO MORE PRODUCT')
        time.sleep(7)
        break


items = driver.find_elements(By.XPATH, '/html/body/div[1]/div/section/div/div[5]/div/div/div')

try:
    id = "ins-editable-button-1580496494"
    driver.find_element(By.ID, id).click()
except:
    a=1
    time.sleep(2)

link_products = []
for i in range(len(items)):
    link_product_xpath = '/html/body/div[1]/div/section/div/div[5]/div/div/div'
    link_product = driver.find_element(By.XPATH, link_product_xpath+'['+str(i+1)+']/div[1]/a').get_attribute('href')
    link_products.append(link_product)

print(link_products)


# MAIN LOOP
i=1
for link in link_products:
    driver.get(link)
    try:
        id = "ins-editable-button-1580496494"
        driver.find_element(By.ID, id).click()
    except:
        a = 1
    try:
        get_tskt(driver)
    except:
        print('FAILED TO GET DETAILS')
    print('-------------------------------------------', i,'/',len(link_products))
    i=i+1


driver.close()

