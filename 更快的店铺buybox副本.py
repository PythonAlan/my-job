#!/usr/bin/env python3
#antuor:Alan


#!/usr/bin/env python3
#antuor:Alan


'''python的multiprocessing模块是处理python多进程的模块，multiprocessing模块中有个dummy的子模块。
multiprocessing.dummy对threading多线程编程进行了包装。 '''

# from multiprocessing import Pool 多进程
from multiprocessing.dummy import Pool as ThreadPool #多线程
import requests
import time

import datetime
from lxml import etree

import sys,os

sys.path.append(os.getcwd())

sku = {

    'B00WSC1XB8':'SP.8VH01GC01ori bulb-FBA0811',
    'B00FWNI68I':'ELPLP41-01',
    'B0067PIEPU':'ELPLP60-Q',
    'B00735Z3S4':'ELPLP42-FBA0612',
    'B007CJQ588':'ELPLP49-A33',
    'B00IWMT734':'ELPLP67-04',
    'B00822GNH2':'ELPLP57-FBA0811-1',
    'B00BPDWS4W':'ELPLP65-FBA0601-9',
    'B00ISM35SQ':'B310032^AMUSF^004',
    'B007TAGX0U':'B310032^AMUSF^001',
    'B00BC5AXRC':'ELPLP41-FBA0519-5',
    'B00HR2EQJA':'ELPLP60pro',
    'B0009JFSRM':'ELPLP33-FBA0519-35',
    'B001AJ8YOE':'B310027&AMUSF&02',
    'B00795EGBS':'20-01175-20-FBA0227-1',
    'B00GMV0U4C':'20-01175-20-A33',
    'B009C8L6D6':'ELPLP67-FBA1103-15',
    'B00AO12JWM':'LMP140orib-FBA1223',
    'B00BL5MT5W':'NP16LP-FBA1223-23',
    'B00FWNIJBW':'ELPLP42-A119',
    'B00GH7MUYO':'VIP210W0.8E20.9Nori bulb-FBA0916-30',
    'B001AJD156':'ELPLP42-PP',
#     'B004IV9LB6':'ELPLP34-FBA0206-13',
#     'B00735Z6CM':'ELPLP49-FBA0707-7',
#     'B00FDRC954':'B310048^AMUSF^002',
#     'B00IPB0XQM':'PJD5134ori bulb-A33',
#     'B00PB4WBNE':'AN-F212LP-FBA0207-4',
#     'B000P59HAO':'B310027^AMUSF^005',
#     'B0041TNRYW':'ELPLP54-FBA1027-12',
#     'B005E2ZNYW':'AN-F212LP-FBA0504-17',
#     'B006C6FB96':'SP-LAMP-069-FBA0906',
#     'B008CPQK86':'NP17LP-FBA0218-4',
#     'B00PEZBXAW':'ELPLP78-FBA1014-18',
#     'B00PVTB4Z0':'ELPLP78-0413FBA-11',
#     'B00QGIDFAW':'BL-FU310Bbulb-FBA0511-16',
#     'B00RF475A2':'RLC-079ori bulb-0309FBA-16',
#     'B007CJQ3BC':'ELPLP49-0528FBA-23',
#     'B00CCWP2NE':'ELPLP50-0421FBA-19',
#     'B00JFSFQ4I':'BL-FP230Dori-FBA0206-8',
#     'B00MNA0O10':'ELPLP54-FBA0923',
#     'B00QF1EHUM':'AN-K15LP-FBA0629',
#     'B00QPMS97S':'01-00247-FBA0106-11',
#     'B005F6NTRK':'UX25951-FBA120-18',
#     'B005HB7Z6O':'BL-FS180C-FBA0916-2',
#     'B00735ZBS6':'ELPLP58-A34',
#     'B00IWL69X6':'ELPLP54-A2',
#     'B00Q9WCNXA':'SP.8VH01GC01ori bulb-0309FBA-17',
#     'B00460JIOO':'ELPLP41-FBA1112',
#     'B005HB7T38':'01-00247-A',
#     'B005HB81XU':'ELPLP41-Y',
#     'B005HB8AHW':'B380576&AMUSF&01',
#     'B0065N4XSG':'ELPLP58-KK',
#     'B007CJNR20':'ELPLP42-FBA0207-17',
#     'B009S8OMGS':'ELPLP67-FBA1027-14',
#     'B00BPDWSDI':'ELPLP71-FBA0923',
#     'B00E3QFGM4':'ELPLP67bulb-A33',
#     'B00Q8F10XW':'MC.JH111.001ori bulb-FBA0916-5',
#     'B00SV9A1AQ':'ELPLP67-0528FBA-24',
#     'B01D1EKJCK':'MC.JFZ11.001bulb-031',
#     'B00460PHCQ':'B310019^AMUSF^001',
#     'B005HB82HA':'ELPLP41-FBA0721',
#     'B005HB8AC2':'VT85LP-FBA1223-32',
#     'B005HB8AEU':'VT85LP-FBA0721',
#     'B005YI68B8':'VLT-XD560LP-FBA0106-8',
#     'B007CJNR8Y':'B310027&AMUSF&01',
#     'B007CJS1IA':'B310036&AMUSF&01',
#     'B00BBG50SY':'XL-2400-FBA1124-11',
#     'B00C1WSMGE':'DT00771-FBA0916-13',
#     'B00FDRC7OC':'ELPLP50-03',
#     'B00G9XEWWY':'ELPLP67-05',
#     'B00HAMNWEM':'ELPLP41-FBA0218-5',
#     'B00NEEIXXU':'ELPLP77-0427FBA-8',
#     'B005E4OXK0':'SP-LAMP-024-FBA1027-20',
#     'B005F6O49M':'915P027010-FBA1014-9',
#     'B00735Z5OG':'ELPLP38-FBA0916-17',
#     'B007JJZTBK':'ELPLP60-FBA1217-10',
#     'B00C4OQORS':'VT85LP-0407FBA-43',
#     'B00GATR742':'B410035&AMUSF&01',
#     'B00GB83R5A':'VLT-XD2000LP -0528FBA-21',
#     'B00GB83UXO':'ET-LAB80-FBA1110-9',
#     'B00HH9MXVG':'NP17LP-FBA1103-12',
#     'B00IRVA6Q2':'RLC-079-FBA0902',
#     'B00QK767SQ':'5811118436-SVV-0528FBA-3',
#     'B00TGT72P2':'ELPLP60-0528FBA-25',
#     'B0119DPQPA':'ELPLP68-FBA127-6',
#     'B0119DSKLW':'ELPLP42-FBA120-11',
#     'B0162PMJOQ':'20-01175-20-FBA0204-2',
#     'B0036VO4SE':'DELL 2400MP-A119',
#     'B005HB7SA2':'SP-LAMP-003-FBA0228-2',
#     'B005HB8CDY':'POA-LMP90-FBA127-10',
#     'B005HB8MCK':'BL-FP200C-FBA0624-4',
#     'B007CJNTF0':'XL-5100-03',
#     'B007YW40JY':'ELPLP54-FBA0214-9',
#     'B009BXC438':'AN-F212LP-FBA127-17',
#     'B00B5BDH0S':'POA-LMP126-FBA1110-10',
#     'B00BPDWZXQ':'01-00228-FBA0906',
#     'B00D8V25YW':'2200MP-FBA0504-7',
#     'B00F32UP00':'BL-FP230D-0309FBA-9',
#     'B00F32USX4':'B350386&AMUSF&01',
#     'B00FAU0460':'XL-2400-1021-1',
#     'B00FDRC7S8':'ELPLP60-MN',
#     'B00FDRCAD0':'ELPLP68-FBA0227-22',
#     'B00FWNIDTK':'ELPLP57-B119',
#     'B00GMV64Z6':'ET-LAD40-FBA0519-12',
#     'B00GMV6PG4':'ELPLP38-0309FBA-11',
#     'B00IYE95MS':'NP16LP-0407FBA-31',
#     'B00J80PAZI':'20-01032-20-FBA0910-3',
#     'B00KTEQDRG':'ELPLP49-C',
#     'B00M0ETHG2':'VIP240W/0.8 E20.9N',
#     'B00P41JYXO':'S500-FBA1110-3',
#     'B00PFABFLS':'AN-K15LP-A2',
#     'B00PU6UEQY':'ELPLP78-FBA0227-24',
#     'B00QGKNDMA':'3200MP-0309FBA-3',
#     'B00S8T4XJ4':'RLC-061-FBA0923',
#     'B00YGUCAUS':'ELPLP78-FBA1223-9',
#     'B010V35AMS':'ELPLP49-FBA0106-9',
#     'B0112MMQ5Q':'ELPLP78-FBA1014-19',
#     'B0119DSWX8':'ELPLP49bulb-1118FBA-13',
#     'B012JWVBGI':'ELPLP54-FBA1229-3',
#     'B0132RYTA4':'BL-FP230J-FBA1027-3',
#     'B015R3NNYO':'VIP210W0.8E20.9N-FBA120-13',
#     'B016U402WU':'ELPLP42-FBA120-12',
#     'B01BHR4JUQ':'5J.JAH05.001-0205',
#     'B002WVE0TM':'B340315&AMUSF&01',
#     'B003QINZ5K':'ET-LAB10-FBA0228-17',
#     'B0047PGSI2':'915P043010-FBA1209-8',
#     'B004IREJRG':'EzCAP170',
#     'B004IV9N7S':'B310027^AMUSF^002',
#     'B00557670A':'DI-VJA4-48UA',
#     'B005713BQ2':'NP13LP-FBA1124-14',
#     'B005FIVJG6':'B310048^AMUSF^003',
#     'B005HB7V40':'DT00841-A33',
#     'B005IUZMFU':'BHL-5009-S-FBA0207-5',
#     'B00603RHTS':'20-01032-20-A33',
#     'B0070ZYYI2':'XL-2400-1016',
#     'B00735YQY6':'ELPLP33-FBA0707-6',
#     'B00795E2QM':'ELPLP50-FBA0207-18',
#     'B00AE0DKM6':'NP13LP-0323FBA-12',
#     'B00AO14KBU':'RLC-072ori-A2',
#     'B00BQUWZ56':'ELPLP49-0308FBA',
#     'B00C74NPYA':'B130224^AMUSM^0212',
#     'B00C74YH0G':'ET-LAV200-FBA0106-6',
#     'B00CXLCZWA':'BL-FP230Iori bulb-FBA0519-33',
#     'B00DI2Q3MQ':'ELPLP42-FBA0811-1',
#     'B00DTTVOYU':'20-01175-20-FBA1109-1',
#     'B00F32UT06':'ELPLP49-FG',
#     'B00FWNIGKG':'NP15LP-0309FBA-14',
#     'B00GAP1L34':'ELPLP54-01',
#     'B00GMV6S8Y':'RLC-061-01',
#     'B00GMV6VPE':'ELPLP40-0316FBA',
#     'B00HJK4ZVY':'2400MP-FBA0729',
#     'B00HK82JKE':'5J.J3T05.001-0309FBA-4',
#     'B00HR2GKGW':'ELPLP67pro',
#     'B00HRT5WVO':'SP-LAMP-070ori-FBA0820',
#     'B00I5CHIVY':'ELPLP42-1',
#     'B00IWLMOOE':'ELPLP60-0407FBA-25',
#     'B00J3BBULU':'ELPLP68-0421FBA-23',
#     'B00JAQHB2U':'ELPLP34-0413FBA-8',
#     'B00MNA26DO':'ELPLP49-FBA0106-4',
#     'B00PFMO5EK':'PK-L2210U-FBA0902',
#     'B00PU5MWVA':'B310055&AMUSF&01',
#     'B00TZO2V22':'ELPLP67-0407FBA-26',
#     'B00U22J386':'ELPLP75-FBA1209-4',
#     'B00UCZ1DSG':'ELPLP49bulb-0407FBA-22',
#     'B00URFBWGO':'SP-LAMP-090-1218-1',
#     'B00VFVDX3E':'1510Xori-0528FBA-19',
#     'B00WQR3ZAM':'B310039&AMUSF&02',
#     'B00YGT1DNO':'20-01501-20-FBA1217-3',
#     'B00YRVDHBC':'20-01032-20-FBA1215',
#     'B011E18YWE':'ELPLP78-1222-3FBA',
#     'B012CNE66G':'SP-LAMP-019-FBA1124-7',
#     'B01A6OML4M':'ELPLP77-FBA0218-7',
#     'B01ALEX8DU':'1020991-0114',
#     'B003QIMBIC':'VT75LP-FBA0228-10',
#     'B003QIQ3BS':'B390592^AMUSF^001',
#     'B00460DHBY':'AN-F212LP-FBA1020',
#     'B00460JT34':'NP07LP-FBA1209-5',
#     'B00460PIAM':'ELPLP42-FBA1027-7',
#     'B004BQ0O3C':'B340340&AMUSF&02',
#     'B0055E35AS':'ET-LAE500-FBA1223-12',
#     'B0056CF2DW':'ELPLP21-FBA0519-16',
#     'B005F6O4V0':'915P028010-FBA0601-24',
#     'B005HB7IQQ':'B350399^AMUSF^001',
#     'B005HB7U5K':'DT00911-B119',
#     'B005HB7WLM':'20-01032-20-FBA0619-3',
#     'B005HB8LNU':'AN-K9LP-FBA0906',
#     'B005HB8M4S':'BL-FS200B-0309FBA-10',
#     'B005HB8MMA':'BP96-01795A-115FBA',
#     'B005HB8NEW':'AN-XR10LP-FBA',
#     'B006RKJQJI':'ELPLP55-FBA1223-5',
#     'B006ZYGLTY':'XL-5100-FBA127-12',
#     'B00735ZBC2':'ELPLP58-Q',
#     'B00735ZBLI':'B310040^AMUSF^002',
#     'B00795DGLE':'20-01032-20-A',
#     'B00795E83Y':'ET-LAF100-0522-13',
#     'B007CJNXN8':'AN-F212LP-FBA0228-26',
#     'B0081PLG3G':'ELPLP42-0528FBA-11',
#     'B0085MLASQ':'VT75LP-FBA0916-9',
#     'B009LKRXBY':'ELPLP42-FBA1110-13',
#     'B009NVBX6C':'VLT-HC910LP-1118FBA',
#     'B00AHT0DV0':'ELPLP67-FBA0906',
#     'B00AORAR84':'B310033^AMUSF^005',
#     'B00C1XE9CE':'DT00911-0430-3',
#     'B00C43NBAC':'ELPLP60-GG',
#     'B00C74UU02':'ELPLP63-0528FBA-13',
#     'B00CCWUYO6':'B310039&AMUSF&01',
#     'B00DURCWS8':'ET-LAD55-0403',
#     'B00EEJTW9S':'01-00247-FBA0910-1',
#     'B00F32UQQ8':'POA-LMP124-FBA1006-9',
#     'B00FDRC9JA':'POA-LMP90-0330-FBA',
#     'B00GAW77RQ':'ELPLP41bulb-FBA0227-19',
#     'B00GB96XB4':'NP07LP-FBA0207-26',
#     'B00HK82KP8':'AN-XR30LP-01',
#     'B00HM2M6EC':'ELPLP61-FBA0930-12',
#     'B00IWFV00E':'ELPLP13-01',
#     'B00IWKQD42':'ELPLP49-K',
#     'B00IYFQP2A':'SP-LAMP-009-0309FBA-18',
#     'B00KBAF0ZO':'AN-D400LP-FBA127-16',
#     'B00KXK6GL4':'B370486^AMUSF^001',
#     'B00M3I6WA4':'POA-LMP140-0409-1',
#     'B00M3VOD34':'SP-LAMP-072-FBA1020',
#     'B00OHQT5FO':'ELPLP63-0413FBA-21',
#     'B00Q2LLBJK':'BL-FP240C-FBA0601-2',
#     'B00QF5OJWO':'B330275^AMUSF^001',
#     'B00QK3TSFE':'BL-FU310B-FBA0713-5',
#     'B00RJJN0IO':'ELPLP78',
#     'B00RMEE76K':'01-00247-FBA0519-11',
#     'B00TGP410K':'ELPLP65-FBA0713-9',
#     'B00WYNDX9G':'SP.8VH01GC01ori bulb-FBA0601-5',
#     'B00Z5G24FI':'VLT-XD600LP-1105FBA',
#     'B00ZCDDUD4':'RLC-079ori bulb-FBA0713-16',
#     'B0110BS0JA':'B310049&AMUSF&02',
#     'B011I0Q478':'ET-LAV100-FBA1014-20',
#     'B012CNHICU':'SP-LAMP-070-1118FBA-8',
#     'B016XZR1H0':'B390595^AMUSM^003',
#     'B016XZR78S':'01-00247-FBA120-1',
#     'B019Z8RNH0':'ELPLP68-FBA127-7',
#     'B019Z8SSRO':'NPLM69-FBA0302-10',
#     'B01CJ7S01C':'RLC-070-0304',
#     'B000S5ZDRC':'AN-XR30LP-01',
#     'B003QAYDCC':'XL-5100-FBA120-20',
#     'B003QIIG4U':'B310004^AMUSF^001',
#     'B003QIVFC0':'TY-LA1001-FBA1209-2',
#     'B003QL370U':'BP96-00826A-1103-10',
#     'B003U4GYBM':'DT00871-FBA0302-5',
#     'B00460I0YS':'ELPLP36-FBA1027-6',
#     'B00460RPFS':'VT75LP-FBA1124-9',
#     'B004B3W43S':'ET-LAB80-1118FBA',
#     'B004H2L150':'4210X-FBA127-15',
}








