# Define a class for your command-line arguments
import enum
from typing import Optional, List


class LatentPreviewMethod(enum.Enum):
    NoPreviews = "none"
    Auto = "auto"
    Latent2RGB = "latent2rgb"
    TAESD = "taesd"


class Configuration:
    config: Optional[str]
    cwd: Optional[str]
    listen: str
    port: int
    enable_cors_header: Optional[str]
    max_upload_size: float
    extra_model_paths_config: Optional[List[str]]
    output_directory: Optional[str]
    temp_directory: Optional[str]
    input_directory: Optional[str]
    auto_launch: bool
    disable_auto_launch: bool
    cuda_device: Optional[int]
    cuda_malloc: bool
    disable_cuda_malloc: bool
    dont_upcast_attention: bool
    force_fp32: bool
    force_fp16: bool
    bf16_unet: bool
    fp16_unet: bool
    fp8_e4m3fn_unet: bool
    fp8_e5m2_unet: bool
    fp16_vae: bool
    fp32_vae: bool
    bf16_vae: bool
    cpu_vae: bool
    fp8_e4m3fn_text_enc: bool
    fp8_e5m2_text_enc: bool
    fp16_text_enc: bool
    fp32_text_enc: bool
    directml: Optional[int]
    disable_ipex_optimize: bool
    preview_method: LatentPreviewMethod
    use_split_cross_attention: bool
    use_quad_cross_attention: bool
    use_pytorch_cross_attention: bool
    disable_xformers: bool
    gpu_only: bool
    highvram: bool
    normalvram: bool
    lowvram: bool
    novram: bool
    cpu: bool
    disable_smart_memory: bool
    deterministic: bool
    dont_print_server: bool
    quick_test_for_ci: bool
    windows_standalone_build: bool
    disable_metadata: bool
    multi_user: bool
    plausible_analytics_base_url: Optional[str]
    plausible_analytics_domain: Optional[str]
    analytics_use_identity_provider: bool

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
