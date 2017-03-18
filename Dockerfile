FROM python:2.7.13
MAINTAINER Your Name "nooopur2393@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "app.py"]
CMD ["https://github.com/noopurjoshi/assignment1-config-example"]