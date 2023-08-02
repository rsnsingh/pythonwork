class employee:
    emp_name=' '
    emp_id=0
    dept=' '
    basic_pay=0
    hra=0
    da=0
    ma=0
    def total_salary(self,name, eid, dpt,bp):
        self.emp_name=name
        self.emp_id=eid
        self.dept=dpt
        self.basic_bay=bp
        self.hra=bp*.20
        self.da=bp*1.20
        self.ma=bp*0.05
        total=self.basic_pay+self.hra+self.da+self.ma
        print(total)
e1=employee()
e1.total_salary("Anupam",12002,"Finance",20000)

        
        
