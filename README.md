# Weapons of Math Instruction: Using mathematics to draw usable operational insights from WiFi data.

##Abstract/Thesis
Three hypotheses and initial conclusions

* The fact that marketeers and corporations collect copious amounts of data from their WiFi infrastructure and use mathematics and data science to better target individual consumers is well known, though the exact methods used often remain nebulous. The open source and information security communities are comfortable with war-driving and WiFi data collection tools like Kismet and the Dope Scope, but deeper understanding of how to leverage this data at scale remains disparate. In this talk we examine the operational insights we can draw from WiFi data for both offensive and defensive applications using mathematical approaches.

* We begin this presentation exploring prior work and relevant current events on this topic. Then, we discuss three hypotheses. First, we hypothesize that through a stationary sensor, the patterns of life (PoL) of WiFi access points (WAPs) reveal the presence of recurring moving infrastructure traversing the observed area. Second, WAP PoL data will allow us to discover if devices are transient or stationary. Third, we hypothesize that use of a surreptitious mobile sensor will allow us to leverage publicly available services to discover previously unknown infrastructure for further detailed analysis. 

* When examining PoL data to detect recurring moving infrastructure or WAPs, we conclude that simple mathematical measurements are sufficient to reveal the presence and behavioral patterns of mobile WAPs. We discuss the methodology required to profile such access points, as well as the methods and equipment required to measure such behavior not just in time, but also in space. When we explore whether or not pattern of life data will allow us to discover if devices are transient or stationary, we reveal a clear difference in the quantity and nature of the signals observed and then further conclude that data science will allow us to classify these signals as mobile or stationary without contextual knowledge such as SSIDs or visual observation. 


Figure 1. Principal Component Analysis of WAP Pattern of Life Data

* Further, when we explore surreptitious mobile sensors to enumerate previously unknown infrastructure, we discuss legal methods for leveraging public services such as the postal service to conduct data collection then present both math and code for calculating the geolocation of an individual WAP in a probabilistic fashion and explore the algorithmic means necessary to objectively identify unusual WAPs for further examination. 


Figure 2. Initial visualizations of probabilistic mapping of a WAP


* Finally, we detail mathematical approaches that allow the use of multiple stationary sensors in concert to draw out operational insights. Notably, we examine the use of set theory to draw out defensive and offensive targets using the WiFi data from multiple campuses. We then present unexpected insights we encountered during our research such as previously undocumented organizationally unique identifiers. 

* While exploring each hypothesis, we discuss our methods and hardware in detail--including the methods we tried that failed--and provide our code and sanitized data in a publically available repository. We will then close, as all good research projects do, with a discussion of future work that would improve upon this project. 
