from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404

from .forms import NewPostForm, NewTopicForm
from .models import Board, Topic, Post


def home(request):
    # boards = Board.objects.all()
    # boards_names = list()

    # for board in boards:
    # boards_names.append(board.name)

    # response_html = '<br>'.join(boards_names)
    # return HttpResponse(response_html)

    boards = Board.objects.all()

    setattr(request, 'view', 'home')
    setattr(request, 'breadcrumb', 'Home')

    return render(request, 'home.html', {'boards': boards})


def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)

    setattr(request, 'view', 'topics')
    setattr(request, 'breadcrumb', 'Topics')

    return render(request, 'topics.html', {'board': board})


def about(request):
    setattr(request, 'view', 'about')
    setattr(request, 'breadcrumb', 'About')

    return render(request, 'about.html')


@login_required
def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)

    setattr(request, 'view', 'newTopic')
    setattr(request, 'breadcrumb', 'New Topic')
    setattr(request, 'submitName', 'Post')

    if request.method == 'POST':
        form = NewTopicForm(request.POST)

        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = request.user
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=request.user
            )

            return redirect('board_topics', pk=board.pk)

    else:
        form = NewTopicForm()

    return render(request, 'newTopic.html', {'board': board, 'form': form})


# TODO: check if this can be changed.
def topic_(request, pk):
    topic_ = get_object_or_404(Topic, pk=pk)

    posts = topic_.posts.all

    board = Board.objects.get(pk=topic_.board.pk)

    setattr(request, 'view', 'topic')
    setattr(request, 'submitName', 'Post')

    if request.method == 'POST':
        form = NewPostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic_
            post.created_by = request.user
            post.save()

    else:
        form = NewPostForm()

    return render(request, 'topic.html', {'posts': posts, 'topic': topic_, 'board': board, 'form': form})
