import os
import subprocess

service_name = "MySQL80"


def start_mysql_service():
    try:
        subprocess.run(["net", "start", service_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error al iniciar el servicio {service_name}: {e}")


if __name__ == "__main__":
    start_mysql_service()
