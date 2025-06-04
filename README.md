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
- `numpy` – numerical computing
- `scipy` – scientific computing and optimization
- `pydynaa` – event-driven simulation
- `NetSquid` – quantum network simulator ([installation instructions](https://www.netsquid.org/))
- [`cryptomyte.trevisan`](https://github.com/CQCL/cryptomite) – randomness extractor (Trevisan)
- [`cascade-python`]([https://github.com/arnaucube/cascade_python_master](https://github.com/brunorijsman/cascade-python)) – error correction protocol

To install the Python packages (except NetSquid), run:

```bash
pip install -r requirements.txt
