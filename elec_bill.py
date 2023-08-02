class Electricity_bill:
    '''cust_name=' '
    bill_id=' '
    meter_no=0
    no_of_units=0
    prev_balance=0
    total_amount=0'''
    def total_bill(self,name, bid, mno,nou,pbalance):
        self.cust_name=name
        self.bill_id=bid
        self.meter_no=mno
        self.no_of_units=nou
        self.prev_balance=pbalance
        if pbalance==0:
            self.total_amount=0
        else:
            self.total_amount=pbalance+ 0.1*pbalance
        if nou<=200:
            self.total_amount=self.total_amount+nou*5
        elif nou>200 and nou<=400:
            self.total_amount+=200*5+(nou-200)*7   #  1000+700 =1700
        elif nou>400 and nou<=800:
            self.total_amount+=200*5+200*7+(nou-400)*10    # 1000+ 1400+ 3000
        elif nou>800 and nou<=1600:
            self.total_amount+=200*5+200*7+400*10+(nou-800)*13     # 1000+1400+4000+3900
        else:
             self.total_amount+=200*5+200*7+400*10+800*13+(nou-800)*15   # 1000+1400+4000+10400+ 13500
        print(self.total_amount)
e1=Electricity_bill()
e1.total_bill("Anupam",'A12002',1234,200,0)
e2=Electricity_bill()
e3=Electricity_bill()
e4=Electricity_bill()
e5=Electricity_bill()
e2.total_bill("Anupam",'A12002',1234,300,0)
e3.total_bill("Anupam",'A12002',1234,700,0)
e4.total_bill("Anupam",'A12002',1234,1100,0)
e5.total_bill("Anupam",'A12002',1234,1700,0)

        
        
