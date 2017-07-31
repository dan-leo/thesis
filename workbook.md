#############################################
Friday 7-7-2017  

Put frame together.

#############################################
Saturday 8-7-2017  

Put motors, ESCs together. Connected Pi, Navio2, GPS antenna.

#############################################
Sunday 9-7-2017  

Bought galvanised steel M3 screws from Apple Tool & Gas. Lengths: 6mm, 8m, 10mm, 12mm. Attached flight controller, case, GPS antenna, 433 MHz transceiver to frame. 

#############################################
Wednesday 12-7-2017  

Connected ACCST transceiver for handheld control, power module.

#############################################
Friday 14-7-2017

Used some math to work out cartesian line to add 6 flight modes. Some of the numbers:

(982), 1166, (1238), 1295, 1425, (1494), 1555, 1685, 1814
18, 30.5, 43, 56, 69, 81
-64, -39, -14, 8, 38, 62

y/x = 25/100 = 25%

Switch A -> I5:  y = 26*x + 37
Switch B -> I6:  y = 75*x + 0

Channel 5 = I5 + I6

#############################################
Saturday 15-7-2017  Flight attempt

Added extra power module for redundancy.

Growing wobble of death. Investigated the timing of the ESCs. There is a slight delay, about 10ms, between two motors when running the motor test {16% throttle, x seconds}. I thought this must be an issue, but this is just due to timing constraints (I assume) when it comes to the real-time kernel in the raspberry pi, before it sends the commands to each motor via the 32-bit external co-processor / microcontroller.

#############################################
Sunday 16-7-2017  First flight

I lowered the gain of the roll/pitch PID values by about 25%. Made the craft slightly less jerky, but enough that oscillatory transients were not present anymore.  Smooth flying.

#############################################
Monday 17-7-2017  Official commencement of Project E448

Met with Dr van Daalen today at 1pm for an ad-hoc meeting. We spoke about the approach, methodology etc with regards to the thesis. Two methods are a systematic approach, which is good, but slow. It can also lead to fixing the wrong problem. The other approach is focusing on the goal, and refining the process thereafter. The latter approach also leads to the discovery of unforeseen problems. One caveat is that subsections are incomplete, as opposed to the systematic approach.

Flew a test on front lawn in Alt-Hold and Stabilise. Flew a mission at De Hoop. 

Mission:
* takeoff to 10m
* move west to waypoint
* land

At the transistion to landing, I discovered that the drone started toilet-boweling. I've seen this before, and handled the situation relatively well. Usually it increases the chance of a crash ten-fold (in my opinion). The greatest problem is that one can only go up and down.

After investigation, it seems that a fix is to attach an external compass, or (which I neglected after a compass re-calibration) a compass-motor-interference recalibration. This determines the magnitude of interference from the motors (induced by current) which affect the compasses.

The current compass-motor-interference calibration is set for previous compass offsets.

#############################################
Tuesday 18-7-2017  First day of classes.

I still need to sort out wifi-reconnections, and to investigate why the 433MHz linkup is not receiving enough power. Range is antennuated to about 10m at most, and usually 2-3m.

I re-did the compass-motor test. This time I did a linear throttle increase, which resulted in a smooth non-linear result, instead of spiky when twitching / lowering the throttle. Interference peaks at about 30%.

When attempting a quick mission in the front lawn, the gps home was offset, which meant that the drone flew into the street. Luckily, I switched to Alt-Hold, and slowly brought the drone down at the other end of the road. Doing that in split second moments is hair-raising enough. In hindsight, perhaps putting it into Brake mode would pause it, but I'll need a quicker switch configuration to enable that.

#############################################
Thursday 20-7-2017  First weekly skripsie meeting

Met with Corné, and finalised the aims for the project.

The aims are as follows:

* To investigate parameters within large-scale areas beneficial to the agricultural sector.
* To design and build an aerial observation platform in order to collect data and estimate these paramters
* Verification by physical measurement is an optional extension.

#############################################
Friday 21-7-2017  Wifi-reconnect added

Tested the range of both 433 MHz HolyBro tranceivers. They have a receive sensitivity of about -130 dBm. The one sends a signal (from within a room) to roughly 700 meters (not LoS). LoS should be about 1.5km. The other one cannot get past 10m. This is using the same power supply. I verified this using an RTL2832 SDR. I spoke to FlyRobot

Spent many hours fiddling with wicd {cli, curses}, the interface file used by ifup / ifdown, wpa_supplicant.conf, iwconfig, ifconfig and trying to get wifi-reconnection to work. In the end, a rather custom interfaces file, and a custom bash script did the trick. It checks if it is connected to an ESSID every few seconds from iwconfig, and if not, it forces a reconnection with `ifup --force wlan0`.

#############################################
Saturday 22-7-2017  

Used up 1142mAh of 1300 mAh battery. Flew in front garden. All's well.

#############################################
Sunday 23-7-2017  

Connected camera. Extended flat 15-pin ribbon cable (200mm + 150mm). This took many hours actually, since it was only successful on the third variation. In fact, regarding the first variation, I didn't realise that the pins needed to be flipped. 

#############################################
Wednesday 26-7-2017

Got dronekit to work. Realised it only shows 8 channels.

#############################################
Saturday 29-7-2017

Flew two sorties on the dehoop upper field. Was late in the evening so blurred shots, and I realised that I had accidently adjusted the lens focus.

#############################################
Sunday 30-7-2017

Delicately refocused lens on camera.

Piped mavlink commands through mavproxy in such a way that ardupilot communicates with the GCS hostname, and not a manual IP address. It also communicates locally on two different UDP ports. One for ardupilot, and another for dronekit. Got rid of the HEARTBEAT mode 0 doesn't exist exception within dronekit from the GCS.

Discovered that CAM_FEEDBACK messages are related to the camera trigger by listening to a large stream of all the messages. Received them in dronekit.

#############################################
Monday 31-7-2017

Windy day. Need to take photos using camera trigger.

