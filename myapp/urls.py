from django.urls import path
from . import views

urlpatterns = [
    path('', views.asset_login, name='asset_login'),
    path('admins/', views.admin_dashboard, name='admin_dashboard'),
    path('assetdb/', views.assetowner_dashboard, name='assetowner_dashboard'),
    path('cisodb/', views.ciso_dashboard, name='ciso_dashboard'),
    path('fndb/', views.fnhead_dashboard, name='fnhead_dashboard'),
    path('sysdb/', views.systemadmin_dashboard, name='systemadmin_dashboard'),
    path('logout/', views.logout_view, name='logout'),


    path('reports/', views.reports_view, name='reports'),
    path('roles/', views.roles, name='roles'),
    path('edit_roles/<int:user_id>/', views.edit_roles, name='edit_roles'),


    path('privileges/', views.privileges, name='privileges'),
    path('privileges/<str:roles>/', views.privilege_page, name='privilege_page'),
    path('update_privileges/<str:roles>/', views.update_privileges, name='update_privileges'),


    path('categories/', views.category_list, name='category_list'),
    path('save_category/', views.save_category, name='save_category'),
    path('categories/edit/<int:category_id>/', views.edit_category, name='edit_category'),
    path('categories/delete/<int:category_id>/', views.delete_category, name='delete_category'),
    


    path('departments/', views.department_list, name='department'),  
    path('edit_department/<int:department_id>/', views.edit_department, name='edit_department'),
    path('delete-department/<int:department_id>/', views.delete_department, name='delete_department'),
    path('department/add/', views.add_department, name='add_department'),


    path('user_list/',views.user_list,name='user_list'),
    path('save_user/', views.save_user, name='save_user'),
    path('edit_user/<int:user_id>/', views.edit_user, name='edit_user'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),



path('employees/',views.employee,name='employee'),
path('delete-employee/<int:employee_id>/', views.delete_employee, name='delete_employee'),
path('edit_employee/<int:employee_id>/', views.edit_employee, name='edit_employee'),
path('add_employee/', views.add_employee, name='add_employee'),





path('asset_list/',views.asset_list,name='asset_list'),
    path('add_asset/', views.add_asset, name='add_asset'),
    path('delete_asset/<int:user_id>/',views.delete_asset,name='delete_asset'),
    path('view/<int:user_id>/', views.view_asset, name='view_asset'),
    path('edit_asset/<int:asset_id>/', views.edit_asset, name='edit_asset'),
    path('assign_asset/<int:asset_id>/', views.assign_asset, name='assign_asset'),
    path('return_asset/<int:asset_id>/', views.return_asset, name='return_asset'),





path('location_list/',views.location_list,name='location_list'),
path('add_location/', views.add_location, name='add_location'),
path('delete_loc/<int:location_id>/',views.delete_loc,name='delete_loc'),
path('location_list/edit/<int:location_id>/', views.edit_location, name='edit_location'),

    
]