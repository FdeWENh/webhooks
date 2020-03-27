import json

import pytest

from bitbucket_webhooks_router import _exceptions
from bitbucket_webhooks_router import decorators
from bitbucket_webhooks_router import router


@decorators.handle_repo_push
def _repo_push_handler(event):
    assert event.repository.name == "webhook-test-project"
    return 1


def test_repo_push_router():
    with open("tests/sample_data/repo_push.json") as f:
        data = json.load(f)
    assert router.route("repo:push", data) == [1]


def test_no_handler_error():
    with pytest.raises(_exceptions.NoHandlerError):
        router.route("random:event", {})
