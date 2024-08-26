
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .models import UserTable,Department,Employee,AssetTable,Category,LocTable,adminprivileges,cisoprivileges,fnprivileges,systemadminprivileges,assetownerprivileges,Assign
from django.contrib.auth import logout
import csv
from django.http import HttpResponse
from .decarators import login_required_custom
from django.utils import timezone

def asset_login(request):
    if request.method == 'POST':
        username = request.POST.get('user_id')
        password = request.POST.get('password')
        try:
            user = UserTable.objects.get(username=username, password=password)
            if user:
                if user.status == 'inactive':
                    messages.error(request, 'Your account is inactive.')
                    return redirect('asset_login')
                request.session['name'] = user.name
                request.session['role'] =user.role
                if user.role == 'Admin':
                    return redirect('admin_dashboard')
                elif user.role == 'CISO':
                    return redirect('ciso_dashboard')
                elif user.role == 'Fnhead':
                    return redirect('fnhead_dashboard')
                elif user.role == 'SystemAdmin':
                    return redirect('systemadmin_dashboard')
                elif user.role == 'AssetOwner':
                    return redirect('assetowner_dashboard')
                else:
                    messages.error(request, 'Unknown user position')
                    return redirect('asset_login')  # Redirect to clear form and message
        except UserTable.DoesNotExist:
            messages.error(request, 'Invalid username or password')
            return redirect('asset_login')  # Redirect to clear form and message
    return render(request, 'asset.html')

def logout_view(request):
    logout(request)
    return redirect('asset_login')

@login_required_custom
def admin_dashboard(request):
    total_users = UserTable.objects.filter(status='active').count()
    total_assets = AssetTable.objects.count()
    total_dept=Department.objects.filter(status='active').count()
    total_emp=Employee.objects.filter(status='active').count()
    name = request.session.get('name',None)
    role = request.session.get('role', None)
    try:
        admin_privileges = adminprivileges.objects.get()
    except ObjectDoesNotExist:
        admin_privileges = None
    context = {
        'total_users': total_users,
        'total_assets': total_assets,
        'total_dept':total_dept,
        'total_emp':total_emp,
        'name':name,
        'role':role,
        'assetview': admin_privileges.assetview if admin_privileges else False,
        'userview': admin_privileges.userview if admin_privileges else False,
        'employeeview': admin_privileges.employeeview if admin_privileges else False,
        'locationview': admin_privileges.locationview if admin_privileges else False,
        'departmentview': admin_privileges.departmentview if admin_privileges else False,
        'categoryview': admin_privileges.categoryview if admin_privileges else False,
        'rolesview': admin_privileges.rolesview if admin_privileges else False,
        'reportview': admin_privileges.reportview if admin_privileges else False,
        'previlegeedit':admin_privileges.privilegeedit if admin_privileges else False,    
     }
    return render(request, 'admin_dashboard.html', context)

@login_required_custom
def assetowner_dashboard(request):
    total_users = UserTable.objects.filter(status='active').count()
    total_assets = AssetTable.objects.count()
    total_dept=Department.objects.filter(status='active').count()
    total_emp=Employee.objects.filter(status='active').count()
    name = request.session.get('name',None)
    role = request.session.get('role', None)
    try:
        admin_privileges = assetownerprivileges.objects.get()
    except ObjectDoesNotExist:
        admin_privileges = None
    context = {
        'total_users': total_users,
        'total_assets': total_assets,
        'total_dept':total_dept,
        'total_emp':total_emp,
        'name':name,
        'role':role,
        'assetview': admin_privileges.assetview if admin_privileges else False,
        'userview': admin_privileges.userview if admin_privileges else False,
        'employeeview': admin_privileges.employeeview if admin_privileges else False,
        'locationview': admin_privileges.locationview if admin_privileges else False,
        'departmentview': admin_privileges.departmentview if admin_privileges else False,
        'categoryview': admin_privileges.categoryview if admin_privileges else False,
        'rolesview': admin_privileges.rolesview if admin_privileges else False,
        'reportview': admin_privileges.reportview if admin_privileges else False,
        'previlegeedit':admin_privileges.privilegeedit if admin_privileges else False,   
    }
    return render(request, 'assetowner_dashboard.html', context)

@login_required_custom
def ciso_dashboard(request):
    total_users = UserTable.objects.filter(status='active').count()
    total_assets = AssetTable.objects.count()
    total_dept=Department.objects.filter(status='active').count()
    total_emp=Employee.objects.filter(status='active').count()
    name = request.session.get('name',None)
    role = request.session.get('role', None)
    try:
        admin_privileges = cisoprivileges.objects.get()
    except ObjectDoesNotExist:
        admin_privileges = None
    context = {
        'total_users': total_users,
        'total_assets': total_assets,
        'total_dept':total_dept,
        'total_emp':total_emp,
        'name':name,
        'role':role,
        'assetview': admin_privileges.assetview if admin_privileges else False,
        'userview': admin_privileges.userview if admin_privileges else False,
        'employeeview': admin_privileges.employeeview if admin_privileges else False,
        'locationview': admin_privileges.locationview if admin_privileges else False,
        'departmentview': admin_privileges.departmentview if admin_privileges else False,
        'categoryview': admin_privileges.categoryview if admin_privileges else False,
        'rolesview': admin_privileges.rolesview if admin_privileges else False,
        'reportview': admin_privileges.reportview if admin_privileges else False,
        'previlegeedit':admin_privileges.privilegeedit if admin_privileges else False,  
    }
    return render(request, 'ciso_dashboard.html', context)

