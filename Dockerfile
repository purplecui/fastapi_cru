FROM python:3.13
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
ENV URL_DATABASE=postgresql://postgres:password@psql:5433/blog_api
EXPOSE 8000
CMD [ "uvicorn","index:app" ]