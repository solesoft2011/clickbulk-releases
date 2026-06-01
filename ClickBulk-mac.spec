# PyInstaller spec for ClickBulk — macOS .app bundle
# Build: pyinstaller ClickBulk-mac.spec --noconfirm
#
# Output: dist/ClickBulk.app  (drag to /Applications or zip and ship)
# -*- mode: python ; coding: utf-8 -*-
import os
import sys

block_cipher = None
APP_NAME     = "ClickBulk"
ICON_PATH    = os.path.join("src", "clickbulk", "resources", "icons", "icon.icns")

a = Analysis(
    ["app.py"],
    pathex=[os.path.abspath("src")],
    binaries=[],
    datas=[
        ("src/clickbulk/resources", "clickbulk/resources"),
    ],
    hiddenimports=[
        # yt-dlp
        "yt_dlp",
        "yt_dlp.extractor",
        "yt_dlp.extractor.youtube",
        "yt_dlp.extractor.tiktok",
        "yt_dlp.extractor.twitter",
        "yt_dlp.extractor.instagram",
        "yt_dlp.extractor.facebook",
        "yt_dlp.extractor.dailymotion",
        "yt_dlp.extractor.soundcloud",
        "yt_dlp.extractor.flickr",
        "yt_dlp.extractor.twitch",
        "yt_dlp.extractor.vimeo",
        "yt_dlp.extractor.googledrive",
        "yt_dlp.postprocessor",
        # openpyxl
        "openpyxl",
        "openpyxl.styles",
        "openpyxl.drawing",
        "openpyxl.drawing.image",
        "openpyxl.utils",
        # requests
        "requests",
        # PyQt6
        "PyQt6",
        "PyQt6.QtCore",
        "PyQt6.QtGui",
        "PyQt6.QtWidgets",
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=[
        "tkinter", "PyQt5", "PySide2", "PySide6",
        "matplotlib", "numpy", "scipy", "pandas",
        "IPython", "jupyter",
        # Windows-only — not needed on macOS
        "comtypes",
    ],
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name=APP_NAME,
    icon=ICON_PATH if os.path.isfile(ICON_PATH) else None,
    console=False,
    disable_windowed_traceback=False,
    bootloader_ignore_signals=False,
    upx=False,
    strip=False,
    debug=False,
    # macOS: don't open a Terminal window
    argv_emulation=False,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    name=APP_NAME,
    upx=False,
    strip=False,
)

# ── macOS .app bundle ──────────────────────────────────────────────────────────
app = BUNDLE(
    coll,
    name=f"{APP_NAME}.app",
    icon=ICON_PATH if os.path.isfile(ICON_PATH) else None,
    bundle_identifier="net.clickbulk.app",
    info_plist={
        "CFBundleName":              APP_NAME,
        "CFBundleDisplayName":       APP_NAME,
        "CFBundleVersion":           "3.4.2",
        "CFBundleShortVersionString":"3.4.2",
        "CFBundleIdentifier":        "net.clickbulk.app",
        "NSHighResolutionCapable":   True,
        "NSHumanReadableCopyright":  "© 2025 ClickBulk",
        # Allow downloads to ~/Downloads without extra permission prompts
        "NSDocumentsFolderUsageDescription": "ClickBulk saves downloaded files here.",
        "NSDownloadsFolderUsageDescription": "ClickBulk saves downloaded files here.",
    },
)
