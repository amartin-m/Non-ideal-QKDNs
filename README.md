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
