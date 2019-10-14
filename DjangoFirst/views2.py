from django.http import HttpResponse

def windmill(request):
    a = '''
        <html>
            <head>
               <style>
                   .item{
                    color:yellow;
                    font-size:20px;
                   }
               </style>
            </head>
            <body>
                %s
            </body>
        </html>

    '''
    k =''
    for x in range(1,10):
        k +='<div class=item>'
        for y in range(1,x+1):
            k += " %d * %d  = %d " % (y, x, y*x)
        k += '</div>'

    return HttpResponse(a % k)