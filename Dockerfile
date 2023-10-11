# build stage
FROM python:3.11-slim AS builder

# install PDM
RUN pip install -U pip setuptools wheel
RUN pip install pdm

# copy files
COPY pyproject.toml pdm.lock README.md /project/
COPY src/ /project/src

# install dependencies and project into the local packages directory
WORKDIR /project
RUN mkdir __pypackages__ && pdm sync --prod --no-editable


# run stage
FROM python:3.11-slim

# retrieve packages from build stage
ENV PYTHONPATH=/project/pkgs
COPY --from=builder /project/__pypackages__/3.11/lib /project/pkgs

# retrieve executables
COPY --from=builder /project/__pypackages__/3.11/bin/* /bin/

RUN groupadd -r user && useradd -r -g user user
USER user

# set command/entrypoint, adapt to fit your needs
CMD ["gunicorn", "-w 4", "--access-logfile=-", "-b app:8000", "app.factory:create_app()"]
