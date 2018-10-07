""" Web Routes """

from masonite.routes import Get, Post


ROUTES = [
    # Pages
    Get().route('/', 'JobController@index'),
    Get().view('/about', 'page/about'),
    Get().view('/privacy', 'page/privacy'),
    Get().view('/contact', 'page/contact'),

    # Jobs
    Get().route('/jobs', 'JobController@index'),
    Post().route('/jobs', 'JobController@create'),
    Get().route('/jobs/new', 'JobController@new'),
    Get().route('/jobs/@slug', 'JobController@show'),
    Get().route('/companies', 'JobController@companies'),
    Get().route('/companies/@slug', 'JobController@show_company'),

    # Blog
    Get().route('/blog', 'BlogController@index')

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
