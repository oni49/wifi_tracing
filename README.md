**Weapons of Math Instruction: Using mathematics to draw usable operational insights from WiFi data.**

1. **Introduction**


The fact that marketeers and corporations collect copious amounts of data from their WiFi infrastructure and use mathematics and data science to better target individual consumers is well known, though the exact methods used often remain nebulous. The open source and information security communities are comfortable with war-driving and WiFi data collection tools like Kismet and the Dope Scope, but deeper understanding of how to leverage this data at scale remains disparate. In this talk we examine the operational insights we can draw from WiFi data for both offensive and defensive applications using mathematical approaches.

We begin this presentation exploring prior work and relevant current events on this topic. Then, we discuss three hypotheses. First, we hypothesize that through a stationary sensor, the patterns of life (PoL) of WiFi access points (WAPs) reveal the presence of recurring moving infrastructure traversing the observed area. Second, WAP PoL data will allow us to discover if devices are transient or stationary. Third, we hypothesize that use of a surreptitious mobile sensor will allow us to leverage publicly available services to discover previously unknown infrastructure for further detailed analysis. 

When examining PoL data to detect recurring moving infrastructure or WAPs, we conclude that simple mathematical measurements are sufficient to reveal the presence and behavioral patterns of mobile WAPs. We discuss the methodology required to profile such access points, as well as the methods and equipment required to measure such behavior not just in time, but also in space. When we explore whether or not pattern of life data will allow us to discover if devices are transient or stationary, we reveal a clear difference in the quantity and nature of the signals observed and then further conclude that data science will allow us to classify these signals as mobile or stationary without contextual knowledge such as SSIDs or visual observation. 

