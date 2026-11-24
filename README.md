# mirror
Small Python script that runs a server for debugging

## Why does this exist?
As I was writing a HTTP Client, I wanted to know what was arriving at the server. 

This is the simplest solution I came up with. Simply run the python script and watch incoming requests.

It also echoes received requests back to the client.

## Cloning & Usage
```bash
git clone https://github.com/shawarma10/mirror
cd mirror
python3 mirror.py
```

## Examples
I am using my own HTTP CLI Client written in Rust here. It's called [rfetch](https://github.com/shawarma10/rfetch).

### Output from the server
```console
[2026-11-24T22:44:22] 127.0.0.1:55596
GET / HTTP/1.1
user-agent: rfetch/1.6.2
accept: */*
host: localhost:8000
```

### Output from the client
```console
Status: 200 OK
Headers:
server: BaseHTTP/0.6 Python/3.14.10
date: Tue, 24 Nov 2026 21:44:22 GMT
content-type: text/plain; charset=utf-8
content-length: 73

Body:
GET / HTTP/1.1
user-agent: rfetch/1.6.2
accept: */*
host: localhost:8000
```
