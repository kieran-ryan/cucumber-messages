import pathlib
import sys

TESTS_DIR = pathlib.Path(__file__).parent
sys.path.insert(0, str(TESTS_DIR / "../src"))

import cucumber_messages


def test_get_worst_test_step_result():
    result = cucumber_messages.get_worst_test_step_result(
        [
            cucumber_messages.TestStepResult(
                status=cucumber_messages.TestStepResultStatus.PASSED
            ),
            cucumber_messages.TestStepResult(
                status=cucumber_messages.TestStepResultStatus.FAILED
            ),
            cucumber_messages.TestStepResult(
                status=cucumber_messages.TestStepResultStatus.PASSED
            ),
        ]
    )

    assert result.status == cucumber_messages.TestStepResultStatus.FAILED
