"""Dashboard page for Reel Forge video processing."""
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from src.theme import TITLE_STYLE, SUBTITLE_STYLE
from src.widgets import BigButtonBox, MacCard


class DashboardPage(QWidget):
    def __init__(self, client, parent=None):
        super().__init__(parent)
        self._client = client
        layout = QVBoxLayout(self)
        layout.setContentsMargins(32, 24, 32, 24)
        layout.setSpacing(24)
        header = QLabel("Dashboard")
        header.setStyleSheet(TITLE_STYLE)
        layout.addWidget(header)
        desc = QLabel("Encode, decode, and process video streams on Jetson AGX Orin.")
        desc.setStyleSheet(SUBTITLE_STYLE)
        layout.addWidget(desc)
        btn_row = QHBoxLayout()
        btn_row.setSpacing(20)
        self.encode_box = BigButtonBox("Start Encode", "Begin hardware-accelerated video encoding.\nConfigure codec and bitrate in Controls.", "▶  Encode", "primary")
        btn_row.addWidget(self.encode_box)
        self.decode_box = BigButtonBox("Start Decode", "Begin hardware-accelerated video decoding.\nConfigure input source in Controls.", "▶  Decode", "secondary")
        btn_row.addWidget(self.decode_box)
        self.stop_box = BigButtonBox("Stop All", "Halt all active encode/decode jobs.\nAll pipeline resources will be released.", "■  Stop All", "danger")
        btn_row.addWidget(self.stop_box)
        layout.addLayout(btn_row)
        cards_row = QHBoxLayout()
        cards_row.setSpacing(16)
        self.status_card = MacCard("Status", "Idle", "", "#616161")
        self.jobs_card = MacCard("Active Jobs", "0", "")
        self.bytes_card = MacCard("Processed", "0", "B")
        cards_row.addWidget(self.status_card)
        cards_row.addWidget(self.jobs_card)
        cards_row.addWidget(self.bytes_card)
        layout.addLayout(cards_row)
        layout.addStretch()