@login_required_custom
def fnhead_dashboard(request):
    total_users = UserTable.objects.filter(status='active').count()
    total_assets = AssetTable.objects.count()
    total_dept=Department.objects.filter(status='active').count()
    total_emp=Employee.objects.filter(status='active').count()
    name = request.session.get('name',None)
    role = request.session.get('role', None)
    try:
        admin_privileges = fnprivileges.objects.get()
    except ObjectDoesNotExist:
        admin_privileges = None
    context = {
        'total_users': total_users,
        'total_assets': total_assets,
        'total_dept':total_dept,
        'total_emp':total_emp,
        'name':name,
        'role':role,
        'assetview': admin_privileges.assetview if admin_privileges else False,
        'userview': admin_privileges.userview if admin_privileges else False,
        'employeeview': admin_privileges.employeeview if admin_privileges else False,
        'locationview': admin_privileges.locationview if admin_privileges else False,
        'departmentview': admin_privileges.departmentview if admin_privileges else False,
        'categoryview': admin_privileges.categoryview if admin_privileges else False,
        'rolesview': admin_privileges.rolesview if admin_privileges else False,
        'reportview': admin_privileges.reportview if admin_privileges else False,
        'previlegeedit':admin_privileges.privilegeedit if admin_privileges else False,
        
    }
    return render(request, 'fnhead_dashboard.html', context)

@login_required_custom
def systemadmin_dashboard(request):
    total_users = UserTable.objects.filter(status='active').count()
    total_assets = AssetTable.objects.count()
    total_dept=Department.objects.filter(status='active').count()
    total_emp=Employee.objects.filter(status='active').count()
    name = request.session.get('name',None)
    role = request.session.get('role', None)
    try:
        admin_privileges = systemadminprivileges.objects.get()
    except ObjectDoesNotExist:
        admin_privileges = None
    context = {
        'total_users': total_users,
        'total_assets': total_assets,
        'total_dept':total_dept,
        'total_emp':total_emp,
        'name':name,
        'role':role,
        'assetview': admin_privileges.assetview if admin_privileges else False,
        'userview': admin_privileges.userview if admin_privileges else False,
        'employeeview': admin_privileges.employeeview if admin_privileges else False,
        'locationview': admin_privileges.locationview if admin_privileges else False,
        'departmentview': admin_privileges.departmentview if admin_privileges else False,
        'categoryview': admin_privileges.categoryview if admin_privileges else False,
        'rolesview': admin_privileges.rolesview if admin_privileges else False,
        'reportview': admin_privileges.reportview if admin_privileges else False,
        'previlegeedit':admin_privileges.privilegeedit if admin_privileges else False,   
    }
    return render(request, 'systemadmin_dashboard.html', context)

@login_required_custom
def category_list(request):
    categories = Category.objects.all()
    name = request.session.get('name', None)
    role = request.session.get('role', None)
    show_add_button = False
    show_edit_icon=False
    show_delete_icon=False
    if role == 'Admin':
        privileges = adminprivileges.objects.first()
        show_add_button = privileges.categoryadd
        show_edit_icon=privileges.categoryedit
        show_delete_icon=privileges.categorydelete
    elif role == 'CISO':
        privileges = cisoprivileges.objects.first()
        show_add_button = privileges.categoryadd
        show_edit_icon=privileges.categoryedit
        show_delete_icon=privileges.categorydelete
    elif role == 'Fnhead':
        privileges = fnprivileges.objects.first()
        show_add_button = privileges.categoryadd
        show_edit_icon=privileges.categoryedit
        show_delete_icon=privileges.categorydelete
    elif role == 'AssetOwner':
        privileges = assetownerprivileges.objects.first()
        show_add_button = privileges.categoryadd
        show_edit_icon=privileges.categoryedit
        show_delete_icon=privileges.categorydelete    
    elif role == 'SystemAdmin':
        privileges =systemadminprivileges.objects.first()
        show_add_button = privileges.categoryadd
        show_edit_icon=privileges.categoryedit  
        show_delete_icon=privileges.categorydelete      
    else:
        show_add_button = False 
        show_edit_icon=False
        show_delete_icon=False 
    context = {
        'categories':categories,
        'name' : name, 
        'role': role,
        'show_add_button': show_add_button,
        'show_edit_icon':show_edit_icon,
        'show_delete_icon':show_delete_icon,
        'assetview': privileges.assetview if privileges else False,
        'userview': privileges.userview if privileges else False,
        'employeeview': privileges.employeeview if privileges else False,
        'locationview': privileges.locationview if privileges else False,
        'departmentview': privileges.departmentview if privileges else False,
        'categoryview': privileges.categoryview if privileges else False,
        'rolesview': privileges.rolesview if privileges else False,
        'reportview': privileges.reportview if privileges else False,
        'previlegeedit':privileges.privilegeedit if privileges else False,
    }
    return render(request, 'category.html',context)

@login_required_custom
def save_category(request):
    if request.method == 'POST':
        category_type = request.POST.get('type')
        status = request.POST.get('status')
        if category_type and status:
            new_category = Category(
                Category_type=category_type,
                Status=status
            )
            new_category.save()
            categories = Category.objects.all().order_by('id')
            for index, categ in enumerate(categories,start=1):
                Category.objects.filter(pk=categ.pk).update(sl_num = index)
        return redirect('category_list')
    return render(request, 'category.html')

@login_required_custom
def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        category.delete()
        categories = Category.objects.all().order_by('id')
        for index, categ in enumerate(categories,start=1):
         Category.objects.filter(pk=categ.pk).update(sl_num = index)
        return redirect('category_list')
    else:
        return render(request, 'error.html', {'error_message': 'Invalid request method.'})

@login_required_custom
def edit_category(request,category_id):
    if request.method == 'POST':   
        category = get_object_or_404(Category, pk=category_id)
        category.Category_type = request.POST.get('type')
        category.Status = request.POST.get('status')
        category.save()
        messages.success(request, 'Category updated successfully.')
        return redirect('category_list')   
    return redirect('category_list')

