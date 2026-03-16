This code is designed for handling the VeReMi Datasets, specifically for data preprocessing of JSON files and label mapping. 
We have selected only the position attacks for analysis.

For more details about the dataset, please visit: https://github.com/josephkamel/F2MD

To download the data, use the following link: https://mega.nz/folder/z0pnGA4a#WFEUISyS5_maabhcEI7HQA



VeReMi Dataset Structure:

The VeReMi dataset is organized into several subsets representing different simulation scenarios. Each subset includes a ground truth (GT) file and multiple message log files containing received message data.

Each message log file represents a log of messages received by a vehicle at specific timestamps. These files record what each vehicle received during the simulation.

The ground truth file contains information about all transmitted messages during a simulation and identifies which messages were sent by attackers. The ground truth includes all sending events from a single simulation, while the message logs contain the corresponding reception events.

Each entry in the message log files contains the following information:
	•	reception timestamp
	•	claimed transmission time
	•	claimed sender ID
	•	simulation-wide unique message ID
	•	position vector
	•	speed vector
	•	received signal strength indicator (RSSI)
	•	position noise vector
	•	speed noise vector
	•	module ID

The module ID originates from the VEINS simulation framework and is used to identify the simulated modules, such as vehicle components, base stations, or the SUMO connector.

In addition, the ground truth file is updated whenever a message is transmitted by any vehicle. This file includes:
	•	transmission time
	•	sender ID
	•	attacker type
	•	message ID
	•	actual position vector
	•	actual speed vector

The attacker type is set to 0 for legitimate vehicles, while other values represent different attacker behaviors. Typically, there may be more than one attacker in a simulation scenario.

Each subset therefore provides both the transmission ground truth data and the corresponding received message logs, allowing researchers to analyze vehicle communication behavior and detect malicious messages
