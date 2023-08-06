from __future__ import annotations

import dataclasses
import enum
from typing import List, Union


@dataclasses.dataclass
class UndefinedParameterType:
    expression: str = ""
    name: str = ""


@dataclasses.dataclass
class Timestamp:
    seconds: int = 0
    nanos: int = 0


@dataclasses.dataclass
class TestStepStarted:
    test_case_started_id: str = ""
    test_step_id: str = ""
    timestamp: Timestamp = dataclasses.field(default_factory=Timestamp)


@dataclasses.dataclass
class Duration:
    seconds: int = 0
    nanos: int = 0


class TestStepResultStatus(str, enum.Enum):
    UNKNOWN = "UNKNOWN"
    PASSED = "PASSED"
    SKIPPED = "SKIPPED"
    PENDING = "PENDING"
    UNDEFINED = "UNDEFINED"
    AMBIGUOUS = "AMBIGUOUS"
    FAILED = "FAILED"


@dataclasses.dataclass
class TestStepResult:
    duration: Duration = dataclasses.field(default_factory=Duration)
    message: Union[str, None] = None
    status: TestStepResultStatus = TestStepResultStatus.UNKNOWN
    exception: Union[Exception, None] = None


@dataclasses.dataclass
class TestStepFinished:
    test_case_started_id: str = ""
    test_step_id: str = ""
    test_step_result: TestStepResult = dataclasses.field(default_factory=TestStepResult)
    timestamp: Timestamp = dataclasses.field(default_factory=Timestamp)


@dataclasses.dataclass
class TestRunStarted:
    timestamp: Timestamp = dataclasses.field(default_factory=Timestamp)


@dataclasses.dataclass
class TestRunFinished:
    message: Union[str, None] = None
    success: bool = False
    timestamp: Timestamp = dataclasses.field(default_factory=Timestamp)
    exception: Union[Exception, None] = None


@dataclasses.dataclass
class TestCaseStarted:
    attempt: int = 0
    id: str = ""
    test_case_id: str = ""
    worker_id: Union[str, None] = None
    timestamp: Timestamp = dataclasses.field(default_factory=Timestamp)


@dataclasses.dataclass
class TestCaseFinished:
    test_case_started_id: str = ""
    timestamp: Timestamp = dataclasses.field(default_factory=Timestamp)
    will_be_retried: bool = False


@dataclasses.dataclass
class Group:
    children: List[Group] = dataclasses.field(default_factory=list)
    start: Union[int, None] = None
    value: Union[str, None] = None


@dataclasses.dataclass
class StepMatchArgument:
    group: Group = dataclasses.field(default_factory=Group)
    parameter_type_name: Union[str, None] = None


@dataclasses.dataclass
class StepMatchArgumentsList:
    step_match_arguments: List[StepMatchArgument] = dataclasses.field(
        default_factory=list
    )


@dataclasses.dataclass
class TestStep:
    hook_id: Union[str, None] = None
    id: str = ""
    pickle_step_id: Union[str, None] = None
    step_definition_ids: Union[List[str], None] = None
    step_match_arguments_lists: Union[List[StepMatchArgumentsList], None] = None


@dataclasses.dataclass
class TestCase:
    id: str = ""
    pickle_id: str = ""
    test_steps: List[TestStep] = dataclasses.field(default_factory=list)


class StepDefinitionPatternType(str, enum.Enum):
    CUCUMBER_EXPRESSION = "CUCUMBER_EXPRESSION"
    REGULAR_EXPRESSION = "REGULAR_EXPRESSION"


@dataclasses.dataclass
class StepDefinitionPattern:
    source: str = ""
    type: StepDefinitionPatternType = StepDefinitionPatternType.CUCUMBER_EXPRESSION


@dataclasses.dataclass
class JavaStackTraceElement:
    class_name: str = ""
    file_name: str = ""
    method_name: str = ""


@dataclasses.dataclass
class JavaMethod:
    class_name: str = ""
    method_name: str = ""
    method_parameter_types: List[str] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class Location:
    line: int = 0
    column: Union[int, None] = None


@dataclasses.dataclass
class SourceReference:
    uri: Union[str, None] = None
    java_method: Union[JavaMethod, None] = None
    java_stack_trace_element: Union[JavaStackTraceElement, None] = None
    location: Union[Location, None] = None


