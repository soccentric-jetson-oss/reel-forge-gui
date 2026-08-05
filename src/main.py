import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt, QTimer
import grpc
from src.client import reel_forge_pb2, reel_forge_pb2_grpc

class ReelForgeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Reel Forge")
        self.setMinimumSize(800, 500)
        self.stub = None
        self._setup_ui()
        self._connect()
        QTimer(self).timeout.connect(self._refresh)
        QTimer(self).start(3000)

    def _setup_ui(self):
        w = QWidget(); self.setCentralWidget(w)
        l = QVBoxLayout(w); l.setContentsMargins(20,20,20,20)
        l.addWidget(QLabel("Reel Forge — Video Processing"))
        r = QHBoxLayout()
        self.encode_btn = QPushButton("▶ Start Encode (H264, 1080p)")
        self.encode_btn.clicked.connect(self._start_encode)
        self.decode_btn = QPushButton("▶ Start Decode (H264, 1080p)")
        self.decode_btn.clicked.connect(self._start_decode)
        self.stop_btn = QPushButton("■ Stop All")
        self.stop_btn.clicked.connect(self._stop_all)
        r.addWidget(self.encode_btn); r.addWidget(self.decode_btn); r.addWidget(self.stop_btn)
        l.addLayout(r)
        self.status = QLabel("Status: Idle")
        self.status.setStyleSheet("color:#888;")
        l.addWidget(self.status)
        l.addStretch()

    def _connect(self):
        try:
            ch = grpc.insecure_channel("localhost:50053")
            self.stub = reel_forge_pb2_grpc.ReelForgeStub(ch)
            r = self.stub.HealthCheck(reel_forge_pb2.HealthRequest(), timeout=2)
            self.status.setText(f"Connected (v{r.version})")
        except: self.status.setText("Disconnected")

    def _refresh(self):
        if not self.stub: return
        try:
            r = self.stub.GetStatus(reel_forge_pb2.StatusRequest(), timeout=2)
            self.status.setText(f"Active jobs: {r.active_jobs} | Processed: {r.bytes_processed}B")
        except: self.status.setText("Disconnected")

    def _start_encode(self):
        if not self.stub: return
        r = self.stub.StartEncode(reel_forge_pb2.EncodeConfig(codec=0,width=1920,height=1080,bitrate=10000000,fps=30), timeout=5)
        self.status.setText(f"Encode: {r.job_id}" if r.success else f"Error: {r.error}")

    def _start_decode(self):
        if not self.stub: return
        r = self.stub.StartDecode(reel_forge_pb2.DecodeConfig(codec=0,width=1920,height=1080), timeout=5)
        self.status.setText(f"Decode: {r.job_id}" if r.success else f"Error: {r.error}")

    def _stop_all(self):
        if not self.stub: return
        self.stub.StopEncode(reel_forge_pb2.JobRequest())
        self.stub.StopDecode(reel_forge_pb2.JobRequest())
        self.status.setText("All stopped")

app = QApplication(sys.argv)
w = ReelForgeApp(); w.show(); sys.exit(app.exec())
