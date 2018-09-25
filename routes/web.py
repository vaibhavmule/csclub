''' Web Routes '''
from masonite.routes import Get, Post

ROUTES = [
    Get().route('/', 'PageController@index'),

    # Jobs
    Get().route('/job', 'JobController@index'),
]

ROUTES = ROUTES + [
    Get().route('/login', 'LoginController@show'),
    Get().route('/logout', 'LoginController@logout'),
    Post().route('/login', 'LoginController@store'),
    Get().route('/register', 'RegisterController@show'),
    Post().route('/register', 'RegisterController@store'),
    Get().route('/home', 'HomeController@show'),
]
