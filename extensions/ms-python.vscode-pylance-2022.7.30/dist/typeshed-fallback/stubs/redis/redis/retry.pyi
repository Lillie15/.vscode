from collections.abc import Iterable

class Retry:
    def __init__(self, backoff, retries, supported_errors=...) -> None: ...
    def update_supported_errors(self, specified_errors: Iterable[Exception]) -> None: ...
    def call_with_retry(self, do, fail): ...
