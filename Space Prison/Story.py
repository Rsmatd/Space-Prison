story = {
	"title":	"Space Prison",
	"start":	"sargis_cell01",
	"sargis_lab1":	{
		"text":		[
			["You go through the automatic door and enter what is clearly some kind of laboratory. You see there are several chemicals sitting around.",
			"You notice some glass bottles that are filled with brightly colored chemicals. One is red, another is blue, and yet another is yellow."]
		],
		"choice":	[
			["Take the red chemical.", "!intelligence+1", "!#red chemical=1", ">>sargis_red1", "?#red chemical=0"],
			["Take the blue chemical.", ">>sargis_bluedeath1", "!fatigue+2"],
			["Take the yellow chemical.", "!fear+1", ">>sargis_yellow1", "?@yellow_chem=0", "!@yellow_chem=1"]
		]
	},
	"sargis_red1":	{
		"text":		[
			["You grab the bottle of the red chemical, but before you can place it to your lips, you notice an experimental weapon.", "It looks unfinished, but you are intrigued.",
			"Your are curious about what the weapon is capable of."]
		],
		"choice":	[
			["Shoot it at the wall.", "!fear+1", ">>sargis_shoot_wall_t"], #Got scared runs away as soon as possible to the next room
			["Use it on yourself,", "!awareness+1", "!score-1", ">>sargis_shoot_self_t"],# Goes to next room after with 1 point of awareness
			["Better leave it there and move on.", "!score+1", ">>sargis_cafeteria"], #Skips to next room
			["Take another look at those bottles.", ">>sargis_lab1"]
		]
	},
	"sargis_shoot_wall_t":	{
		"text":		[
			["You pick up the weapon, weighing it in your hand and turning it to look at it. You point it at the wall and pull the trigger.", 1,
			"A sharp, high-pitched sound rips through the room, as a photon projectile leaves a big smudge on the wall.", 2,
			"The weapon sizzles and hums and emits an awful lot of smoke. You decide that it's definitely unfinished, and probably not very safe."]
		],
		"choice":	[
			["Get out of there.", ">>sargis_cafeteria"]
		]
	},
	"sargis_shoot_self_t":	{
		"text":		[
			["You pick up the weapon, weighing it in your hand and turning it to look at it.", 2,
			"Without thinking, you turn it around, looking at the muzzle end of the weapon, while your thumb pushes down on the trigger.", 3,
			"The weapon emits a deep hum, and starts billowing out black smoke.", 1,
			"Luckily the weapon didn't work, or your face would've been plastered on the wall by now."]
		],
		"choice":	[
			["Put the weapon down and leave.", ">>sargis_cafeteria"]
		]
	},
	"sargis_yellow1":	{
		"text":		[
			["The yellow chemical seems harmless, so you give it a taste. But as soon as you take it you start hallucinating. Big, ugly monsters creep all around you!", 2,
			"You find yourself trembling, sinking into a corner.", 1, "Before long, however, you shake your head and realize that the monsters aren't real.", 1,
			"You get back up, annoyed at the time wasted being scared of your own imagination, when suddenly you notice a chamber that has a real, live alien creature trapped in it."]
		],
		"choice":	[
			["Try to release the alien.", "!score+5", ">>sargis_aliendeath1"],
			["Better keep it moving.", "!thirst+1", "!score+1", ">>sargis_cafeteria"], #Proceed to to next room skips scene
			["Take another look at those bottles.", ">>sargis_lab1"]
		]
	},
	"sargis_aliendeath1":	{
		"text":		[
			["Quickly you pull the switch to release the alien. No creature should be trapped on this failing rock.", 2,
			"The alien wakes up and looks at you with an evil, hungry look.", 2,
			"Perhaps releasing it was a bit of a mistake...", 2,
			"You make a break for the door, but the alien zooms right after you, snarling viciously.", 1.5,
			"With very little trouble, the alien catches you and proceeds to eat you alive.", 1,
			"Humans make good alien snacks, turns out."]
		],
		"choice":	[
			["You're stuffing.. What an end!", ">>restart"]
		],
	},
	"sargis_bluedeath1":	{
		"text":		[
			["You pick up the bottle of blue chemical, admiring it for a moment, before taking a swig.", 2,
			"The taste is pretty nice, but soon you start to feel very strange. What did this blue chemical drink do to you?", 1, "Hopefully nothing.", 2,
			"you start feeling really nauseous and your stomach feels like it's expanding. You feel like you might just explode."]
		],
		"choice":	[
			["Get out of there!", "!score+2", ">>sargis_bluedeath2_t"]
		]
	},
	"sargis_bluedeath2_t":	{
		"text":		[
			["You move towards the lab exit, but now you can feel your stomach is definitely growing!", 2,
			"By the time you get to the door, your stomach is as big as a ball, and...", 2,
			"...BOOM!", 1, "You burst, like an overripened watermelon."]
		],
		"choice":	[
			["At least the walls have a lovely color now.", ">>restart"]
		]
	},
	"sargis_cafeteria":	{
		"text":		[
			["You make it to the cafeteria.", 1,
			"there seems to be a lot going on around here, strangely. You see bottles of water, of course, as well as a food counter. But there's also a large group of people here - other prisoners from the prison.", 2,
			"The other prisoners here are just hanging out, apparently oblivious to the alarms and the trembling of the lunaroid. Although, they don't look like they're in a particularly good mood.", 2,
			"A snack could be good, though. All this excitement has made you a little hungry.", 1,
			"%1"],
			["And thirsty.", "%1", "?thirst>0"]
		],
		"choice":	[
			["Have some water.", "!fear-1", "!thirst-1", "!score+1", "?thirst>0", ">>sargis_caf_water"],
			["Grab a meal from the meal counter.", ">>sargis_caf_meal"]
		]
	},
	"sargis_caf_water":	{
		"text":		[
			["You grab a bottle of water and have a big gulp.", 2,
			"It's really refreshing, pretty much the greatest thing you've had in a while."]
		],
		"choice":	[
			["Also take some food from the meal counter.", ">>sargis_caf_meal"],
			["Better keep it moving.", "?@sec_sw_shaft_laser=1", ">>sargis_shaft1"],
			["Better keep it moving.", "?@sec_sw_shaft_laser=0", ">>sargis_shaft_laser_t"]
		],
	},
	"sargis_caf_meal":	{
		"text":		[
			["You check out the food counter, only to find that there's one meal plate left.", "It does look delicious, though..", 1.5,
			"it's a very nice looking steak with rice, and a slice of cake with strawberries and sprinkles as dessert.", 2,
			"As you reach for it, you glance up and notice everyone there looking at you.", 1, "Looks like everyone else wants a piece of that meal.", 2,
			"Makes you wonder if it would be good to take it or not.", 1,
			"A meal would be really good about now, but can you get away with it?"]
		],
		"choice":	[
			["Take the food.", "!score+2", ">>sargis_caf_death_meal"],
			["Leave it.", "!intelligence+1", "!fatigue+1", ">>sargis_caf_leave"],
			["Throw the food and troll everyone!", "!score+1", ">>sargis_caf_awkward"]
		],
	},
	"sargis_caf_awkward":	{
		"text":		[
			["You grab the plate and toss it into the middle of the room, making it spill all over the floor, and turn to make a break for it, expecting the mean-looking crowd to come after you for such a stunt.", 4,
			"But it looks like the joke's on you. When you don't hear the roar of anger behind you, you turn - only to see the other prisoners staring blankly at you.", 1,
			"I guess nobody cared about the steak, and now you get to continue, hungry."]
		],
		"choice":	[
			["What a waste.", "?@sec_sw_shaft_laser=1", ">>sargis_shaft1"],
			["What a waste.", "?@sec_sw_shaft_laser=0", ">>sargis_shaft_laser_t"]
		]
	},
	"sargis_caf_death_meal":	{
		"text":		[
			["You grab the plate.", 1,
			"As you turn around, you see the people around you in the cafeteria are all looking at you.",
			"You took the last meal and everybody else wanted it for themselves.", 2,
			"They get up and surround you, starting to physically assault you", 2,
			"A punch to the face!!", 0.5, "a punch in the gut!!", 0.5, "a punch in the eye!..", 0.5, "Soon they're all over you, beating the last life out of you."]
		],
		"choice":	[
			["Well, that didn't go well..", ">>restart"]
		]
	},
	"sargis_caf_leave":	{
		"text":		[
			["You decide it's better to leave the meal behind. You don't want this crowd on your back.", 2,
			"As you start moving away, you notice that the other prisoners start having a loud conversation on who gets to have the last remaining meal.", 2,
			"You keep observing as a fight breaks out. While the meal is protected safely in the counter from all the mess going on, everyone there is distracted by the fight.", 2,
			"you realize you can actually sneak back and take the food and still get away.", 2,
			"The fight turned out helpful to you, after all."]
		],
		"choice":	[
			["Sneakily grab the meal and head out.", "?@sec_sw_shaft_laser=1", "!#steak and cake=1", ">>sargis_shaft1"], #proceed to next room
			["Sneakily grab the meal and head out.", "?@sec_sw_shaft_laser=0", ">>sargis_shaft_laser_t"]
		]
	},
	"sargis_shaft_laser_t":	{
		"text":		[
			["Moving from the cafeteria and down the hallway you see what appears to be a maintenance shaft.", 2,
			"You move a little closer, but don't get far, before you hear a loud *BLARP*.", 2,
			"panels open on both sides of the hallway, and two way-too-large laser turrets whip out and cut you into impressively thin slices."]
		],
		"choice":	[
			["Boar's Head, you are not..", ">>restart"]
		]
	},
	"sargis_guard_station": {
		"text": [
			["You step into the Guard Station. It's completely deserted.", 1.5,
			"In front of you is a security control console, with a series of poorly labeled buttons and some flashing lights, next to which is an automatic door. There are also two doors; one on the right and one on the left."],
		],
		"choice": [
			["Go through the left door.", ">>sargis_gun_storage"],
			["Go through the right door.", ">>sargis_empty_room"],
			["Go through the automatic door.", ">>sargis_next_locked_t", "?@sec_door_unlocked=0"],
			["Go through the automatic door.", "?@sec_door_unlocked=1", "?@sec_sw_lab_guns=0", ">>sargis_lab_guns_t"],
			["Go through the automatic door.", "?@sec_door_unlocked=1", "?@sec_sw_lab_guns=1", ">>sargis_lab1"],
			["Examine the security console.", ">>sargis_security_station"],
			["Go back.", ">>sargis_cell_hall03"]
		]
	},
	"sargis_next_locked_t":	{
		"text":		[
			["You approach the automatic, but it doesn't open.", 1,
			"It probably needs to be activated through the security console."]
		],
		"choice":	[
			["Of course.", ">>sargis_guard_station"]
		]
	},
	"sargis_gun_storage": {
		"text": [
			["You enter the room on the left and see that it's the Guard Station's gun storage. There are racks along the wall designed to hold guns. Most of them are empty, but there are a few stun rifles left.", 2,
			"You'd expect these racks to be locked, but it appears they aren't."]
		],
		"choice": [
			["Look around.", ">>sargis_gun_storage_look_around", "!score+1", "!@look_code=1", "?@look_code=0"],
			["grab a stun rifle.", "!fear-1", ">>sargis_gun_storage_pickup_a_gun"],
			["Go back", ">>sargis_guard_station"]
		]
	},
	"sargis_gun_storage_pickup_a_gun":	{
		"text": [
			["You walk over to the gun rack and reach for a stun rifle.", 2,
			"As soon as you touch it, the rifle's automatic DNA sequencer determines that your profile does not match that of any guard employed by the lunaroid prison facility.", 2,
			"A robotic voice blares out \"UNAUTHORIZED ACCESS\", and an unpleasantly tingling current of a few hundred amps is shot through your body.", 1,
			"You are left convulsing on the floor, with smoke emanating from where your eyeballs used to be."],
		],
		"choice": [
			["Shocking!",">>restart"],
		]
	},
	"sargis_gun_storage_look_around":{
		"text": [
			["Looking around, you see a some numbers scribbled on the wall just next to the door:", "%1"],
			["4321", "%1", "?awareness=0"],
			["5812", "%1", "?awareness=1"],
			["9461", "%1", "?awareness=2"],
			["0001", "%1", "?awareness>2"]
		],
		"choice": [
			["those look significant.", ">>sargis_guard_station"],
		]
	},
	"sargis_empty_room": {
		"text": [
			["Behind the door on the right is - a small, empty room.", 1,
			"All you see here are two more doors, one red and one green."]
		],
		"choice": [
			["Go through the red door.", ">>sargis_empty_room_red_door"],
			["Go through the green door.", ">>sargis_empty_room_green_door"],
			["Just go back.", ">>sargis_guard_station"]
		],
	},
	"sargis_empty_room_red_door":{
		"text": [
			["nothing interesting in here%1."],
			[" either", "%1", "?@green_door=1"]
		],
		"choice": [
			["back, I guess.", "!@red_door=1", ">>sargis_empty_room"]
		],
	},
	"sargis_empty_room_green_door":{
		"text": [
			["Nothing interesting in here%1."],
			[" either", "%1", "?@red_door=1"]
		],
		"choice": [
			["Back, back.", "!@green_door=1", ">>sargis_empty_room"]
		],
	},
	"sargis_security_station": {
		"text": [
			["You walk up to the security control console.", 1,
			"It has a numeric keypad, labeled \"DOOR\", as well as 5 large switches in one vertical row, each with a green light next to it.", 1, "The labels next to each switch are horribly worn. All you can read, from 1 through 5, is:",
			"\"GU▒ ▓░TR░▒\", \"░X¥▒E▓ S░▒P▒Y\", \"AI░_O▒< ░▒TE C▒░S⌐░R\", \"L▒SE░ ▓UR░E▒░\", and \"DO▒R ░▓W░R\".", "%1"],
			["A robotic voice booms through the speaker: \"LABORATORY GUNS DEACTIVATED\".", "%1", "?@do=1"],
			["A robotic voice booms through the speaker: \"OXYGEN SUPPLY DEACTIVATED\".", "%1", "?@do=2"],
			["A robotic voice booms through the speaker: \"AIRLOCK GATE CRUSHER DEACTIVATED\".", "%1", "?@do=3"],
			["A robotic voice booms through the speaker: \"SHAFT LASER TURRETS DEACTIVATED\".", "%1", "?@do=4"],
			["A robotic voice booms through the speaker: \"DOOR POWER DEACTIVATED\".", "%1", "?@do=5"],
		],
		"choice": [
			["Deactivate switch #1.", "?@sec_sw_lab_guns=0", "!@sec_sw_lab_guns=1", "!@do=1"],
			["Deactivate switch #2.", "?@sec_sw2=0", "!@sec_sw2=1", "!@do=2"],
			["Activate switch #2.", "?@sec_sw2=1", "!@sec_sw2=0", ">>sargis_security_2"],
			["Deactivate switch #3.", "?@sec_sw_airlock_gate=0", "!@sec_sw_airlock_gate=1", "!@do=3"],
			["Deactivate switch #4.", "?@sec_sw_shaft_laser=0", "!@sec_sw_shaft_laser=1", "!@do=4"],
			["Deactivate switch #5.", "?@sec_sw5=0", "!@sec_sw5=1", "!@do=5"],
			["Activate switch #5.", "?@sec_sw5=1", "!@sec_sw5=0", ">>sargis_security_5"],
			["Go back.", ">>sargis_guard_station", "?@sec_sw5=0", "?@sec_sw2=0"],
			["Use keypad.", "!score+1", "?@sec_sw2=0", "?@sec_sw5=0", "?@sec_door_unlocked=0", ">>sargis_security_keypad_t"]
		]
	},
	"sargis_security_keypad_t":	{
		"text":		[
			["You look closer at the keypad.", 1, "It's just a keypad.", 1,
			"It seems to be controlling the door next to the console.", "%1"],
			["A small speaker goes *BLARP*, while a red light flashes twice. Probably not the right code.", "%1", "?@sec_door_locked=1"],
			["You hear a satisfying *BWEEP*, and a whoosh from the automatic door as it slides open.", "%1", "?@sec_door_unlocked=1"]
		],
		"choice":	[
			["Type \"1234\" onto the keypad.", "?@sec_door_unlocked=0", "!@sec_door_locked=1"],
			["Type \"5812\" onto the keypad.", "?@sec_door_unlocked=0", "?awareness=1", "?@look_code=1", "!@sec_door_locked=0", "!@sec_door_unlocked=1"],
			["Type \"4231\" onto the keypad.", "?@sec_door_unlocked=0", "?@look_code=0", "!@sec_door_locked=1"],
			["Type \"9462\" onto the keypad.", "?@sec_door_unlocked=0", "!@sec_door_locked=1"],
			["Type \"0001\" onto the keypad.", "?@sec_door_unlocked=0", "?awareness>2", "?@look_code=1", "!@sec_door_locked=0", "!@sec_door_unlocked=1"],
			["Type \"5555\" onto the keypad.", "?@sec_door_unlocked=0", "!@sec_door_locked=1"],
			["Type \"9461\" onto the keypad.", "?@sec_door_unlocked=0", "?awareness=2", "?@look_code=1", "!@sec_door_locked=0", "!@sec_door_unlocked=1"],
			["Type \"1991\" onto the keypad.", "?@sec_door_unlocked=0", "!@sec_door_locked=1"],
			["Type \"4321\" onto the keypad.", "?@sec_door_unlocked=0", "?awareness=0", "?@look_code=1", "!@sec_door_locked=0", "!@sec_door_unlocked=1"],
			["Type \"8522\" onto the keypad.", "?@sec_door_unlocked=0", "!@sec_door_locked=1"],
			["Never mind.", "?@sec_door_unlocked=0", "!@sec_door_locked=0", ">>sargis_security_station"],
			["Great!", "?@sec_door_unlocked=1", ">>sargis_security_station"]
		]
	},
	"sargis_security_2": {
		"text": [
			["Frantically, you try to reactivate the oxygen supply, but the switch is stuck in the OFF position", 2,
			"You push and push, but it just won't budge. You start feeling lightheaded as the oxygen seeps out of the room.", 2,
			"Eventually you collapse over the console."]
		],
		"choice": [
			["\"Take a deep breath\" sounds good, but what can you do?", ">>restart"]
		]
	},
	"sargis_security_5": {
		"text": [
			["Trying to switch the door power back on you manage to somehow snap the switch right off.", 2,
			"You stand staring at it for a few moments, baffled.", 0.5,
			"You toss the broken switch to the side, and stick your finger into the gap to try and move the mechanism that way.", 2,
			"You feel a warm jolt, as high voltage shoots from the console up through your finger."]
		],
		"choice": [
			["Smells like barbecue.", ">>restart"]
		]
	},
	"sargis_lab_guns_t":	{
		"text":		[
			["You go through the automatic door, into what is clearly some kind of laboratory.", 2,
			"You are startled by a loud, robotic voice blaring \"UNAUTHORIZED ACCESS\", and before you can react, 5 massive guns emerge from the ceiling, pointing straight at you.", "%1"],
			["You keep as still as you possibly can, so as to not trigger then guns.", "%1", "?@gun_trigger=1"]
		],
		"choice":	[
			["Don't move!", "?@gun_trigger=0", "!fear+10", "!score+1", "!@gun_trigger=1"],
			["Run for it!", ">>sargis_lab_gunned_t"]
		]
	},
	"sargis_lab_gunned_t":	{
		"text":		[
			["You make a break for it, diving for cover.", 3, "These guns are no joke, however.", 1,
			"You are soon better ventilated than Swiss cheese."]
		],
		"choice":	[
			["Well, you tried.", ">>restart"]
		]
	},
	"sargis_control_room": {
		"text":		[
			["You drop down into the control room and look around. Nobody is in the room, but you do see shiny computers that look out of this world lining the wall, with camera monitors displaying various locations around the lunaroid.", 1.5, "%1"],
			["On the far wall is a closed door.", "%1", "?@check_door=0", "?#break room key=0"],
			["On the far wall is a door.", "%1", "?@check_door=0", "?#break room key=1"],
			["On the far wall is a locked door.", "%1", "?@check_door=1", "?#break room key=0"],
			["On the far wall is the locked door.", "%1", "?@check_door=1", "?#break room key=1"]
		],
		"choice":	[
			["Investigate the computers.", ">>sargis_control_room_computers"],
			["Look at the camera monitors.", "!awareness+1", "?@alien_encounter=0", ">>sargis_control_room_cameras"],
			["Look around the room.", "?#break room key=0", ">>sargis_control_room_investigate"],
			["Open the door.", "?@check_door=0", "!@check_door=1", "?#break room key=0", ">>sargis_control_room_locked_t"],
			["leave through the door.", "?#break room key=1", "!score+1", ">>sargis_break_room"]
		]
	},
	"sargis_control_room_locked_t":	{
		"text":		[
			["You walk over and grab the door handle.", 1.5,
			"Nothing.", 1.5, "The door is locked."]
		],
		"choice":	[
			["That's unfortunate.", ">>sargis_control_room"]
		]
	},
	"sargis_control_room_computers": {
		"text":		[
			["The computers look almost brand new and very complicated. Maybe you can figure out how to operate them."]
		],
		"choice":	[
			["Push some buttons.", "!score+7", ">>sargis_control_room_explode"],
			["Eh, maybe not.", ">>sargis_control_room"]
		]
	},
	"sargis_control_room_explode": {
		"text":		[
			["You tap a few buttons, trying to turn on one of the computers.", 2,
			"Accidentally finding the key combination for the apparent self-destruct function, you - and the computers - are blown to smithereens."]
		],
		"choice":	[
			["You're a smudge on the wall.", ">>restart"]
		]
	},
	"sargis_control_room_cameras": {
		"text":		[
			["You stand for a while, looking at the mostly static images on the camera monitors.", 2,
			"Hold on!", 1, "What was that?", 3,
			"You think you saw the shadow of creature run past one of the cameras."]
		],
		"choice":	[
			["Rub your eyes.", "!fear+2", ">>sargis_control_room_unaware"],
			["Step away.", "!score+1", "!fear+1", ">>sargis_control_room_smart"]
		]
	},
	"sargis_control_room_unaware": {
		"text":		[
			["You rub your eyes.", 1, "You were probably just seeing things.", 2,
			"You look again and see nothing.", 1, "Confident, you turn around, and a robotic creature leans down from the ceiling and bites your head off.", 2,
			"The rest of your body flops onto the floor."]
		],
		"choice":	[
			["Momma always said \"don't lose your head\"..", ">>restart"]
		]
	},
	"sargis_control_room_smart": {
		"text":		[
			["You decide that, whatever that was, you really don't want to find out."]
		],
		"choice":	[
			["Look around the room.", "?fear>=2", ">>sargis_control_room_blind"],
			["Panic!", "!fear+21", ">>sargis_control_room_bruh"],
			["Hide under one of the computer desks.", ">>sargis_control_room_cower"]
		]
	},
	"sargis_control_room_blind": {
		"text":		[
			["You look around, trying your best to find something that can help you, but you don't see anything.", 2,
			"As you're looking, suddenly you hear footsteps rapidly approaching you from behind.", 2,
			"You're about to turn, as a sharp blade is thrust into your back and out through your chest."]
		],
		"choice":	[
			["Someone's not very neighborly..", ">>restart"]
		]
	},
	"sargis_control_room_bruh": {
		"text":		[
			["You stand there like a baby and cry out of fear.", 1,
			"Through your tears you see a shadow blocking the light from the door. There's a shiny, black, robotic alien monstrosity standing at the door, grinning at you.", 2,
			"It jumps over to you in the blink of an eye, and removes your head."]
		],
		"choice":	[
			["You really liked that head.", ">>restart"]
		]
	},
	"sargis_control_room_cower": {
		"text":		[
			["You jump under one of the computers.", 2,
			"While you're hiding, you hear something enter the room. You can't help but feel curious about what it is, but is it safe?"]
		],
		"choice":	[
			["Sneak a peek.", "!score+3", ">>sargis_control_room_curious"],
			["Maybe not.", "!score+1", ">>sargis_control_room_obvious"]
		]
	},
	"sargis_control_room_curious": {
		"text":		[
			["Cautiously peeking out from under the desk, you see a shiny, black, robotic alien creeping around the room.", 2, "Trying your best not to wet yourself, you tuck yourself back under the desk, hoping for it to leave the room."]
		],
		"choice":	[
			["Remember the screwdriver?", "?#screwdriver=1", "!score+2", ">>sargis_control_room_attack_t"],
			["Hold your breath and stay very still.", "!score+1", "!@alien_encounter=1", ">>sargis_control_room_safe"],
			["Close your eyes.", ">>sargis_control_room_obvious"]
		]
	},
	"sargis_control_room_obvious": {
		"text":		[
			["You cower in fear under the desk, nervous about the thing out there.", 1,
			"After a while, you notice that there is no sound coming from the beast.", 2,
			"Trembling, you poke your head out from under the desk slowly.", 2,
			"Right in front of your face is the grinning maw of the slick, black robotic alien, who is only too happy to relieve you of your face."]
		],
		"choice":	[
			["Was that how you imagined this would turn out?", ">>restart"]
		]
	},
	"sargis_control_room_attack_t":	{
		"text":		[
			["Pulling the screwdriver from your pocket, you yell out loud and jump at the monster.", 3,
			"The alien is not impressed with your leap, choosing to reward your bravery with a claw through your gut."]
		],
		"choice":	[
			["Not a pretty sight, to be honest.", ">>restart"]
		]
	},
	"sargis_control_room_investigate": {
		"text":		[
			["You notice a key tucked under one of the computer mouse pads."]
		],
		"choice":	[
			["Take key.", "!#break room key=1", ">>sargis_control_room"],
			["leave it there.", ">>sargis_control_room"]
		]
	},
	"sargis_control_room_safe": {
		"text":		[
			["You hold your breath, eyes wide, listening for any little noise from the beast.", 2,
			"You can hear it sniffing around, pushing one of the chairs as it moves through the room.", 3,
			"Maybe it's gone...", 2,
			"Nope! You hear its claws drag against the floor again. You stay extra still.", 5,
			"Finally, you hear the beast's noises grow farther away, leaving the room. You breathe a sigh of relief and get up."]
		],
		"choice":	[
			["Exit through the door.", "?#break room key=1", "!score+1", "!fear-1", ">>sargis_break_room"],
			["Look around the room.", ">>sargis_control_room"]
		]
	},
	"sargis_break_room":	{
		"text":		[
			["%1you hear a noise, like grunting and moaning.", 2,
			"Curious,%2 you locate the source of the sound. It appears to be coming from the the bathroom."],
			["You open the door scared of what awaits you in this room. As you step into the room, closing the door behind you, ", "%1", "?@break_room=0"],
			[" and a little scared,", "%2", "?fear>4"]
		],
		"choice":	[
			["Cautiously investigate the bathroom.", "!awareness+1", ">>sargis_break_room_george"],
			["Hide behind a couch.", "!fear+1", "!@break_room=1", ">>sargis_break_room_hide"],
			["Peek through the key hole.", "!fear-2", ">>sargis_break_room_pervert"]
		]
	},
	"sargis_break_room_george":	{
		"text":		[
			["You open the door slowly and carefully, trying not to make a sound.", 1,
			"You are surprised to see a couple engaged in sexual intercourse!", 2,
			"shocked, you slam the door and bolt out, making a run for the door.", 2,
			"Almost to the door, you feel a hot punt in your back.", 0.4,
			"You fall to the ground and see a man behind you, aiming a gun at you. Slowly, everything fades to black."]
		],
		"choice":	[
			["Better respect people's private time.", ">>restart"]
		]
	},
	"sargis_break_room_hide":	{
		"text":		[
			["You sneak behind a couch, to hide and wait out whatever is going on. The sounds get louder and louder, until culminating in a high pitched scream.", 2,
			"Things quiet down.", 1, "After a while, two people - a man and a woman - come out of the bathroom. The man is clearly a guard, while the woman appears to be from the manager's office.", 2,
			"They sit down on the couch you're hiding behind and start talking.", "%1"],
			["You notice a police baton on the floor beside the couch.", "%1", "?awareness>3"]
		],
		"choice":	[
			["Take the baton.", "!fear-1", "!score+1", "!#police baton=1", ">>sargis_break_room_beat"],
			["Leave it.", "!@couple_talk=1", ">>sargis_break_room_wuss"]
		]
	},
	"sargis_break_room_beat":	{
		"text":		[
			["Silently, you reach over and grab the baton. This thing can definitely do some damage!", 1,
			"The couple are still chatting on the couch. They seem really calm, despite the lunaroid trembling around them."]
		],
		"choice":	[
			["Attack the woman with the baton.", "!score+1", ">>sargis_break_room_misogynist"],
			["Attack the man with the baton.", "!score+1", ">>sargis_break_room_superman"],
			["Stay hiding behind the couch.", "!@couple_talk=1", ">>sargis_break_room_wuss"]
		]
	},
	"sargis_break_room_superman":	{
		"text":		[
			["You jump up and whack the man across the head with the baton, and watch him flop to the ground.", 2, "The woman looks at you and screams.", 1, "You decide to give her a whack as well.", 3,
			"As you get up, you see that there's nothing useful in the room, except a glass of water."]
		],
		"choice":	[
			["Might as well drink the water and move on.", "!thirst-1", "?@sec_sw_airlock_gate=1", ">>sargis_airlock1"],
			["Might as well drink the water and move on.", "!thirst-1", "?@sec_sw_airlock_gate=0", ">>sargis_airlock_t"]
		]
	},
	"sargis_break_room_misogynist":	{
		"text":		[
			["You jump up and hit the woman over the head with the baton.", 0.5, "She's out cold!", 2,
			"You barely have time to enjoy that, however, before you hear a loud \"BANG!\"", 2,
			"Neither the man, nor his gun, seem to appreciate your handiwork."]
		],
		"choice":	[
			["Your head is leaking vital fluids.", ">>restart"]
		]
	},
	"sargis_break_room_wuss":	{
		"text":		[
			["You decide it is best to just wait it out.", 1.5,
			"The couple keeps talking. It seems like the conversation goes on forever.", 2,
			"%1", "%2"],
			["As you get up from behind the couch, all you see of value in the room is a glass of water.", "%2", "?@couple_talk=9"],
			["\"Do you really think the station will implode?\" you hear the woman ask, to which the man responds that he does...", "%1", "?@couple_talk=2"],
			["They just keep switching between talking about their imminent destruction, and random inanities..", "%1", "?@couple_talk=3"],
			["\"It's too bad we didn't do this sooner..\" the man says. The woman doesn't seem to respond.", "%1", "?@couple_talk=5"],
			["They sure do go on about nothing!", "%1", "?@couple_talk=6"],
			["\"Wanna go again?\" says the woman.", "%1", "?@couple_talk=8"],
			["They get up off the couch and go back into the bathroom. Some people's priorities, really...!", "%1", "?@couple_talk=9"]
		],
		"choice":	[
			["Keep waiting..", "!@couple_talk+1", "?@couple_talk<8"],
			["Attack the woman with the baton.", "!score+1", "?@couple_talk<9", "?#police baton=1", ">>sargis_break_room_misogynist"],
			["Keep waiting..", "!@couple_talk+1", "!score+1", "?@couple_talk=8"],
			["Attack the man with the baton.", "!score+1", "?@couple_talk<9", "?#police baton=1", ">>sargis_break_room_superman"],
			["Grab the water and move on.", "!thirst-1", "?@couple_talk=9", "?@sec_sw_airlock_gate=1", ">>sargis_airlock1"],
			["Grab the water and move on.", "!thirst-1", "?@couple_talk=9", "?@sec_sw_airlock_gate=0", ">>sargis_airlock_t"]
		]
	},
	"sargis_airlock_t":	{
		"text":		[
			["You step out of the room, but are faced with nothing but a big, blank wall.", 2,
			"You hear a *CLUNK* behind you, and you turn quickly, only to see that the door behind you has been replaced by a similar big, blank wall.", 3,
			"Suddenly, the two walls start moving towards each other.", 0.5,
			"%1they don't seem terribly concerned, nor hindered, by your standing between them."],
			["Even though you try to block them with the baton, ", "%1", "?#police baton=1"]
		],
		"choice":	[
			["You're 2-dimensional.", ">>restart"]
		]
	},
	"sargis_break_room_pervert":	{
		"text":		[
			["You decide to peek through the keyhole to see what's beyond the door.", 2,
			"What you see is two people going at it in the shower!", 1,
			"You question why these people aren't trying to escape, given the sorry state of the lunaroid. Maybe they're just resigned, and decided to go out with a bang.", 2,
			"You think to yourself that you should get moving, but somehow can't help but keep watching, interested in what's going on in there.", 3,
			"That's when you feel the cold metal of a gun pressed against your head. You barely have time to turn your head, before a bullet tears through your skull, leaving you well ventilated."]
		],
		"choice":	[
			["Nothing good comes from being a peeping tom.",">>restart"]
		]
	},
	"sargis_shaft_death1":	{
		"text":		[
			["You decide you don't need the extra burden of a wounded man, and leave him behind as you run towards the shaft entrance.", 2,
			"You don't get more than a few feet, before a big, ugly, robotic alien emerges around the corner ahead of you.", 1,
			"You try to get to the shaft, but the alien is quicker than you."]
		],
		"choice":	[
			["Crispy human must be a delicacy where ever it's from.", ">>restart"]
		]
	},
	"sargis_shaft_death_run":	{
		"text":		[
			["You and the guard make a break for the maintenance shaft, but with the extra weight, you move like a crippled tortoise.", 2,
			"The robotic alien helps you along by swiftly melting away all excess fat."]
		],
		"choice":	[
			["Not your favorite diet.", ">>restart"]
		]
	},
	"sargis_shaft_death2":	{
		"text":		[
			["Eager to escape, you run through the secret passageway.", 2,
			"In the control room below, the guards hear your footsteps.", 1, 
			"They fire a barrage of laser blasts up through the ceiling and into the passageway. You'd enjoy the light-show, if you weren't so busy dying from it."]
		],
		"choice":	[
			["I guess the high ground doesn't always give an advantage.", ">>restart"]
		]
	},
	"sargis_shaft_death3":	{
		"text":		[
			["%1", 2,
			"%2you turn around and find yourself face to face with the wide grin of %3 big, ugly, robotic alien creature.", 2,
			"You inhale to scream, but find you don't have time for that, now that you %4are engulfed in flame."],
			["You help the guard up, and help him over towards some containment units where he can hide in relative safety.", "%1", "?@alien_passed=0"],
			["After gently setting him down and reassuring him that he'll be okay, ", "%2", "?@alien_passed=0"],
			["a", "%3", "?@alien_passed=0"],
			["the", "%3", "?@alien_passed=1"],
			["- and the guard - ", "%4", "?@alien_passed=0"],
		],
		"choice":	[
			["You're a walking gyro. Delicious!", ">>restart"]
		]
	},
	"sargis_shaft_death4":	{
		"text":		[
			["You continue along the path to your left.", 1,
			"After a few feet, the floor beneath you begins to wobble and then crumble, and you plummet head first into the floor several stories below."]
		],  
		"choice":	[
			["Thankfully your face and several vertebra broke your fall.", ">>restart"]
		]
	},
	"sargis_shaft_death5":	{
		"text":		[
			["Keeping right, you continue along the pathway.", 2,
			"After a while the pathway widens up into a proper hallway. You turn a corner, and walk straight into a patrol of guards.", 2,
			"You attempt to act like their commanding officer. They do not seem convinced by your prisoner's drapes, however."]
		],
		"choice":	[
			["So this is what Swiss cheese feels like.", ">>restart"]
		]	
	},
	"sargis_shaft1":	{
		"text":		[
			["Moving from the cafeteria and down the hallway you see what appears to be a maintenance shaft. You look a little closer, and despite the flashing red lights and blaring sirens, you see a speck of light. Maybe you can finally get off this damn rock.", 2,
			"Between you and the entrance to the maintenance shaft, you notice a guard who has been wounded and left for dead.", 1, "He sees you and cries out 'HELP ME PLEASE! I'll get you where you need to go, just help me move!'. You hesitate.", 1.5, "You hear something approaching from further down the hallway - - something big, and no-doubt ugly."]
		],
		"choice":	[
			["Help the injured guard and bring him with you.", ">>sargis_shaft2", "!awareness+2", "!thirst+1", "!fear-1", "!score+1", "!fatigue+3"],   # you help the guard, and then you have to hide, run or 
			["Help the injured guard, but leave him in a safe place.", "!score+1", "!fear-2", ">>sargis_shaft_death3"],   #  the guard gets up, and is a distraction for the alien
			["ignore the injured guard and leave him to die.", "!awareness-1", "!fear+1", ">>sargis_shaft_death1"]    # you run away, and the alien eats you
		]
	},
	"sargis_shaft2":	{
		"text":		[
			["You help the guard get up and out of harm's way. From the hallway ahead you hear the noise getting closer.", 2,
			"You notice a loose panel. It appears to be covering up a small, empty compartment in the wall.", 1,
			"You pull at the side of the panel and it opens up. This compartment looks just big enough for two people.",
			"You and the guard squeeze yourselves into the compartment, pulling the panel closed in front of you.", 2,
			"Around the corner down the hallway, you can see a big, ugly, robotic alien emerge, scanning walls and floors with a laser scanner as it moves through the hall. Any opening it finds, with even the smallest suspicion of life, it blasts with a burst of fire, incinerating anything it detects.", 3,
			"You feel the area around you getting warmer. A cooler breeze is coming from the maintenance shaft not far away."]
		],
		"choice":	[	
			["Ditch the guard and make a break for the shaft.", "!fear+1", ">>sargis_shaft_death1"],
			["Help the guard up and make for the shaft.", ">>sargis_shaft_death_run", "!fatigue+1"],
			["Stay hidden with the guard in the compartment.", ">>sargis_shaft3", "!intelligence+1", "!fear+1", "!thirst+1"]
		]
	},
	"sargis_shaft3":	{
		"text":		[
			["The robotic alien slowly moves closer to the compartment, beeping noises mixing with snarls as it scans for any sign of life.", 2,
			"It pauses just outside the compartment. Both you and the guard hold your breath and close your eyes. Is this the end?", 3,
			"With a click, a whirr, and a grunt, the alien starts moving again, gliding past your compartment and through the door, out of sight.", 1,
			"Both of you breathe a sigh of relief.", 2,
			"Now that imminent danger seems to have passed, you climb back out of the compartment and look toward the shaft. You see the robotic alien has left pretty much everything on fire. There is ared hot steel beam blocking the entrance to the shaft.", 3,
			"The guard shows you the entrance to a secret passageway to the airlocks. However, he tells you, it goes right above the control room, which is heavily patrolled by guards."]
		],
		"choice":	[
			["Enter the passageway and run toward the airlocks.", "!score+2", ">>sargis_shaft_death2"],
			["Turn around and look for another way.", "!@alien_passed=1", ">>sargis_shaft_death3"],
			["Heed the guard's warning, and go through the passageway very quietly.", "!awareness-2", "!score+1", ">>sargis_shaft4"]
		]
	},
	"sargis_shaft4":	{
		"text":		[
			["Thanking the wounded guard for his help, you quietly you make your way through the passageway, making sure not to alert the other guards below.", 2,
			"Eventually you come at a crossroads. The passageway splits into two different directions. There is also a hatch, allowing you to move down into the control room.", "%1"],
			["You're starting to feel pretty hungry.", "%1", "?#steak and cake=1", "?fatigue>3"],
			["You snarf down the steak and the cake. You wish you could say it was delicious...", "%1", "?@ate_steak=1"]
		],
		"choice":	[
			["Keep right and continue along the passageway.", ">>sargis_shaft_death5"],
			["Follow the passageway to the left.", ">>sargis_shaft_death4"],
			["Look through the grating on the hatch below.", ">>sargis_shaft5"],
			["Now is as good at time as any to eat that steak and cake.", "?#steak and cake=1", "!fatigue-3", "!#steak and cake=0", "!@ate_steak=1"]
		]
	},
	"sargis_shaft5":	{
		"text":		[
			["You peek through the grating into the room below. Surprisingly, it appears completely deserted.", 1,
			"It seems the guards have all left to tend to some more pressing issue -- perhaps getting off this lunaroid."]
		],
		"choice":	[
			["Ignore the room, and follow the passageway to the right.", ">>sargis_shaft_death5"],
			["Better just continue along passageway to the left.", ">>sargis_shaft_death4"],
			["Open the hatch and lower yourself into the control room.", "!score+1", "!awareness+1", ">>sargis_control_room"],
			["Now is as good at time as any to eat that steak and cake.", "?#steak and cake=1", "!fatigue-3", "!#steak and cake=0", "!@ate_steak=1"]
		]
	},
	"sargis_airlock_death1":	{
		"text":		[
			["You press the button again, and hear an ear-piercing beep.", 1,
			"Congratulations, you managed to fry the panel and electrocute yourself."]
		],
		"choice":	[
			["What a shocking way to go.", ">>restart"]
		]
	},
	"sargis_airlock_death2":	{
		"text":		[
			["You walk over and pull the lever to open the air vent.", 2,
			"Immediately the room depressurizes and you get blown out of the space prison, into the vast emptiness of the unknown."]
		],
		"choice":	[
			["You'd try to enjoy the view, if your eyeballs hadn't frozen solid.", ">>restart"]
		]
	},
	"sargis_airlock_death3":	{
		"text":		[
			["You try to ignore the banging, though it's getting louder and louder.", 2,
			"Suddenly an escaped alien prisoner bursts out of the airlock door with guards chasing it.",
			"It picks you up and uses you as a human shield against the hail of fire from the guards.", 2,
			"The guards seem less than impressed."]
		],
		"choice":	[
			["At least you had some use...", ">>restart"]
		]
	},
	"sargis_airlock_death4":	{
		"text":		[
			["You walk over to the airlock door to find out what's banging.", 1,
			"You barely reach it, as it it flies open, and an alien creature storms out, followed by armed guards, all of which proceed to trample you.", 3,
			"Remember that scene at the end of the 'Spongebob' movie, when Plankton gets stampeded by people wearing his bucket helmets, and they had to scrape him off the floor with a tiny shovel?", 2,
			"That's you."]
		],
		"choice":	[
			["A bit of a flat feeling.", ">>restart"]
		]
	},
	"sargis_airlock_death5":	{
		"text":		[
			["You make a break for it, forgetting in the heat of the moment you tied yourself to a steel beam.", 2,
			"When the guards spot you, they waste neither time, nor laser bolts."]
		],
		"choice":	[
			["Like fish in a barrel.", ">>restart"]
		]
	},
	"sargis_airlock_death6":	{
		"text":		[
			["You stand completely motionless, in the hope that you won't get spotted.", 2,
			"Sadly, this isn't Jurassic Park."]
		],
		"choice":	[
			["They definitely spared some expenses.", ">>restart"]
		]
	},
	"sargis_airlock1":	{
		"text":		[
			["You walk into an area that seems completely strange to you.",
			"All you are able to see around you are flashing red lights and a large, domed ceiling that reveals the vast blankness of space.", 2,
			"As you look around the room, you see a console with a big red button labeled \"AIRLOCK\".", "%2", "%1"],
			["You press the button, and nothing happens.", "%1", "?@airlock_button=1"],
			["There is a long rope rolled up next to the console.", "%2", "?#long rope=0"],
			["You pick up the rope and swing it over your shoulder.", "%2", "?#long rope=1"]
		],
		"choice":	[
			["Press the button.", "?@airlock_button=0", "!@airlock_button=1"],
			["Take the rope.", "?#long rope=0", "!#long rope=1"],
			["Press the button again.", "?@airlock_button=1", ">>sargis_airlock_death1"],
			["Whack the console with the baton.", "?@airlock_button=1", "?#police baton=1", "!#police baton=0", ">>sargis_airlock1_baton_t"],
			["Wait a moment, to see what happens.", "?@airlock_button=1", ">>sargis_airlock4"],
			["Look around for another exit.", "?@airlock_button=1", ">>sargis_airlock2"]
		]
	},
	"sargis_airlock1_baton_t":	{
		"text":		[
			["You pull out the police baton and smash it into the console.", 1, "You've managed to break the baton in half, doing absolutely nothing to the console."]
		],
		"choice":	[
			["What's it made of, balsa wood?", ">>sargis_airlock1"]
		]
	},
	"sargis_airlock2":	{
		"text":		[
			["Seems the button is broken. Does anything work on this wretched rock?", 2,
			"You look around for other possible options. You spot a small air vent to the left."]
		],
		"choice":	[
			["Go to the air vent and open it.", ">>sargis_airlock_death2"],
			["Secure yourself with the rope, and go open the air vent.", "?#long rope=1", "!score+1", "!intelligence+1", "!fear-1", "!#long rope=0", ">>sargis_airlock3"]
		]
	},
	"sargis_airlock3":	{
		"text":		[
			["You tie the rope securely around your waist, as well as around a steel beam next to the vent.",
			"Bracing yourself, you prepare to pull the lever for the air vent. Just then, you hear a loud banging on the airlock door.", 2,
			"You pull the level, just as the door bursts open, an alien prisoner swooping in, chased by guards firing at him with their laser guns."],
		],
		"choice":	[
			["Jump into the air vent to avoid getting caught.", "!fear+1", "!score+1", ">>sargis_airlock5"],
			["Make a run for the door!", ">>sargis_airlock_death5"],
			["Don't move! Maybe the guards won't spot you.", "!fear+4", ">>sargis_airlock_death6"]
		]	
	},
	"sargis_airlock4":	{
		"text":		[
			["You wait around, hoping for the button to have some effect.", 2,
			"Suddenly you hear a loud banging on the airlock door."],
		],
		"choice":	[
			["What's that banging?", ">>sargis_airlock_death4"],
			["Whatever it is, it can't be good.", ">>sargis_airlock_death3"]
		]
	},
	"sargis_airlock5":	{
		"text":		[
			["You leap into the air vent, safely secured to the beam next to it.", 1,
			"the alien and guards run past you, seemingly oblivious to the whoosh from the vent.", 2,
			"Now that the airlock door is broken, you can escape through."]
		],
		"choice":	[
			["Pull yourself out of the vent and head for the airlock.", ">>sargis_final_podbay"]
		]
	},
	"sargis_cell01":	{
		"text":		[
			["%2",
			"%3Alarms are blaring all around you, with ominous red lights flashing brightly.", 1,
			"You are%5 in a cell on the orbital Prison Lunaroid. The door to the cell is open. You have no idea why you are here.", 
			"%4you can't help but notice that the ground is trembling intermittently.. This seems bad!", 
			"%1"],
			["You notice a screwdriver by the wall just outside the cell.", "%1", "?awareness>0", "?#screwdriver<1"],
			["*BLAARP* *BLAARP* *BLAARP* *BLAARP*", "%2", "?@exit_cell=0"],
			["You wake up, feeling dizzy. ", "%3", "?@exit_cell=0"],
			["As you get up from the floor, ", "%4", "?@exit_cell=0"],
			[" on the floor", "%5", "?@exit_cell=0"]
		],
		"choice":	[
			["Take the screwdriver.", "!#screwdriver=1", "!score+1", "?awareness>0", "?#screwdriver<1"],
			["Go out of the cell.", ">>sargis_cell_hall01", "!@exit_cell=1"],
			["Look around.", "!awareness+1", "?awareness<1"],
			["Go lay down on the cell bunk, try and sleep it off..", "!score+10", ">>sargis_sleep_death"]
		]
	},
	"sargis_sleep_death":	{
		"text":		[
			["You flomp yourself down onto the bunk and close your eyes.. All this is too much to handle, and you just want to rest. Maybe when you wake up all will be better.",
			"", 2, "While you sleep, the lunaroid crackles and buckles around you. You don't have long to react to the cold of space around you, as you freeze in a matter of seconds. Floating through the emptiness, the last image you see is the planet off in the distance.",
			4, "By the time your frozen body enters its atmosphere, you are already long gone. Which is good, kinda, since it means you don't get to feel yourself burning up during entry.", 2]
		],
		"choice":	[
			["You died. Well done.", ">>restart"]
		]
	},
	"sargis_cell_hall01":	{
		"text":		[
			["You're outside the cell. Gray, metallic halls stretch in both directions. The alarms seem even louder out here.",
			"The halls are relatively dim, aside from the flashing, red lights. However, the hall stretching to the left of the cell seems to have a blue tinge at the end of it."]
		],
		"choice":	[
			["Go back in the cell.", ">>sargis_cell01"],
			["Walk down the right stretching hall.", "!score+1", ">>sargis_cell_hall02"],
			["Walk left, towards the blue tinge.", "!score+2", ">>sargis_fake_escape01"]
		]
	},
	"sargis_fake_escape01":	{
		"text":		[
			["You make your way down the hall towards the blue. As you get closer, and the blue light gets brighter, the alarms seem less loud, and the red flashing is also becoming less intrusive.",
			1, "Finally you make it to a clearing and, what's this?", 1,
			"An escape pod!! Now, that is convenient!",
			"%1"],
			["Oh, but what's this? This escape pod does seem a bit slanted in its hold. And it has several little warning lights flashing. And there's a crack in the window..", "%1", "?@pod_check=1"]
		],
		"choice":	[
			["Go back towards the cell.", ">>sargis_cell_hall01"],
			["Get in the pod. Let's get off this rock!", ">>sargis_fake_escape02"],
			["Examine the pod closer.", "!score+1", "?@pod_check=0", "!awareness+1", "!@pod_check=1"]
		]
	},
	"sargis_fake_escape02":	{
		"text":		[
			["Ducking into the escape pod, you slip into the seat. Not the most comfortable seat you've ever rested your behind in, but it beats the cell floor from before.",
			1, "There's a big, friendly button, in the middle of what appears to be the control console. It's labeled 'LAUNCH'. %1"],
			["Surrounding the big button are several little flashing lights. What could that mean? You notice a hissing sound behind your head.", "%1", "?@pod_check=1"]
		],
		"choice":	[
			["Slam that LAUNCH button!", "!score+3", ">>sargis_fake_escape_death"],
			["Get back out of the escape pod.", ">>sargis_fake_escape01"]
		]
	},
	"sargis_fake_escape_death":	{
		"text":		[
			["With great determination you pound your fist into the big 'LAUNCH' button.", 1,
			"With a hiss, the pod door slides closed, lights flashing left and right. Getting out of here is going to be great!", 2,
			"The pod starts sliding out of its hold, the sound of metal scraping against metal quite audible behind the hissing. You hear a loud 'CLUNK' and feel the pod jerk down.", 2, 
			"Paused for a moment, you look around. Before you can see what made that noise, the pod starts moving again, the scraping now more of a rattle. The hold releases the pod and you shoot into space, away from the lunaroid. You're finally free!", 4,
			"Suddenly, the window behind you cracks and blows out, letting the chill of outer space in to keep you company.", 2,
			"Frozen stiff, but otherwise comfortably seated in your titanium coffin, you drift through space aimlessly.. Who knows, maybe someday someone will find you and thaw you out."]
		],
		"choice":	[
			["All that for nothing..", ">>restart"]
		]
	},
	"sargis_cell_hall02":	{
		"text":		[
			["The hall stretches far in front of you. Every 10 or 20 feet there's a cell door, closed and locked. No one seems to be inside any of them. Did they all get out? Or were you always alone in this part of the complex?",
			"After walking past a few doors you stop in front of the next one. It looks exactly like the ones you passed.", "%1"],
			["The sad remains of a broken screwdriver litter the floor.", "%1", "?@driver_gone=1"],
			["Hold on, though.. Upon further inspection the door seems to be ever-so-slightly ajar.", "%1", "?@hall_door=1"],
			["You jam the screwdriver into the door crack and pull. There's a loud snap as the screwdriver breaks in half.", "%1", "?@door_driver=1"]
		],
		"choice":	[
			# Man, these choices became convoluted to get the result I wanted.
			# Important thing is that it works, I guess.
			["Go back towards the cell.", "!@driver_gone=1", "!@door_driver=0", "?@driver_gone=0", "?@door_driver=1", ">>sargis_cell_hall01"],
			["Continue on down the hall.", "!@driver_gone=1", "!@door_driver=0", "?@driver_gone=0", "?@door_driver=1", ">>sargis_cell_hall03"],
			["Go back towards the cell.", "?@door_driver=0", ">>sargis_cell_hall01"],
			["Continue on down the hall.", "?@door_driver=0", ">>sargis_cell_hall03"],
			["Look closer at the door.", "!@hall_door=1", "?@hall_door=0", "?@door_driver=0", "?@driver_gone=0"],
			["Use screwdriver on door.", "!@door_driver=1", "!@hall_door=0", "!score-1", "!#screwdriver=0", "?@hall_door=1", "?#screwdriver>0"]
		]
	},
	"sargis_cell_hall03":	{
		"text":		[
			["After a while you come to another door. This one is different - not a cell door.", 1,
			"Looking above it, you see a sign that says \"GUARD STATION\".", 2,
			"This is probably the guard station."]
		],
		"choice":	[
			["Better head back away from here.", "!fear+1", ">>sargis_cell_hall02"],
			["Enter the guard station.", "!score+1", "!intelligence+1", ">>sargis_guard_station"]
		]
	},
	"sargis_final_podbay":	{
		"text":		[
			["You enter into what appears to be another very large room. Every sound echoes around you, mixing in with the growing rumble from around the lunaroid.", 2, "There are some dim lights here and there, but all in all the room is pretty dark.", "%1"],
			["There is a bright panel next to the door where you came in. On the panel is a big, blue button, labeled \"LIGHTS\".", "%1", "?@podbay_look=1", "?@pod_lights=0"]
		],
		"choice":	[
			["Look closer at the lights behind you.", "?@podbay_look=0", "!@podbay_look=1", "?@pod_lights=0"],
			["Press the button to turn on the lights.", "?@podbay_look=1", "!score+1", "@!pod_lights=1", ">>sargis_final_podbay_lights"],
			["Go back from whence you came.", ">>sargis_airlock5"]
		]
	},
	"sargis_final_podbay_lights":	{
		"text":		[
			["You are in a very large, echoey room. The lunaroid rumbles around you.", 1, "All along the far wall, you see rows upon rows of little doors, leading to individual escape pods.", 2, 
			"%1", "%2"],
			["A few feet in front of you is a massive control panel. It looks like it might be controlling the pods.", "%1", "?@pod_control_look=0"],
			["The control panel in front of you has a row of buttons with lights, most of which are red. This seems to indicate whether the numbered pod is available or already launched.", "%1", "?@pod_control_look=1"],
			["The indicator for pod #1 is red, showing that this pod is already launched.", "%2", "?@pod1=1", "?@pod2=0"],
			["The indicator for pod #2 is red, showing that this pod is also already launched.", "%2", "?@pod2=1", "?@pod3=0"],
			["The indicator for pod #3 is red, showing that also this pod is launched.", "%2", "?@pod3=1", "?@pod4=0"],
			["The indicator for pod #4 is red, showing that the pod is already launched.", "%2", "?@pod4=1", "?@pod5=0"],
			["The indicator for pod #5 is green, showing that the pod is available.", "%2", "?@pod5=1"]
		],
		"choice":	[
			["Examine the control panel.", "?@pod_control_look=0", "!@pod_control_look=1"],
			["Check the controls for pod #1.", "?@pod_control_look=1", "?@pod1=0", "!@pod1=1"],
			["Check the controls for pod #2.", "?@pod_control_look=1", "?@pod2=0", "?@pod1=1", "!@pod2=1"],
			["Check the controls for pod #3.", "?@pod_control_look=1", "?@pod3=0", "?@pod2=1", "!@pod3=1"],
			["Push the button to activate pod #5.", "?@pod_control_look=1", "?@pod5=1", "!score+1", ">>sargis_final_pod5_pushed"],
			["Go back and turn the lights back off.", "!score-1", "!@pod_lights=0", ">>sargis_final_podbay"],
			["Check the controls for pod #4.", "?@pod_control_look=1", "?@pod4=0", "?@pod3=1", "!@pod4=1"],
			["Check the controls for pod #5.", "?@pod_control_look=1", "?@pod5=0", "?@pod4=1", "!@pod5=1", "!score+1"]
		]
	},
	"sargis_final_pod5_pushed":	{
		"text":		[
			["With a satisfying click, followed by an optimistic beep as you push the button, the light indicator for pod #5 starts flashing bright green.", 2,
			"On the far wall you hear a hiss and a hum as the door to pod #5 slides open, warm lights filling the interior of the pod.",
			"%1"],
			["Pushing the button again you realize that nothing happens - the pod is already activated.", "%1", "?@pod5_double=1"]
		],
		"choice":	[
			["Do a little celebratory dance, while humming \"Celebrate!\" by Kool and the Gang to yourself.", "!score+5", ">>sargis_final_tardy"],
			["Run to the now open escape pod.", "!score+2", ">>sargis_final_pod5"],
			["Push the button for pod #5 again.", "!@pod5_double=1", "?@pod5_double=0"],
			["This is too much. Go back out of the room.", ">>sargis_airlock5"]
		]
	},
	"sargis_final_pod5":	{
		"text":		[
			["You dart over to the open pod and climb inside.", 1.5,
			"Sinking into the seat, you briefly ponder how great it is to be off your feet. Hopefully this pod will take you away from this floating disaster and to safety.", 1.75,
			"%2", "In front of you there's a big, friendly button, in the middle of what appears to be the control console. It's labeled 'LAUNCH'.", "%1"],
			["You see nothing else. Everything looks good to go!", "%1", "?@pod5_check=1"],
			["This seat is lumpy! Are you sitting on something?", "%2", "?#screwdriver=1", "?@screwmoved=0"],
			["With the screwdriver out of the way, this seat is really quite comfortable.", "%2", "?#screwdriver=1", "?@screwmoved=1"]
		],
		"choice":	[
			["The screwdriver is in your pocket, isn't it?", "?#screwdriver=1", "?@screwmoved=0", "!@screwmoved=1"],
			["Go back out of the pod.", ">>sargis_final_pod5_pushed"],
			["Examine the pod further.", "!@pod5_check=1", "?@pod5_check=0", "?intelligence>1"],
			["Smash that \"LAUNCH\" button!", "!score+1", ">>sargis_final_escape"]
		]
	},
	"sargis_final_escape":	{
		"text":		[
			["Holding your breath, you place your hand on the \"LAUNCH\" button and press it down.", 2,
			"With an optimistic hum, the pod door whirrs closed in front of you.", 0.5, "Automatic safety belts glide over your shoulders, keeping you firmly seated.", 2,
			"The foor fully closed, there's a loud CLUNK as the pod releases from its catch. For a few moments, you feel it slowly sliding out away from the chamber.", 2,
			"You watch as the pod clears the launch tube. Space twinkles around the front viewport.", 1,
			"You feel a jolt as the thrusters kick in, shooting the pod at great speed away from the lunaroid.", 2,
			"Through the viewport you see the station growing smaller with distance.", 0.25,
			"Seems you got out not a moment too soon. A split forms not far from where your pod launched. The lunaroid breaks in half with a completely soundless boom, scattering the rest of its contents through space."]
		],
		"choice":	[
			["Am I safe?", ">>sargis_final_final_escape"]
		]
	},
	"sargis_final_tardy":	{
		"text":		[
			["Grooving to the tune in your head, you suddenly sense someone near you.", 2,
			"You turn and see, dancing along next to you, a large, robotic alien creature.", 2,
			"A second or two passes, when it notices you stopped dancing, and it stops as well. For a few moments, you stare at the alien, and it stares back at you through its laser visor.", 2,
			"After a while, the alien's maw broadens into a wide, disgusting grin. This is the last thing you see."]
		],
		"choice":	[
			["Everyone's a critic...", ">>restart"]
		]
	},
	"sargis_final_final_escape":	{
		"text":		[
			["yeah.. You made it.", 3, "Congratulations!", 3]
		],
		"choice":	[
			["I wanna go again!", ">>restart"]
		]
	}
}

