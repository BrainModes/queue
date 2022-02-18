FROM python:3.7-buster
ARG pip_username
ARG pip_password
RUN groupadd --gid 1004 deploy \
    && useradd --home-dir /home/deploy --create-home --uid 1004 \
        --gid 1004 --shell /bin/sh --skel /dev/null deploy
WORKDIR /home/deploy
COPY .  ./
RUN chown -R deploy:deploy /home/deploy
USER deploy
RUN chmod +x /home/deploy/gunicorn_starter.sh
RUN PIP_USERNAME=$pip_username PIP_PASSWORD=$pip_password pip install --no-cache-dir -r requirements.txt -r internal_requirements.txt --user
ENV PATH="/home/deploy/.local/bin:${PATH}"
CMD ["./gunicorn_starter.sh"]
# CMD ["python","app.py"]

