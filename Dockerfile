# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.11-rc-slim

# Warning: A port below 1024 has been exposed. This requires the image to run as a root user which is not a best practice.
# For more information, please refer to https://aka.ms/vscode-docker-python-user-rights`
EXPOSE 80

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
COPY start.sh .
RUN python -m pip install -r requirements.txt -i https://mirrors.bfsu.edu.cn/pypi/web/simple

WORKDIR /app
COPY . /app

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
ENTRYPOINT ["bash", "./start.sh"]
