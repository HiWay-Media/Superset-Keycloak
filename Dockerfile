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
#RUN pip install --upgrade pip
#RUN pip uninstall fbprophet pystan
#RUN pip install --upgrade pip setuptools
RUN pip install lunarcalendar==0.0.9 tqdm==4.64.0 
RUN pip install cython==0.29.21 
RUN pip install "pystan<3.0"
RUN pip install "prophet>=1.0.1,<1.1"
#
CMD ["/bin/sh","-c","/usr/bin/run-server.sh"]
USER superset
#
