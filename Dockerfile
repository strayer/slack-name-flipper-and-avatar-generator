FROM python:3.9 AS builder

RUN pip3 install poetry==1.0.5
RUN python3 -m venv /venv

COPY pyproject.toml poetry.lock ./
RUN poetry export -f requirements.txt | /venv/bin/pip install -r /dev/stdin

COPY . .
RUN poetry build && /venv/bin/pip install dist/*.whl

FROM python:3.9-slim AS final

COPY --from=builder /venv /venv

ENV PATH=/venv/bin/:$PATH

RUN apt-get update && apt-get install --no-install-recommends -y libtiff5 libjpeg62-turbo libopenjp2-7 libcairo2 && rm -rf /var/lib/apt/lists

CMD ["snfaag"]