@login_required_custom
def user_list(request):
    users=UserTable.objects.all()
      # Filter departments and locations based on status
    departments = Department.objects.filter(status='active')
    locations = LocTable.objects.filter( loc_status='active')
    
    name = request.session.get('name', None)
    role = request.session.get('role', None)
    show_add_button = False
    show_edit_icon=False
    show_delete_icon=False
    if role == 'Admin':
        privileges = adminprivileges.objects.first()
        show_add_button = privileges.useradd
        show_edit_icon=privileges.useredit
        show_delete_icon=privileges.userdelete
    elif role == 'CISO':
        privileges = cisoprivileges.objects.first()
        show_add_button = privileges.useradd
        show_edit_icon=privileges.useredit
        show_delete_icon=privileges.userdelete
    elif role == 'Fnhead':
        privileges = fnprivileges.objects.first()
        show_add_button = privileges.useradd
        show_edit_icon=privileges.useredit
        show_delete_icon=privileges.userdelete
    elif role == 'AssetOwner':
        privileges = assetownerprivileges.objects.first()
        show_add_button = privileges.useradd
        show_edit_icon=privileges.useredit
        show_delete_icon=privileges.userdelete   
    elif role == 'SystemAdmin':
        privileges = systemadminprivileges.objects.first()
        show_add_button = privileges.useradd
        show_edit_icon=privileges.useredit
        show_delete_icon=privileges.userdelete     
    else:
        show_add_button = False 
        show_edit_icon=False
        show_delete_icon=False
    context = { 
        'name': name,
        'locations':locations,
        'users':users,
        'departments':departments,
        'role':role,
        'show_add_button':show_add_button,
        'show_edit_icon':show_edit_icon,
        'show_delete_icon':show_delete_icon,
        'assetview': privileges.assetview if privileges else False,
        'userview': privileges.userview if privileges else False,
        'employeeview': privileges.employeeview if privileges else False,
        'locationview': privileges.locationview if privileges else False,
        'departmentview': privileges.departmentview if privileges else False,
        'categoryview': privileges.categoryview if privileges else False,
        'rolesview': privileges.rolesview if privileges else False,
        'reportview': privileges.reportview if privileges else False,
        'previlegeedit':privileges.privilegeedit if privileges else False,    
    }
    return render(request,'user.html',context)

@login_required_custom
def save_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_no = request.POST.get('phone_no')
        email = request.POST.get('email') 
        location = request.POST.get('location')
        department = request.POST.get('department')
        status = request.POST.get('status')
        role = request.POST.get('role')
        username = request.POST.get('username')
        password = request.POST.get('password')
        new_user = UserTable(
            name=name,
            phone_no=phone_no,
            email=email,
            location=location,
            department=department,
            status=status,
            role=role,
            username=username,
            password=password
        )
        new_user.save()
        users = UserTable.objects.all().order_by('id')
        for index, use in enumerate (users,start=1):
            UserTable.objects.filter(pk=use.pk).update(sl_num= index)
        return redirect('user_list')  
    return render(request, 'user.html') 

@login_required_custom
def edit_user(request,user_id):
    if request.method == 'POST':
        user_id = request.POST.get('id')
        user = get_object_or_404(UserTable, pk=user_id)
        user.name = request.POST.get('name')
        user.phone_no = request.POST.get('phone_no')
        user.email = request.POST.get('email')
        user.location = request.POST.get('location')
        user.department = request.POST.get('department')
        user.status = request.POST.get('status')
        user.role = request.POST.get('role')
        user.username = request.POST.get('username')
        user.password = request.POST.get('password')
        user.save()
        messages.success(request, 'User updated successfully.')
        return redirect('user_list')  # Redirect to user list page
    else:
        return redirect('user_list')  # Redirect if not a POST request    

@login_required_custom
def delete_user(request, user_id):
    user = get_object_or_404(UserTable, id=user_id)
    if request.method == 'POST': 
        user.delete()
        users = UserTable.objects.all().order_by('id')
        for index, use in enumerate (users,start=1):
            UserTable.objects.filter(pk=use.pk).update(sl_num= index)
        return redirect('user_list')  
    return redirect('user_list')

@login_required_custom
def department_list(request):
    departments = Department.objects.all()
    locations = LocTable.objects.filter( loc_status='active')
    name = request.session.get('name', None)
    role = request.session.get('role', None)
    show_add_button = False
    show_edit_icon=False
    show_delete_icon=False
    if role == 'Admin':
        privileges = adminprivileges.objects.first()
        show_add_button = privileges.departmentadd
        show_edit_icon=privileges.departmentedit
        show_delete_icon=privileges.departmentdelete
    elif role == 'CISO':
        privileges = cisoprivileges.objects.first()
        show_add_button = privileges.departmentadd
        show_edit_icon=privileges.departmentedit
        show_delete_icon=privileges.departmentdelete
    elif role == 'Fnhead':
        privileges = fnprivileges.objects.first()
        show_add_button = privileges.departmentadd
        show_edit_icon=privileges.departmentedit
        show_delete_icon=privileges.departmentdelete
    elif role == 'AssetOwner':
        privileges = assetownerprivileges.objects.first()
        show_add_button = privileges.departmentadd
        show_edit_icon=privileges.departmentedit
        show_delete_icon=privileges.departmentdelete   
    elif role == 'SystemAdmin':
        privileges = systemadminprivileges.objects.first()
        show_add_button = privileges.departmentadd
        show_edit_icon=privileges.departmentedit
        show_delete_icon=privileges.departmentdelete      
    else:
        show_add_button = False 
        show_edit_icon=False
        show_delete_icon=False
    context = { 
        'name': name,
        'departments': departments,
        'locations':locations,
        'role':role,
        'show_add_button':show_add_button,
        'show_edit_icon':show_edit_icon,
        'show_delete_icon':show_delete_icon, 
        'assetview': privileges.assetview if privileges else False,
        'userview': privileges.userview if privileges else False,
        'employeeview': privileges.employeeview if privileges else False,
        'locationview': privileges.locationview if privileges else False,
        'departmentview': privileges.departmentview if privileges else False,
        'categoryview': privileges.categoryview if privileges else False,
        'rolesview': privileges.rolesview if privileges else False,
        'reportview': privileges.reportview if privileges else False,
        'previlegeedit':privileges.privilegeedit if privileges else False,
    }
    return render(request, 'department_list.html',context)

