import re


__item__ = "Amazon Web Services Web Application Firewall (Amazon)"


def detect(content, **kwargs):
    headers = kwargs.get("headers", None)
    content = str(content)
    detection_schema = (
        re.compile(r"<RequestId>[0-9a-zA-Z]{16,25}<.RequestId>", re.I),
        re.compile(r"<Error><Code>AccessDenied<.Code>", re.I),
        re.compile(r"\bAWS", re.I),
        re.compile(r"x.amz.id.\d+", re.I),
        re.compile(r"x.amz.request.id", re.I)
    )
    for detection in detection_schema:
        if detection.search(content) is not None:
            return True
        elif detection.search(str(headers)) is not None:
            return True
