# VFD startup settings
This config is to verify the VFD and spindle using the front panel and some sane default config.
| parameter | value | Description |
| --------- | ----- | ----------- |
| PD000     | 0     | Parameter lock, 0=unlock |
| PD001     | 0     | Use the front panel for easier debugging |
| PD002     | 1     | Use the front potentiometer |
| PD005     | 400   | Max operating frequency |
| PD004     | 400   | Base frequency |
| PD003     | 400   | Main frequency |
| PD007     | 20    | Min frequency, for the VF curve |
| PD008     | 220   | Max output volt, for a 220V spindle |
| PD009     | 15    | Intermediate voltage on the VF curve|
| PD010     | 8     | Minimum voltage |
| PD011     | 100   | Minimum frequency, the spindle could overheat at lower speed and the spindle does not have torque at low speed |
| PD014     | 8     | Acceleration time, can be lower for faster acceleration |
| PD015     | 8     | Deceleration time, can be lower for faster braking |
| PD141     | 220   | Motor rated voltage, its 220 even in North America, the VFD will convert the 240V at the input in 220V at the output, as required. This is for the 220V spindle|
| PD142     | 9     | Motor maximum Amp, its 9A for the 220V spindle |
| PD143     | 2     | Number of poles, 2 for the standard 2.2kW spindle |
| PD144     | 3000  | A value of 3000 = 24k RPM, this is to have the correct RPM on the display of the VFD |

# Wiring
## North America, 240V
This is the recommended setup dues to the lower wire size required. A normal 120V 15A circuit does not have enough power for a 2.2kW spindle/VFD, only 1440W is available on a normal outlet.

A Nema 6-15 is enough to power the VFD and your stepper drivers, this outlet only requires a dual pole 15A breaker and AWG14 wires. This outlet allow access to both 120V phase in your electrical panel, with both of them, you can have a 240V device. Most of modern electronic will use directly 240V without modifications.

Your oven, dryer, water heater are already connected at 240V. 

[A video about 240V in North America](https://www.youtube.com/watch?v=jMmUoZh3Hq4)

Connect each phase to R and S VFD terminals.

## Rest of the world
You probably have easy access to single phase 220V or 240V outlet. Connect live and neutral to R and S terminals

## Grounding / shielding
Rules of thumb, chinese products are always grounded incorrectly, verify the ground before powering up equipment. 

The ground of the input cable need to be connected to the red screw labeled ground on the VFD. The input cable ground also need to be connected to your enclosure. Since you probably need that ground connected to multiple devices, you can use some terminals to connected all of them in a star pattern. 

The spindle shield and ground will also be connected on this red screw on the VFD. The spindle shield need to be connected to ground on both end (VFD and spindle). This is different than a normal signal shield, where only 1 end is connected to ground. A doubly shielded cable with a aluminium foil and a braid is preferable. To make a clean connection, cut the outer jacked, unbraid the braid and twist all the strands. Both the green/yellow ground wire and the braid need to be connected on the 4th pin. 

![Cable shield](..../Media/Images/cable_shield.jpg)

The screws in the plastic case in the lower left and right are not connected to ground. Does not use them for grounding.
![VFD ground](.../Media/Images/vfd_internal.jpg)

The spindle might not be grounded at the factory, you can verify by removing the 4 screws holding the connector to the spindle and pulling on the connector. If the 4th pin is not connected, you will need to open your spindle to add a ground wire to the case. 

![Spindle ground](../Media/Images/spindle_ground.jpg)

To open the spindle, remove the 4 hex screws and pull the top. There might be some silicone caulk holding the top, hitting it with a rubber mallet might be necessary to remove the top. Solder a AWG18 wire to the 4th pin connector and connected the other end to the spindle case using a eye terminal. Clean the old caulk, verify the O rings where the water will flow in the outer casing, add some new silicone caulk and close it back. Wait 24 hours for the caulk to dry before testing the water cooling. 

# First startup
1. Verify your watercooling loop by running it to check for leaks, keep it running while you are doing the setup.
2. Wire the input of the VFD (not the output yet) and power up the VFD
3. Configure using the startup settings
4. Unplug power
5. Connect the spindle to the output of the VFD. The ground pin of your plug should have continuity with the spindle metal case.
6. Plug your power, verify the water flow. Set the potentiometer in the middle. Set the display to Hz on the VFD.
7. Press on RUN button. Adjust the potentiometer to warm up the spindle at 100Hz. Let it run for at leat 5 minutes than ramp the speed up slowly every minutes until you reach 400Hz. The spindle should draw about 1.5A to 2A, this value can be displayed on the VFD screen. 
8. If the spindle is going the wrong direction, swap any of the 2 output phase, it will reverse the direction. 

# LinuxCNC with RS484
A USB to RS484 adapter can be used to control the spindle and show information about the current state of the VFD in the LinuxCNC GUI
TODO
