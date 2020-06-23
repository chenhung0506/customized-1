FROM python:3.7-alpine
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
ADD ./module /usr/src/app
ARG testArg
RUN echo "testArg: $testArg"
# EXPOSE 3000
# ENV FLASK_APP app.py
# ENV FLASK_RUN_HOST 0.0.0.0
# RUN apk add --no-cache gcc musl-dev linux-headers
# Alpine Linux 
# apk update
# apk upgrade
# apk add bash
RUN apk add bash
RUN ls /usr/src/app
RUN pip install -r /usr/src/app/requirements.txt
# RUN rm -rf /usr/src/app/*
# CMD ["flask", "run"]
CMD ["python", "server.py"]
# ENTRYPOINT [ "/code/test.py" ]