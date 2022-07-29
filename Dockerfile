FROM ubuntu
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install --upgrade pip
RUN pip3 install pyogrio pyproj rtree shapely geopandas
WORKDIR /app
COPY . .
CMD ["python3","-u", "src/rpsbackend.py"]