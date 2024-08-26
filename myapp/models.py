from django.db import models
    
class UserTable(models.Model):
    sl_num = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=100)
    email = models.EmailField(blank=False, null=False)
    location = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    role=models.CharField(max_length=100)
    username=models.CharField(max_length=100,db_collation='utf8_bin')
    password=models.CharField(max_length=100,db_collation='utf8_bin')

    def __str__(self):
        return self.name

class Department(models.Model):
    sl_num = models.CharField(max_length=100)
    department=models.CharField(max_length=100) 
    location=models.CharField(max_length=100) 
    status=models.CharField(max_length=100) 
   
    def __str__(self):
        return self.department
    
class Employee(models.Model):
    sl_num = models.CharField(max_length=100)
    employee_name=models.CharField(max_length=100)
    phone_no=models.CharField(max_length=100)
    email = models.EmailField(blank=False, null=False)
    location=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    status=models.CharField(max_length=100)



class AssetTable(models.Model):
    sl_num = models.CharField(max_length=100)
    Asset_name = models.CharField(max_length=100)
    Asset_type = models.CharField(max_length=100)
    Status = models.CharField(max_length=100)
    Item_code= models.CharField(max_length=255,unique=True)
    images=models.ImageField(upload_to='assets/images/',blank=True,null=True)
    Serial_number=models.CharField(max_length=100)
    Model_number=models.CharField(max_length=100)
    Machine_OS_configuration=models.CharField(max_length=100)
    Movable_nonmovable=models.CharField(max_length=100)
    Vender_Supplier=models.CharField(max_length=100)
    Maintenance=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    Year_of_purchasing=models.DateField()
    Year_of_expiry=models.DateField()
    Age_life=models.CharField(max_length=100)
    Supporting_docs=models.FileField(upload_to=None, max_length=254,blank=True,null=True)
    Notes=models.TextField(max_length=100)

    def __str__(self):
        return self.Asset_name    
    
