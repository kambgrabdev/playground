FROM python:3.6
RUN pip install flask gunicorn
COPY app /opt/app/
COPY minesweeper.py /opt/minesweeper.py
WORKDIR /opt
EXPOSE 5001
CMD ["gunicorn", "-b", "0.0.0.0:5001", "--reload", "app:app"]