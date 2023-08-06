from .messages import TestStepResult, TestStepResultStatus
from .time_conversion import milliseconds_to_duration


def get_worst_test_step_result(
    test_step_results: list[TestStepResult],
) -> TestStepResult:
    sorted_results = sorted(test_step_results, key=lambda r: ordinal(r.status) * -1)

    if sorted_results:
        return sorted_results[0]
    else:
        return TestStepResult(TestStepResultStatus.UNKNOWN, milliseconds_to_duration(0))


def ordinal(status) -> int:
    return [
        TestStepResultStatus.UNKNOWN,
        TestStepResultStatus.PASSED,
        TestStepResultStatus.SKIPPED,
        TestStepResultStatus.PENDING,
        TestStepResultStatus.UNDEFINED,
        TestStepResultStatus.AMBIGUOUS,
        TestStepResultStatus.FAILED,
    ].index(status)
