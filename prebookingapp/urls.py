from django.contrib import admin
from django.urls import path
from. import views

urlpatterns = [
    path('',views.index),
    path('user_register/',views.user_register),
    path('restaurant_register/',views.restaurant_register),
    path('login/',views.login),
    path('logout/',views.logout),



    path('user_home/',views.user_home),
    path('user_profile/',views.user_profile),
    path('user_edit_profile/',views.user_edit_profile),
    path('user_view_menu/',views.user_view_menu,name="user_view_menu"),
    path('user_view_restaurant/',views.user_view_restaurant),
    path('user_booking_restaurant/<int:r_id>/',views.user_booking_restaurant),
    path('user_cancel_bookings/',views.user_cancel_bookings),
    path('user_view_booking_status/',views.user_view_booking_status),
    path('user_view_restaurant_details/',views.user_view_restaurant_details),
    path('user_view_menu_details/',views.user_view_menu_details),
    path('add_to_cart/',views.add_to_cart),
    path('user_cartpage/',views.user_cartpage),
    path('delete_cart/',views.delete_cart),
    path('cart_menu_payment/',views.cart_menu_payment),
    path('user_payment/',views.user_payment),
    path('user_search_restaurants/',views.user_search_restaurants),
    path('user_send_feedback/<int:r_id>/',views.user_send_feedback),
    path('user_send_menu_feedback/<int:m_id>/',views.user_send_menu_feedback),
    path('user_view_booking/',views.user_view_booking),
    path('user_cancel_bookings/',views.user_cancel_bookings),
    




    path('restaurant_home/',views.restaurant_home),
    path('restaurant_profile/',views.restaurant_profile),
    path('restaurant_edit_profile/',views.restaurant_edit_profile),
    path('restaurant_menu/',views.restaurant_menu),
    path('restaurant_view_menu/',views.restaurant_view_menu),
    path('restaurant_edit_menu/',views.restaurant_edit_menu),
    path('restaurant_view_bookings/',views.restaurant_view_bookings),
    path('restaurant_confirm_bookings/',views.restaurant_confirm_bookings),
    path('restaurant_cancel_bookings/',views.restaurant_cancel_bookings),
    path('restaurant_view_canceled_bookings/',views.restaurant_view_canceled_bookings),
    path('restaurant_view_feedback/',views.restaurant_view_feedback),
    path('restaurant_view_menu_feedback/<int:m_id>/',views.restaurant_view_menu_feedback),
    path('restaurant_view_orders/',views.restaurant_view_orders),
    path('restaurant_add_worker/',views.restaurant_add_worker),
    path('restaurant_view_workers/',views.restaurant_view_workers),
    path('restaurant_delete_worker/',views.restaurant_delete_worker),
    path('restaurant_view_workers_status/',views.restaurant_view_workers_status),
    path('restaurant_allocate_work/',views.restaurant_allocate_work),
   






    path('admin_home/',views.admin_home),
    path('admin_view_restaurant/',views.admin_view_restaurant),
    path('admin_approve_restaurant/',views.admin_approve_restaurant),
    path('admin_reject_restaurant/',views.admin_reject_restaurant),
    path('admin_view_user/',views.admin_view_user),
    path('admin_view_feedback/',views.admin_view_feedback),
    path('admin_view_bookings/',views.admin_view_bookings),
    path('admin_view_orders/',views.admin_view_orders),



    path('worker_home/',views.worker_home),
    path('worker_view_alloted_work/',views.worker_view_alloted_work),
    path('worker_accept_work/',views.worker_accept_work),
    path('worker_view_accepted_work/',views.worker_view_accepted_work),
    path('worker_complete_work/',views.worker_complete_work),
    path('worker_view_completed_work/',views.worker_view_completed_work),
    path('worker_profile/',views.worker_profile),
    path('worker_edit_profile/',views.worker_edit_profile),




]