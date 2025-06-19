# Smart Grey Water Management with AR and 5G Technology

**Awarded 2nd prize in the Nan Mudhalvan Statewide Hackathon on 4G/5G Communication Networks.**

## Introduction

This project introduces a "Smart Customizable Water Management with AR and 5G Technology" system. Developed by Team VERSATILES from Meenakshi Sundararajan Engineering College, this initiative offers an innovative solution for water management in densely populated urban areas. The system integrates IoT for water automation and leverages 5G technology for real-time monitoring, control, and data visualization through Augmented Reality (AR).

## Problem Statement

The core problem this project addresses is the efficient management of grey and black water in urban and densely populated areas, which typically suffer from limited land availability for conventional water treatment systems. The conventional systems consume significant space, making them unsuitable for dense urban environments.

## Components Required

### Hardware Components:

* **ESP32 Microcontroller**
* **Ultrasonic Sensor (HC-SR04):** For water level detection.
* **Float Sensor:** To detect if the underground tank is full.
* **Water Flow Sensor (YF-S201):** To measure water flow rate.
* **Water Motor (Actuator) with Relay:** For controlling water flow.
* **Two USB cables**
* **Two 5G smartphones** (one as sender and other as receiver or user)

### Software Components:

* **Arduino IDE:** For programming the ESP32.
* **MongoDB Cloud:** For storing sensor data.
* **Node.js Server:** Backend server to receive sensor data from ESP32 and send it to MongoDB.
* **Flask:** For building the 3D building web application.
* **Coupling Together app:** Installed in the sender smartphone. This app acts as a bridge between the microcontroller and 5G technology, receiving sensor values and sending them to the user simultaneously. Built using Flutter and Kotlin.
* **Connection Forever app:** Installed in the receiver/user smartphone. Used by the user to receive real-time data and send commands. Built using Flutter and Kotlin.
* **Google Firebase:** For data transmission and pairing between the 5G apps.
* **Wired medium:** For communication between the microcontroller and the "Coupling Together" app.

## Features

* **Space-Optimized Greywater Treatment:** Filters are attached to building walls (between the first and ground floor), reducing the total area consumed by 50% compared to conventional systems, and also by using combined filters.
* **Comprehensive Gas Sensing:** The previous iteration included an INMP441 I2S microphone for sound monitoring and various gas sensors (MQ-5 for LPG, MQ-7 for CO, MQ-135 for Alcohol, Benzene, Ammonia) along with a thermistor for temperature.
* **IoT-based Water Automation:** The system uses IoT for automated water management.
* **Real-Time Monitoring:** Provides real-time sensor data for water level, flow rate, and total water used.
* **5G Communication Integration:**
    * Utilizes 5G characteristics like Beamforming for sending to specific connected nodes, Ultra-Reliable Low Latency for transferring continuously changing data with reliability, Massive Machine-Type Communication (mMTC) if sensor nodes are far apart, and Enhanced Mobile Broadband (eMBB) to improve coverage for distant users.
    * Employs a cost-effective approach using 5G System On Chip (SOC) integrated chips from smartphones for implementation, as 5G SOCs are cheaper than 5G modules. The "Coupling Together" app is central to integrating the 5G mobile SOC for connectivity.
    * Mobile applications ("Coupling Together" and "Connection Forever") act as a bridge between the microcontroller and 5G technology, enabling data broadcasting to multiple receivers.
* **Augmented Reality (AR) Visualization:** AR is used to display real-time sensor data for water level, flow, and quality when pointing at specific locations. This enhances user interaction by allowing direct visualization of water status, improving monitoring and decision-making. The base of the 3D model has been developed for AR integration. 5G enhances the user experience in the AR display, which is included in the Receiver app.
* **Remote Accessibility:** Once paired, the user can receive the real-time data anywhere, anytime.
* **Scalability:** This method can be used in individual houses, large apartments, shopping malls, schools, offices, industries etc.

## Conclusion

This project successfully presents a smart and customizable water management solution for densely populated urban areas, demonstrating a significant reduction in the land area required for water treatment by proposing wall-mounted filters. The integration of IoT for automation, alongside the innovative and cost-effective approach to 5G communication using smartphone SOCs, enables real-time data monitoring and control. The current development of the "Coupling Together" app for 5G mobile SOC integration and the base 3D model for AR underscores the project's progress. The system's ability to seamlessly transmit continuous sensor readings with low latency and high reliability, facilitated by 5G, addresses crucial communication challenges. This project not only offers a viable solution for sustainable water management but also demonstrates a versatile method for integrating 5G into various IoT and automation projects.
