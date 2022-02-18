FROM python:3.7-buster

ARG pip_username
ARG pip_password

WORKDIR /home/deploy
COPY ./  ./
RUN PIP_USERNAME=$pip_username PIP_PASSWORD=$pip_password pip install --no-cache-dir -r requirements.txt -r internal_requirements.txt --user
ENV PATH="/home/deploy/.local/bin:${PATH}"
CMD ["python3", "./main.py"]
# CMD ["python","app.py"]
