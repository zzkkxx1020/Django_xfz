from django.shortcuts import render


# 查询页
def search(request):
    return render(request, 'search/search.html')
