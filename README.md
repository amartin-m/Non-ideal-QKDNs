# Non-ideal-QKDNs
Using NetSquid, we provide a framework for simulating non ideal quantum communications and quantum cryptographic protocols.

## 💻 Environment

This codebase was developed and tested with the following setup:

- **Python version**: 3.8.19
- **Operating System**: macOS Sonoma 14.5

### 📦 Key Dependencies

Standard libraries (no need to install):
- `random`, `copy`, `typing`

Third-party libraries:
- `numpy` – numerical computing (1.24.4)
- `scipy` – scientific computing and optimization (scipy.optimize) (1.9.3)
- `pydynaa` – event-driven simulation (1.0.2)
- `NetSquid` – quantum network simulator ([installation instructions](https://www.netsquid.org/)) (1.1.7)
- [`cryptomyte.trevisan`](https://github.com/CQCL/cryptomite) – randomness extractor (Trevisan)
- [`cascade-python`](https://github.com/brunorijsman/cascade-python) – error correction protocol

To install the Python packages (except NetSquid), run:

```bash
pip install -r requirements.txt
```

## 📁 Project Structure and Module Descriptions

### 📄 `fake_qkd.py`

This module implements a **mock BB84 protocol** used for testing and simulation purposes. It mimics the behavior of a quantum key distribution session without invoking actual BB84 operations implemented in NetSquid. Useful for validating network flow, timing, or component integration in the absence of quantum backends.

**Main features:**
- `FakeQKDProtocol` class: Simulates a fake QKD session between two nodes.
- Functions to imitate key generation and communication delays: `generate_binary_list`, `calculate_error_rate`, `parameter_estimation`, `apply_loss_and_noise`

---

### 📄 `math_tools.py`

A collection of **mathematical utility functions** used throughout the simulation, particularly for calculating entropy and error probabilities.

**Key functions:**
- `H2(p)`: Binary Shannon entropy.
- `P_Loss()`, `P_Depolar()`, `P_DCR()`: Models for loss, depolarization, and dark count rates.
- `expected_qber()`: Estimates QBER under noisy conditions.

These tools support both performance analysis and protocol decision-making logic.
