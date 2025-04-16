{
    "scope": {
        "type": "http",
        "asgi": {
            "version": "3.0",
            "spec_version": "2.3"
        },
        "http_version": "1.1",
        "server": ("127.0.0.1", 8000),
        "client": ("127.0.0.1", 60667),
        "scheme": "http",
        "method": "GET",
        "root_path": "",
        "path": "/google/callback",
        "raw_path": b"/google/callback",
        "query_string": b"code=4%2F0Ab_5qlnFLUw3oqXfuju0NC5JbKGLdMUNwsryseK-D43lMlrC2ciYqGH4MY8KJ4NE9KfiEA&scope=email+profile+openid+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email&authuser=0&prompt=consent",
        "headers": [
            (b"host", b"localhost:8000"),
            (b"connection", b"keep-alive"),
            (b"cache-control", b"max-age=0"),
            (b"upgrade-insecure-requests", b"1"),
            (b"user-agent", b"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"),
            (b"accept", b"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8"),
            (b"sec-gpc", b"1"),
            (b"accept-language", b"en-US,en;q=0.9"),
            (b"sec-fetch-site", b"cross-site"),
            (b"sec-fetch-mode", b"navigate"),
            (b"sec-fetch-user", b"?1"),
            (b"sec-fetch-dest", b"document"),
            (b"sec-ch-ua", b'"Not A(Brand";v="8", "Chromium";v="132", "Brave";v="132"'),
            (b"sec-ch-ua-mobile", b"?0"),
            (b"sec-ch-ua-platform", b'"macOS"'),
            (b"accept-encoding", b"gzip, deflate, br, zstd"),
            (b"cookie", b"token=your_token_value; csrftoken=your_csrf_token_value; sessionid=your_session_id; session=your_session_value")
        ],
        "state": {},
        "app": "<fastapi.applications.FastAPI object at 0x104dd9940>",
        "starlette.exception_handlers": (
            {
                "<class 'starlette.exceptions.HTTPException'>": "<function http_exception_handler at 0x1049ac900>",
                "<class 'starlette.exceptions.WebSocketException'>": "<bound method ExceptionMiddleware.websocket_exception of <starlette.middleware.exceptions.ExceptionMiddleware object at 0x104ddb0e0>>",
                "<class 'fastapi.exceptions.RequestValidationError'>": "<function request_validation_exception_handler at 0x1049acae0>",
                "<class 'fastapi.exceptions.WebSocketRequestValidationError'>": "<function websocket_request_validation_exception_handler at 0x1049acb80>"
            },
            {}
        ),
        "router": "<fastapi.routing.APIRouter object at 0x104d539d0>",
        "endpoint": "<function google_callback at 0x104e6c040>",
        "path_params": {},
        "route": "APIRoute(path='/google/callback', name='google_callback', methods=['GET'])"
    },
    "_receive": "<bound method RequestResponseCycle.receive of <uvicorn.protocols.http.h11_impl.RequestResponseCycle object at 0x104de6ea0>>",
    "_send": "<function wrap_app_handling_exceptions.<locals>.wrapped_app.<locals>.sender at 0x104e6c4a0>",
    "_stream_consumed": False,
    "_is_disconnected": False,
    "_form": None,
    "_query_params": "QueryParams('code=REDACTED_CODE&scope=email+profile+openid+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email&authuser=0&prompt=consent')",
    "_headers": "Headers({'host': 'localhost:8000', 'connection': 'keep-alive', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8', 'sec-gpc': '1', 'accept-language': 'en-US,en;q=0.9', 'sec-fetch-site': 'cross-site', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'sec-ch-ua': '\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\", \"Brave\";v=\"132\"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '\"macOS\"', 'accept-encoding': 'gzip, deflate, br, zstd', 'cookie': 'token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImJlODM1ZTQyLWRhNGItNDg5NC05NzczLWMyYmFlZmJhMTliYSJ9.L2yV8_zb2g6hjGGLGuxxgT4YiOk4Zzt2oAlpRAON5kI; csrftoken=reEJh3vHLgq7m5OA1tCs8JbKnxDcT57l; sessionid=ciyu15dkod8ndd13ciqc81uokmjrmleh; session=eyJpZCI6ICI4NWExZDVlNy02Y2NmLTQ5ZjQtOTJjYi0yMjUyMWM3ODc0OTMifQ==.Z_T9vA.CZ0eAYuGHLv4t4KyNXNLrhbbnds'})",
    "_cookies": {
        "token": "your_token_value",
        "csrftoken": "your_csrf_token_value",
        "sessionid": "your_session_id",
        "session": "your_session_value"
    },
}