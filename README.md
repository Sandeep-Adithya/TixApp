## Setup & Installation

Make sure you have the latest version of Python installed.
Tested on Python 3.8.10

```bash
pip install -r requirements.txt
```

## Running The App

```bash
python main.py
```

## Viewing The App

Go to `http://127.0.0.1:5000`

## CRUD API

Venue CURD API Useage:

Create : 

```bash
curl -v -H "Content-Type: application/json" -X POST -d "{ \"name\": \"{name}\" , \"address\": \"{address}\", \"city\": \"{city}\", \"capacity\": \"{capacity}\" }" --url 127.0.0.1:5000/api/venues/create
```

DEMO:
```bash
C:\Windows\System32>curl -v -H "Content-Type: application/json" -X POST -d "{ \"name\": \"IMAX\" , \"address\": \"Forum Mall\", \"city\": \"Chennai\", \"capacity\": \"250\" }" --url 127.0.0.1:5000/api/venues/create
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 127.0.0.1:5000...
* Connected to 127.0.0.1 (127.0.0.1) port 5000 (#0)
> POST /api/venues/create HTTP/1.1
> Host: 127.0.0.1:5000
> User-Agent: curl/8.0.1
> Accept: */*
> Content-Type: application/json
> Content-Length: 82
>
< HTTP/1.1 200 OK
< Server: Werkzeug/2.2.2 Python/3.8.10
< Date: Sun, 23 Apr 2023 16:39:12 GMT
< Content-Type: application/json
< Content-Length: 99
< Connection: close
<
{
  "address": "Forum Mall",
  "capacity": 250,
  "city": "Chennai",
  "id": 6,
  "name": "IMAX"
}
* Closing connection 0
```
Retrive:
```bash
curl -v -H "Content-Type: application/json" -X GET --url 127.0.0.1:5000/api/venues
curl -v -H "Content-Type: application/json" -X GET --url http://127.0.0.1:5000/api/venues/{id}
```
DEMO:
```bash
C:\Windows\System32>curl -v -H "Content-Type: application/json" -X GET --url 127.0.0.1:5000/api/venues
Note: Unnecessary use of -X or --request, GET is already inferred.
*   Trying 127.0.0.1:5000...
* Connected to 127.0.0.1 (127.0.0.1) port 5000 (#0)
> GET /api/venues HTTP/1.1
> Host: 127.0.0.1:5000
> User-Agent: curl/8.0.1
> Accept: */*
> Content-Type: application/json
>
< HTTP/1.1 200 OK
< Server: Werkzeug/2.2.2 Python/3.8.10
< Date: Sun, 23 Apr 2023 16:50:00 GMT
< Content-Type: application/json
< Content-Length: 573
< Connection: close
<
[
  {
    "address": "VR Mall",
    "capacity": 100,
    "city": "Chennai",
    "id": 1,
    "name": "PVR"
  },
  {
    "address": "Daba Gardens",
    "capacity": 100,
    "city": "Vizag",
    "id": 2,
    "name": "INOX"
  },
  {
    "address": "Daba Gardens",
    "capacity": 100,
    "city": "Mumbai",
    "id": 3,
    "name": "Cinepolis"
  },
  {
    "address": "Daba Gardens",
    "capacity": 100,
    "city": "Hyderabad",
    "id": 4,
    "name": "PVR"
  },
  {
    "address": "VR Mall",
    "capacity": 100,
    "city": "Vizag",
    "id": 5,
    "name": "INOX"
  }
]
* Closing connection 0

C:\Windows\System32>curl -v -H "Content-Type: application/json" -X GET --url 127.0.0.1:5000/api/venues/2
Note: Unnecessary use of -X or --request, GET is already inferred.
*   Trying 127.0.0.1:5000...
* Connected to 127.0.0.1 (127.0.0.1) port 5000 (#0)
> GET /api/venues/2 HTTP/1.1
> Host: 127.0.0.1:5000
> User-Agent: curl/8.0.1
> Accept: */*
> Content-Type: application/json
>
< HTTP/1.1 200 OK
< Server: Werkzeug/2.2.2 Python/3.8.10
< Date: Sun, 23 Apr 2023 16:50:48 GMT
< Content-Type: application/json
< Content-Length: 99
< Connection: close
<
{
  "address": "Daba Gardens",
  "capacity": 100,
  "city": "Vizag",
  "id": 2,
  "name": "INOX"
}
* Closing connection 0
```
Update:
```bash
curl -v -H "Content-Type: application/json" -X PUT -d "{ \"name\": \"{name}\" , \"address\": \"{address}\", \"city\": \"{city}\", \"capacity\": \"{capacity}\" }" --url 127.0.0.1:5000/api/venues/{id}
```
DEMO:
```bash
C:\Windows\System32>curl -v -H "Content-Type: application/json" -X PUT -d "{\"address\": \"Nexus Vijaya Forum Mall\"}" --url 127.0.0.1:5000/api/venues/6
*   Trying 127.0.0.1:5000...
* Connected to 127.0.0.1 (127.0.0.1) port 5000 (#0)
> PUT /api/venues/6 HTTP/1.1
> Host: 127.0.0.1:5000
> User-Agent: curl/8.0.1
> Accept: */*
> Content-Type: application/json
> Content-Length: 95
>
< HTTP/1.1 200 OK
< Server: Werkzeug/2.2.2 Python/3.8.10
< Date: Sun, 23 Apr 2023 16:40:29 GMT
< Content-Type: application/json
< Content-Length: 112
< Connection: close
<
{
  "address": "Nexus Vijaya Forum Mall",
  "capacity": 250,
  "city": "Chennai",
  "id": 6,
  "name": "IMAX"
}
* Closing connection 0
```
Delete:
```bash
curl -v -H "Content-Type: application/json" -X DELETE --url 127.0.0.1:5000/api/venues/{id}
```
DEMO:
```bash
C:\Windows\System32>curl -v -H "Content-Type: application/json" -X DELETE --url 127.0.0.1:5000/api/venues/6
*   Trying 127.0.0.1:5000...
* Connected to 127.0.0.1 (127.0.0.1) port 5000 (#0)
> DELETE /api/venues/6 HTTP/1.1
> Host: 127.0.0.1:5000
> User-Agent: curl/8.0.1
> Accept: */*
> Content-Type: application/json
>
< HTTP/1.1 204 NO CONTENT
< Server: Werkzeug/2.2.2 Python/3.8.10
< Date: Sun, 23 Apr 2023 16:43:08 GMT
< Content-Type: text/html; charset=utf-8
< Connection: close
<
* Closing connection 0
```


