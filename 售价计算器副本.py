#!/usr/bin/env python3
#antuor:Alan
import settings
from tkinter import *





class LoadCalculator():




    def __init__(self):
        window = Tk()
        window.title("B2C计算器E邮宝version1.0 author: 吕毅")
#################################部件############################################################
        label1 = Label(window,text="售价:").grid(row = 1,sticky=W)
        label2 = Label(window,text="采购价¥ :").grid(row =2,sticky=W)
        label3 = Label(window,text="重量g :").grid(row=3,sticky=W)

        label4 = Label(window,text="0% 利润率").grid(row=12,sticky=W)
        label5 = Label(window,text="5% 利润率").grid(row=13,sticky=W)
        label6 = Label(window,text="10% 利润率").grid(row=14,sticky=W)
        label7 = Label(window,text="15% 利润率").grid(row=15,sticky=W)
        label8 = Label(window,text="20% 利润率").grid(row=16,sticky=W)
        label9 = Label(window,text="25% 利润率").grid(row=17,sticky=W)
        label10 = Label(window,text="30% 利润率").grid(row=18,sticky=W)
        label18 = Label(window,text="总成本¥ :",bg = 'red').grid(row=5,sticky=W)#
        label21 = Label(window,text="当前利润率 :").grid(row=11,sticky=W) #要向后改
        label_ShippingMethod = Label(window,text="物流方式:").grid(row=4,sticky=W)
        label_ChinaShippingFee = Label(window,text="FBA费(本地货币):").grid(row=6,sticky=W)
        label_EubShippingFee = Label(window,text="E邮宝邮费(头程)¥:").grid(row=7,sticky=W)
        label_CommissionFee = Label(window,text="平台费¥:").grid(row=8,sticky=W)
        label_PackageCost = Label(window,text="包装费¥:").grid(row=9,sticky=W)
        label_GrossProfit = Label(window,text="毛利润¥:",bg = 'red').grid(row=10,sticky=W)










        label_FBA_UK = Label(window,text="FBA_UK").grid(row=4,column=4,sticky=E)
        label_FBA =Label(window,text="FBA_US").grid(row=4,column=2,sticky=E)
        label_First_Class = Label(window,text='E邮宝_US').grid(row=4,column=3,sticky=E)
#####################################输入框#########################################
        self.SalePrice = DoubleVar()           #saleprice
        entry_a = Entry(window,textvariable = self.SalePrice,width=7).grid(row=1,column=4)
        self.PurchasePrice = DoubleVar()    #采购价
        entry_b = Entry(window,textvariable = self.PurchasePrice,width=7).grid(row=2,column=4)
        self.ShippingWeight = DoubleVar()  #重量g
        entry_c = Entry(window,textvariable = self.ShippingWeight,width=7).grid(row =3,column=4)
#######################################售价换成RMB##############################################
        self.Exchange_to_RMB = StringVar()
        label_Exchange_to_RMB = Label(window,textvariable = self.Exchange_to_RMB).grid(row=1,column=3,sticky=E)

##################################FBA显示部件###################################################
        self.First_Class_US = StringVar()
        label_First_Class_US = Label(window,textvariable = self.First_Class_US).grid(row=7,column=2,sticky=E)
        self.PackageCost_FBA_US = StringVar()
        label_PackageCost_FBA_US = Label(window,textvariable = self.PackageCost_FBA_US).grid(row=9,column=2,sticky=E)
        self.FBA_US_Cost = StringVar()
        label_FBA_US_Cost  = Label(window,textvariable = self.FBA_US_Cost).grid(row=6,column=2,sticky=E)
        self.CommissionFee_fba = StringVar()
        label_CommissionFee_fba = Label(window,textvariable = self.CommissionFee_fba).grid(row=8,column=2,sticky=E)
        self.GrossProfit_fba = StringVar()
        label_GrossProfit_fba = Label(window,textvariable = self.GrossProfit_fba).grid(row=10,column=2,sticky=E)
        self.ToTalCost = StringVar()
        label19 = Label(window,textvariable = self.ToTalCost).grid(row=5,column=2,sticky=E)
        self.NowProfit = StringVar()
        label20 = Label(window,textvariable = self.NowProfit).grid(row=11,column=2,sticky=E)
        self.ZeroPercent = StringVar()
        label11 = Label(window,textvariable = self.ZeroPercent).grid(row=12,column=2,sticky=E)
        self.FivePercent = StringVar()
        label12 = Label(window,textvariable = self.FivePercent).grid(row=13,column=2,sticky=E)
        self.TenPercent = StringVar()
        label13 = Label(window,textvariable = self.TenPercent).grid(row=14,column=2,sticky=E)
        self.FifteenPercent = StringVar()
        label14 = Label(window,textvariable = self.FifteenPercent).grid(row=15,column=2,sticky=E)
        self.TwentyPercent = StringVar()
        label15 = Label(window,textvariable = self.TwentyPercent).grid(row=16,column=2,sticky=E)
        self.TwentyFivePercent = StringVar()
        label16 = Label(window,textvariable = self.TwentyFivePercent).grid(row=17,column=2,sticky=E)
        self.ThirtyPercent = StringVar()
        label17 = Label(window,textvariable = self.ThirtyPercent).grid(row=18,column=2,sticky=E)

