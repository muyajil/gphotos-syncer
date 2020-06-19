FROM gilesknap/gphotos-sync:latest

COPY sync.py /sync.py

ENTRYPOINT [ "python", "/sync.py" ]