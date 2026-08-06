"""Reel Forge GUI - gRPC client wrapper."""

import grpc
from src.client import reel_forge_pb2, reel_forge_pb2_grpc


class ReelForgeClient:
    """Thread-safe gRPC client for Reel Forge server."""

    def __init__(self, address: str = "localhost:50053", timeout: float = 2.0):
        self._address = address
        self._timeout = timeout
        self._channel = None
        self._stub = None
        self._connected = False

    @property
    def connected(self) -> bool:
        return self._connected

    def connect(self) -> bool:
        try:
            self._channel = grpc.insecure_channel(self._address)
            self._stub = reel_forge_pb2_grpc.ReelForgeStub(self._channel)
            resp = self._stub.HealthCheck(
                reel_forge_pb2.HealthRequest(), timeout=self._timeout
            )
            self._connected = resp.status == "SERVING"
        except Exception:
            self._connected = False
        return self._connected

    def start_encode(self, codec=0, width=1920, height=1080,
                     bitrate=10000000, fps=30) -> dict:
        if not self._stub:
            return {"success": False, "job_id": "", "error": "Not connected"}
        try:
            resp = self._stub.StartEncode(
                reel_forge_pb2.EncodeConfig(
                    codec=codec, width=width, height=height,
                    bitrate=bitrate, fps=fps
                ),
                timeout=5.0,
            )
            return {"success": resp.success, "job_id": resp.job_id, "error": resp.error}
        except Exception as e:
            return {"success": False, "job_id": "", "error": str(e)}

    def start_decode(self, codec=0, width=1920, height=1080) -> dict:
        if not self._stub:
            return {"success": False, "job_id": "", "error": "Not connected"}
        try:
            resp = self._stub.StartDecode(
                reel_forge_pb2.DecodeConfig(codec=codec, width=width, height=height),
                timeout=5.0,
            )
            return {"success": resp.success, "job_id": resp.job_id, "error": resp.error}
        except Exception as e:
            return {"success": False, "job_id": "", "error": str(e)}

    def stop_encode(self) -> dict:
        if not self._stub:
            return {"success": False, "error": "Not connected"}
        try:
            resp = self._stub.StopEncode(reel_forge_pb2.JobRequest(), timeout=5.0)
            return {"success": resp.success, "error": resp.error}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def stop_decode(self) -> dict:
        if not self._stub:
            return {"success": False, "error": "Not connected"}
        try:
            resp = self._stub.StopDecode(reel_forge_pb2.JobRequest(), timeout=5.0)
            return {"success": resp.success, "error": resp.error}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def get_status(self) -> dict:
        if not self._stub:
            return {"active_jobs": 0, "bytes_processed": 0}
        try:
            resp = self._stub.GetStatus(
                reel_forge_pb2.StatusRequest(), timeout=self._timeout
            )
            return {"active_jobs": resp.active_jobs, "bytes_processed": resp.bytes_processed}
        except Exception:
            self._connected = False
            return {"active_jobs": 0, "bytes_processed": 0}
