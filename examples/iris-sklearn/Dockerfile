
FROM python:3.10.6-slim AS base
LABEL maintainer="salman@scaleoutsystems.com"
WORKDIR /app

# Copy the requirements file first, to ensure it's available for pip install
COPY requirements.txt .

# Fix the RUN command to correctly install gcc and python3-dev
RUN apt-get update \
    && apt-get install --no-install-recommends -y git gcc python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install git+https://github.com/dininduviduneth/fedn-attack-sim-uu.git@master#egg=fedn\&subdirectory=fedn \
    && pip install --no-cache-dir -r requirements.txt

FROM python:3.10.6-slim AS build
COPY --from=base /usr/local/lib/python3.10/site-packages/ /usr/local/lib/python3.10/site-packages/
COPY --from=base /usr/local/bin/fedn /usr/local/bin/
WORKDIR /app
# Update the ENTRYPOINT to the correct path if /venv/bin/fedn is not correct
# ENTRYPOINT [ "fedn" ]