@login_required_custom
def edit_department(request,department_id):
    if request.method == 'POST':
        department_id = request.POST.get('id')
        department = get_object_or_404(Department, id=department_id)
        department.department = request.POST.get('department')
        department.location = request.POST.get('location')
        department.status = request.POST.get('status')
        department.save()
        messages.success(request, 'Department updated successfully.')
        return redirect('department') 
    else:
        return redirect('department') 

@login_required_custom
def delete_department(request, department_id):
    department = get_object_or_404(Department, pk=department_id)
    
    if request.method == 'POST':
        department.delete()       
        departments = Department.objects.all().order_by('id')
        for index, dept in enumerate(departments, start=1):
            Department.objects.filter(pk=dept.pk).update(sl_num=index)
        messages.success(request, 'Department deleted successfully.')
        return redirect('department')  # Replace 'department_list' with your actual URL name
    return redirect('department')  # Redirect to a relevant page

@login_required_custom
def add_department(request):
    if request.method == 'POST':
        department_name = request.POST.get('department')
        location = request.POST.get('location')
        status = request.POST.get('status')  
        new_department = Department(
            department=department_name,
            location=location,
            status=status
        )
        new_department.save()
        departments = Department.objects.all().order_by('id')
        for index, dept in enumerate(departments, start=1):
            Department.objects.filter(pk=dept.pk).update(sl_num=index)
        return redirect('department')
    return render(request, 'department_list.html')

@login_required_custom
def reports_view(request):
    name = request.session.get('name', None)
    role = request.session.get('role', None)
    show_report_button=False
    if role == 'Admin':
        privileges = adminprivileges.objects.first()
        show_report_button = privileges.reportdownload   
    elif role == 'CISO':
        privileges = cisoprivileges.objects.first()
        show_report_button = privileges.reportdownload   
    elif role == 'Fnhead':
        privileges = fnprivileges.objects.first()
        show_report_button = privileges.reportdownload   
    elif role == 'AssetOwner':
        privileges = assetownerprivileges.objects.first()
        show_report_button = privileges.reportdownload       
    elif role == 'SystemAdmin':
        privileges =systemadminprivileges.objects.first()
        show_report_button = privileges.reportdownload
    else:
        privileges =systemadminprivileges.objects.first()
        show_report_button =False
    context = {'name':name,
               'role':role,
               'show_report_button':show_report_button,
                'assetview': privileges.assetview if privileges else False,
                'userview': privileges.userview if privileges else False,
                'employeeview': privileges.employeeview if privileges else False,
                'locationview': privileges.locationview if privileges else False,
                'departmentview': privileges.departmentview if privileges else False,
                'categoryview': privileges.categoryview if privileges else False,
                'rolesview': privileges.rolesview if privileges else False,
                'reportview': privileges.reportview if privileges else False,
                'previlegeedit':privileges.privilegeedit if privileges else False,
                }
    tables = ['AssetTable', 'Department', 'Category', 'Employee']
    context['tables'] = tables
    if request.method == 'POST':
        selected_table = request.POST.get('table')
        print(f"Selected table: {selected_table}")  # Debug print
        if selected_table == 'AssetTable':
            context['data'] = AssetTable.objects.all()
            context['selected_table'] = 'AssetTable'
        elif selected_table == 'Department':
            context['data'] = Department.objects.all()
            context['selected_table'] = 'Department'
        elif selected_table == 'Category':
            context['data'] = Category.objects.all()
            context['selected_table'] = 'Category'
        elif selected_table == 'Employee':
            context['data'] = Employee.objects.all()
            context['selected_table'] = 'Employee'
        print(f"Context data: {context['data']}") 
        for item in context['data']:
            if selected_table == 'AssetTable':
                print(item.Status)  
            elif selected_table == 'Department':
                print(item.status)  
            elif selected_table == 'Category':
                print(item.Status)  
            elif selected_table == 'Employee':
                print(item.status)  
        if 'export' in request.POST:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="{selected_table}.csv"'
            writer = csv.writer(response)
            if selected_table == 'AssetTable':
                writer.writerow(['sl_num', 'Asset_name', 'Asset_type', 'Status', 'Item_code', 'Assigned_To', 'Serial_number',
                                 'Model_number', 'Machine_OS_configuration', 'Movable_nonmovable', 'Vender_Supplier', 'Maintenance',
                                 'price', 'Year_of_purchasing', 'Year_of_expiry', 'Age_life'])
                for asset in context['data']:
                    writer.writerow([asset.sl_num, asset.Asset_name, asset.Asset_type, asset.Status, asset.Item_code,
                                     asset.Assigned_To, asset.Serial_number, asset.Model_number, asset.Machine_OS_configuration,
                                     asset.Movable_nonmovable, asset.Vender_Supplier, asset.Maintenance, asset.price,
                                     asset.Year_of_purchasing, asset.Year_of_expiry, asset.Age_life])
            elif selected_table == 'Department':
                writer.writerow(['Department', 'Location', 'Status'])
                for department in context['data']:
                    writer.writerow([department.department, department.location, department.status])
            elif selected_table == 'Category':
                writer.writerow(['sl_num', 'Category_type', 'Status'])
                for category in context['data']:
                    writer.writerow([category.sl_num, category.Category_type, category.Status])
            elif selected_table == 'Employee':
                writer.writerow(['sl_num','employee_name','phone_no','email','location','department','status'])
                for employee in context['data']:
                    writer.writerow([employee.sl_num, employee.employee_name, employee.phone_no, employee.email,
                                     employee.location, employee.department, employee.status])
            return response
    return render(request, 'reports.html', context)

