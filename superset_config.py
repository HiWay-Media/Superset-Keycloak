import os
from typing import Optional
#
def get_env_variable(var_name: str, default: Optional[str] = None) -> str:
    """Get the environment variable or raise exception."""
    try:
        return os.environ[var_name]
    except KeyError:
        if default is not None:
            return default
        else:
            error_msg = "The environment variable {} was missing, abort...".format(
                var_name
            )
            raise EnvironmentError(error_msg)
        #
    #   
#
ENABLE_PROXY_FIX = True
DASHBOARD_RBAC = True
FEATURE_FLAGS = {"DASHBOARD_RBAC": True}
#################################
#       METADATA DATABASE       #
#################################
DATABASE_DIALECT = get_env_variable("DB_DIALECT")
DATABASE_USER = get_env_variable("DB_USER")
DATABASE_PASSWORD = get_env_variable("DB_PASSWORD")
DATABASE_HOST = get_env_variable("DB_HOST")
DATABASE_PORT = get_env_variable("DB_PORT")
DATABASE_DB = get_env_variable("DB_NAME")
#
SQLALCHEMY_DATABASE_URI = "%s://%s:%s@%s:%s/%s?charset=utf8" % (
    DATABASE_DIALECT,
    DATABASE_USER,
    DATABASE_PASSWORD,
    DATABASE_HOST,
    DATABASE_PORT,
    DATABASE_DB,
)
#
#---------------------------KEYCLOACK ----------------------------
# See: https://github.com/apache/superset/discussions/13915
# See: https://stackoverflow.com/questions/54010314/using-keycloakopenid-connect-with-apache-superset/54024394#54024394
from keycloak_security_manager          import  OIDCSecurityManager
from flask_appbuilder.security.manager  import AUTH_OID, AUTH_OAUTH
#
OIDC_ENABLE = get_env_variable("OIDC_ENABLE", 'False')
#
if OIDC_ENABLE == 'True':
    AUTH_TYPE                       = AUTH_OID
    SECRET_KEY                      = get_env_variable("SECRET_KEY", 'secret_key')
    OIDC_CLIENT_SECRETS             = get_env_variable("OIDC_CLIENT_SECRETS", '/app/pythonpath/client_secret.json')
    OIDC_ID_TOKEN_COOKIE_SECURE     = False
    OIDC_REQUIRE_VERIFIED_EMAIL     = False
    OIDC_OPENID_REALM               = get_env_variable("OIDC_OPENID_REALM",'realm')
    OIDC_INTROSPECTION_AUTH_METHOD  = 'client_secret_post'
    CUSTOM_SECURITY_MANAGER         = OIDCSecurityManager
    AUTH_ROLES_SYNC_AT_LOGIN        = True
    AUTH_USER_REGISTRATION          = True
    AUTH_USER_REGISTRATION_ROLE     = get_env_variable("AUTH_USER_REGISTRATION_ROLE", 'Gamma')
#--------------------------------------------------------------
#
#
SMTP_ENABLE = get_env_variable("SMTP_ENABLE", 'False')
#
#############################################
#       EMAIL REPORTS CONFIGURATION         #
#############################################
if SMTP_ENABLE == 'True':
    SMTP_HOST = get_env_variable("SMTP_HOST")
    SMTP_STARTTLS = True
    SMTP_SSL = False
    SMTP_USER = get_env_variable("SMTP_USER")
    SMTP_PORT = get_env_variable("SMTP_PORT")
    SMTP_PASSWORD = get_env_variable("SMTP_PASSWORD")
    SMTP_MAIL_FROM = get_env_variable("SMTP_MAIL_FROM")
#
