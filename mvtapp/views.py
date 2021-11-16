from django.http import HttpResponse
from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

from mvtapp.models import LectureDetail

from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from mvtapp.models import LectureDetail
from django.urls import reverse

def detail(request):

        if request.method == 'POST':
                title = request.POST.get('title')
                count = request.POST.get('count')

                # ORM을 위한, 모델 오브젝트 생성
                data = LectureDetail()
                data.title = title
                data.count = int(count)

                data.save()

                return HttpResponseRedirect(reverse('mvtapp:detail'))
                #after input, for review datas in DB
                #datas = LectureDetail.objects.all()

                #return render(request, 'mvtapp/new_mvt_detail.html', context={'datas':datas})
        else:
            datas = LectureDetail.objects.all()

        return render(request, 'mvtapp/new_mvt_detail.html', context={'datas':datas})
        #return HttpResponse('response detail')
        #return render(request, 'mvtapp/new_mvt_detail.html')
