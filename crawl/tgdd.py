import time
import csv

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By


LOGIN_URL = 'https://www.thegioididong.com/dtdd#c=42&o=3&pi=0'
options = Options()
driver = webdriver.Chrome(executable_path='C:\\Users\\GS75\\Desktop\\chromedr\\chromedriver.exe', chrome_options=options)
driver.get(LOGIN_URL)
driver.get(LOGIN_URL)
ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
time.sleep(5)


def is_findable_element(driver, attribute, attribute_value, target=None):
    attribute = attribute.upper()

    if target and attribute == 'XPATH':
        raise Exception('XPATH is invalid to find in target')

    driver.implicitly_wait(0)

    finder = target or driver
    result = finder.find_elements(getattr(By, attribute), attribute_value)

    time.sleep(1)

    return bool(result)


def get_tskt(driver):
    name_xpath = '/html/body/section[1]/h1'
    new_price_xpath ='/html/body/section[1]/div[3]/div[2]/div[3]/div[2]/div/p[1]'
    old_price_xpath ='/html/body/section[1]/div[3]/div[2]/div[3]/div[2]/div/p[2]'

    try:
        name =driver.find_element(By.XPATH, name_xpath).text
    except:
        name =''
    try:
        new_price = driver.find_element(By.XPATH, new_price_xpath).text
    except:
        new_price=''
    try:
        old_price = driver.find_element(By.XPATH, old_price_xpath).text
    except:
        old_price =''
    print(name, ' -- ',new_price, ' -- ' ,old_price)
    k = 1

    try:
        tskt = driver.find_element(By.CLASS_NAME, 'btn-detail.btn-short-spec ')
        tskt.click()
        time.sleep(2)

        cong_nghe_man_hinh = ''
        do_phan_giai =''
        man_hinh_rong =''
        do_sang_toi_da=''
        mat_kinh_cam_ung =''
        camera_sau = ''
        camera_truoc = ''
        he_dieu_hanh = ''
        cpu=''
        toc_do_cpu=''
        gpu=''
        ram=''
        bo_nho_trong=''
        the_nho=''
        sim=''
        bluetooth=''
        cong_ket_noi=''
        dung_luong_pin=''
        kich_thuoc_khoi_luong=''
        thoi_diem_ra_mat=''

        ten_cot =[]
        data=[]

        ths = driver.find_elements(By.CLASS_NAME, 'ctLeft')
        tds = driver.find_elements(By.CLASS_NAME, 'ctRight')

        for th in ths:
            a=str(th.text)
            if (a=='????? ph??n gi???i:') and k==1:
                a='????? ph??n gi???i m??n h??nh:'
                k=2
            if (a=='????? ph??n gi???i:') and k==2:
                a='????? ph??n gi???i camera sau:'
                k=3
            if ((a=='????? ph??n gi???i:') and k==3):
                a='????? ph??n gi???i camera tr?????c:'
                k=4
            ten_cot.append(a)

        for td in tds:
            data.append(td.text)
        zip_iterator = zip(ten_cot, data)
        table = dict(zip_iterator)

        for data_head in table:
            if data_head=='C??ng ngh??? m??n h??nh:':
                cong_nghe_man_hinh=str(table.get(data_head))
            if data_head=='????? ph??n gi???i m??n h??nh:':
                do_phan_giai=str(table.get(data_head))
            if data_head=='M??n h??nh r???ng:':
                man_hinh_rong=str(table.get(data_head))
            if data_head=='????? s??ng t???i ??a:':
                do_sang_toi_da=str(table.get(data_head))
            if data_head=='M???t k??nh c???m ???ng:':
                mat_kinh_cam_ung=str(table.get(data_head))
            if data_head=='????? ph??n gi???i camera sau:':
                camera_sau=str(table.get(data_head))
            if data_head=='????? ph??n gi???i camera tr?????c:':
                camera_truoc=str(table.get(data_head))
            if data_head=='H??? ??i???u h??nh:':
                he_dieu_hanh=str(table.get(data_head))
            if data_head=='Chip x??? l?? (CPU):':
                cpu=str(table.get(data_head))
            if data_head=='T???c ????? CPU:':
                toc_do_cpu=str(table.get(data_head))
            if data_head=='Chip ????? h???a (GPU):':
                gpu=str(table.get(data_head))
            if data_head == 'RAM:':
                ram = str(table.get(data_head))
            if data_head=='B??? nh??? trong:':
                bo_nho_trong=str(table.get(data_head))
            if data_head=='Th??? nh???:':
                the_nho=str(table.get(data_head))
            if data_head=='SIM:':
                sim=str(table.get(data_head))
            if data_head=='Bluetooth:':
                bluetooth=str(table.get(data_head))
            if data_head=='C????ng k????t n????i/sa??c:':
                cong_ket_noi=str(table.get(data_head))
            if data_head=='Dung l?????ng pin:':
                dung_luong_pin=str(table.get(data_head))
            if data_head=='K??ch th?????c, kh???i l?????ng:':
                kich_thuoc_khoi_luong=str(table.get(data_head))
            if data_head=='Th???i ??i???m ra m???t:':
                thoi_diem_ra_mat=str(table.get(data_head))

        with open('C:\\Users\\GS75\\PycharmProjects\\crawling_new\\tgdd_phone.csv', 'a',newline='',encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([name,new_price,old_price,cong_nghe_man_hinh,do_phan_giai,man_hinh_rong,
                             do_sang_toi_da,mat_kinh_cam_ung,camera_sau,camera_truoc,
                             he_dieu_hanh,cpu,toc_do_cpu,gpu,ram,bo_nho_trong,the_nho,sim,bluetooth,
                             cong_ket_noi,dung_luong_pin,kich_thuoc_khoi_luong,thoi_diem_ra_mat])
    except:
        print('FAILED TO GET TSKT')


#   SHOW MORE PRODUCT
for i in range(100):
    try:
        more_product = driver.find_element(By.XPATH,'/html/body/section[1]/div[3]/div[2]')
        more_product.click()
        time.sleep(2)
    except:
        print('NO MORE PRODUCT')
        break


#   GET LINKS OF PRODUCT
items = driver.find_elements(By.XPATH, '/html/body/section[1]/div[3]/ul/li')
link_products = []
for i in range(len(items)):
    link_product_xpath = '/html/body/section[1]/div[3]/ul/li'
    link_product = driver.find_element(By.XPATH, link_product_xpath+'['+str(i+1)+']/a[1]').get_attribute('href')
    link_products.append(link_product)


#   MAIN LOOP
i=1
for link in link_products:
    driver.get(link)
    get_tskt(driver)
    print('------------------------------------------------------',i)
    i = i+1

driver.close()

