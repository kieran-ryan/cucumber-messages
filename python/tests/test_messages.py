import pathlib
import sys

TESTS_DIR = pathlib.Path(__file__).parent
sys.path.insert(0, str(TESTS_DIR / "../src"))

import cucumber_messages

partial = """
{
    "gherkin_document": {
        "feature": {
            "children": [
                {
                    "scenario": {
                        "id": "1",
                        "keyword": "Scenario",
                        "location": {"column": 3, "line": 3},
                        "name": "minimalistic",
                        "steps": [
                            {
                                "id": "0",
                                "keyword": "Given ",
                                "keyword_type": "Context",
                                "location": {"column": 5, "line": 4},
                                "text": "the minimalism"
                            }
                        ]
                    }
                }
            ],
            "keyword": "Feature",
            "language": "en",
            "location": {"column": 1, "line": 1},
            "name": "Minimal"
        },
        "uri": "testdata/good/minimal.feature"
    }
}
"""


def test_envelope():
    expected_envelope = cucumber_messages.Envelope(
        gherkin_document=cucumber_messages.GherkinDocument(
            feature=cucumber_messages.Feature(
                children=[
                    cucumber_messages.FeatureChild(
                        scenario=cucumber_messages.Scenario(
                            id="1",
                            keyword="Scenario",
                            location=cucumber_messages.Location(column=3, line=3),
                            name="minimalistic",
                            steps=[
                                cucumber_messages.Step(
                                    id="0",
                                    keyword="Given ",
                                    keyword_type=cucumber_messages.StepKeywordType.CONTEXT,
                                    location=cucumber_messages.Location(
                                        column=5, line=4
                                    ),
                                    text="the minimalism",
                                )
                            ],
                        )
                    )
                ],
                keyword="Feature",
                language="en",
                location=cucumber_messages.Location(column=1, line=1),
                name="Minimal",
            ),
            uri="testdata/good/minimal.feature",
        )
    )

    envelope = cucumber_messages.parse_envelope(partial)

    assert (
        expected_envelope.gherkin_document.feature.children[0]
        == envelope.gherkin_document.feature.children[0]
    )
