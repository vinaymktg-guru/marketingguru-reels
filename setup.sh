#!/usr/bin/env bash
# One-time setup in a fresh session: python deps + Kokoro voice model (from GitHub releases).
set -e
cd "$(dirname "$0")"
pip install --break-system-packages -q kokoro-onnx soundfile scipy pillow numpy 2>&1 | grep -v -i warning || true
mkdir -p models
[ -s models/kokoro.onnx ] || curl -sSL -o models/kokoro.onnx https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.int8.onnx
[ -s models/voices-v1.0.bin ] || curl -sSL -o models/voices-v1.0.bin https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin
which ffmpeg >/dev/null || { echo "ffmpeg missing"; exit 1; }
python3 -c "import kokoro_onnx, soundfile, scipy; print('setup ok')"