#################################FBA_UK显示部件###########################################################
        self.First_Class_UK = StringVar()
        label_First_Class_UK = Label(window,textvariable = self.First_Class_UK).grid(row=7,column=4,sticky=E)
        self.PackageCost_FBA_UK = StringVar()
        label_PackageCost_FBA_UK = Label(window,textvariable = self.PackageCost_FBA_UK).grid(row=9,column=4,sticky=E)
        self.FBA_UK_Cost = StringVar()
        label_FBA_UK_Cost  = Label(window,textvariable = self.FBA_UK_Cost).grid(row=6,column=4,sticky=E)
        self.CommissionFee_fba_uk = StringVar()
        label_CommissionFee_fba_uk = Label(window,textvariable = self.CommissionFee_fba_uk).grid(row=8,column=4,sticky=E)
        self.GrossProfit_fba_uk = StringVar()
        label_GrossProfit_fba_uk = Label(window,textvariable = self.GrossProfit_fba_uk).grid(row=10,column=4,sticky=E)
        self.ToTalCost_uk = StringVar()
        label19_uk = Label(window,textvariable = self.ToTalCost_uk).grid(row=5,column=4,sticky=E)
        self.NowProfit_uk = StringVar()
        label20_uk = Label(window,textvariable = self.NowProfit_uk).grid(row=11,column=4,sticky=E)
        self.ZeroPercent_uk = StringVar()
        label11_uk = Label(window,textvariable = self.ZeroPercent_uk).grid(row=12,column=4,sticky=E)
        self.FivePercent_uk = StringVar()
        label12_uk = Label(window,textvariable = self.FivePercent_uk).grid(row=13,column=4,sticky=E)
        self.TenPercent_uk = StringVar()
        label13_uk = Label(window,textvariable = self.TenPercent_uk).grid(row=14,column=4,sticky=E)
        self.FifteenPercent_uk = StringVar()
        label14_uk = Label(window,textvariable = self.FifteenPercent_uk).grid(row=15,column=4,sticky=E)
        self.TwentyPercent_uk = StringVar()
        label15_uk = Label(window,textvariable = self.TwentyPercent_uk).grid(row=16,column=4,sticky=E)
        self.TwentyFivePercent_uk = StringVar()
        label16_uk = Label(window,textvariable = self.TwentyFivePercent_uk).grid(row=17,column=4,sticky=E)
        self.ThirtyPercent_uk = StringVar()
        label17_uk = Label(window,textvariable = self.ThirtyPercent_uk).grid(row=18,column=4,sticky=E)