Movie CURD API Useage:

Create : 

```bash
curl -v -H "Content-Type: application/json" -X POST -d "{ \"name\": \"{name}\" , \"rating\": \"{rating}\", \"description\": \"{description}\", \"poster\": \"{poster_url}\" }" --url 127.0.0.1:5000/api/movies/create
```
DEMO:
```bash
C:\Windows\System32>curl -v -H "Content-Type: application/json" -X POST -d "{ \"name\": \"Avatar\" , \"rating\": \"4.1\" }" --url 127.0.0.1:5000/api/movies/create
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 127.0.0.1:5000...
* Connected to 127.0.0.1 (127.0.0.1) port 5000 (#0)
> POST /api/movies/create HTTP/1.1
> Host: 127.0.0.1:5000
> User-Agent: curl/8.0.1
> Accept: */*
> Content-Type: application/json
> Content-Length: 38
>
< HTTP/1.1 200 OK
< Server: Werkzeug/2.2.2 Python/3.8.10
< Date: Sun, 23 Apr 2023 17:05:45 GMT
< Content-Type: application/json
< Content-Length: 141
< Connection: close
<
{
  "description": "No description available",
  "id": 6,
  "name": "Avatar",
  "poster": "/static/assets/img/poster.jpg",
  "rating": 4.1
}
* Closing connection 0
```

