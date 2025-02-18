from .nodes import *
from .experimental_temperature import ExperimentalTemperaturePatchSDXL,ExperimentalTemperaturePatchSD15
# from .nodes_sag_custom import * 

NODE_CLASS_MAPPINGS = {
    "Automatic CFG": simpleDynamicCFG,
    "Automatic CFG - Negative": simpleDynamicCFGlerpUncond,
    "Automatic CFG - Warp Drive": simpleDynamicCFGwarpDrive,
    "Automatic CFG - Preset Loader": presetLoader,
    "Automatic CFG - Excellent attention": simpleDynamicCFGExcellentattentionPatch,
    "Automatic CFG - Advanced": advancedDynamicCFG,
    "Automatic CFG - Post rescale only": postCFGrescaleOnly,
    "Automatic CFG - Custom attentions": simpleDynamicCFGCustomAttentionPatch,
    "Automatic CFG - Attention modifiers": attentionModifierParametersNode,
    "Automatic CFG - Attention modifiers tester": attentionModifierBruteforceParametersNode,
    "Automatic CFG - Unpatch function": simpleDynamicCFGunpatch,
    "Temperature settings SDXL": ExperimentalTemperaturePatchSDXL,
    "Temperature settings SD 1.5": ExperimentalTemperaturePatchSD15,
    # "SAG delayed activation": SelfAttentionGuidanceCustom,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Automatic CFG - Unpatch function": "Automatic CFG - Unpatch function(Deprecated)",
}