###EUB显示部分
        self.ChinaShippingFee = StringVar() #该行为FBA费
        label_ChinaShippingFee_a = Label(window,textvariable = self.ChinaShippingFee).grid(row=6,column=3,sticky=E)
        self.EubShippingFee = StringVar()
        label_EubShippingFee_a = Label(window,textvariable = self.EubShippingFee).grid(row=7,column=3,sticky=E)
        self.CommissionFee = StringVar()
        label_CommissionFee_a = Label(window,textvariable = self.CommissionFee).grid(row=8,column=3,sticky=E)
        self.PackageCost = StringVar()
        label_PackageCost_a = Label(window,textvariable = self.PackageCost).grid(row=9,column=3,sticky=E)
        self.GrossProfit = StringVar()
        label_GrossProfit_a = Label(window,textvariable = self.GrossProfit).grid(row=10,column=3,sticky=E)
        self.ToTalCost_US = StringVar()
        label30 = Label(window,textvariable = self.ToTalCost_US).grid(row=5,column=3,sticky=E)
        self.NowProfit_US = StringVar()
        label31 = Label(window,textvariable = self.NowProfit_US).grid(row=11,column=3,sticky=E)
        self.ZeroPercent_US = StringVar()
        label32 = Label(window,textvariable = self.ZeroPercent_US).grid(row=12,column=3,sticky=E)
        self.FivePercent_US = StringVar()
        label33 = Label(window,textvariable = self.FivePercent_US).grid(row=13,column=3,sticky=E)
        self.TenPercent_US = StringVar()
        label34 = Label(window,textvariable = self.TenPercent_US).grid(row=14,column=3,sticky=E)
        self.FifteenPercent_US = StringVar()
        label35 = Label(window,textvariable = self.FifteenPercent_US).grid(row=15,column=3,sticky=E)
        self.TwentyPercent_US = StringVar()
        label36 = Label(window,textvariable = self.TwentyPercent_US).grid(row=16,column=3,sticky=E)
        self.TwentyFivePercent_US = StringVar()
        label37 = Label(window,textvariable = self.TwentyFivePercent_US).grid(row=17,column=3,sticky=E)
        self.ThirtyPercent_US = StringVar()
        label38 = Label(window,textvariable = self.ThirtyPercent_US).grid(row=18,column=3,sticky=E)


####################################################下拉菜单################################
###########选择fba_US重量段######1组#######
        self.v1 = StringVar()
        self.v1.set('美国FBA重量')   #默认值
        FBA_US_W = OptionMenu(window,self.v1,'0～1lb','1～2lb','Over 2lb').grid(row=19,sticky=W)
        #使用方法：OptionMenu(容器,variable,value)
#########选则fba_US尺寸Large or Small Std Size########2组########
        self.v2 = StringVar()
        self.v2.set('美国FBA尺寸')
        s = OptionMenu(window,self.v2,'38.1x30.48x1.9cm','45.72x35.56x20.32cm').grid(row=20,sticky=W)

#########选则fba_UK尺寸########3组########
        self.v3 = StringVar()
        self.v3.set('英国FBA尺寸')
        FBA_UK_S = OptionMenu(window,self.v3,'≤20x15x1cm','≤33x23x2.5cm','≤33x23x5cm','≤45x34x26cm').grid(row=21,sticky=W)


###############美国FBA头程计费选择#############6.9号新增
        self.v4 = StringVar()
        self.v4.set("出口易FBA专线(US)")
        FBA_US_FirstClass = OptionMenu(window,self.v4,"10~21kg","21~30kg","31~60kg").grid(row=22,sticky=W)



#################按钮部分############
        btExit = Button(window,text="退出程序",command = window.quit).grid(row=21,column=4,sticky=E)
        btCompute = Button(window,text = "开始计算",command = self.ComputeSalePrice).grid(row=20,column=4,sticky=E)

        window.mainloop()