#Re_review = '<span id="acrCustomerReviewText" class="a-size-base">(.*?)</span>'
#Re_price = '<span id="priceblock_ourprice" class="a-size-medium a-color-price">(.*?)</span>'  #不匹配货币符号，用斜杠转译
#Re_soldby = '>(.*?)</a> and'
#Re_other_price = '<span class="a-size-medium a-color-price">(.*?)</span>'
#Re_other_sellers = '<span class="a-size-small mbcMerchantName">(.*?)</span>'

price_xpath = '//td[2]/span[1]/text()'
review_xpath = '//div[3]/div/span[3]/a/span/text()'
soldby_xpath = '//div[5]/div[14]/div/a/text()'
otherprice_xpath = '//div/div[1]/div/div[2]/div/span[2]/div/div[1]/span[1]/text()'
otherseller_xpath = '//div/div[1]/div/div[2]/div/span[2]/div/div[2]/span[2]/text()'
otherprice_2_xpath = '//div/div[1]/div/div[3]/div/span[2]/div/div[1]/span[1]/text()'
otherseller_2_xpath = '//div/div[1]/div/div[3]/div/span[2]/div/div[2]/span[2]/text()'


urls = []
model_numbers = []
for i,v in sku.items():
    product_page = 'http://www.amazon.com/dp/{}'.format(i)
    urls.append(product_page)
    model_numbers.append(v)