@login_required_custom
def employee(request):
    employees = Employee.objects.all()
    departments = Department.objects.filter(status='active')
    locations = LocTable.objects.filter( loc_status='active')
    name = request.session.get('name', None)
    role = request.session.get('role', None)
    show_add_button = False
    show_edit_icon=False
    show_delete_icon=False
    if role == 'Admin':
        privileges = adminprivileges.objects.first()
        show_add_button = privileges.employeeadd
        show_edit_icon=privileges.employeeedit
        show_delete_icon=privileges.employeedelete
    elif role == 'CISO':
        privileges = cisoprivileges.objects.first()
        show_add_button = privileges.employeeadd
        show_edit_icon=privileges.employeeedit
        show_delete_icon=privileges.employeedelete
    elif role == 'Fnhead':
        privileges = fnprivileges.objects.first()
        show_add_button = privileges.employeeadd
        show_edit_icon=privileges.employeeedit
        show_delete_icon=privileges.employeedelete
    elif role == 'AssetOwner':
        privileges = assetownerprivileges.objects.first()
        show_add_button = privileges.employeeadd
        show_edit_icon=privileges.employeeedit
        show_delete_icon=privileges.employeedelete  
    elif role == 'SystemAdmin':
        privileges = adminprivileges.objects.first()
        show_add_button = privileges.employeeadd
        show_edit_icon=privileges.employeeedit
        show_delete_icon=privileges.employeedelete    
    else:
        show_add_button = False 
        show_edit_icon=False
        show_delete_icon=False
    context = { 
        'name': name,
        'employees': employees,
        'locations':locations,
        'departments':departments,
        'role':role,
        'show_add_button':show_add_button,
        'show_edit_icon':show_edit_icon,
        'show_delete_icon':show_delete_icon,
        'assetview': privileges.assetview if privileges else False,
        'userview': privileges.userview if privileges else False,
        'employeeview': privileges.employeeview if privileges else False,
        'locationview': privileges.locationview if privileges else False,
        'departmentview': privileges.departmentview if privileges else False,
        'categoryview': privileges.categoryview if privileges else False,
        'rolesview': privileges.rolesview if privileges else False,
        'reportview': privileges.reportview if privileges else False,
        'previlegeedit':privileges.privilegeedit if privileges else False,

    }
    return render(request, 'employee.html',context)

@login_required_custom
def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    if request.method == 'POST':
        employee.delete()
        employees=Employee.objects.all().order_by('id')
        for index, emp in enumerate(employees,start=1):
            Employee.objects.filter(pk=emp.pk).update(sl_num=index)
        messages.success(request,'Employee deleted successfully.')
        return redirect('employee')  # Replace 'department_list' with your actual URL name
    return redirect('employee') 

@login_required_custom
def edit_employee(request,employee_id):
    if request.method == 'POST':
        employee_id = request.POST.get('id')
        employee = get_object_or_404(Employee, id=employee_id)
        employee.employee_name = request.POST.get('employee_name')
        employee.phone_no = request.POST.get('phone_no')
        employee.email = request.POST.get('email')
        employee.location = request.POST.get('location')
        employee.department = request.POST.get('department')
        employee.status = request.POST.get('status')
        employee.save()
        messages.success(request, 'Employee updated successfully.')
        return redirect('employee')
    else:
        return redirect('employee')  

@login_required_custom
def add_employee(request):
    if request.method == 'POST':
        employee_name = request.POST.get('employee_name')
        phone_no = request.POST.get('phone_no')
        email = request.POST.get('email')
        location = request.POST.get('location')
        department = request.POST.get('department')
        status = request.POST.get('status')
   
        new_employee = Employee(
            employee_name=employee_name,
            phone_no=phone_no,
            email=email,
            location=location,
            department=department,
            status=status
        )
        new_employee.save()
        employees=Employee.objects.all().order_by('id')
        for index, emp in enumerate(employees,start=1):
            Employee.objects.filter(pk=emp.pk).update(sl_num=index)
        messages.success(request, 'Employee added successfully.')
        return redirect('employee')  # Redirect to employee list page
    return render(request, 'employee_list.html')  # Adjust the template name as necessary

@login_required_custom
def asset_list(request):
    users = AssetTable.objects.all()
    categories = Category.objects.filter( Status='active')
    employees = Employee.objects.filter( status='active')
    name = request.session.get('name', None)
    role = request.session.get('role', None)
    show_add_button = False
    show_edit_icon=False
    show_delete_icon=False
    if role == 'Admin':
        privileges = adminprivileges.objects.first()
        show_add_button = privileges.assetadd
        show_edit_icon=privileges.assetedit
        show_delete_icon=privileges.assetdelete
    elif role == 'CISO':
        privileges = cisoprivileges.objects.first()
        show_add_button = privileges.assetadd
        show_edit_icon=privileges.assetedit
        show_delete_icon=privileges.assetdelete
    elif role == 'Fnhead':
        privileges = fnprivileges.objects.first()
        show_add_button = privileges.assetadd
        show_edit_icon=privileges.assetedit
        show_delete_icon=privileges.assetdelete
    elif role == 'AssetOwner':
        privileges = adminprivileges.objects.first()
        show_add_button = privileges.assetadd
        show_edit_icon=privileges.assetedit
        show_delete_icon=privileges.assetdelete   
    elif role == 'SystemAdmin':
        privileges = systemadminprivileges.objects.first()
        show_add_button = privileges.assetadd
        show_edit_icon=privileges.assetedit
        show_delete_icon=privileges.assetdelete    
    else:
        show_add_button = False 
        show_edit_icon=False
        show_delete_icon=False
        
    asset_histories = {}
    for user in users:
        histories = Assign.objects.filter(asset_id=user.id).values(
            'assigned_to', 'assigned_by', 'start_date', 'end_date', 'remarks'
        )
        asset_histories[user.id] = list(histories)    
    context = { 
        'name': name,
        'users': users,
        'categories':categories,
        'role':role,
        'employees' : employees,
        'show_add_button': show_add_button,
        'show_edit_icon':show_edit_icon,
        'show_delete_icon':show_delete_icon,
        'assetview': privileges.assetview if privileges else False,
        'userview': privileges.userview if privileges else False,
        'employeeview': privileges.employeeview if privileges else False,
        'locationview': privileges.locationview if privileges else False,
        'departmentview': privileges.departmentview if privileges else False,
        'categoryview': privileges.categoryview if privileges else False,
        'rolesview': privileges.rolesview if privileges else False,
        'reportview': privileges.reportview if privileges else False,
        'previlegeedit':privileges.privilegeedit if privileges else False,
        'asset_histories':asset_histories,

        }
    return render(request, 'asset_pro.html', context)

