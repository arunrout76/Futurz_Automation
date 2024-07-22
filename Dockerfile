# # Use Alpine Linux as the base image
# #FROM alpine

# # Install Python 3.11 and pip
# #RUN apk add --no-cache python3=3.11.0-r0 \
# #    && python3 -m ensurepip \
# #    && rm -r /usr/lib/python*/ensurepip \
# #    && pip3 install --upgrade pip setuptools \
# #    && ln -s /usr/bin/python3 /usr/bin/python \
# #    && ln -s /usr/bin/pip3 /usr/bin/pip

# FROM python:3.11-slim

# # Install curl
# # Install required tools
# RUN apt-get update && apt-get install -y \
#     curl \
#     unzip

# # Install Allure Command-Line tools (version 2.13.2)
# RUN curl -o /tmp/allure.zip -L https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.2/allure-commandline-2.13.2.zip \
#     && unzip /tmp/allure.zip -d /opt/ \
#     && ln -s /opt/allure-2.13.2/bin/allure /usr/bin/allure

# # Set environment paths for Python and Allure binaries
# ENV PATH $PATH:/usr/bin:/opt/allure-2.13.2/bin

# RUN pip install --no-cache-dir behave==1.2.6

# RUN pip install allure-behave==2.13.2

# # Set the working directory
# WORKDIR /Futurz

# # Copy the Selenium-Cucumber-Python project into the container
# COPY Driver Driver
# COPY features features
# COPY locators locators
# COPY Logs Logs
# COPY pages pages
# COPY Report Report
# COPY Screenshots Screenshots
# COPY Utility Utility
# COPY venv venv
# COPY start.bat start.bat
# COPY run.sh run.sh


# # # Command to run when the container starts
# # CMD ["behave", "-f", "allure_behave.formatter:AllureFormatter", "-o", "Report/Allure_Result", "./features"]
# # Run the run.sh file
# CMD ["bash", "run.sh"]







# Use Python 3.11 slim image with Debian buster as the base image
FROM python:3.11-slim-buster

# Install required tools
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    openjdk-11-jre-headless

# Install Selenium
RUN pip install --no-cache-dir selenium==4.9.0

# Install Allure Command-Line tools (version 2.13.2)
RUN curl -o /tmp/allure.zip -L https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.2/allure-commandline-2.13.2.zip \
    && unzip /tmp/allure.zip -d /opt/ \
    && ln -s /opt/allure-2.13.2/bin/allure /usr/bin/allure

# Set environment paths for Python, Selenium, Java, and Allure binaries
ENV PATH $PATH:/usr/bin:/opt/allure-2.13.2/bin

# Install Behave and Allure-Behave
RUN pip install --no-cache-dir behave==1.2.6 allure-behave==2.13.2

# Set the working directory
WORKDIR /app/Futurz

# Copy the Selenium-Cucumber-Python project into the container
COPY Driver Driver
COPY features features
COPY locators locators
COPY Logs Logs
COPY pages pages
COPY Report Report
COPY Screenshots Screenshots
COPY Utility Utility
COPY venv venv
COPY start.bat start.bat
COPY run.sh run.sh


# # Set up the virtual environment
# RUN python -m venv venv

# # Activate the virtual environment
# SHELL ["bash", "-c"]
# RUN source venv/bin/activate


# # Give execute permission to the script
# RUN chmod +x /run.sh

# # Command to run when the container starts
# CMD ["bash", "run.sh"]


# # Run Behave with Allure formatter
# CMD ["behave", "-f", "allure_behave.formatter:AllureFormatter", "-o", "Report/Allure_Result", "./features"]

# ENTRYPOINT ["behave", "-f", "allure_behave.formatter:AllureFormatter", "-o", "Report/Allure_Result", "./features"]

# CMD [ "ls", "-a" ]
# # Command to run when the container starts
# CMD ["bash", "run.sh"]











# # Use Python 3.11 slim image with Debian buster as the base image
# FROM python:3.11-slim-buster

# # Install required tools
# RUN apt-get update && apt-get install -y \
#     curl \
#     unzip \
#     openjdk-11-jre-headless

# # Install Selenium
# RUN pip install --no-cache-dir selenium==3.141.0

# # Install Allure Command-Line tools (version 2.13.2)
# RUN curl -o /tmp/allure.zip -L https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.2/allure-commandline-2.13.2.zip \
#     && unzip /tmp/allure.zip -d /opt/ \
#     && ln -s /opt/allure-2.13.2/bin/allure /usr/bin/allure

# # Set environment paths for Python, Selenium, Java, and Allure binaries
# ENV PATH $PATH:/usr/bin:/opt/allure-2.13.2/bin

# # Install Behave and Allure-Behave
# RUN pip install --no-cache-dir behave==1.2.6 allure-behave==2.13.2

# # Set the working directory
# WORKDIR /app


