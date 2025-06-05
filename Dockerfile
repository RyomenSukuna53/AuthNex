# Base image
FROM python:3.10

# Working directory inside the container
WORKDIR /app/AuthNex

# Copy project files
COPY . .

# Install dependencies
RUN pip install --upgrade pip setuptools
RUN pip install -U -r requirements.txt
RUN pip install git+https://github.com/RyomenSukuna53/AuthBot.git

# Run the application
CMD ["python3", "-m", "AuthNex"]

EXPOSE 8080
