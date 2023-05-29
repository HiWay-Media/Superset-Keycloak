FROM apache/superset:pr-24161
USER root
RUN pip install mysqlclient itsdangerous==2.0.1 flask-oidc==1.4.0  Flask-OpenID==1.3.0
#
# Add custom superset_config.py file and shell files
COPY superset_config.py /app/
ENV SUPERSET_CONFIG_PATH /app/superset_config.py
#
ADD keycloak_security_manager.py /app/pythonpath
#
CMD ["/bin/sh","-c","/usr/bin/run-server.sh"]
USER superset
#