@login_required_custom
def add_asset(request):
    if request.method == 'POST':
        asset_type = request.POST.get('Asset_type')
        asset_name = request.POST.get('Asset_name')
        serial_number = request.POST.get('Serial_number')
        model_number = request.POST.get('Model_number')
        item_code = request.POST.get('Item_code') 
        
        
        # Generate a sequential Item_code if not provided
         # Generate the Item_code based on the asset_type
        prefix = 'MS' + asset_type[:3].upper()
        latest_asset = AssetTable.objects.filter(Item_code__startswith=prefix).order_by('id').last()
        if latest_asset:
            last_number = int(latest_asset.Item_code[-5:])
            new_number = last_number + 1
        else:
            new_number = 1
        item_code = f"{prefix}{new_number:05d}"
        
        machine_os_configuration = request.POST.get('Machine_OS_configuration')
        movable_nonmovable = request.POST.get('Movable_nonmovable')
        status = request.POST.get('Status')
        vender_supplier = request.POST.get('Vender_Supplier')
        maintenance = request.POST.get('Maintenance')
        price = request.POST.get('price')
        year_of_purchasing = request.POST.get('Year_of_purchasing')
        year_of_expiry = request.POST.get('Year_of_expiry')
        age_life = request.POST.get('Age_life')
        supporting_docs = request.FILES.get('Supporting_docs')
        images = request.FILES.get('images')
        notes = request.POST.get('Notes')
        asset = AssetTable(
            Asset_name=asset_name,
            Asset_type=asset_type,
            Serial_number=serial_number,
            Model_number=model_number,
            Item_code=item_code,  
            Machine_OS_configuration=machine_os_configuration,
            Movable_nonmovable=movable_nonmovable,
            Status=status,
            Vender_Supplier=vender_supplier,
            Maintenance=maintenance,
            price=price,
            Year_of_purchasing=year_of_purchasing,
            Year_of_expiry=year_of_expiry,
            Age_life=age_life,
            Supporting_docs=supporting_docs,
            images=images,
            Notes=notes
        )
        asset.save()
        assets = AssetTable.objects.all().order_by('id')
        for index, asset in enumerate(assets, start=1):
            AssetTable.objects.filter(pk=asset.pk).update(sl_num=index)
            
        return redirect('asset_list')

    return render(request, 'assets/add_asset.html')

@login_required_custom
def assign_asset(request, asset_id):
    asset = get_object_or_404(AssetTable, pk=asset_id)
    #assign = Assign.objects.all()
    #employees = Employee.objects.all()
    
    if request.method == 'POST':
        
        assigned_to_id = request.POST.get('assigned_to')
        start_date = request.POST.get('start_date')
        remarks = request.POST.get('remarks')

        assigned_by_name = request.session.get('name')
        # Handle the generation of sl_num safely
        last_entry = Assign.objects.order_by('-id').first()
        
        if last_entry and last_entry.sl_num.isdigit():
            new_sl_num = int(last_entry.sl_num) + 1
        else:
            new_sl_num = 1

          # Fetch employee name from the ID
        assigned_to_employee = get_object_or_404(Employee, pk=assigned_to_id)
        assigned_to_name = assigned_to_employee.employee_name

        assignment = Assign(sl_num=str(new_sl_num),
                            asset_id = asset,
                            assigned_to=assigned_to_name, 
                            assigned_by=assigned_by_name,
                            start_date=start_date, 
                            remarks=remarks)
        assignment.save()

        messages.success(request, 'Asset assigned successfully.')
        return redirect('asset_list')
    else:
        employees = Employee.objects.all()
        return render(request, 'assign_asset.html', {'asset': asset, 'employees': employees})



def return_asset(request, asset_id):
    # Get the assignment record for this asset
    assignment = get_object_or_404(Assign, asset_id=asset_id, end_date__isnull=True)
    
    # Update the end_date and remarks
    assignment.end_date = request.POST.get('return_date')
    assignment.remarks = request.POST.get('remarks')
    
    # Save the changes
    assignment.save()
    
    # Redirect to the appropriate page (e.g., asset list)
    return redirect('asset_list')

@login_required_custom
def delete_asset(request, user_id):
    user = get_object_or_404(AssetTable, id=user_id)
    if request.method == 'POST':
        user.delete()
        assets = AssetTable.objects.all().order_by('id')
        for index, asset in enumerate(assets, start=1):
            AssetTable.objects.filter(pk=asset.pk).update(sl_num=index)
        messages.success(request, 'Asset deleted successfully.')
        return redirect('asset_list')
    else:
        messages.error(request, 'Invalid request method.')
        return redirect('asset_list')

@login_required_custom
def view_asset(request, user_id):
    asset = get_object_or_404(AssetTable, id=user_id)
    return render(request, 'view_asset.html', {'asset': asset})

