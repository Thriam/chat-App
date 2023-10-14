FROM python
EXPOSE 8088
RUN pip install Flask
COPY . ./app
WORKDIR /app
ENTRYPOINT python app.py
