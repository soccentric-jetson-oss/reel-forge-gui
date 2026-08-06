"""Reel Forge GUI - Main application window."""

from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton
)
from PySide6.QtCore import QTimer
from src.client.client import ReelForgeClient


class ReelForgeApp(QMainWindow):
    """Main application window for Reel Forge GUI."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Reel Forge")
        self.setMinimumSize(800, 500)
        self._client = ReelForgeClient()
        self._setup_ui()
        self._client.connect()
        self._update_status()

        self._timer = QTimer(self)
        self._timer.timeout.connect(self._refresh)
        self._timer.start(3000)

    def _setup_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        layout.setContentsMargins(20, 20, 20, 20)

        layout.addWidget(QLabel("Reel Forge — Video Processing"))

        # Action buttons
        btn_row = QHBoxLayout()
        self.encode_btn = QPushButton("▶ Start Encode (H264, 1080p)")
        self.encode_btn.clicked.connect(self._on_start_encode)
        self.decode_btn = QPushButton("▶ Start Decode (H264, 1080p)")
        self.decode_btn.clicked.connect(self._on_start_decode)
        self.stop_btn = QPushButton("■ Stop All")
        self.stop_btn.clicked.connect(self._on_stop_all)
        btn_row.addWidget(self.encode_btn)
        btn_row.addWidget(self.decode_btn)
        btn_row.addWidget(self.stop_btn)
        layout.addLayout(btn_row)

        # Status display
        self.status_label = QLabel("Status: Idle")
        self.status_label.setStyleSheet("color:#616161;")
        layout.addWidget(self.status_label)
        layout.addStretch()

    def _update_status(self):
        if self._client.connected:
            self.status_label.setText("Connected")
        else:
            self.status_label.setText("Disconnected")

    def _refresh(self):
        if not self._client.connected:
            self._client.connect()
            self._update_status()
            return
        status = self._client.get_status()
        self.status_label.setText(
            f"Active jobs: {status['active_jobs']} | "
            f"Processed: {status['bytes_processed']}B"
        )

    def _on_start_encode(self):
        result = self._client.start_encode()
        if result["success"]:
            self.status_label.setText(f"Encode: {result['job_id']}")
        else:
            self.status_label.setText(f"Error: {result['error']}")

    def _on_start_decode(self):
        result = self._client.start_decode()
        if result["success"]:
            self.status_label.setText(f"Decode: {result['job_id']}")
        else:
            self.status_label.setText(f"Error: {result['error']}")

    def _on_stop_all(self):
        self._client.stop_encode()
        self._client.stop_decode()
        self.status_label.setText("All stopped")
