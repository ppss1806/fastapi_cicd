from fastapi import APIRouter

from fastapi_cicd.web.api.echo.schema import Message

router = APIRouter()


@router.post("/", response_model=Message)
async def send_echo_message(
    incoming_message: Message,
) -> Message:
    """
    Send echo back to user.

    :param incoming_message: incoming message.
    :returns: message same as the incoming.
    """
    return incoming_message


@router.get("/")
async def echo_hello_world() -> Message:
    """
    Say hi to user.

    :param
    :returns: message same as the incoming.
    """
    return Message(message="hello world")
