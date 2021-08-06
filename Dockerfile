FROM python:3.9

WORKDIR /usr/src/app

COPY app.py /usr/src/app/
COPY calculate.py /usr/src/app/
COPY dependencies.txt /usr/src/app/
ADD ML_model.tar.gz /usr/src/app/

RUN pip install -r dependencies.txt

EXPOSE 5000

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]