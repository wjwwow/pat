from django.shortcuts import render
from django.utils.deprecation import MiddlewareMixin

# loginRequired_list=['/userinfo/',]
#
# class LoginMiddleware(MiddlewareMixin):
#     def process_request(self,request):
#
#         if request.path in loginRequired_list:
#             username=request.session.get('username')
#             if not username:
#                 return render(request,'pathtml/login.html')