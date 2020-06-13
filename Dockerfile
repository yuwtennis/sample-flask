# Keep container small
FROM alpine:3.12.0

# 
RUN apk add --no-cache python3 py3-pip

# 
WORKDIR app

#
RUN pip3 install setuptools wheel

#
COPY dist/ /app

#
RUN pip3 install *whl

#
ENV SECRET_KEY 'dev'

#
EXPOSE 8080

#
CMD /usr/bin/waitress-serve --call 'flaskr:deploy'
