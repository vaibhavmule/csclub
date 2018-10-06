""" Web Routes """

from masonite.routes import Get, Post, Match


ROUTES = [
    Get().route('/', 'PageController@index'),

    # Jobs
    Match(['GET', 'POST']).route('/jobs', 'JobController@index'),
    Get().route('/jobs/new', 'JobController@new'),
    Get().route('/jobs/@slug', 'JobController@show'),
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
