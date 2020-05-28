FROM python:3.8-slim AS base

FROM base AS builder

RUN pip3 install poetry==1.0.5
RUN python3 -m venv /venv

COPY pyproject.toml poetry.lock ./
RUN poetry export -f requirements.txt | /venv/bin/pip install -r /dev/stdin

COPY . .
RUN poetry build && /venv/bin/pip install dist/*.whl

FROM base AS final

COPY --from=builder /venv /venv

ENV PATH=/venv/bin/:$PATH

RUN apt-get update && apt-get install --no-install-recommends -y libcairo2-dev && rm -rf /var/lib/apt/lists

CMD ["snfaag"]
