from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Board

def home(request):
    #boards = Board.objects.all()
    #boards_names = list()

    #for board in boards:
        #boards_names.append(board.name)

    #response_html = '<br>'.join(boards_names)
    #return HttpResponse(response_html)

    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})

def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', {'board': board})

def about(request):
    response_html = 'about'
    return HttpResponse(response_html)

