import flask
import authomatic.adapters
import authomatic

import application
import application.core.settings


auth = authomatic.Authomatic(application.core.settings.AUTHOMATIC_CONFIG,
                             application.core.settings.AUTHOMATIC_SECRET_STRING,
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
