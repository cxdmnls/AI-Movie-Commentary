"""
电影自动解说工作流 — 全局配置文件
所有模型路径、API密钥、处理参数统一在此管理
"""
import os

# ===== 路径配置 =====
# 项目根目录（自动检测）
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
WORKSPACE_DIR = os.path.join(PROJECT_ROOT, "workspace")
BGM_LIBRARY_DIR = os.path.join(PROJECT_ROOT, "bgm_library")
PROMPTS_DIR = os.path.join(PROJECT_ROOT, "prompts")

# ffmpeg 可执行文件路径（Windows 使用 imageio-ffmpeg）
import imageio_ffmpeg
FFMPEG_BIN = imageio_ffmpeg.get_ffmpeg_exe()
FFPROBE_BIN = FFMPEG_BIN.replace("ffmpeg", "ffprobe")

# ===== Whisper 配置 (M1 字幕提取) =====
WHISPER_MODEL_PATH = ""
WHISPER_MODEL_SIZE = "small"  # 可选: tiny/base/small/medium/large-v3
WHISPER_DEVICE = "cpu"  # GPU
WHISPER_COMPUTE_TYPE = "float32"  # CPU 使用 float32
WHISPER_VAD_FILTER = True  # 启用 VAD 过滤

# ===== 场景检测配置 (M2) =====
SCENE_THRESHOLD = 27.0  # ContentDetector 阈值，越低越敏感
SCENE_MIN_DURATION_SEC = 2.0  # 最短场景时长（秒）
SCENE_THUMBNAIL_WIDTH = 320  # 缩略图宽度

# ===== 信息采集配置 (M3) =====
TMDB_API_KEY = ""  # 需自行配置
TMDB_BASE_URL = "https://api.themoviedb.org/3"
OMDB_API_KEY = "thewdb"  # OMDb 公共测试 key，可替换为自有 key
OMDB_BASE_URL = "https://www.omdbapi.com/"
DOUBAN_HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
INFO_SEARCH_SOURCES = ["douban", "baidu_baike", "tmdb", "imdb_omdb"]  # 采集源优先级
M3_QWEN_MODEL = "qwen3.5-plus"  # M3 剧情增强模型
M3_SYNOPSIS_TARGET_CHARS = 1000  # 目标剧情梳理字数
M3_KEYSCENE_COUNT = 20  # 关键场景数量

# ===== 时间戳匹配配置 (M3 关键场景模式) =====
TIMESTAMP_MATCHER_WINDOW = 120  # 时间窗口（秒）
TIMESTAMP_MATCHER_THRESHOLD = 75  # 模糊匹配阈值（0-100）
TIMESTAMP_MIN_INTERVAL = 30  # 场景间最小间隔（秒）

# ===== LLM API 配置 (M4 剧本生成) — 唯一 API 调用 =====
DASHSCOPE_API_KEY = ""  # 替换为真实 key
QWEN_MODEL = "qwen-max"
QWEN_MAX_TOKENS = 8192
QWEN_TEMPERATURE = 0.7
SCRIPT_TARGET_DURATION_MIN = 20  # 目标解说时长（分钟）
SCRIPT_TARGET_WORDS = 7000  # 目标解说词字数（约 6000-8000 字 ≈ 20 分钟）
WORDS_PER_MINUTE = 350  # 中文语速：每分钟约 350 字
EMOTION_TYPES = ["平静", "紧张", "悲伤", "欢快", "震撼", "温馨", "悬疑"]

# ===== TTS 配置 (M5 语音合成) =====
COSYVOICE_MODEL_PATH = "/models/CosyVoice2-0.5B"
TTS_DEVICE = "cuda"
TTS_SAMPLE_RATE = 22050
TTS_DEFAULT_SPEED = 1.0
DEFAULT_VOICE_REF = ""  # 运行时通过 CLI 传入参考音频路径

# ===== BGM 配置 (M6) =====
BGM_VOLUME_DB = -15  # BGM 音量（相对人声，dB）
BGM_FADE_DURATION_SEC = 2.0  # 淡入淡出时长（秒）
BGM_SKIP_IF_EMPTY = True  # 曲库为空时自动跳过

# ===== 视频配置 (M7 裁切 / M8 合成) =====
OUTPUT_RESOLUTION = "1280:720"  # ffmpeg scale 格式
OUTPUT_FPS = 24
OUTPUT_VIDEO_CODEC = "libx264"
OUTPUT_AUDIO_CODEC = "aac"
OUTPUT_AUDIO_BITRATE = "192k"
OUTPUT_PRESET = "medium"  # ffmpeg 编码预设 (ultrafast/fast/medium/slow)
OUTPUT_CRF = 23  # 视频质量，越低越好（18-28 合理范围）
ORIGINAL_AUDIO_VOLUME = 0.1  # 原声保留比例，0 为完全静音
TRANSITION_DURATION_SEC = 0.5  # 片段间过渡时长（秒）

# ===== 日志配置 =====
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
