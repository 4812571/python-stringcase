FROM fuzzers/atheris:2.0.7-python3.9
COPY . /python-stringcase
RUN apt-get -y update
RUN apt-get install -y git
WORKDIR /python-stringcase
RUN pip install .
RUN chmod +x /python-stringcase/mayhem/convert.py