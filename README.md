# Data Pre-Processing for VeReMi (Version 2)

Pre-processing code for the VeReMi dataset (JSON message logs → cleaned CSV with labels). It is used by the paper:

> **Privacy-Preserving Misbehavior Detection in Vehicular Ad Hoc Networks Using Horizontal Federated Learning: An Empirical Ablation Study of Data Heterogeneity, Aggregation Strategies, and Client Dropout**
> Muradi Al-Otaibi and Muhamad Felemban, KFUPM.

🔗 **Main repository (federated learning experiments):** [`<link-to-main-repo>`](https://github.com/muradialotabi/<main-repo-name>)

---

## Overview

This code handles the VeReMi datasets, specifically:

- Pre-processing of the raw JSON files (Type-3 BSM data)
- Label mapping (receiver IDs → attack labels)

Only the **position attacks** are selected for analysis.

## Files

| File | Description |
|---|---|
| `Data pro-cessing.py` | Loads the JSON logs, cleans the data, and saves a CSV |
| `label mapping.py` | Maps messages to their ground-truth attack labels |

## Data

- Dataset details (F2MD framework): <https://github.com/josephkamel/F2MD>
- Raw data download: <https://mega.nz/folder/z0pnGA4a#WFEUISyS5_maabhcEI7HQA>

## VeReMi Dataset Structure

The dataset is organized into subsets representing different simulation scenarios. Each subset includes a **ground truth (GT)** file and multiple **message log** files.

**Message logs** record what each vehicle received. Each entry contains:

- reception timestamp
- claimed transmission time
- claimed sender ID
- simulation-wide unique message ID
- position vector
- speed vector
- received signal strength indicator (RSSI)
- position noise vector
- speed noise vector
- module ID (from the VEINS simulation framework)

**Ground truth** records every transmitted message and identifies attackers. Each entry contains:

- transmission time
- sender ID
- attacker type (`0` = legitimate vehicle, other values = attacker behaviors)
- message ID
- actual position vector
- actual speed vector

A simulation may contain more than one attacker.

## Usage

```bash
git clone https://github.com/muradialotabi/Data-Pre-Processing.git
cd Data-Pre-Processing
pip install pandas scikit-learn

# 1. Download the raw VeReMi data (see the Data section) and set the path inside the scripts
# 2. Run the pre-processing
python "Data pro-cessing.py"
# 3. Run the label mapping
python "label mapping.py"
```

> Edit the commands above if the scripts take different arguments or must be run in a different order.

## Ready-Made Data

The already partitioned data (IID and quantity-skew non-IID) used in the paper is available here:
📦 [Google Drive](https://drive.google.com/drive/folders/17BUsj6rkDRB3EgGo840wUHDqs6MHhUge)

## Citation

If you use any part of this repository (code, data, or results) in your research, please cite the associated paper:

```bibtex
@article{alotaibi2026hfl_vanet,
  title  = {Privacy-Preserving Misbehavior Detection in Vehicular Ad Hoc Networks Using Horizontal Federated Learning: An Empirical Ablation Study of Data Heterogeneity, Aggregation Strategies, and Client Dropout},
  author = {Al-Otaibi, Muradi and Felemban, Muhamad},
  year   = {2026},
  note   = {Submitted for publication}
}
```