@login_required_custom
def edit_asset(request, asset_id):
    asset = get_object_or_404(AssetTable, pk=asset_id)
    if request.method == 'POST':
        asset.Asset_type = request.POST.get('Asset_type')
        asset.Asset_name = request.POST.get('Asset_name')
        asset.Serial_number = request.POST.get('Serial_number')
        asset.Model_number = request.POST.get('Model_number')
         # Only update Item_code if it is provided in the POST data
        if 'Item_code' in request.POST and request.POST.get('Item_code'):
            asset.Item_code = request.POST.get('Item_code')
        asset.Machine_OS_configuration = request.POST.get('Machine_OS_configuration')
        asset.Movable_nonmovable = request.POST.get('Movable_nonmovable')
        asset.Status = request.POST.get('Status')
        asset.Vender_Supplier = request.POST.get('Vender_Supplier')
        asset.Maintenance = request.POST.get('Maintenance')
        asset.price = request.POST.get('price')
        asset.Year_of_purchasing = request.POST.get('Year_of_purchasing')
        asset.Year_of_expiry = request.POST.get('Year_of_expiry')
        asset.Age_life = request.POST.get('Age_life')  

        if request.FILES.get('Supporting_docs'):
            asset.Supporting_docs = request.FILES.get('Supporting_docs')
        
        if request.FILES.get('images'):
            asset.images = request.FILES.get('images')
        asset.Notes = request.POST.get('Notes')

        asset.save()
        messages.success(request, 'Asset updated successfully.')
        return redirect('asset_list')
    else:
        asset.Year_of_purchasing = asset.Year_of_purchasing.strftime('%Y-%m-%d')
        asset.Year_of_expiry = asset.Year_of_expiry.strftime('%Y-%m-%d')
        return render(request, 'edit_asset.html', {'asset': asset})

@login_required_custom
def location_list(request):
    users=LocTable.objects.all()
    name = request.session.get('name', None)
    role = request.session.get('role', None)
    show_add_button = False
    show_edit_icon=False
    show_delete_icon=False
    if role == 'Admin':
        privileges = adminprivileges.objects.first()
        show_add_button = privileges.locationadd
        show_edit_icon=privileges.locationedit
        show_delete_icon=privileges.locationdelete
    elif role == 'CISO':
        privileges = cisoprivileges.objects.first()
        show_add_button = privileges.locationadd
        show_edit_icon=privileges.locationedit
        show_delete_icon=privileges.locationdelete
    elif role == 'Fnhead':
        privileges = fnprivileges.objects.first()
        show_add_button = privileges.locationadd
        show_edit_icon=privileges.locationedit
        show_delete_icon=privileges.locationdelete
    elif role == 'AssetOwner':
        privileges = assetownerprivileges.objects.first()
        show_add_button = privileges.locationadd
        show_edit_icon=privileges.locationedit
        show_delete_icon=privileges.locationdelete  
    elif role == 'SystemAdmin':
        privileges =systemadminprivileges.objects.first()
        show_add_button = privileges.locationadd
        show_edit_icon=privileges.locationedit
        show_delete_icon=privileges.locationdelete    
    else:
        show_add_button = False 
        show_edit_icon=False
        show_delete_icon=False
    context = { 
        'name': name,
        'users': users,
        'role':role,
        'show_add_button': show_add_button,
        'show_edit_icon':show_edit_icon,
        'show_delete_icon':show_delete_icon,
        'assetview': privileges.assetview if privileges else False,
        'userview': privileges.userview if privileges else False,
        'employeeview': privileges.employeeview if privileges else False,
        'locationview': privileges.locationview if privileges else False,
        'departmentview': privileges.departmentview if privileges else False,
        'categoryview': privileges.categoryview if privileges else False,
        'rolesview': privileges.rolesview if privileges else False,
        'reportview': privileges.reportview if privileges else False,
        'previlegeedit':privileges.privilegeedit if privileges else False,

    }
    return render(request,'location_pro.html',context)

