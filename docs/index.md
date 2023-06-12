# Superset-Keycloak
[![Docker SuperSet Keycloak](https://github.com/HiWay-Media/Superset-Keycloak/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/HiWay-Media/Superset-Keycloak/actions/workflows/docker-publish.yml)

Superset-Keycloak is a Docker repository that provides a setup for running Apache Superset with Keycloak as the authentication and authorization provider. This integration allows you to secure your Superset instance using Keycloak's robust identity and access management capabilities.

## Description

This repository contains Docker and configuration files necessary to deploy Superset with Keycloak. It enables you to authenticate users through Keycloak and manage access to Superset's features and resources based on Keycloak roles and permissions.

## Features

- Integration of Apache Superset with Keycloak for authentication and authorization.
- Centralized user management and access control using Keycloak.
- Seamless login and Single Sign-On (SSO) experience for users.


## Prerequisites

Before running the Superset-Keycloak setup, ensure that you have the following installed on your system:

- Docker
- Keycloak

## Access Superset:

- Open your browser and navigate to http://localhost:8088 to access Superset.
- You will be redirected to the Keycloak login page, where you can authenticate with your Keycloak credentials.
- After successful authentication, you will be redirected back to Superset.

For more detailed instructions and advanced configurations, please refer to the documentation.

## Contributions
Contributions to the Superset-Keycloak repository are welcome! If you find any issues, have suggestions for improvements, or want to contribute enhancements, please open an issue or submit a pull request on the GitHub repository.

Please follow the existing code style and provide clear descriptions and documentation for any changes or additions.

## License
Superset-Keycloak is licensed under the MIT License.