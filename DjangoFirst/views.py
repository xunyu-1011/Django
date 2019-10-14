from django.http import HttpResponse
import time

# def index(request):
#     return HttpResponse("hello world")

# def birthday(request, month, day):
#     month = int(month)
#     day = int(day)
#     d = time.localtime(
#         time.mktime(
#             time.struct_time((2019, month, day, 0, 0, 0, 0, 0, 0))
#         )
#     ).tm_yday
#     return HttpResponse("<p style='color:pink;font-size:66px;'>祝你生日快乐~!<br>你的生日是%s月%s日,是一年中的第%s天</p>" % (month, day, d))

def chengfa(request):
    d =''
    for x in range(1,10):
        d +='<br>'
        for y in range(1,x+1):
            d += " %d * %d  = %d " % (y, x, y*x)

    return HttpResponse("<p style='color:pink;font-size:25px;'>"+d+"</p>")


a = '''
    <html>
        <head>
           <style>
               .item{
                color:yellow;
                font-size:50px;
               }
           </style>
        </head>
        <body>
            <div class=item>九九乘法表</div>
        </body>
    </html>

'''

# from django.http import HttpResponse
#
# def index(request):
#     return HttpResponse("hello")


