''' Web Routes '''
from masonite.routes import Get, Post

ROUTES = [
    Get().route('/', 'PageController@index'),

    # Jobs
    Get().route('/job', 'JobController@index'),
]
