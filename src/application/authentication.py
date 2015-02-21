import application
import application.settings
import flask
import authomatic.adapters
import authomatic


auth = authomatic.Authomatic(application.settings.AUTHOMATIC_CONFIG,
                             application.settings.AUTHOMATIC_SECRET_STRING,
                             report_errors=False)


@application.app.route('/login/<provider_name>/', methods=['GET', 'POST'])
def login(provider_name):
    response = flask.make_response()
    result = auth.login(authomatic.adapters.WerkzeugAdapter(flask.request, response), provider_name)

    if result:
        if result.user:
            result.user.update()
        return flask.render_template('index.html', result=result)
    return response
