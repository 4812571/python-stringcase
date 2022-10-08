FROM fuzzers/atheris:2.0.7-python3.9

COPY . /python-stringcase

# Build Project
WORKDIR /thefuzz
RUN pip install .

# Change Permissions
RUN chmod +x /thefuzz/mayhem/convert.py