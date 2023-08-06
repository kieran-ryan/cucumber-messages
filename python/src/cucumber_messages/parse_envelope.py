import json

import dacite

from .messages import (
    AttachmentContentEncoding,
    Envelope,
    PickleStepType,
    SourceMediaType,
    StepKeywordType,
    TestStepResultStatus,
)


def parse_envelope(json_: str) -> Envelope:
    plain = json.loads(json_)
    return dacite.from_dict(
        data_class=Envelope,
        data=plain,
        config=dacite.Config(
            type_hooks={
                TestStepResultStatus: TestStepResultStatus,
                PickleStepType: PickleStepType,
                SourceMediaType: SourceMediaType,
                StepKeywordType: StepKeywordType,
                AttachmentContentEncoding: AttachmentContentEncoding,
            },
        ),
    )
