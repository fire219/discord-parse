# Configuration values used by parser

import os

# Location of discord export
EXPORT_DIR = os.path.join(os.getcwd(), "export")

# === MESSAGES ===

# You must have sent a message within the past N days to mark a guild as active.
# This is relative to the most recent logged telemetry event.
IS_ACTIVE_DAYS = 7

# === REPORT ===
DARK_THEME_BG_COLOUR = "#23272A"
DARK_THEME_COLOUR = "white"
DARK_THEME_TABLE = "white"
LIGHT_THEME_BG_COLOUR = "white"
LIGHT_THEME_COLOUR = "#23272A"
LIGHT_THEME_TABLE = "#23272A"