![image alt text](https://github.com/ryko212/wifi_tracing/blob/master/images/image2.png)

Figure 1. Principal Component Analysis of WAP Pattern of Life Data

Further, when we explore surreptitious mobile sensors to enumerate previously unknown infrastructure, we discuss legal methods for leveraging public services such as the postal service to conduct data collection then present both math and code for calculating the geolocation of an individual WAP in a probabilistic fashion and explore the algorithmic means necessary to objectively identify unusual WAPs for further examination. 

![image alt text](https://github.com/ryko212/wifi_tracing/blob/master/images/image3.png)

Figure 2. Initial visualizations of probabilistic mapping of a WAP

Finally, we detail mathematical approaches that allow the use of multiple stationary sensors in concert to draw out operational insights. Notably, we examine the use of set theory to draw out defensive and offensive targets using the WiFi data from multiple campuses. We then present unexpected insights we encountered during our research such as previously undocumented organizationally unique identifiers. 

While exploring each hypothesis, we discuss our methods and hardware in detail--including the methods we tried that failed--and provide our code and sanitized data in a publically available repository. Finally, as all good research projects do, we discuss future work that would improve upon this project. 

As we continue our work, our code and sanitized data are available at [https://www.github.com/ryko212/wifi_tracing](https://www.github.com/ryko212/wifi_tracing) 

2. **Lit Review:** In this section, we discuss previous work directly related to or similar to our project. Most notably, we examine SensePost’s work creating Snoopy, a distribute WiFi based profiling system ([https://sensepost.com/blog/2012/snoopy-a-distributed-tracking-and-profiling-framework/](https://sensepost.com/blog/2012/snoopy-a-distributed-tracking-and-profiling-framework/) ) and then current events such as hotels’ use of Wifi orchestration and security frameworks to prevent consumers from using private WiFi options ([http://fortune.com/2015/11/04/fcc-hotels-wifi-blocking/](http://fortune.com/2015/11/04/fcc-hotels-wifi-blocking/) ).

3. **Stationary sensors.** In this section we discuss the hypotheses and work related to data collection from one or more stationary monitoring posts. The two primary hypotheses examined are:

    **H1: PoL info reveals the presence of recurring moving infrastructure.**

    **H2: PoL will allow us to classify if devices are mobile or stationary.**

    1. **Sensor and data strategies.** Here we discuss the hardware and architecture of the stationary sensors. Then, we describe the scripts and logic behind data collection and the environment in which each sensor was employed--and the type of data we expected to see. Finally, we discuss data anonymization and sanitization. 

    2. **Leveraging the data collected.** To effectively leverage the data, we first have to identify what it is we are looking at. From data collected by a stationary sensor over a month and a half, we collected 191 unique SSIDs over 194 MAC addresses. We hypothesized there would be two distinct classes of WAP: transient and stationary. This particular sensor was calibrated to record a MAC/SSID pair if it had not been observed in five minutes. Therefore, we would one record for any MAC/SSID pair every 5 minutes if it was within persistent range of the stationary sensor and also capture configuration changes evident in these fields. We suppose a mobile WAP would necessarily have fewer recorded instances of detected frames than that of a stationary WAP. 
    However, we needed a way to express the unique PoL of a WAP--one that goes above and beyond simple sparsity of data collected--in order to classify it as mobile or stationary. To answer this question, we built collected each observed MAC/SSID pair’s PoL as a vector with 1440 fields - the number of minutes in a day. For each minute, we entered the number of times the WAP was seen. For example, if a WAP is stationary, its beacon frames would be recorded the same time every day, increasing the "minute of day" count. If it was mobile like a MiFi puck then its beacon frames may be seen at various minutes of the day--which may or may not overlap. In short, we’ve created a fingerprint of each WAP’s behavior for each minute of day - an array, where each position represents the number of times it was detected for each minute of the day. 


With the data collected and organized, we analyze it with a combination of techniques across mathematics, data science, and statistics such as:

        1. Simple counting metrics (visualized using bar graphs)

        2. Descriptive statistics including median, mode, and mean (presented numerically)

        3. Interquartile range (visualized using box and whisker plots)

        4. Uniform Manifold Approximation and Projection (visualized using scatter plots)

        5. Principal Component Analysis (visualized using scatter plots)

        6. Logistic Regression/Support Vector Machine/mean-shift clustering/DBSCAN (to be tested)

4. **Defensive and Offensive Insights from Stationary Sensor Data.** In this section we examine how to operationalize data collected from one or more stationary sensors. We discuss:

    1. **Alerting.** The simplest method of gaining operational value from stationary sensors is to create a rules based or observation based alerting system. We discuss how this system operates based on the following two rules:

        1. **Alert when a new WAP is observed.** For defenders, this--potentially noisey--alert allows immediate identification of new or rogue hotspot comes online. For attackers, this allows the detailed tracking of the expansion of target infrastructure which allows for attacks of opportunity and identification of security policy violations which may be exploited. 

        2. **Alert when a specific WAP is observed**. This allows both attackers and defenders to track a suspicious device in detail and is most useful when a device is tightly associated to a person or situation. 

    2. **Set theory.** Set theory provides us with means to quickly analyze data across multiple sensors. We demonstrate and discuss the analysis of data collected from multiple stationary sensors as if they represent three separate corporate campuses--instead of our apartments. Each sensor’s data is deduplicated into a set containing a hash representing each WAP and a reference of times each WAP was observed. 
    With a set off WAPs observed at each campus, the set intersection of all campuses immediately provides operational insight when examined during a given time window. The set intersection for each campus represents devices present at multiple campuses. **A WAP present at all campuses designates either a VIP (target for offense) or an actor conducting deliberate reconnaissance (target for defense).**

    3. **Change detection.** Change detection uses behavior based fingerprints in order to identify when a WAP’s behavior diverges from its normal. We discuss the creation of vectors which represent significant highlights of behavior and how to examine them for changes using methods such as clustering and cosine difference. This allows defenders to identify:

        1. **Change in clustering:** This indicates when a certain type of device begins to behave as a different kind of device.

        2. **Substantial cosine difference when measured against itself:** This indicates when a device has substantially altered its behavior. It has become a new type of device, changed when its active, changed where its active, etc.

    4. **Geo-data’s impact on alerts and change detection.** All of our means of operationalizing WiFi data become even better when enriched with geo-data. Using collectable data such as the RSSI field, the locations and movement patterns of WAPs (or client devices) can be observed, recorded, fingerprinted, and monitored for significant change. 

5. **Moving Sensors.** In this section we discuss the hypothesis and work related to data collection from mobile monitoring posts. The primary hypothesis examined is:

    **H3: Surreptitious mobile sensors will allow us to leverage existing infrastructure to discover previously unknown infrastructure for further detailed analysis**


    1. **Sensor methodology.** The collection process for this particular dataset required two separate pieces: the sensor itself (consisting of both hardware and software) and the deployment method.

        1. **Hardware.** Our primary focus when building our moving sensor focused around battery longevity. With this in mind we started with a raspberry pi zero w as the base for the sensor. This would provide us with a low-cost and relatively low power device that afforded us compute power. Next, we added GPS capability over USB by employing a Garmin GlobalSat BU-353 GPS device. Finally, we added a DS3231 real time clock module that connected to GPIO pins of the raspberry pi zero w. Finally, we powered the entire setup off of an external battery pack. A 20100 mAh battery pack would provide enough power for approximately three days of wifi data collection.

        2. **Software.** Since we were focused on reducing the power consumption of the sensor, we decided to not use an external Alfa antenna for wifi packet collection. Instead we used the updated nexmon firmware/drivers ([https://github.com/seemoo-lab/nexmon/blob/master/README.md](https://github.com/seemoo-lab/nexmon/blob/master/README.md)) to allow us to put the onboard wifi controller into promiscuous mode. Next, we installed kismet version 2016-07-R1 and set it up as a service to start on boot.

        3. **Deployment.** Once we built the sensor, we needed a way to efficiently canvas potentially disparate and distant geographic locations. The simplest method we settled on was to package up the sensor (raspberry pi zero w, rtc, gps, and battery) into a foam setting that fit into a small flat rate package from the USPS. We could then provide a destination address, pay for shipping, and drop the entire setup in the mail. To initially ensure that we would receive the sensor back with the data intact, we chose someone we knew to receive the sensor. They would then either physically hand the sensor back to us or mail it back. Once returned, we could pull the sd card and download the kismet logs for further analysis.

![image alt text](https://github.com/ryko212/wifi_tracing/blob/master/images/image0.jpg)

Figure 3. Sensor ready for shipping

    2. **Kismet Data Review.** To visualize potential geolocation of detected WAPs, we started with the XML files that Kismet produces. Initially, we reviewed the netxml file as it seemed to have the appropriate information we needed to start our analysis (latitude, longitude, RSSI, and BSSID). However, when we dove further into the data we realized that while the netxml file has a lot of information in it, it only maintains one entry per BSSID. In the version we used, Kismet updates eachentry if the sensor received additional frames from the same source. Unfortunately, this first seen/last seen data set would not support our analysis. 
    Pivoting to the gpsxml file from Kismet, it became quite clear that we could use the data in that file to build our intended heatmaps. The gpsxml file creates an entry per frame that is received. However, Kismet also tracks additional information that we do not require for our analysis. Kismet continually polls the attached GPS device and, if a time threshold is reached with no new frame received, Kismet writes an entry to the gpsxml file with the bssid of "GP:SD:TR:AC:KL:OG" and the rest of the appropriate data for a fully formed gpsxml entry.

    3. **Data Processing.** Since the size of the gpsxml file is directly proportional to the time the sensor is powered on, we could end up in a large file (over 200 MB) and  needed a way to first clean/cull the data prior to processing to reduce the size of the file so that the Python script can more efficiently process the xml. From there we decided to sanitize the data to replace the BSSIDs with a hash of the current BSSID and a secret key (this step may not be required). 
   Once we had a clean and sanitized xml file, we could then begin the data processing in earnest. The developed Python script reads the xml file and creates a dictionary of BSSID as the key and a list of all latitude, longitude and RSSI tuples for each entry. From there a center latitude/longitude pair is determined to provide the center of the map. A google map instance is then created and the list of 3-tuples is then iterated over. The diameter of the circle placed at each latitude/longitude pair is determined by using the RSSI value and a version of the mean path loss model equation from the seminal paper "914 mhz Path Loss Prediction Models for Indoor Wireless Communications in Multifloored Buildings" by Seidel and Rappaport.![image alt text](https://github.com/ryko212/wifi_tracing/blob/master/images/image_3.png)
    When we solve for distance, the formula becomes:
![image alt text](https://github.com/ryko212/wifi_tracing/blob/master/images/image_4.png)
    where n is the path loss exponent which compensates for how fast the signal attenuates given the location (i.e. vegetation, buildings, etc.), TxPower is the transmit power of the WAP, and RSSI is the received signal strength at the mobile sensor. For our analysis I use an n value of 2.7 (2.0 is the value for a signal in a vacuum) and a TxPower value of -20 dBm. 

See below for the algorithm used to process the data:

        `1. Cleaning/culling gpsxml data
            1. Remove 00:00:00:00:00:00 and GP:SD:TR:AC:KL:OG entries
            2. Remove corrupted data entries
        2. Parse xml data -> dictionary with macs as the key and a list of tuples (latitude, longitude, rssi) as the associated value.
        3. Iterate over the gps dictionary and create a new map from the list of tuples.
            1. Process all lat/lon pairs in the list to find the map center
            2. Create gmap instance
            3. Iterate over lat/lon/rssi 3-tuples
                1. Use rssi to find estimated AP distance from sensor location
            4. Plot circle on map using lat/lon/radius
            5. Write map out to disk
        4. Review
            1. See if a building fall within darkened circles on map
            2. Any instance of an AP detected with no building within reasonable distance -> further analysis`

6. **Other outputs.** In this section we examine other insights we encountered and hypotheses emerging over the course of our research. For example, we examine OUI information available in our data set and attempt to use context (dropped out of our public data sets) to reveal OUIs that are not available in our baseline OUI list. 

7. **Future work.** In this section we explore future work that would improve this research project and make it more relevant. At the time of this writing, future work includes:

    1. **Stationary Sensor.** Deploying multiple stationary sensors per monitored campus and enriching all data using geolocation lessons learned from mobile sensor work. Further, we wish to examine the best offensive applications and how to best transition from stationary collection to collection with mobile, manned-sensors. 

    2. **Moving Sensor.**

        1. **Math refinement. **Continue to develop the mathematical expressions to assign each WAP to the nearest real property/infrastructure and assign a probabilistic confidence interval to the location of each WAP RSSI-based heatmaps circles are written to the map.

        2. **Mobility expansion.** Examine the following:

            1. Determine alternate methods of canvassing geographic areas with sensors to cover areas that the postal service does not and guarantee deployment methods are available when we cannot use the original method.

            2. Add data exfiltration while each sensor is enroute. Data exfiltration would allow us to see the data as it is being collected and would allow us access to a partial data sets even if a sensor is compromised or damaged. 

            3. Develop a heartbeat beacon that would alert us to the location of the sensor during its deployment. These heartbeats would be rough indicators of the location and health of the sensor at a particular time. In turn, this would maximize our ability to recover a damaged, lost, or stranded sensor. 

8. **Conclusion.** Code, data, and future updates to this project and this outline can be found at [https://github.com/ryko212/wifi_tracing](https://github.com/ryko212/wifi_tracing)  
