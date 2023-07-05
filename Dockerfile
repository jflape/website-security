# Use an official Python runtime as the base image
#FROM python
FROM python:slim-bullseye
# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file and install dependencies
COPY socweb/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project code to the container
COPY socweb/. /app/


# Expose the container port
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]