####运费逻辑运算
    def ComputeSalePrice(self):
        try:
            #计算FBA
            TotalShippingCost = self.computeshippingcost(
                float(self.PurchasePrice.get()),  #采购价
                float(self.ShippingWeight.get())*self.FBA_US_FirstRate(),  #头程
                self.selectLevel()*settings.fee_rate['exchangeRate'],  #根据重量尺寸选择FBA的费用
                float(settings.fee_rate['packageCost']), #包装费
                self.commission_cost()   #平台费
                      )
            #平台费单独计算（6.6的时候平台费低消1刀）
            Commission_Fee =self.commission_cost()


            #视图获取相应的计算值
            self.Exchange_to_RMB.set('￥'+str(self.SalePrice.get()*settings.fee_rate['exchangeRate']))  #将售价换成RMB
            FixCost = self.fixed_costs(TotalShippingCost,self.commission_cost())
            self.First_Class_US.set(format(self.ShippingWeight.get()*self.FBA_US_FirstRate(),'.2f'))
            self.PackageCost_FBA_US.set(settings.fee_rate['packageCost'])
            self.FBA_US_Cost.set('$'+format(self.selectLevel(),'.2f'))
            self.CommissionFee_fba.set(format(Commission_Fee,'.2f'))
            self.GrossProfit_fba.set(format(self.SalePrice.get()*settings.fee_rate['exchangeRate'] - TotalShippingCost,'.2f'))
            self.ZeroPercent.set('$'+format(FixCost/settings.fee_rate['exchangeRate']/0.85,'.2f'))
            self.FivePercent.set('$'+format(FixCost/settings.fee_rate['exchangeRate']/0.80,'.2f'))
            self.TenPercent.set('$'+format(FixCost/settings.fee_rate['exchangeRate']/0.75,'.2f'))
            self.FifteenPercent.set('$'+format(FixCost/settings.fee_rate['exchangeRate']/70,'.2f'))
            self.TwentyPercent.set('$'+format(FixCost/settings.fee_rate['exchangeRate']/0.65,'.2f'))
            self.TwentyFivePercent.set('$'+format(FixCost/settings.fee_rate['exchangeRate']/0.60,'.2f'))
            self.ThirtyPercent.set('$'+format(FixCost/settings.fee_rate['exchangeRate']/0.55,'.2f'))
            self.ToTalCost.set(format(TotalShippingCost,'.2f'))
            self.NowProfit.set('{:.2f} %'.format((self.SalePrice.get()*settings.fee_rate['exchangeRate'] - TotalShippingCost)/(self.SalePrice.get()*settings.fee_rate['exchangeRate'])*100))

            #计算FBA_UK
            TotalShippingCost_FBA_UK = self.compute_fba_uk(
                float(self.PurchasePrice.get()),  #采购价
                float(self.ShippingWeight.get())*settings.fee_rate['firstClass_uk'],  #头程
                self.selectLevel_fba_uk()*settings.fee_rate['exchangeRate_uk'],  #根据重量尺寸选择FBA的费用,针对UK在写一个selectlevel的函数
                float(settings.fee_rate['packageCost']), #包装费
                self.commission_uk_cost()   #调用commission_uk_cost()计算UK平台费
                      )

            Commission_Fee_UK = self.commission_uk_cost() #平台费单独计算
            #UK视图
            FixCost_UK = self.fixed_costs(TotalShippingCost_FBA_UK,self.commission_uk_cost())
            self.First_Class_UK.set(format(self.ShippingWeight.get()*settings.fee_rate['firstClass_uk'],'.2f'))
            self.PackageCost_FBA_UK.set(settings.fee_rate['packageCost'])
            self.FBA_UK_Cost.set('£'+str(self.selectLevel_fba_uk()))
            self.CommissionFee_fba_uk.set(format(Commission_Fee_UK,'.2f'))
            self.GrossProfit_fba_uk.set(format(self.SalePrice.get()*settings.fee_rate['exchangeRate_uk'] - TotalShippingCost_FBA_UK,'.2f'))
            self.ZeroPercent_uk.set('£'+format(FixCost_UK/settings.fee_rate['exchangeRate_uk']/0.88,'.2f'))
            self.FivePercent_uk.set('£'+format(FixCost_UK/settings.fee_rate['exchangeRate_uk']/0.83,'.2f'))
            self.TenPercent_uk.set('£'+format(FixCost_UK/settings.fee_rate['exchangeRate_uk']/0.78,'.2f'))
            self.FifteenPercent_uk.set('£'+format(FixCost_UK/settings.fee_rate['exchangeRate_uk']/0.73,'.2f'))
            self.TwentyPercent_uk.set('£'+format(FixCost_UK/settings.fee_rate['exchangeRate_uk']/0.68,'.2f'))
            self.TwentyFivePercent_uk.set('£'+format(FixCost_UK/settings.fee_rate['exchangeRate_uk']/0.63,'.2f'))
            self.ThirtyPercent_uk.set('£'+format(FixCost_UK/settings.fee_rate['exchangeRate_uk']/0.58,'.2f'))
            self.ToTalCost_uk.set(format(TotalShippingCost_FBA_UK,'.2f'))
            self.NowProfit_uk.set('{:.2f} %'.format((self.SalePrice.get()*settings.fee_rate['exchangeRate_uk'] - TotalShippingCost_FBA_UK)/(self.SalePrice.get()*settings.fee_rate['exchangeRate_uk'])*100))


            #计算EUB费用
            TotalShippingCost_EUB = self.compute_eub(
                float(self.PurchasePrice.get()),
                float(self.compute_eub_shipping_fee()),
                float(settings.fee_rate['packageCost']),
                self.commission_cost(),
            )

            #视图获取相应的计算值
            FixCost_EUB = self.fixed_costs(TotalShippingCost_EUB,self.commission_cost())
            self.ChinaShippingFee.set(0)  #跟FBA费用一行，这里为0
            self.EubShippingFee.set(format(self.compute_eub_shipping_fee(),'.2f'))
            self.CommissionFee.set(format(Commission_Fee,'.2f'))
            self.PackageCost.set(settings.fee_rate['packageCost'])
            self.GrossProfit.set(format(self.SalePrice.get()*settings.fee_rate['exchangeRate'] - TotalShippingCost_EUB,'.2f'))
            self.ZeroPercent_US.set('$'+format(FixCost_EUB/settings.fee_rate['exchangeRate']/0.85,'.2f'))
            self.FivePercent_US.set('$'+format(FixCost_EUB/settings.fee_rate['exchangeRate']/0.80,'.2f'))
            self.TenPercent_US.set('$'+format(FixCost_EUB/settings.fee_rate['exchangeRate']/0.75,'.2f'))
            self.FifteenPercent_US.set('$'+format(FixCost_EUB/settings.fee_rate['exchangeRate']/0.70,'.2f'))
            self.TwentyPercent_US.set('$'+format(FixCost_EUB/settings.fee_rate['exchangeRate']/0.65,'.2f'))
            self.TwentyFivePercent_US.set('$'+format(FixCost_EUB/settings.fee_rate['exchangeRate']/0.60,'.2f'))
            self.ThirtyPercent_US.set('$'+format(FixCost_EUB/settings.fee_rate['exchangeRate']/0.55,'.2f'))
            self.ToTalCost_US.set(format(TotalShippingCost_EUB,'.2f'))
            self.NowProfit_US.set('{:.2f} %'.format((self.SalePrice.get()*settings.fee_rate['exchangeRate'] - TotalShippingCost_EUB)/(self.SalePrice.get()*settings.fee_rate['exchangeRate'])*100))
        except ZeroDivisionError:
            print('售价不能为0')




