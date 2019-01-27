FROM python:3.6
COPY . ./
RUN python -m pip install --upgrade pip
RUN pip install -r base-requirements.txt
ENV FLASK_APP=service.py
ENV FLASK_ENV=development
EXPOSE 5000/tcp
CMD ["python", "service.py"]