Retrive:
```bash
curl -v -H "Content-Type: application/json" -X GET --url 127.0.0.1:5000/api/movies
curl -v -H "Content-Type: application/json" -X GET --url http://127.0.0.1:5000/api/movies/{id}
```
DEMO:
```bash
C:\Windows\System32>curl -v -H "Content-Type: application/json" -X GET --url 127.0.0.1:5000/api/movies
Note: Unnecessary use of -X or --request, GET is already inferred.
*   Trying 127.0.0.1:5000...
* Connected to 127.0.0.1 (127.0.0.1) port 5000 (#0)
> GET /api/movies HTTP/1.1
> Host: 127.0.0.1:5000
> User-Agent: curl/8.0.1
> Accept: */*
> Content-Type: application/json
>
< HTTP/1.1 200 OK
< Server: Werkzeug/2.2.2 Python/3.8.10
< Date: Sun, 23 Apr 2023 17:07:02 GMT
< Content-Type: application/json
< Content-Length: 1013
< Connection: close
<
[
  {
    "description": "No description available",
    "id": 1,
    "name": "Avengers",
    "poster": "/static/assets/img/poster.jpg",
    "rating": 4.5
  },
  {
    "description": "No description available",
    "id": 2,
    "name": "Avengers: Endgame",
    "poster": "/static/assets/img/poster.jpg",
    "rating": 4.5
  },
  {
    "description": "No description available",
    "id": 3,
    "name": "Avengers: Infinity War",
    "poster": "/static/assets/img/poster.jpg",
    "rating": 4.5
  },
  {
    "description": "No description available",
    "id": 4,
    "name": "Avengers: Age of Ultron",
    "poster": "/static/assets/img/poster.jpg",
    "rating": 4.5
  },
  {
    "description": "No description available",
    "id": 5,
    "name": "Captain America: The First Avenger",
    "poster": "/static/assets/img/poster.jpg",
    "rating": 4.5
  },
  {
    "description": "No description available",
    "id": 6,
    "name": "Avatar",
    "poster": "/static/assets/img/poster.jpg",
    "rating": 4.1
  }
]
* Closing connection 0

C:\Windows\System32>curl -v -H "Content-Type: application/json" -X GET --url 127.0.0.1:5000/api/movies/3
Note: Unnecessary use of -X or --request, GET is already inferred.
*   Trying 127.0.0.1:5000...
* Connected to 127.0.0.1 (127.0.0.1) port 5000 (#0)
> GET /api/movies/3 HTTP/1.1
> Host: 127.0.0.1:5000
> User-Agent: curl/8.0.1
> Accept: */*
> Content-Type: application/json
>
< HTTP/1.1 200 OK
< Server: Werkzeug/2.2.2 Python/3.8.10
< Date: Sun, 23 Apr 2023 17:07:36 GMT
< Content-Type: application/json
< Content-Length: 157
< Connection: close
<
{
  "description": "No description available",
  "id": 3,
  "name": "Avengers: Infinity War",
  "poster": "/static/assets/img/poster.jpg",
  "rating": 4.5
}
* Closing connection 0
```

Update:
```bash
curl -v -H "Content-Type: application/json" -X PUT -d "{ \"name\": \"{name}\" , \"rating\": \"{rating}\", \"description\": \"{description}\", \"poster\": \"{poster_url}\" }" --url 127.0.0.1:5000/api/movies/{id}
```
DEMO:
```bash
C:\Windows\System32>curl -v -H "Content-Type: application/json" -X PUT -d "{ \"description\": \"By James Cameron\" }" --url 127.0.0.1:5000/api/movies/6
*   Trying 127.0.0.1:5000...
* Connected to 127.0.0.1 (127.0.0.1) port 5000 (#0)
> PUT /api/movies/6 HTTP/1.1
> Host: 127.0.0.1:5000
> User-Agent: curl/8.0.1
> Accept: */*
> Content-Type: application/json
> Content-Length: 73
>
< HTTP/1.1 200 OK
< Server: Werkzeug/2.2.2 Python/3.8.10
< Date: Sun, 23 Apr 2023 17:13:03 GMT
< Content-Type: application/json
< Content-Length: 133
< Connection: close
<
{
  "description": "By James Cameron",
  "id": 6,
  "name": "Avatar",
  "poster": "/static/assets/img/poster.jpg",
  "rating": 4.1
}
* Closing connection 0
```

Delete:
```bash
curl -v -H "Content-Type: application/json" -X DELETE --url 127.0.0.1:5000/api/movies/{id}
```
DEMO:
```bash
C:\Windows\System32>curl -v -H "Content-Type: application/json" -X DELETE --url 127.0.0.1:5000/api/movies/6
*   Trying 127.0.0.1:5000...
* Connected to 127.0.0.1 (127.0.0.1) port 5000 (#0)
> DELETE /api/movies/6 HTTP/1.1
> Host: 127.0.0.1:5000
> User-Agent: curl/8.0.1
> Accept: */*
> Content-Type: application/json
>
< HTTP/1.1 204 NO CONTENT
< Server: Werkzeug/2.2.2 Python/3.8.10
< Date: Sun, 23 Apr 2023 17:16:07 GMT
< Content-Type: text/html; charset=utf-8
< Connection: close
<
* Closing connection 0
```