@login_required_custom
def add_location(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        loc_status = request.POST.get('loc_status')
        location_loc = LocTable(
            location=location,
            loc_status=loc_status,
        )
        location_loc.save()
        locations=LocTable.objects.all().order_by('id')
        for index, loc in enumerate(locations,start=1):
            LocTable.objects.filter(pk=loc.pk).update(sl_num=index)    
        return redirect('location_list') 
    return render(request, 'location_pro.html')

@login_required_custom
def delete_loc(request, location_id):
    user = get_object_or_404(LocTable, id=location_id)
    if request.method == 'POST':
        user.delete()
        locations=LocTable.objects.all().order_by('id')
        for index, loc in enumerate(locations,start=1):
            LocTable.objects.filter(pk=loc.pk).update(sl_num=index)
        messages.success(request, 'location deleted successfully.')
        return redirect('location_list')
    else:
        messages.error(request, 'Invalid request method.')
        return redirect('location_list')

@login_required_custom
def edit_location(request,location_id):
    if request.method == 'POST':
        print(request.POST)
        location = get_object_or_404(LocTable, pk=location_id)
        location.location = request.POST.get('location')
        loc_status = request.POST.get('loc_status')
        if loc_status:
            location.loc_status = loc_status
        else:
            messages.error(request, 'Location status is required.')
            return redirect('location_list')
        location.save()
        messages.success(request, 'location updated successfully.')
        return redirect('location_list')
    return redirect('location_list')

@login_required_custom
def roles(request):
    users=UserTable.objects.all()
    name = request.session.get('name', None)
    role = request.session.get('role', None)
    show_edit_icon=False
    if role == 'Admin':
        privileges = adminprivileges.objects.first()
        show_edit_icon=privileges.rolesedit
    elif role == 'CISO':
        privileges = cisoprivileges.objects.first()
        show_edit_icon=privileges.rolesedit
    elif role == 'Fnhead':
        privileges = fnprivileges.objects.first()
        show_edit_icon=privileges.rolesedit
    elif role == 'AssetOwner':
        privileges = assetownerprivileges.objects.first()
        show_edit_icon=privileges.rolesedit  
    elif role == 'SystemAdmin':
        privileges =systemadminprivileges.objects.first()
        show_edit_icon=privileges.rolesedit     
    else:
        show_edit_icon=False
          
    context = { 
        'name': name,
        'users': users,
        'role':role,
        'show_edit_icon':show_edit_icon,
       'assetview': privileges.assetview if privileges else False,
        'userview': privileges.userview if privileges else False,
        'employeeview': privileges.employeeview if privileges else False,
        'locationview': privileges.locationview if privileges else False,
        'departmentview': privileges.departmentview if privileges else False,
        'categoryview': privileges.categoryview if privileges else False,
        'rolesview': privileges.rolesview if privileges else False,
        'reportview': privileges.reportview if privileges else False,
        'previlegeedit':privileges.privilegeedit if privileges else False,

    }
    return render(request,'roles.html',context)

@login_required_custom
def edit_roles(request,user_id):
    if request.method == 'POST':
        user_id = request.POST.get('id')
        user = get_object_or_404(UserTable, pk=user_id)
        user.name = request.POST.get('name') 
        user.status = request.POST.get('status')
        user.role = request.POST.get('role')
        user.save()
        messages.success(request, 'User updated successfully.')
        return redirect('roles')  # Redirect to user list page
    else:
        return redirect('roles')  # Redirect if not a POST request    

@login_required_custom    
def update_privileges(request,roles):
    name = request.session.get('name', None)
    role = request.session.get('role', None)
    models = {
        'Admin': adminprivileges,
        'SystemAdmin': systemadminprivileges,
        'CISO': cisoprivileges,
        'Fnhead': fnprivileges,
        'AssetOwner': assetownerprivileges,
    }
    if roles not in models:
        return redirect('privileges')  # Redirect or handle invalid role

    PrivilegesModel = models[roles]
    privileges, _ = PrivilegesModel.objects.get_or_create(id=1)
    if request.method == 'POST':
        fields = [
            'assetview', 'assetedit', 'assetdelete', 'assetadd',
            'userview', 'useredit', 'userdelete', 'useradd',
            'employeeview', 'employeeedit', 'employeedelete', 'employeeadd',
            'locationview', 'locationedit', 'locationdelete', 'locationadd',
            'departmentview', 'departmentedit', 'departmentdelete', 'departmentadd',
            'categoryview', 'categoryedit', 'categorydelete', 'categoryadd',
            'rolesview', 'rolesedit', 'privilegeedit', 'reportview','reportdownload'
        ]

        for field in fields:
            setattr(privileges, field, request.POST.get(field) == 'on')

        privileges.save()
        messages.success(request, 'Privilege updated successfully.')
        return redirect('privileges')
    context = {
        'privileges': privileges,
        'name':name,
        'role':role
    }
    return render(request, f'privilege_{roles}.html', context)

@login_required_custom
def privileges(request):
    privileges, _ = adminprivileges.objects.get_or_create(id=1)
    name = request.session.get('name', None)
    role = request.session.get('role', None)
    if role == 'Admin':
        privileges = adminprivileges.objects.first()    
    elif role == 'CISO':
        privileges = cisoprivileges.objects.first()  
    elif role == 'Fnhead':
        privileges = fnprivileges.objects.first()   
    elif role == 'AssetOwner':
        privileges = assetownerprivileges.objects.first() 
    elif role == 'SystemAdmin':
        privileges = systemadminprivileges.objects.first() 
    else:
        privileges = adminprivileges.objects.first()
    context = {
        'privileges': privileges,
        'role':role,
        'name':name, 
        'assetview': privileges.assetview if privileges else False,
        'userview': privileges.userview if privileges else False,
        'employeeview': privileges.employeeview if privileges else False,
        'locationview': privileges.locationview if privileges else False,
        'departmentview': privileges.departmentview if privileges else False,
        'categoryview': privileges.categoryview if privileges else False,
        'rolesview': privileges.rolesview if privileges else False,
        'reportview': privileges.reportview if privileges else False,
        'previlegeedit':privileges.privilegeedit if privileges else False,

    }
    return render(request, 'privilege.html', context)

@login_required_custom
def privilege_page(request,roles):
    name = request.session.get('name', None)
    role = request.session.get('role', None)
    models = {
        'Admin': adminprivileges,
        'SystemAdmin': systemadminprivileges,
        'CISO': cisoprivileges,
        'Fnhead': fnprivileges,
        'AssetOwner': assetownerprivileges,
    }
    PrivilegesModel = models.get(roles)
    if not PrivilegesModel:
        return redirect('privileges')  # Handle invalid role

    privileges, _ = PrivilegesModel.objects.get_or_create(id=1)
    if role == 'Admin':
        privileges1 = adminprivileges.objects.first()    
    elif role == 'CISO':
        privileges1 = cisoprivileges.objects.first()   
    elif role == 'Fnhead':
        privileges1 = fnprivileges.objects.first()   
    elif role == 'AssetOwner':
        privileges1 = assetownerprivileges.objects.first()   
    elif role == 'SystemAdmin':
        privileges1 = systemadminprivileges.objects.first() 
    else:
        privileges1 = adminprivileges.objects.first()
    context = {
        'privileges': privileges,
        'name':name,
        'role':role,
        'roles': roles,
        'assetview': privileges1.assetview if privileges1 else False,
        'userview': privileges1.userview if privileges1 else False,
        'employeeview': privileges1.employeeview if privileges1 else False,
        'locationview': privileges1.locationview if privileges1 else False,
        'departmentview': privileges1.departmentview if privileges1 else False,
        'categoryview': privileges1.categoryview if privileges1 else False,
        'rolesview': privileges1.rolesview if privileges1 else False,
        'reportview': privileges1.reportview if privileges1 else False,
        'previlegeedit':privileges1.privilegeedit if privileges1 else False,
    }
    return render(request,  f'privilege_{roles}.html', context)