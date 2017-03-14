from django.http import HttpResponse
from .models import Album, Song
from django.shortcuts import render,get_object_or_404
from django.http import Http404

'''
# from django.template import loader

instead of using this loader we can use another shortcut
which will work same but in a nicer way
'''
# you always pass 'request' and send the respose

def index(request):
    all_albums = Album.objects.all()
    # by default django looks in the directory name "templates"
    # if we mention 'music/index.html' it would load the correct file

    # template=loader.get_template('music/index.html')
    '''This bit we dont need to use as we will use the render'''

    # whenever we pass any information to template we need to pass
    # it via a dictionary {}, convention to name it "context"

    context={'all_albums':all_albums, }
    # we will return the render() function with the context and the request
    # we will catch the value from the index.html
    # return HttpResponse(template.render(context,request))
    '''instead of using the HttpResponse we will use the render'''
    return render(request,'music/index.html',context)

def detail(request,album_id):

    # try:
    #     album=Album.objects.get(pk=album_id)
    # except Album.DoesNotExist:
    #     raise Http404("Album does not exists")
    album=get_object_or_404(Album,pk=album_id)
    return render(request,'music/detail.html',context={'album':album })

def favorite(request,album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song=album.song_set.get(pk=request.POST['song'])
    except (KeyError,Song.DoesNotExist):
        return render(request,'music/detail.html',{
            'album':album,
            'error_message':"You did not select a valid song"})
    else:
        print(" his the song is saved")
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'music/detail.html', context={'album': album})

