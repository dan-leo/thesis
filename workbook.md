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

Tuesday 18-7-2017  First day of classes.

I still need to sort out wifi-reconnections, and to investigate why the 433MHz linkup is not receiving enough power. Range is antennuated to about 10m at most, and usually 2-3m.

I re-did the compass-motor test. This time I did a linear throttle increase, which resulted in a smooth non-linear result, instead of spiky when twitching / lowering the throttle. Interference peaks at about 30%.

When attempting a quick mission in the front lawn, the gps home was offset, which meant that the drone flew into the street. Luckily, I switched to Alt-Hold, and slowly brought the drone down at the other end of the road. Doing that in split second moments is hair-raising enough. In hindsight, perhaps putting it into Brake mode would pause it, but I'll need a quicker switch configuration to enable that.