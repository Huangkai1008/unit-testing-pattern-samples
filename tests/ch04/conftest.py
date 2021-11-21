import pytest

from samples.ch04.message_render import MessageRender


@pytest.fixture
def message_render() -> MessageRender:
    return MessageRender()
