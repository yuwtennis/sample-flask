# Keep container small
FROM alpine:3.12.0

# Add python packages
RUN apk add --no-cache python3 py3-pip

# Prepare working directory 
WORKDIR app

# Install setuptools , etc
RUN pip3 install setuptools wheel

# Copy wheel file
COPY dist/ /app

# Install wheel file
RUN pip3 install *whl

# SECRET for flask
ENV SECRET_KEY SOMEVALUE

# Export port 8080
EXPOSE 8080

# Run waitress when container start
CMD /usr/bin/gunicorn -w 4 -b 127.0.0.1:8080 flaskr:deploy
