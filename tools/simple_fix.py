import sys
import signal
# --- Start Monkeypatch for signal ---
# This section is necessary because directly references signal.SIGKILL in
# nemo.utils.exp_manager.FaultToleranceParams.rank_termination_signal
# during class definition as if linux, which causes an ImportError on Windows.
# We need to define a dummy SIGKILL attribute in the signal module *before*
# importing the NeMo module.
if sys.platform == "win32":
    # Check if SIGKILL is already defined (unlikely on standard Windows Python)
    if not hasattr(signal, 'SIGKILL'):
        # Define a dummy SIGKILL. Its actual integer value doesn't matter here
        # for the import to succeed, as long as the attribute exists.
        # Using CTRL_BREAK_EVENT value instead to pass the class definition check.
        signal.SIGKILL = signal.CTRL_BREAK_EVENT
        # Note: We could also potentially try to define it as a signal.Signals enum member
        # but setting a simple integer attribute is less complex and sufficient
        # to prevent the AttributeError during import.
# --- End Monkeypatch for signal ---

import nemo.collections.asr as nemo_asr
asr_model = nemo_asr.models.ASRModel.from_pretrained(model_name="nvidia/parakeet-tdt-0.6b-v2")

# wget https://dldata-public.s3.us-east-2.amazonaws.com/2086-149220-0033.wav

# output = asr_model.transcribe(['2086-149220-0033.wav'])
output = asr_model.transcribe(['test_audio.wav'])
print(output[0].text)

output = asr_model.transcribe(['test_audio.wav'], timestamps=True)
# by default, timestamps are enabled for char, word and segment level
word_timestamps = output[0].timestamp['word'] # word level timestamps for first sample
segment_timestamps = output[0].timestamp['segment'] # segment level timestamps
char_timestamps = output[0].timestamp['char'] # char level timestamps

for stamp in segment_timestamps:
    print(f"{stamp['start']}s - {stamp['end']}s : {stamp['segment']}")