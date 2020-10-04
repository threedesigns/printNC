# Print Settings
## Suggested Filaments and Settings
The below guide is highly dependent on your own printer, filament and printer profiles and experience. These settings are based on Hobbyking PLA or PETG.

Good layer adhesion and high strength are the primary factors in determining your settings. There is no significant bridging or supports required on any parts and as such much hotter temperatures may be used that traditionally seen.

Parts       	|Filament|	Temp|	Infill|Walls|	QTY    |Notes	
--------------|--------|------|-------|-----|--------|-----
Assembly Tools|	PLA |	235 |	20	    |3 |	1 x Each|	PLA preferred as it is less likely to crack when tapping centre points	
Ball Screw Face Plates Front	|PLA	|235|	60	|3|	3
Ball Screw Face Plates Rear	|PLA	|235|	60	|3|	3
BK12 Mounts|	PLA|	235|	60|	4	|3
BF12 Mounts|	PLA|	235|	60|	4	|3 	
Nema 17 Dual X Mount*	|PETG|	255|	40|	3	|1|	Must be a high temp filament, Support required (Extremely small and easy to remove)	
Nema 17 Y Mount*	|PLA/PETG|	235/255|	40	|3|	2		
Nema 23 Mount*	|PLA/PETG	|235/255	|40	|3	|3		
Tensioner & Brace|	PLA/PETG|	235/255|	30|	3|	1|	Only required for Nema 17 Dual Mount	
Z Motor Mount (17 or 23)	|PETG|	255|	60|	3	|1|	Z Motor Mount is tapped down onto HGR Rails and a very tight fit, good layer adhension required	
T8 Riser|	PLA/PETG	|235/255|	60|	3|	1	

\* Nema 17 OR Nema 23 mounts required depending on the build configuration.

Ender 3 Print Profile
This is the Ender3 Profile that I use. It has been highly tuned and provides excellent quality results with very little stringing and high strength for all functional parts. To switch between PLA and PETG simply change the temps PLA: 235 (bed 40) PETG: 255 (bed 90)

0.6 Nozzle, 0.35 layer Height, 60mm/s This is a fast printing profile. The largest part (Dual Motor Mount) prints in ~5.5 hours

[Ender 3 Print Profile](src/Ender3_Print_Profile.ini)