print("'Story' Loaded")


# How to Build a Story Dict
# -=======================-
#
# Required keys are:
# "title" - the title of the game
# "start" - the scene a new game starts in
# and at least one scene, built like so:
# "sceneID":	{ Unique ID so the game can find the scene
#		"text": 	[	At least one list with string(s) describing the scene to the player.
#								More lists can be added for optional text.
#		],
#		"choice":	[ At least one list with strings describing a choice and what happens if chosen.
#		]
# }
#
# In the "text" section:
# The initial text string(s) can contain several %# (i.e. %1, %2, etc.) markers,
# that will be replace with the optional lines below, if conditions are met.
#
# Symbol meanings:
# % - optional sentence ("text" section only)
#				In main text string(s), %# signifies where the optional sentences go.
#				In the following text lists, the % signifies which position above it goes into.
# !	-	change a stat ("choice" section only)
#				format: "!stat+1" where "stat" is the name of the stat to change,
#														the modifier can be "+" (increase stat), "-" (decrease),
#																						 or "=" (set to precise value)
#														followed by the number to change by/to.
# ? - check a stat (both sections)
#				format: "?stat<2". Similar to "!", except conditionals instead of modifiers:
#														"<" less than, "<=" less than or equal to
#														">" greater than, ">=" greater than or equal to
#														"=" equal to
#														followed by the number to check against.
# >> - Go to ("choice" section only)
#				format: ">>scene" where "scene" is the sceneID of the scene you want to go to.
#
# Stat symbols:
# no symbol = normal stat.
# "#" symbol = inventory item.
# "@" symbol = game switch. Can be used where something might be depending on
#														something else, but independent of stats/inventory.

