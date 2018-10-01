""" Web Routes """

from masonite.routes import Get, Post


ROUTES = [
    Get().route('/', 'PageController@index'),

    # Jobs
    Get().route('/jobs', 'JobController@index'),
]

ROUTES = ROUTES + [
    Get().route('/login', 'LoginController@show'),
    Get().route('/logout', 'LoginController@logout'),
    Post().route('/login', 'LoginController@store'),
    Get().route('/register', 'RegisterController@show'),
    Post().route('/register', 'RegisterController@store'),
    Get().route('/email/verify', 'ConfirmController@verify_show'),
    Get().route('/email/verify/@id:signed', 'ConfirmController@confirm_email'),
]
