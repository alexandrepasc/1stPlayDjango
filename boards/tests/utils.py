from boards.models import Board, Topic, User


def add_data():
    add_just_board_data()

    User.objects.create_user(username='test', email='', password='')
    Topic.objects.create(subject='test1', board=Board.objects.get(id=1), starter=User.objects.get(username='test'))


def add_just_board_data():
    Board.objects.create(name='Django', description='Django board.')
    Board.objects.create(name='Python', description='Python board.')
