FROM fuzzers/atheris:2.0.7-python3.9

COPY . /python-stringcase

# Build Project
WORKDIR /python-stringcase
RUN pip install .

# Change Permissions
RUN chmod +x /thefuzz/mayhem/convert.py