#计算平台费（低于6.6刀的情况）
    def commission_cost(self):
        if self.SalePrice.get()<6.6:
            return 1*settings.fee_rate['exchangeRate']
        else:
            return self.SalePrice.get()*settings.fee_rate['commissionRate']*settings.fee_rate['exchangeRate']

#计算UK平台费（低于3.4镑的情况）
    def commission_uk_cost(self):
        if self.SalePrice.get()*settings.fee_rate['exchangeRate_us_to_uk']<3.4:
            return 0.4*settings.fee_rate['exchangeRate_uk']
        else:
            return self.SalePrice.get()*settings.fee_rate['commissionRate_uk']*settings.fee_rate['exchangeRate_uk']
# 计算EUB重量低于70g的情况
    def compute_eub_shipping_fee(self):
        if self.ShippingWeight.get()<70:
            return settings.fee_rate['EUB_min_weight']*settings.fee_rate['EUB_Rate']+settings.fee_rate['EUB_HandlingCharge']
        else:
            return self.ShippingWeight.get()*settings.fee_rate['EUB_Rate']+settings.fee_rate['EUB_HandlingCharge']

#计算FBA，总成本函数
    def computeshippingcost(self,PurchasePrice,FirstClassCost,FbaFee,PackageCost,Commission):


        TotalShippingCost = PurchasePrice + FirstClassCost + FbaFee + PackageCost + Commission

        return TotalShippingCost

#计算E邮宝,总成本函数
    def compute_eub(self,PurchasePrice,FirstShoppingCost,PackageCost,Commission):

        TotalShippingCost_b = PurchasePrice+FirstShoppingCost+PackageCost+Commission

        return TotalShippingCost_b


#计算FBA_UK，总成本函数
    def compute_fba_uk(self,PurchasePrice,FirstClassCost,FbaFee,PackageCost,Commission):

        TotalShippingCost = PurchasePrice + FirstClassCost + FbaFee+ PackageCost+Commission

        return TotalShippingCost