@dataclasses.dataclass
class StepDefinition:
    id: str = ""
    pattern: StepDefinitionPattern = dataclasses.field(
        default_factory=StepDefinitionPattern
    )
    source_reference: SourceReference = dataclasses.field(
        default_factory=SourceReference
    )


class SourceMediaType(str, enum.Enum):
    TEXT_X_CUCUMBER_GHERKIN_PLAIN = "text/x.cucumber.gherkin+plain"
    TEXT_X_CUCUMBER_GHERKIN_MARKDOWN = "text/x.cucumber.gherkin+markdown"


@dataclasses.dataclass
class Source:
    uri: str = ""
    data: str = ""
    media_type: SourceMediaType = SourceMediaType.TEXT_X_CUCUMBER_GHERKIN_PLAIN


@dataclasses.dataclass
class PickleTag:
    name: str = ""
    ast_node_id: str = ""


@dataclasses.dataclass
class PickleTableCell:
    value: str = ""


@dataclasses.dataclass
class PickleTableRow:
    cells: List[PickleTableCell] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class PickleTable:
    rows: List[PickleTableRow] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class PickleDocString:
    media_type: Union[str, None] = None
    content: str = ""


@dataclasses.dataclass
class PickleStepArgument:
    doc_string: Union[PickleDocString, None] = None
    data_table: Union[PickleTable, None] = None


class PickleStepType(str, enum.Enum):
    UNKNOWN = "Unknown"
    CONTEXT = "Context"
    ACTION = "Action"
    OUTCOME = "Outcome"


@dataclasses.dataclass
class PickleStep:
    argument: Union[PickleStepArgument, None] = None
    ast_node_ids: List[str] = dataclasses.field(default_factory=list)
    id: str = ""
    type: Union[PickleStepType, None] = None
    text: str = ""


@dataclasses.dataclass
class Pickle:
    id: str = ""
    uri: str = ""
    name: str = ""
    language: str = ""
    steps: List[PickleStep] = dataclasses.field(default_factory=list)
    tags: List[PickleTag] = dataclasses.field(default_factory=list)
    ast_node_ids: List[str] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class ParseError:
    source: SourceReference = dataclasses.field(default_factory=SourceReference)
    message: str = ""


@dataclasses.dataclass
class ParameterType:
    name: str = ""
    regular_expressions: List[str] = dataclasses.field(default_factory=list)
    prefer_for_regular_expression_match: bool = False
    use_for_snippets: bool = False
    id: str = ""
    source_reference: Union[SourceReference, None] = None


@dataclasses.dataclass
class Product:
    name: str = ""
    version: Union[str, None] = None


@dataclasses.dataclass
class Git:
    remote: str = ""
    revision: str = ""
    branch: Union[str, None] = None
    tag: Union[str, None] = None


@dataclasses.dataclass
class Ci:
    name: str = ""
    url: Union[str, None] = None
    build_number: Union[str, None] = None
    git: Union[Git, None] = None


@dataclasses.dataclass
class Meta:
    protocol_version: str = ""
    implementation: Product = dataclasses.field(default_factory=Product)
    runtime: Product = dataclasses.field(default_factory=Product)
    os: Product = dataclasses.field(default_factory=Product)
    cpu: Product = dataclasses.field(default_factory=Product)
    ci: Union[Ci, None] = None


@dataclasses.dataclass
class Hook:
    id: str = ""
    name: Union[str, None] = None
    source_reference: SourceReference = dataclasses.field(
        default_factory=SourceReference
    )
    tag_expression: Union[str, None] = None


@dataclasses.dataclass
class Tag:
    location: Location = dataclasses.field(default_factory=Location)
    name: str = ""
    id: str = ""


@dataclasses.dataclass
class TableCell:
    location: Location = dataclasses.field(default_factory=Location)
    value: str = ""


@dataclasses.dataclass
class TableRow:
    location: Location = dataclasses.field(default_factory=Location)
    cells: List[TableCell] = dataclasses.field(default_factory=list)
    id: str = ""


@dataclasses.dataclass
class DocString:
    location: Location = dataclasses.field(default_factory=Location)
    media_type: Union[str, None] = None
    content: str = ""
    delimiter: str = ""


@dataclasses.dataclass
class DataTable:
    location: Location = dataclasses.field(default_factory=Location)
    rows: List[TableRow] = dataclasses.field(default_factory=list)


