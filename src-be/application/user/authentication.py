import flask
import authomatic.adapters
import authomatic
import application
import application.core.settings
import application.user.services
import application.core.session


auth = authomatic.Authomatic(application.core.settings.AUTHOMATIC_CONFIG,
                             application.core.settings.AUTHOMATIC_SECRET_STRING,
                             report_errors=False)


def social_login(provider_name):
    response = flask.make_response()
    try:
        result = auth.login(authomatic.adapters.WerkzeugAdapter(flask.request, response), provider_name)
    except Exception:
        return flask.redirect('/')

    if result:
        if result.user:
            result.user.update()
            # TODO Save the social auth somewhere
            email = result.user.email
            user = application.user.services.fetch_by_email(email)
            if user:
                response_details = flask.redirect('/')
                # TODO .. fix the following
                session, resp = application.core.session.set_session(email)
                return resp
        return flask.render_template('verify.html', social=result)
    return response