##选择FBA重量段函数
    def selectLevel(self):
        fbaFee = 3.02
        if self.v1.get() == '0～1lb' and self.v2 == '38.1x30.48x1.9cm':   #1lb内 且尺寸为small Std Size ，= $2.56
            fbaFee = settings.fee_rate['fbaFee_s_1lb']
        elif self.v1.get() == '0～1lb' and self.v2 == '45.72x35.56x20.32cm': #1lb内 且尺寸为Large Std Size ，＝ $3.02
            fbaFee = settings.fee_rate['fbaFee_l_1lb']
        elif self.v1.get() == '1～2lb':                                 #1-2lb内，默认尺寸为Large Std Size， =$4.01
            self.v2.set('45.72x35.56x20.32cm')
            fbaFee = settings.fee_rate['fbaFee_l_2lb']
        elif self.v2.get() =='38.1x30.48x1.9cm':                       #尺寸为‘small Std Size', 重量默认为1lb
            self.v1.set('0～1lb')
            fbaFee = settings.fee_rate['fbaFee_s_1lb']
        elif self.v1.get() == 'Over 2lb':      #Std Size超2lb ： $4.01+0.39/lb（超2lb）部份
            self.v2.set('45.72x35.56x20.32cm')
            fbaFee = settings.fee_rate['fbaFee_l_2lb']+(self.ShippingWeight.get()/453-2)*settings.fee_rate['over 2lb']

        return fbaFee

#FBA_UK选择尺寸函数
    def selectLevel_fba_uk(self):
        fbaFee = 1.7
        if self.v3.get() =='≤20x15x1cm' and self.ShippingWeight.get()<=100:
            fbaFee = settings.fee_rate['SmallEnvelope_0-100']
        elif self.v3.get() == '≤33x23x2.5cm' and self.ShippingWeight.get() <=100:
            fbaFee = settings.fee_rate['StandardEnvelope_0-100']
        elif self.v3.get() =='≤33x23x2.5cm' and self.ShippingWeight.get() >100 and self.ShippingWeight.get()<=250:
            fbaFee = settings.fee_rate['StandardEnvelope_101-250']
        elif self.v3.get() =='≤33x23x2.5cm' and self.ShippingWeight.get() >251 and self.ShippingWeight.get()<=500:
            fbaFee = settings.fee_rate['StandardEnvelope_251-500']
        elif self.v3.get() =='≤33x23x5cm' and self.ShippingWeight.get() <=1000:
            fba = settings.fee_rate['LargeEnvelope_0-1000']
        elif self.v3.get() =='≤45x34x26cm' and self.ShippingWeight.get()<=250:
            fbaFee = settings.fee_rate['StandardParcel_0-250']
        elif self.v3.get() =='≤45x34x26cm' and self.ShippingWeight.get() >251 and self.ShippingWeight.get()<=500:
            fbaFee = settings.fee_rate['StandardParcel_251-500']
        elif self.v3.get() =='≤45x34x26cm' and self.ShippingWeight.get() >500 and self.ShippingWeight.get()<=1000:
            fbaFee = settings.fee_rate['StandardParcel_501-1000']
        elif self.v3.get() =='≤45x34x26cm' and self.ShippingWeight.get() >1000 and self.ShippingWeight.get() <=1500:
            fbaFee = settings.fee_rate['StandardParcel_1001-1500']
        elif self.v3.get() =='≤45x34x26cm' and self.ShippingWeight.get() >1500 and self.ShippingWeight.get()<=2000:
            fbaFee = settings.fee_rate['StandardParcel_1501-2000']
        elif self.v3.get() =='≤45x34x26cm' and self.ShippingWeight.get() >2000:
            fbaFee = settings.fee_rate['StandardParcel_2001-3000']
        return fbaFee
#除去平台费固定成本函数
    def fixed_costs(self,TotalCost,CommissionCost):
        Fixed_Costs = TotalCost - CommissionCost
        return Fixed_Costs
#FBA头程因重量不同计算函数  6.9号新增
    def FBA_US_FirstRate(self):
        f =  settings.fee_rate['firstClass_a'] #默认36元一公斤
        if self.v4.get() == "10~21kg":
            firstClass = settings.fee_rate['firstClass_a']
        elif self.v4.get() =="21~30kg":
            firstClass = settings.fee_rate['firstClass_b']
        elif self.v4.get() =="31~60kg":
            firstClass = settings.fee_rate['firstClass_c']
        else:
            firstClass = f #默认36元一公斤
        return firstClass




LoadCalculator()