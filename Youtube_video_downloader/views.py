from django.http import HttpResponse 
from django.shortcuts import render
from .forms import linkForm
import yt_dlp,os, re
from django.conf import settings

media_root=settings.MEDIA_ROOT

# media_url=os.path.join(media_root,)
def download(link, format, quality):
    try:
        ydl_opts={
            'outtmpl':f'{media_root}%(title)s.%(ext)s',  # Specify the output file name and location
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
            info=ydl.extract_info(link,)
            title=info.get('title')
            ext=info.get('ext', 'unknown')          
            return title+"."+format
 
    except Exception as e:
        error=f"Error occured while downloading {str(e)}"

def index(request):
    if request.method=='GET':
        return render(request, 'index.html', context={'linkForm':linkForm})
    elif request.method=='POST':
 
        link=request.POST.get('link')
        format=request.POST.get('format')
        quality=request.POST.get('quality')

        pattern=rf'{media_root}'

        filename=str(download(link, format, quality=''))
        # filename=re.sub(pattern, "", filename)

        return render(request, 'index.html', context={'linkForm':linkForm, 'video':'media/'+filename, "link":link})

