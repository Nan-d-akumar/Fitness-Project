from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name='homeorg'),
    path('contact',views.contact,name='contact'),
    path('about-us', views.aboutus, name='about-us'),
    path('customer_registration',views.customer_registration,name='customer_reg'),
    path('trainer_registration',views.trainer_registration,name='trainer_reg'),
    path('traineredit/<int:cid>/',views.traineredit,name='traineredit'),
    path('login',views.LoginFunction,name='login'),
    path('logout',views.LogoutFunction,name='logout'),
    path('custhome/<int:id>/<int:scid>/',views.custhome,name='custhome'),
    path('custvideos/<int:tid>/<int:cid>/',views.custhomevideos,name='custvideos'),
    path('custDiet',views.custDiet,name='custDiet'),
    path('payment_fun',views.Payment_Function,name='paym'),
    path('payment_confirmation',views.payment_confirm,name='pcfm'),
    path('request_diet',views.request_diet,name='rqdt'),
    path('trainercust',views.trainercustview,name='tcust'),
    path('trainercust2/<int:id>/', views.trainercustview2, name='tcust2'),
    path('payment_fun2/<int:tid>/',views.Payment_Function2,name='paym2'),
    path('paycomfirm2/<int:tid>/',views.payment_confirm2,name='pc2'),
    path('trainer_cust_list', views.trainer_cust_all, name='tcl'),
    path('tcv/<int:id>/',views.trainer_customer_view,name='tcview'),
    path('leaderpoints',views.LeaderPoint,name='points'),
    path('status',views.LeaderPoint,name='points'),
    path('leadertable',views.leadertable,name='ltble'),
    path('feedback', views.feedback, name='feedback'),
    path('billdiet/<int:id>/', views.billdiet, name='billdiet'),
    path('billtrainer/<int:id>/', views.billtrainer, name='billtrainer'),
    path('search',views.Search,name='search'),
]