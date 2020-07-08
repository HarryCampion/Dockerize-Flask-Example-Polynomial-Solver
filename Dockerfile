FROM python:3.7.3

# copy flask app and requirments
COPY ./requirements.txt /app/
COPY ./solver /app/
WORKDIR /app/

# install dependencies
RUN pip install -r ./requirements.txt

# expose port 
EXPOSE 5000

# run app
CMD python run.py
