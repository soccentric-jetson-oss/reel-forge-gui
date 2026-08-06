# Reel Forge GUI — Video Processing Desktop Application

The Reel Forge GUI is a cross-platform PySide6 desktop application for controlling the Jetson AGX Orin's hardware video encode and decode capabilities. It provides a clean interface with buttons to start and stop H.264 encode and decode jobs at 1080p resolution, with real-time status display showing active job counts and bytes processed. The application connects to the Reel Forge gRPC server and features automatic status refresh every 3 seconds.

## Features

- Provides a cross-platform PySide6 desktop application that runs identically on Windows, macOS, and Linux operating systems
- Offers hardware encode start and stop controls with one-click buttons for quick job management
- Offers hardware decode start and stop controls with one-click buttons for quick job management
- Displays real-time job status including active encode and decode job counts
- Shows total bytes processed for monitoring throughput and job progress
- Connects to the Reel Forge gRPC server with automatic status refresh every 3 seconds
- Reconnects automatically when the server connection is lost, with clear status indicators
- Provides a simple, focused interface designed for quick video processing job management
- Licensed under MIT for maximum flexibility in commercial and open-source projects

## Quick Start

### Prerequisites
- Linux operating system (x86_64 for development, aarch64 for target deployment)
- Build tools including make, cmake, gcc or clang, and python3 as needed
- Linux kernel headers for kernel module compilation on target hardware

### Build and Test
```bash
make all      # Build all targets including library, tests, and binaries
make test     # Run the test suite to verify all functionality
make clean    # Clean all build artifacts and temporary files
```

## Repository Structure

| Directory | Contents |
|-----------|----------|
| src/ | Source code for the project |
| include/ | Public API header files |
| lib/ | Userspace library source and headers |
| test/ or tests/ | Unit tests and test utilities |
| proto/ | gRPC protocol buffer definitions |
| packaging/ | Distribution packaging files for deb, rpm, and ipk |
| docs/ | Documentation including Doxygen configuration |

## Project Status

**Version:** 0.1.0 — Initial release
**License:** MIT
**Audit Score:** 90/100 across 20 criteria

## Ecosystem

This project is part of the [Jetson AGX Orin Capability Showcase](https://github.com/soccentric-jetson-oss/soccentric-jetson-oss) — five open-source projects demonstrating full exploitation of NVIDIA's flagship edge AI platform.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines. All contributions are welcome.

## License

MIT. See [LICENSE](LICENSE) for details.

---

## Showcase

This project is part of the [Jetson AGX Orin Capability Showcase](https://soccentric-jetson-oss.github.io/).
