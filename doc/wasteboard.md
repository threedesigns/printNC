#Wasteboard materials

On any CNC router, workholding is more commonly provided directly by the machine table. This also tends to be a sacrificial piece for through cuts that would otherwise damage the table. 

This means that any wasteboard arrangement has to consider two things: how the workpiece will be held, and cheap it will have to be, given that it's effectively a consumable piece. 

This is why the most common option is MDF. It's cheap, it's soft, meaning that it will almost certainly cut easier than what the machine is intended to cut at that moment (so it won't ruin an endmill going through it at speeds higher than intended, as would an aluminum table when cutting a wood piece), and it's easy to add multiple types of workholding options to it. Thickness will vary, but between 10 and 20mm they are going be adequate, depending on machine size and the presence/position of middle supports. A thicker wasteboard will reduce Z clearance, but have more life between needing to be exchanged

The biggest issue with MDF, though, is that it warps when in contact with water, which stops us from using any kind of coolant, even a mist is going to damage it quickly. It also dulls really sharp endmills.
This is going to be an issue when cutting a lot of plastics: every time the cutter touches the wasteboard, it may be considered scrap for cutting plastics like acrylic. 

The solution to that is the more expensive, but still easily workable HDPE: as a plastic, it's not going to dull a sharp one flute endmill, and it's also not going to suffer from any sort of liquid damage.

The last solution, is of course aluminum or steel. These are more machine tables than wasteboards, though, and you will probably want to add MDF on top of them when doing a through cut. The upside to that is that they are flatter, more stable, and much more versatile as far as workholding goes: as such, they are especially suited for a machine that is going to use vises, and other more traditional workholding.

#Wasteboard workholding

I'm now going to focus on how we can attach the workpieces to the table.

The first, and easiest method, is just to drive a screw through the piece, and into the table. Simple, quick, and it holds really well. On an MDF table, it's not even going to ruin it that much. However, the table will still require periodical surfacing since removing the screw can raise a burr or even a small mound of material.

Next, we have a very common method, which is dual sided tape, or painter's tape on the piece and wasteboard, burnished and glued together through CA glue. Both tape metods hold thin sheets really well, don't require the use of tabs for internal through cuts, and work decently for any sheet good. However, they require the table to be flat, so more care is needed, and they take more time: double sided tape is easy to set up, but cleanup may take time, while painters tape and glue requires around 10 or so minutes to fully setup for cutting. Also, in case you have a coolant resistant table, you can't use any form of liquid on these tapes, unless you buy especially resistant ones, but they tend to be more expensive.

Lastly, we have repeatable workholding through features in the wasteboard. They tend to be machined directly by the router, ensuring that they are square to the axis and in known positions.  Let's go through those.

A first option is a grid of holes, with threaded inserts added in. This gives us places to use screws to affix various kinds of clamps, squaring fixtures, jigs, and vises. However, the threaded inserts effectively reduce the life of a spoilboard: multiple resurfacings will expose the threaded inserts, to a point where no more surfacings can be done. 

A second option is the use of bench dogs: bigger holes in the wasteboard, that will accept a metal pipe that will locate and provide a pivot point for fixture, jigs, and cam actions clamps. This is especially effective if combined with the first option: the bench dogs can provide repeatable fixturing, similar to pins, and cam action clamps, while still allowing the use of normal screw based clamps.

An option seen on AvidCNC routers, and other similarly sized machines, is the presence of pill shaped slots to use normal C-clamps to hold the stock. This however required clearance under the wasteboard for the clamp, and it may not be an option in many printNC builds. 

Lastly, an option more common for woodworkers (but also present in any professional machine tool), is the use of T-slot tracks. These will be present by default in any aluminum extrusion table, but can be added on any other wasteboard. There are specific router bits for it, aluminum T-tracks to be inserted in a machined slot (but they tend to be expensive) and they can also be made in pieces. Refer here for the last type of T-track (https://youtu.be/jqpJy86iwxc?t=458). T-slot tables have the advantage of not being limited to a grid of threaded holes, but instead have a set of parallel lines where any screw can be tightned through the use of T-nuts. These slots, if made on the machine, are also a reference parallel to one axis, for squaring and aligning.

#Wasteboard preparation and fixturing

On the printNC, according the build, there are multiple ways to affix a wasteboard to the machine.

The first, and easiest one, is to drill and tap holes on the bottom supports, at both extremes, and in the center support, and use countersunk bolts to fix the board in place.

When not using the middle supports the wasteboard can also be fixed at the bottom of the machine, with the added advantage that no matter how thick it is, it will never influence the z clearance.

However, other options are present, especially when using middle supports.

Given how cheap a wasteboard can be, the use of different wasteboards for different jobs can be attractive. in this case, I'd suggest using the machine to either drill (helically bore with a small endmill) or at least mark a set of holes in the supports. they can be then threaded or left plain for pins, to allow for multiple, easily positioned fixtures. The middle supports also allow us to have that is effectively two wasteboards, or more, that can be easily swapped indipendently. Given the large workarea of the machine, it makes them easier to handle and replace, but also allows for setting up multiple jobs and then using G54-G59 commands to have different coordinate systems, and machine a jobs while changing a pallet (this assuming, of course, that the pieces can fit on the smaller boards, and we can access all the screws while the machine is moving. It's not going to be optimal in any case).

After fixing a wasteboard in place, the first step should then to be surface it, to guarantee it's parallel to the XY plane of the machine. Special planing bits exist for this job, but they tend to be expensive, and a normal router bit can be used. After that, extra machining can be done for the chosen workholding method