class StepKeywordType(str, enum.Enum):
    UNKNOWN = "Unknown"
    CONTEXT = "Context"
    ACTION = "Action"
    OUTCOME = "Outcome"
    CONJUNCTION = "Conjunction"


@dataclasses.dataclass
class Step:
    location: Location = dataclasses.field(default_factory=Location)
    keyword: str = ""
    keyword_type: Union[StepKeywordType, None] = None
    text: str = ""
    doc_string: Union[DocString, None] = None
    data_table: Union[DataTable, None] = None
    id: str = ""


@dataclasses.dataclass
class Examples:
    location: Location = dataclasses.field(default_factory=Location)
    tags: List[Tag] = dataclasses.field(default_factory=list)
    keyword: str = ""
    name: str = ""
    description: str = ""
    table_header: Union[TableRow, None] = None
    table_body: List[TableRow] = dataclasses.field(default_factory=list)
    id: str = ""


@dataclasses.dataclass
class Scenario:
    location: Location = dataclasses.field(default_factory=Location)
    tags: List[Tag] = dataclasses.field(default_factory=list)
    keyword: str = ""
    name: str = ""
    description: str = ""
    steps: List[Step] = dataclasses.field(default_factory=list)
    examples: List[Examples] = dataclasses.field(default_factory=list)
    id: str = ""


@dataclasses.dataclass
class Background:
    location: Location = dataclasses.field(default_factory=Location)
    keyword: str = ""
    name: str = ""
    description: str = ""
    steps: List[Step] = dataclasses.field(default_factory=list)
    id: str = ""


@dataclasses.dataclass
class RuleChild:
    background: Union[Background, None] = None
    scenario: Union[Scenario, None] = None


@dataclasses.dataclass
class Rule:
    location: Location = dataclasses.field(default_factory=Location)
    tags: List[Tag] = dataclasses.field(default_factory=list)
    keyword: str = ""
    name: str = ""
    description: str = ""
    children: List[RuleChild] = dataclasses.field(default_factory=list)
    id: str = ""


@dataclasses.dataclass
class FeatureChild:
    rule: Union[Rule, None] = None
    background: Union[Background, None] = None
    scenario: Union[Scenario, None] = None


@dataclasses.dataclass
class Feature:
    location: Location = dataclasses.field(default_factory=Location)
    tags: List[Tag] = dataclasses.field(default_factory=list)
    language: str = ""
    keyword: str = ""
    name: str = ""
    description: str = ""
    children: List[FeatureChild] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class Comment:
    location: Location = dataclasses.field(default_factory=Location)
    text: str = ""


@dataclasses.dataclass
class GherkinDocument:
    uri: Union[str, None] = None
    feature: Union[Feature, None] = None
    comments: List[Comment] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class Exception:
    type: str = ""
    message: Union[str, None] = None


class AttachmentContentEncoding(str, enum.Enum):
    IDENTITY = "IDENTITY"
    BASE64 = "BASE64"


@dataclasses.dataclass
class Attachment:
    body: str = ""
    content_encoding: AttachmentContentEncoding = AttachmentContentEncoding.IDENTITY
    file_name: Union[str, None] = None
    media_type: str = ""
    source: Union[Source, None] = None
    test_case_started_id: Union[str, None] = None
    test_step_id: Union[str, None] = None
    url: Union[str, None] = None


@dataclasses.dataclass
class Envelope:
    attachment: Union[Attachment, None] = None
    gherkin_document: Union[GherkinDocument, None] = None
    hook: Union[Hook, None] = None
    meta: Union[Meta, None] = None
    parameter_type: Union[ParameterType, None] = None
    parse_error: Union[ParseError, None] = None
    pickle: Union[Pickle, None] = None
    source: Union[Source, None] = None
    step_definition: Union[StepDefinition, None] = None
    test_case: Union[TestCase, None] = None
    test_case_finished: Union[TestCaseFinished, None] = None
    test_case_started: Union[TestCaseStarted, None] = None
    test_run_finished: Union[TestRunFinished, None] = None
    test_run_started: Union[TestRunStarted, None] = None
    test_step_finished: Union[TestStepFinished, None] = None
    test_step_started: Union[TestStepStarted, None] = None
    undefined_parameter_type: Union[UndefinedParameterType, None] = None
