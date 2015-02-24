import flask
import authomatic.adapters
import authomatic

import application
import application.core.settings


auth = authomatic.Authomatic(application.core.settings.AUTHOMATIC_CONFIG,
                             application.core.settings.AUTHOMATIC_SECRET_STRING,
                             report_errors=False)


def social_login(provider_name):
    response = flask.make_response()
    result = auth.login(authomatic.adapters.WerkzeugAdapter(flask.request, response), provider_name)

    if result:
        if result.user:
            result.user.update()
        return flask.render_template('login.html', result=result)
    return response


    # {# Check for errors. #}
    #  {% if result.error %}
    # <h2>Damn that error: {{ result.error.message }}</h2>
    #                                                  {% endif %}
    #
    # {# Welcome the user. #}
    #  {% if result.user %}
    # <h1>Hi {{ result.user.name }}</h1>
    #                                <h2>Your id is: {{ result.user.id }}</h2>
    #                                                                      <h2>Your email is: {{ result.user.email }}</h2>
    #                                                                                                                  {% endif %}
    #
    # {# If the user has credentials, we can access his/her protected resources. #}
    #  {% if result.user.credentials %}
    #
    # {# Let's get the user's 5 most recent statuses. #}
    #  {% if result.provider.name == 'fb' %}
    # Your are logged in with Facebook.<br />
    #                         {% endif %}{# result.provider.name == 'fb' #}
    #
    # {# Do the same for Twitter. #}
    # {% if result.provider.name == 'tw' %}
    # Your are logged in with Twitter.<br />
    # {% endif %}{# result.provider.name == 'tw' #}
    #
    # {% endif %}{# result.user.credentials #}
