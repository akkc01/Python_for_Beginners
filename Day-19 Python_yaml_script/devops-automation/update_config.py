from utils.file_updater import FileUpdater


# Application Configuration
application_file = "config/application.conf"

app_config = FileUpdater(application_file)


# Change server name
app_config.update_server_name(
    "prod-server-01"
)


# Change environment
app_config.update_environment(
    "prod"
)



# Kubernetes Deployment
deployment_file = "config/deployment.yaml"

deployment = FileUpdater(deployment_file)


# Change Docker image tag
deployment.update_image_tag(
    "myacr.azurecr.io/axion-api",
    "v2.0.0"
)


print("\nConfiguration update completed!")