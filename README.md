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
- `fake_QKD` main function: Simulates a fake QKD session between two nodes. Implements the BB84 protocol, but "skips" the quantum communication part. We simulate all sources of noise and randomness with properly implementing them, as we do when using NetSquid.
- Functions to imitate key generation and communication delays: `generate_binary_list`, `calculate_error_rate`, `parameter_estimation`, `apply_loss_and_noise`

---

### 📄 `math_tools.py`

A collection of **mathematical utility functions** used throughout the simulation. This include calculating relevant probabilities to model noise and loses, estimating fundamental parameters to test the behavior of the QKD protocol (KBR, QBER, limit distance) or calculating the minimum photons needed to meet output key length requirements posed by the user. This is the implementation of our theoretical analysis.

**Key functions:**
- `H(p)`: Binary Shannon entropy.
- `P_Loss()`, `P_Depolar()`, `P_DCR()`: Models for loss, depolarization, and dark count rates.
- `expected_qber()`: Estimates QBER under noisy conditions. Specifically, this function calculates the probability of a bit flip occurring between Alice's and Bob's raw keys.
- `expected_KBR`: This function estimates the KBR, given as number of output bits per quantum channel usage, for a given set of parameters. It also estimates the standard deviation of this quantity according to our theoretical analysis.
- `m_solution`: Finds the value for m, the output key length after applying the Trevisan extractor, solving the implicit equation for this variable. For that purpose, `scipy.fsolve` is used.
- `limit_distance`: Calculates the maximum distance for which a non-zero secret key can be obtained after executing the protocol. This is obtained for a given set of parameters.
- `get_minimum_photons`: Estimate the minimum number of photons required to generate a secure key of length M over a quantum link with given physical parameters. This function allows to set the preferred paramater estimation strategy.

---

### 📄 `network.py`

This module defines the **network-level architecture and delay model** for the QKD simulation environment. It sets up the topology, timing behavior, and node interconnections required to simulate realistic quantum communication scenarios.

**Main components:**
- `QKDNetwork` class: Manages the creation and connection of QKD nodes across a simulated network in NetSquid.
- `GaussianDelayModel` class: Introduces realistic communication delays for the quantum channel based on a Gaussian distribution, mimicking latency in optical fiber links.

This module is central to initializing the simulated environment used by the BB84 and fake QKD protocols.




