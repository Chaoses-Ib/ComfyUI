import asyncio
import json
import sys
import uuid
from typing import Optional

from .multi_event_tracker import MultiEventTracker
from .plausible import PlausibleTracker
from ..api.model.prompt import Prompt

_event_tracker: MultiEventTracker


def track_event(name: str, url: str = "app://comfyui", props: Optional[dict] = None):
    global _event_tracker
    # not awaited, we don't care about event tracking in terms of blocking
    _event_tracker.track_event(name, url, props=props)


def initialize_event_tracking(loop: asyncio.AbstractEventLoop):
    global _event_tracker
    _event_trackers = []
    # perform the imports at the time this is invoked to prevent side effects and ordering issues
    from ..cli_args import args

    identity = str(uuid.uuid4())
    if args.analytics_use_identity_provider and sys.platform == "nt":
        from .identity_provider_nt import get_user_name
        identity = get_user_name()

    if args.plausible_analytics_domain is not None and args.plausible_analytics_base_url is not None:
        _event_trackers.append(PlausibleTracker(loop, user_agent=identity, base_url=args.plausible_analytics_base_url,
                                                domain=args.plausible_analytics_domain))

    if len(_event_trackers) == 0:
        return

    _event_tracker = MultiEventTracker(_event_trackers)
    # patch nodes
    # for now, track SaveImage
    from ..nodes.base_nodes import SaveImage, KSampler, KSamplerAdvanced, CLIPTextEncode, LoraLoader, \
        CheckpointLoaderSimple
    save_images = SaveImage.save_images

    # todo: patch execution
    def save_images_tracked(self: SaveImage, *_args, **kwargs):
        if 'prompt' in kwargs:
            prompt = Prompt(**kwargs['prompt'])
            k_samplers = [prompt[k] for k in prompt.keys() if
                          prompt[k]["class_type"] in (KSampler.__name__, KSamplerAdvanced.__name__)]
            positive_prompt_ids = [k["inputs"]["positive"] for k in k_samplers]
            positive_prompt_ids = [key for (key, _) in positive_prompt_ids]
            negative_prompt_ids = [k["inputs"]["negative"] for k in k_samplers]
            negative_prompt_ids = [key for (key, _) in negative_prompt_ids]
            positive_prompts = "; ".join(frozenset(str(prompt[id]["inputs"]["text"]) for id in positive_prompt_ids if
                                                   prompt[id]["class_type"] == CLIPTextEncode.__name__))
            negative_prompts = "; ".join(frozenset(str(prompt[id]["inputs"]["text"]) for id in negative_prompt_ids if
                                                   prompt[id]["class_type"] == CLIPTextEncode.__name__))
            loras = "; ".join(frozenset(
                str(prompt[id]["inputs"]["lora_name"]) for id in prompt.keys() if prompt[id]["class_type"] == LoraLoader.__name__))
            checkpoints = "; ".join(frozenset(str(prompt[id]["inputs"]["ckpt_name"]) for id in prompt.keys() if
                                              prompt[id]["class_type"] == CheckpointLoaderSimple.__name__))
            prompt_str = json.dumps(kwargs['prompt'], separators=(',', ':'))
            len_prompt_str = len(prompt_str)
            prompt_str_pieces = []
            for i in range(0, len_prompt_str, 1000):
                prompt_str_pieces += [prompt_str[i:min(i + 2000, len_prompt_str)]]
            prompt_str_props = {}
            for i, prompt_str_piece in enumerate(prompt_str_pieces):
                prompt_str_props[f"prompt.{i}"] = prompt_str_piece
            track_event(SaveImage.__name__, props={
                "positive_prompts": positive_prompts,
                "negative_prompts": negative_prompts,
                "loras": loras,
                "checkpoints": checkpoints,
                **prompt_str_props
            })
        return save_images(self, *_args, **kwargs)

    SaveImage.save_images = save_images_tracked
