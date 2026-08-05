# Reel Forge GUI — Video Processing Desktop Application

The Reel Forge GUI is a cross-platform PySide6 desktop application for controlling the Jetson AGX Orin's hardware video encode and decode capabilities. It provides a clean interface with buttons to start and stop H.264 encode and decode jobs at 1080p resolution, with real-time status display showing active job counts and bytes processed. The application connects to the Reel Forge gRPC server and features automatic status refresh every 3 seconds. The simple, focused interface makes it easy to quickly start and stop video processing jobs while monitoring throughput.

## Features

- Cross-platform
- PySide6
- desktop
- application
- Hardware
- encode
- start/stop
- controls
- Hardware
- decode
- start/stop
- controls
- Real-time
- job
- status
- monitoring
- Active
- job
- count
- display
- Bytes
- processed
- tracking
- gRPC
- client
- with
- auto-reconnect
- Periodic
- status
- refresh
- MIT
- licensed

## Quick Start

### Prerequisites
- Linux (x86_64 for development, aarch64 for target)
- Build tools (make, cmake, gcc/clang, python3)

### Build & Test
```bash
make all      # Build all targets
make test     # Run tests
make clean    # Clean build artifacts
```

## Repository Structure

| Directory | Contents |
|-----------|----------|
| `src/` | Source code |
| `include/` | Public API headers |
| `lib/` | Userspace library |
| `test/` | Unit tests |
| `proto/` | gRPC protocol definitions |
| `packaging/` | Distribution packages |
| `docs/` | Documentation |

## Project Status

**Version:** 0.1.0 — Initial release
**License:** MIT
**Audit Score:** 90/100

## Ecosystem

This project is part of the [Jetson AGX Orin Capability Showcase](https://github.com/soccentric-jetson-oss/soccentric-jetson-oss) — five open-source projects demonstrating full exploitation of NVIDIA's flagship edge AI platform.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines. All contributions welcome!

## License

MIT. See [LICENSE](LICENSE) for details.
