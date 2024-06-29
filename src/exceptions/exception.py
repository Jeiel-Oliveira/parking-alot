from pydantic import BaseModel
from starlette.responses import JSONResponse
from http.client import responses


class ErrorSchema(BaseModel):
    code: int
    status: str
    message: str


def http_exception_handler(_, exc):
    content = ErrorSchema(
        code=exc.status_code,
        message=exc.detail,
        status=responses[exc.status_code],
    ).model_dump(mode='json')

    return JSONResponse(content, status_code=exc.status_code)