a = len(urls)
b = len(model_numbers)

product_dict = dict(map(lambda x,y:[x,y], urls,model_numbers))



#count = 0 #计算数量

headers_am = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
#如果请求头有变化，请及时更新不然脚本会出错
def Scraper(url):
    # global other_seller_2nd
    global other_price_2nd
    global price
    #global count  #计算数量
    try:
        response = requests.get(url,headers=headers_am).content #get().content 返回的类型是<class 'bytes'> 而get().text<class 'str'>                                                         #类型是response type(response)返回<Response [200]>
        tree = etree.HTML(response)
        Reviews = tree.xpath(review_xpath)[0]
        price =   tree.xpath(price_xpath)[0]#tree.xpath返回的是列表
        soldby = tree.xpath(soldby_xpath) #用lxml，xpath获取节点元素
        other_price = tree.xpath(otherprice_xpath)[0].strip()
        other_seller = tree.xpath(otherseller_xpath)[0].strip()
        other_price_2nd = tree.xpath(otherprice_2_xpath)[0].strip()
        other_seller_2nd = tree.xpath(otherseller_2_xpath)[0].strip()
        with open('am_scraper.txt','a') as f:   #‘a’新建追加模式
            f.write('ASIN:{0},评价:{8},爬去完毕at{1},'
                    '结果:,Buybox价:{2},Soldby:{3},Fulfill_by:{9},'
                    '其它卖家(1){4},By:{5},'
                    '其它卖家(2){6},By:{7}\n'.format(url,
                                                 time.ctime(),
                                                 price,
                                                 soldby[0],
                                                 other_price,
                                                 other_seller,
                                                 other_price_2nd,
                                                 other_seller_2nd,
                                                 Reviews,
                                                 soldby[1]
                                                 ))


    #count +=1
        print('-------ASIN:{0} \033[1;31;40m评价:{8}\033[0m 爬去完毕at{1}结果:\nBuybox价:\033[1;31;40m{2}\033[0m,Soldby:\033[1;32;40m{3}\033[0m,'
              '\n\033[1;35;40mFullfill_by:{9}\033[0m'
              '\n\033[1;36;40m其它卖家(1)\033[0m:{4} By:{5} '
              '\n\033[1;36;40m其它卖家(2)\033[0m:{6} By:{7}'.format(url,
                                                                time.ctime(),
                                                                price,
                                                                soldby[0],
                                                                other_price,
                                                                other_seller,
                                                                other_price_2nd,
                                                                other_seller_2nd,
                                                                Reviews,
                                                                soldby[1],
                                                                #model_number,
                                                                #count,
                                                                ))
    except Exception as e:
        pass



if __name__ == '__main__':
    pool = ThreadPool(9)
    time_start = datetime.datetime.now()
    results = pool.map(Scraper,urls)
    pool.close()
    pool.join()
    time_end = datetime.datetime.now()
    time_cost = time_end - time_start
    print('共耗时:',time_cost)