from __future__ import annotations  # for Python 3.7-3.9

import typing
from typing import Optional, Literal, Protocol, TypeAlias, Union, NamedTuple, List

import PIL.Image
from typing_extensions import NotRequired, TypedDict

from .queue_types import BinaryEventTypes
from ..nodes.package_typing import InputTypeSpec


class ExecInfo(TypedDict):
    queue_remaining: int


class QueueInfo(TypedDict):
    exec_info: ExecInfo


class StatusMessage(TypedDict):
    status: QueueInfo
    sid: NotRequired[str]


class ExecutingMessage(TypedDict):
    node: str | None
    prompt_id: NotRequired[str]
    output: NotRequired[dict]
    sid: NotRequired[str]


class ProgressMessage(TypedDict):
    value: float
    max: float
    prompt_id: Optional[str]
    node: Optional[str]
    sid: NotRequired[str]
    output: NotRequired[dict]


class UnencodedPreviewImageMessage(NamedTuple):
    format: Literal["JPEG", "PNG"]
    pil_image: PIL.Image.Image
    max_size: int = 512


ExecutedMessage: TypeAlias = ExecutingMessage

SendSyncEvent: TypeAlias = Union[Literal["status", "executing", "progress", "executed"], BinaryEventTypes, None]

SendSyncData: TypeAlias = Union[StatusMessage, ExecutingMessage, ProgressMessage, UnencodedPreviewImageMessage, bytes, bytearray, str, None]


class ExecutorToClientProgress(Protocol):
    """
    Specifies the interface for the dependencies a prompt executor needs from a server.

    Attributes:
        client_id (Optional[str]): the client ID that this object collects feedback for
        last_node_id: (Optional[str]): the most recent node that was processed by the executor
        last_prompt_id: (Optional[str]): the most recent prompt that was processed by the executor
    """

    client_id: Optional[str]
    last_node_id: Optional[str]
    last_prompt_id: Optional[str]
    receive_all_progress_notifications: Optional[bool]

    def send_sync(self,
                  event: SendSyncEvent,
                  data: SendSyncData,
                  sid: Optional[str] = None):
        """
        Sends feedback to the client with the specified ID about a specific node

        :param event: a string event name, BinaryEventTypes.UNENCODED_PREVIEW_IMAGE, BinaryEventTypes.PREVIEW_IMAGE, 0 (?) or None
        :param data: a StatusMessage dict when the event is status; an ExecutingMessage dict when the status is executing, binary bytes with a binary event type, or nothing
        :param sid: websocket ID / the client ID to be responding to
        :return:
        """
        pass

    def queue_updated(self, queue_remaining: Optional[int] = None):
        """
        Indicates that the local client's queue has been updated
        :return:
        """
        pass


ExceptionTypes = Literal["custom_validation_failed", "value_not_in_list", "value_bigger_than_max", "value_smaller_than_min", "invalid_input_type", "exception_during_inner_validation", "return_type_mismatch", "bad_linked_input", "required_input_missing", "invalid_prompt", "prompt_no_outputs", "exception_during_validation", "prompt_outputs_failed_validation"]


class ValidationErrorExtraInfoDict(TypedDict, total=False):
    exception_type: NotRequired[str]
    traceback: NotRequired[List[str]]
    dependent_outputs: NotRequired[List[str]]
    class_type: NotRequired[str]
    input_name: NotRequired[str]
    input_config: NotRequired[typing.Dict[str, InputTypeSpec]]
    received_value: NotRequired[typing.Any]
    linked_node: NotRequired[str]
    traceback: NotRequired[str]
    exception_message: NotRequired[str]
    exception_type: NotRequired[str]


class ValidationErrorDict(TypedDict):
    type: str
    message: str
    details: str
    extra_info: list[typing.Never] | ValidationErrorExtraInfoDict


class NodeErrorsDictValue(TypedDict, total=False):
    dependent_outputs: NotRequired[List[str]]
    errors: List[ValidationErrorDict]
    class_type: str


class ValidationTuple(typing.NamedTuple):
    valid: bool
    error: Optional[ValidationErrorDict]
    good_output_node_ids: List[str]
    node_errors: list[typing.Never] | typing.Dict[str, NodeErrorsDictValue]


class ValidateInputsTuple(typing.NamedTuple):
    valid: bool
    errors: List[ValidationErrorDict]
    unique_id: str