class Assign(models.Model):
    sl_num = models.CharField(max_length=100)
    asset_id = models.ForeignKey(AssetTable, on_delete=models.CASCADE)
    assigned_to = models.CharField(max_length=100,null=True, blank=True)  # Adjust field type as needed
    assigned_by = models.CharField(max_length=100, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    remarks = models.TextField(null=True,blank=True)       
    
class Category(models.Model):
    sl_num = models.CharField(max_length=100)
    Category_type=models.CharField(max_length=100)
    Status=models.CharField(max_length=100)

    def __str__(self):
        return self.Category_type    
    

class LocTable(models.Model):
   sl_num=models.CharField(max_length=100)
   location = models.CharField(max_length=100)
   loc_status=models.CharField(max_length=50,default='Active')    

class adminprivileges(models.Model):
    assetview = models.BooleanField(default=False)
    assetedit = models.BooleanField(default=False)
    assetdelete = models.BooleanField(default=False)
    assetadd = models.BooleanField(default=False)
    userview = models.BooleanField(default=False)
    useredit = models.BooleanField(default=False)
    userdelete = models.BooleanField(default=False)
    useradd = models.BooleanField(default=False)
    employeeview = models.BooleanField(default=False)
    employeeedit = models.BooleanField(default=False)
    employeedelete = models.BooleanField(default=False)
    employeeadd = models.BooleanField(default=False)
    locationview = models.BooleanField(default=False)
    locationedit = models.BooleanField(default=False)
    locationdelete = models.BooleanField(default=False)
    locationadd = models.BooleanField(default=False)
    departmentview = models.BooleanField(default=False)
    departmentedit = models.BooleanField(default=False)
    departmentdelete = models.BooleanField(default=False)
    departmentadd = models.BooleanField(default=False)
    categoryview = models.BooleanField(default=False)
    categoryedit = models.BooleanField(default=False)
    categorydelete = models.BooleanField(default=False)
    categoryadd = models.BooleanField(default=False)
    rolesview = models.BooleanField(default=False)
    rolesedit = models.BooleanField(default=False)
    privilegeedit = models.BooleanField(default=False)
    reportdownload = models.BooleanField(default=False)
    reportview = models.BooleanField(default=False)

class cisoprivileges(models.Model):
    assetview = models.BooleanField(default=False)
    assetedit = models.BooleanField(default=False)
    assetdelete = models.BooleanField(default=False)
    assetadd = models.BooleanField(default=False)
    userview = models.BooleanField(default=False)
    useredit = models.BooleanField(default=False)
    userdelete = models.BooleanField(default=False)
    useradd = models.BooleanField(default=False)
    employeeview = models.BooleanField(default=False)
    employeeedit = models.BooleanField(default=False)
    employeedelete = models.BooleanField(default=False)
    employeeadd = models.BooleanField(default=False)
    locationview = models.BooleanField(default=False)
    locationedit = models.BooleanField(default=False)
    locationdelete = models.BooleanField(default=False)
    locationadd = models.BooleanField(default=False)
    departmentview = models.BooleanField(default=False)
    departmentedit = models.BooleanField(default=False)
    departmentdelete = models.BooleanField(default=False)
    departmentadd = models.BooleanField(default=False)
    categoryview = models.BooleanField(default=False)
    categoryedit = models.BooleanField(default=False)
    categorydelete = models.BooleanField(default=False)
    categoryadd = models.BooleanField(default=False)
    rolesview = models.BooleanField(default=False)
    rolesedit = models.BooleanField(default=False)
    privilegeedit = models.BooleanField(default=False)
    reportdownload = models.BooleanField(default=False)
    reportview = models.BooleanField(default=False)    

class fnprivileges(models.Model):
    assetview = models.BooleanField(default=False)
    assetedit = models.BooleanField(default=False)
    assetdelete = models.BooleanField(default=False)
    assetadd = models.BooleanField(default=False)
    userview = models.BooleanField(default=False)
    useredit = models.BooleanField(default=False)
    userdelete = models.BooleanField(default=False)
    useradd = models.BooleanField(default=False)
    employeeview = models.BooleanField(default=False)
    employeeedit = models.BooleanField(default=False)
    employeedelete = models.BooleanField(default=False)
    employeeadd = models.BooleanField(default=False)
    locationview = models.BooleanField(default=False)
    locationedit = models.BooleanField(default=False)
    locationdelete = models.BooleanField(default=False)
    locationadd = models.BooleanField(default=False)
    departmentview = models.BooleanField(default=False)
    departmentedit = models.BooleanField(default=False)
    departmentdelete = models.BooleanField(default=False)
    departmentadd = models.BooleanField(default=False)
    categoryview = models.BooleanField(default=False)
    categoryedit = models.BooleanField(default=False)
    categorydelete = models.BooleanField(default=False)
    categoryadd = models.BooleanField(default=False)
    rolesview = models.BooleanField(default=False)
    rolesedit = models.BooleanField(default=False)
    privilegeedit = models.BooleanField(default=False)
    reportdownload = models.BooleanField(default=False)
    reportview = models.BooleanField(default=False)    

class assetownerprivileges(models.Model):
    assetview = models.BooleanField(default=False)
    assetedit = models.BooleanField(default=False)
    assetdelete = models.BooleanField(default=False)
    assetadd = models.BooleanField(default=False)
    userview = models.BooleanField(default=False)
    useredit = models.BooleanField(default=False)
    userdelete = models.BooleanField(default=False)
    useradd = models.BooleanField(default=False)
    employeeview = models.BooleanField(default=False)
    employeeedit = models.BooleanField(default=False)
    employeedelete = models.BooleanField(default=False)
    employeeadd = models.BooleanField(default=False)
    locationview = models.BooleanField(default=False)
    locationedit = models.BooleanField(default=False)
    locationdelete = models.BooleanField(default=False)
    locationadd = models.BooleanField(default=False)
    departmentview = models.BooleanField(default=False)
    departmentedit = models.BooleanField(default=False)
    departmentdelete = models.BooleanField(default=False)
    departmentadd = models.BooleanField(default=False)
    categoryview = models.BooleanField(default=False)
    categoryedit = models.BooleanField(default=False)
    categorydelete = models.BooleanField(default=False)
    categoryadd = models.BooleanField(default=False)
    rolesview = models.BooleanField(default=False)
    rolesedit = models.BooleanField(default=False)
    privilegeedit = models.BooleanField(default=False)
    reportdownload = models.BooleanField(default=False)
    reportview = models.BooleanField(default=False)
    
class systemadminprivileges(models.Model):
    assetview = models.BooleanField(default=False)
    assetedit = models.BooleanField(default=False)
    assetdelete = models.BooleanField(default=False)
    assetadd = models.BooleanField(default=False)
    userview = models.BooleanField(default=False)
    useredit = models.BooleanField(default=False)
    userdelete = models.BooleanField(default=False)
    useradd = models.BooleanField(default=False)
    employeeview = models.BooleanField(default=False)
    employeeedit = models.BooleanField(default=False)
    employeedelete = models.BooleanField(default=False)
    employeeadd = models.BooleanField(default=False)
    locationview = models.BooleanField(default=False)
    locationedit = models.BooleanField(default=False)
    locationdelete = models.BooleanField(default=False)
    locationadd = models.BooleanField(default=False)
    departmentview = models.BooleanField(default=False)
    departmentedit = models.BooleanField(default=False)
    departmentdelete = models.BooleanField(default=False)
    departmentadd = models.BooleanField(default=False)
    categoryview = models.BooleanField(default=False)
    categoryedit = models.BooleanField(default=False)
    categorydelete = models.BooleanField(default=False)
    categoryadd = models.BooleanField(default=False)
    rolesview = models.BooleanField(default=False)
    rolesedit = models.BooleanField(default=False)
    privilegeedit = models.BooleanField(default=False)
    reportdownload = models.BooleanField(default=False)
    reportview = models.BooleanField(default=False) 


