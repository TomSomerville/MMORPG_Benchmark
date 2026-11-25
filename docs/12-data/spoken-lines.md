# Spoken Lines — voice script, boss lines, books and chatter

[← Data Index](00-data-index.md) · Audio list: [Audio §8](../10-art/09-audio.md#8-npc-voice-barks) · Pipeline: [P19 voice lines](../14-asset-pipeline/03-audio-pipelines.md) · Other text: [Game Text](game-text.md) · [Quest Text](../06-quests/text/00-quest-text-index.md)

The audio list counts voice lines and the voice pipeline says it reads "the written lines". This page is those lines: every bark, story line, announcer call and boss line that is spoken, plus the readable books and the street chatter that are text only. Each spoken line is also its own subtitle.

## 1. Rules

| Rule | Detail |
|---|---|
| Ids | `vo.<set>.<line>` for spoken lines · `book.<n>` · `chatter.<place>.<n>`. All are rows in the string table |
| Spoken or text | Sections 2 to 5 are voiced by pipeline P19. Sections 6 and 7 are text only |
| Asset count | The voice count in the asset manifest is the number of voiced lines in sections 2 to 5 of this page: 142 barks, 20 story lines, 14 announcer lines and 72 boss lines, about 250 in all. Emote lines in italics are text and are not voiced. The eight player error lines per body in the audio list (32 lines, such as "Out of range") are voiced as well and are listed in the [Asset Manifest](../15-asset-manifest/00-manifest-index.md), which has one row for every voiced line. Where the audio list's estimate differs, this page stands |
| Delivery | Barks are 1 to 4 words, said plainly. Boss lines are said once per fight at the moment named, never repeated within 20 seconds |
| Boss lines in chat | Shown as a creature yell (red) with the boss's name, and heard by everyone in the room |
| Beasts and constructs with no speech | Use the emote lines given, shown in orange, with a creature sound from the sound list |

### Pronunciation list for the voice pipeline

Halcyra *hal-SEER-ah* · Meridia *meh-RID-ee-ah* · Khazrun *KAZ-roon* · Sundrel *SUN-drel* · Solhaven *SOL-hay-ven* · Aurelian *aw-REE-lee-an* · Vaelric *VALE-rik* · Tor Vael *tor VALE* · Seraphine Vael *SEH-rah-feen VALE* · Ashgrave *ASH-grave* · Maelis Dorne *MAY-liss DORN* · Brunhild Deepscroll *BROON-hild* · Ysolde Thornwake *ee-ZOLD* · Corvane *kor-VAIN* · Korvash *KOR-vash* · Ilyra *ih-LEER-ah* · Ghul'thar *GOOL-thar* · Khardun *KAR-doon* · Thurga *THUR-gah* · Sael'anor *SALE-ah-nor* · Pyrraxis *pih-RAK-sis* · Gorrath *GOR-ath* · Aubrec *OH-brek* · Kray *KRAY*.

## 2. NPC barks

Each voice has three greetings, two farewells, two annoyed lines (after being clicked five times quickly) and one vendor line.

| Voice | Greetings | Farewells | Annoyed | Vendor |
|---|---|---|---|---|
| Human commoner, male | "Morning." · "Yes?" · "What is it?" | "Dawn keep you." · "Mind the road." | "I've work to do." · "Enough, now." | "Have a look." |
| Human soldier, male | "Citizen." · "Report." · "Speak up." | "Carry on." · "Stay sharp." | "Hands off." · "Move along." | "Queen's prices." |
| Human scholar, male | "Ah. Yes?" · "Quietly, please." · "You have a question." | "Read more." · "Good day." | "I was mid-sentence." · "Must you?" | "Handle it gently." |
| Human commoner, female | "Hello, love." · "Yes?" · "Need something?" | "Safe home." · "Dawn keep you." | "That's enough." · "I'm busy." | "Fresh today." |
| Human soldier, female | "Citizen." · "State your business." · "Go on." | "Eyes open." · "Dismissed." | "Don't push it." · "Step back." | "Standard issue." |
| Human scholar, female | "Yes, yes?" · "One moment." · "You again." | "Mind the shelves." · "Good day." | "I am counting." · "Stop that." | "No haggling." |
| Mountain dwarf, male 1 | "Aye?" · "Stone keep you." · "Well?" | "Forge warm you." · "Go on, then." | "Mind the beard." · "I'm not an anvil." | "Good steel." |
| Mountain dwarf, male 2 | "Speak." · "What d'you want?" · "Hm." | "Keep your edge." · "Off with you." | "Quit that." · "Bah." | "Made right." |
| Mountain dwarf, female 1 | "Aye, what?" · "Stone keep you." · "Out with it." | "Forge warm you." · "Watch the lintel." | "Do I look like a bell?" · "Enough." | "Fair weight." |
| Mountain dwarf, female 2 | "Well met." · "Aye?" · "You're in my light." | "Deep roads." · "Mind your head." | "Poke someone else." · "Tch." | "No rust on it." |
| Hill dwarf, male 1 | "Mornin'." · "How's the road?" · "Ah, hello." | "Good harvest." · "Mind the ewes." | "Easy, now." · "I've hay to turn." | "Picked this week." |
| Hill dwarf, male 2 | "Well now." · "Aye?" · "Sit, if you like." | "Full barns to you." · "Go easy." | "That's plenty." · "Leave off." | "Brewed proper." |
| Hill dwarf, female 1 | "Hello, dear." · "Aye?" · "Come in, come in." | "Good harvest." · "Mind how you go." | "Now, now." · "I'll fetch the broom." | "Still warm." |
| Hill dwarf, female 2 | "Mornin'." · "What's the news?" · "Yes, dear?" | "Fair weather." · "Go easy." | "Not the hat." · "Enough of that." | "Best in the dale." |

| Voice | Greeting | Warning | Attack call |
|---|---|---|---|
| Human guard | "Keep the peace." · "Move along." | "Stand down." · "Last warning." | "To arms!" · "For Solhaven!" |
| Dwarf guard | "Mind yourself." · "Aye, go on." | "Blades away." · "Don't try it." | "Shields!" · "For the Thane!" |

| Voice | Six lines |
|---|---|
| Elf envoy (Ysolde Thornwake) | "You walk loudly." · "The Choir hears you." · "Say it, then." · "Go softly." · "We are not friends." · "Not yet." |
| Ogre (Mugga, Hrokk) | "Small one." · "What?" · "Talk fast." · "Go." · "No touch." · "Stonemaw remembers." |
| Covenant legate (Corvane) | "Citizen of the lesser realm." · "Speak. I have time." · "How brief you are." · "Until the next age." · "Do not presume." · "The Empire endures." |

## 3. Story lines

Voiced once each, at the quest moment named.

| Id | Speaker | Moment | Line |
|---|---|---|---|
| vo.story.01 | Hale Morrow | Dying, BM-16 | "It burns clean. You'll beg for it." |
| vo.story.02 | Magister Ashgrave | Engaged, Brandspire | "A crown for every brow. I only asked for mine first." |
| vo.story.03 | Magister Ashgrave | Dying | "There is nothing in here. Look. Look how light I am." |
| vo.story.04 | Archivist Dorne | Chain 2 opens | "They are alive, you understand. That is the dreadful part. They are alive and nobody is in." |
| vo.story.05 | Lorekeeper Deepscroll | Chain 2 opens | "Don't let her frighten you. Let me frighten you. I have the older books." |
| vo.story.06 | Archivist Dorne | A Crown in Five Pieces | "Vaelric did not want to rule forever. He wanted to stop being afraid." |
| vo.story.07 | Lorekeeper Deepscroll | A Crown in Five Pieces | "Five shards. We know where one is. Somebody else knows where four are." |
| vo.story.08 | Archivist Dorne | After the Slagworks | "They were not melting it down. They were teaching it to hold a shape." |
| vo.story.09 | Lorekeeper Deepscroll | After the Slagworks | "I'd rather be wrong. Write that down. I would dearly love to be wrong." |
| vo.story.10 | Ysolde Thornwake | Three Envoys | "Break it. Every hour it exists, something green goes grey." |
| vo.story.11 | Legate Corvane | Three Envoys | "We have been free three hundred years. Crown him again and the dead kneel first." |
| vo.story.12 | Legate Corvane | Three Envoys | "You will notice that I am asking. Remember that I asked." |
| vo.story.13 | Ysolde Thornwake | Three Envoys, parting | "When this is done we will not thank you. We will simply not be enemies today." |
| vo.story.14 | Captain Morrigan Blackspade | RL-15 | "I dig. I don't ask what's down there. Asking is extra." |
| vo.story.15 | Archivist Dorne | Too Late | "We were a day behind. We were a day behind for a month." |
| vo.story.16 | Lady Seraphine (diary, read aloud) | VM-27 | "He told me my name tonight. Not the one they gave me. The one that was taken." |
| vo.story.17 | Lady Seraphine | Dying | "I only wanted somebody to come home to." |
| vo.story.18 | Lorekeeper Deepscroll | Raid attunement | "Ten of you. I asked for an army and the Thane sent me ten. So be an army." |
| vo.story.19 | Vaelric | The Crown breaks | "Then who will hold it all together?" |
| vo.story.20 | Archivist Dorne | Epilogue | "Nobody. That was always the answer. Nobody holds it. We just keep hold of each other." |

## 4. Announcers

| Id | Voice | Event | Line |
|---|---|---|---|
| vo.bg.01 | Crownfall herald | Match start | "The Crown has fallen. Take it." |
| vo.bg.02 | | A carrier picks up the Crown | "The Crown is taken!" |
| vo.bg.03 | | The carrier dies | "The Crown is on the ground!" |
| vo.bg.04–06 | | The hill changes hands | "Red holds the hill!" · "Blue holds the hill!" · "Yellow holds the hill!" |
| vo.bg.07 | | A shrine is captured | "A shrine is claimed." |
| vo.bg.08 | | A team is 100 points from winning | "One hundred to victory." |
| vo.bg.09 | | Your team wins | "Victory. The Crown is yours." |
| vo.bg.10 | | Your team loses | "Defeat. The Crown passes on." |
| vo.pit.01 | Pitmaster Grask | Two minutes before the chest | "Chest's coming up. Sharpen something." |
| vo.pit.02 | | The chest opens | "It's open! Whoever's left, it's yours!" |
| vo.pit.03 | | A player loots the chest | "{name}! Champion of the Dustpit! For now." |
| vo.pit.04 | | A player enters the sand | "Fresh meat on the sand." |
| vo.world.01 | Zone yell | Grimroot appears | *The Hangman's Oak pulls its roots from the earth.* |
| vo.world.02 | Zone yell | Pyrraxis appears | *A shadow crosses the sun over the Barrens. Something is burning.* |
| vo.world.03 | Zone yell | Gorrath appears | *The ground of the Rift opens its mouth.* |
| vo.world.04 | Zone yell | Any world boss dies | *{name} has been slain by the heroes of the Concord.* |

The three world yells and the death notice are text emotes; the rest are voiced.

## 5. Boss lines

"Engage" is said when the fight starts, "Kill" when the boss kills a player, "Death" when the boss dies. Other moments name the ability or phase from [Encounter Data](encounters.md).

### Gallowmere Crypts

| Boss | Moment | Line |
|---|---|---|
| Gravedigger Holt | Engage | "No, no. You're not on the list." |
| | Digs up helpers | "Up you get. There's work." |
| | Kill | "I'll dig you a good one." |
| | Death | "Who'll... who'll fill them in now?" |
| The Stitched Choir | Engage | *(six voices, out of tune)* "Dawn... that... lights... us..." |
| | A voice is silenced | "One of us has stopped." |
| | Kill | "Sing with us." |
| | Death | "Amen. Amen. Amen." |
| Sister Maudlin | Engage | "You left me in the dark. All of you." |
| | Candles go out | "He put the candles out one by one." |
| | Kill | "Now you know." |
| | Death | "Is it morning?" |
| Brandfather Kray | Engage | "Kneel, and it only hurts once." |
| | Brands a player | "A crown for every brow!" |
| | At 30% | "The Heir sees you. The Heir sees everything I see." |
| | Kill | "Ash to ash. As promised." |
| | Death | "I kept the faith. I just... changed which." |

### The Slagworks

| Boss | Moment | Line |
|---|---|---|
| Overseer Grint | Engage | "You're not on the shift sheet." |
| | Calls laborers | "Levers! Now, you dogs!" |
| | Kill | "Docked. Permanently." |
| | Death | "Somebody... carry the ledger..." |
| Molten Maw | Engage | *The slag heaves, and something in it opens.* |
| | Submerges | *Molten Maw sinks beneath the crust.* |
| | Death | *Molten Maw cools, cracks, and goes dark.* |
| Bellows-Master Thurga | Engage | "Cinderpaw. Fetch." |
| | Cinderpaw dies first | "You'll burn for that. Slowly." |
| | Thurga dies first | *Cinderpaw howls, and the fires rise.* |
| | Kill | "Too much air, not enough iron." |
| | Death | "Keep it... hot." |
| Forgemaster Khardun | Engage | "Exiled for good work. Come and see how good." |
| | Phase 2, at 50% | "It rings, do you hear? Hollow rings truest." |
| | Kill | "Slag." |
| | Death | "The shard... is already promised." |

### Hollowspire Keep

| Boss | Moment | Line |
|---|---|---|
| Castellan Vorn | Engage | "The Lady is not receiving." |
| | Lowers the portcullis | "Gates. As ordered." |
| | Kill | "I shall have that cleaned up." |
| | Death | "Tell her... I held the door." |
| Lord-Chamberlain Aubrec | The Banquet begins | "Guests! Be seated. There is a place for each of you." |
| | A noble rises | "Do try the next course." |
| | Kill | "One more for the table." |
| | Death | "The house... is closed." |
| Librarian Quill | Engage | "Shh." |
| | Floods the floor with ink | "Everything written. Nothing kept." |
| | Kill | "Filed." |
| | Death | "I never finished the index." |
| Ser Aldous | Engage | "I swore to the Dawn and I swore to her. One of them was listening." |
| | Inverts a blessing | "Be un-blessed." |
| | Kill | "Faith did not save you either." |
| | Death | "Then let it have been... for her." |
| Lady Seraphine Vael | Engage | "You came all this way to tell an orphan she cannot have her family back." |
| | Raises the shards | "He is calling. Can you really not hear him?" |
| | At 25% | "Grandfather. Grandfather, they are hurting me." |
| | Kill | "I am sorry. I did say." |
| | Death | "I only wanted somebody to come home to." |

### The Hollow Throne

| Boss | Moment | Line |
|---|---|---|
| The Bulwark of Tor Vael | Engage | "Gate sealed. Present authority." |
| | A lane is struck | "Authority not recognised." |
| | Death | "Gate... open." |
| The Echo Sisters | Engage | "Petitioners!" · "Petitioners." · "...petitioners..." |
| | One sister dies | "She has only stopped speaking. We have not." |
| | Kill | "Heard." |
| | Death (last sister) | "And now... no one answers." |
| Marshal Korvash | Engage | "Three hundred years at attention. At ease is over." |
| | Calls the ballistae | "Loose!" |
| | Kill | "Fall out." |
| | Death | "Parade... dismissed." |
| Ghul'thar | Engage | *The wyrm uncoils from the broken dome.* |
| | Takes to a ledge | *Ghul'thar climbs, and the glass begins to fall.* |
| | Death | *Ghul'thar slides from the ledge and does not rise.* |
| Archmagister Ilyra | Engage | "I am the voice he no longer has. Listen closely." |
| | Hollows a player | "You will not miss what I take." |
| | Kill | "Quiet, now." |
| | Death | "He will have to speak... for himself." |
| Vaelric, the Hollow King | Engage | "Subjects. You are late by three centuries." |
| | Phase 2 | "I held the world in one hand. Do you know what it weighs?" |
| | Phase 3, the hall shrinks | "Closer. Everything comes closer in the end." |
| | Kill | "Rest. I never could." |
| | Death | "Then who will hold it all together?" |

### World bosses

| Boss | Moment | Line |
|---|---|---|
| Grimroot | Engage | *Ropes creak in the branches of the Hangman's Oak.* |
| | Heartwood Exposed, at 30% | *The bark splits. Something inside is still beating.* |
| | Death | *Grimroot stands very still, and is only a tree.* |
| Pyrraxis | Engage | *Pyrraxis lands, and the ash rises to meet it.* |
| | Takes flight | *The Cinder Wyrm takes wing. Find cover.* |
| | Death | *The Cinder Wyrm's fire gutters out.* |
| Gorrath | Engage | *The Rift Maw has found something to eat.* |
| | Swallows a player | *Gorrath swallows {name} whole.* |
| | Death | *The Rift Maw closes for the last time.* |

## 6. The Athenaeum books

Twelve readable books at the Athenaeum in Solhaven (Under-Librarian Dust). Each opens as a two-page parchment window.

| # | Title | Text |
|---|---|---|
| 1 | The Three Lands | Halcyra is three lands and one sea. Meridia in the west is green and farmed and ours. Khazrun in the north-east is stone, snow and dwarves, and theirs, and by the Hearth-Oath ours as well. Sundrel in the south is broken, and belongs to whoever is left. Between them lies the Sundering Sea, which was not there when the Empire drew its maps. |
| 2 | Of the Dawnflame | Before anything was named there was a light, and it was warm. The priests of Solhaven call it Dawn and see it rise. The priests of Hammerdeep call it Forge and keep it fed. They have argued for three centuries over which is the truer name. The Flame has not given an opinion, and is warm for both. |
| 3 | The Verdant Choir | Every living thing has a voice, and the oldest of them were singing before the first prayer. A Hedgewarden does not command the Choir. A Hedgewarden asks, and waits, and is sometimes answered. Those who have heard it say it is less like a hymn than like rain on a great many leaves. |
| 4 | On the Lattice | Look up on a clear night and you see the Lattice: the web of star-light along which aether moves through the world. It gathered, once, at a single place in Sundrel, which the Empire called the Wellspring and built a throne upon. It gathers there no longer. |
| 5 | The Aurelian Empire | For fourteen hundred years one empire ruled every shore. Its roads were straight, its lamps never went out, and its citizens of every race paid the same tax. We remember it kindly because it is gone. Those who lived under it left few letters saying they were happy. |
| 6 | The Sundering | In the last year of the Empire, Vaelric the Last bound the Wellspring to a crown, so that he need never die and it need never fail. The Wellspring broke instead. Sundrel shattered. The causeway fell into the sea. The gate-city of Tor Vael was swallowed by the earth in a single afternoon, and the canyon country that remained is called the Riftlands. We count our years from that day. |
| 7 | The Hearth-Oath | In the forty-first year After Sundering, King Aldric of Solhaven and High Thane Brunna Deepanvil broke one loaf over one fire and swore that neither people would shut a door against the other. That is the whole of the Oath. Everything else the Concord has built is commentary. |
| 8 | The Thorn Wars | The folk of the western deepwoods did not ask us to stop cutting. They stopped us. For thirteen years the forest moved by night and the border moved with it. It rests now at Thornwick, where both sides keep watch and neither waves. |
| 9 | The Ash Crusade | A century ago the Concord sailed south to lay the dead of Sundrel to rest. The dead declined. They called themselves the Empire still, and held the walls of Vael Morrow for six years until our fleet went home. Soldiers who were there do not use the word "undead". They say "the citizens", and lower their voices. |
| 10 | Mountain and Dale | A dwarf of the mountain will tell you a true dwarf lives under stone. A dwarf of the dale will tell you a true dwarf can grow his own supper. They are one people, and each is sure the other has forgotten something important. Do not take a side at table. |
| 11 | A Traveller's Guide to Kite's Rest | Kite's Rest stands on a pillar of rock in the Riftlands and belongs to nobody, which is why everybody trades there. You will see elves, ogres, and envoys who do not breathe. Keep your blade in its sheath, pay the lift-keeper, and do not ask what the salvagers have found. |
| 12 | A Warning Concerning Hollow Things | Aether forced through a living soul does not fill it. It scours it. What is left walks and speaks and remembers, and wants. The Athenaeum holds three objects recovered from such persons. They are kept apart from one another, in the dark, and the vault is not open to readers. |

## 7. Street chatter

Text only, in the say channel, between two ambient citizens who stop for a moment near each other. One exchange per pair of citizens every 3 to 6 minutes; a player hears at most one every 40 seconds.

| Place | Exchanges (first speaker / second speaker) |
|---|---|
| Solhaven | "Fish is dear this week." / "Everything's dear this week." · "Did you see the dwarf ship come in?" / "Heard it. They sing when they row." · "My boy wants to be a Cleric." / "Mine wants to be a pirate. Count your blessings." · "They say there's fire-folk in the Vale." / "They say a lot in the Vale." · "The Queen rode out this morning." / "Then the roads are safe till noon." · "Athenaeum's shut the vault again." / "Was it ever open?" · "You're limping." / "Stairs. This whole city is stairs." · "Dawn keep you." / "And you. And your stairs." |
| Hammerdeep | "Forge is running hot." / "Forge is always running hot. That's the forge." · "Dalefolk sent the grain late." / "Dalefolk sent the grain. Be glad." · "Lift's slow today." / "Lift's old. You'll be slow at that age." · "Smell that? Rootvault's in bloom." / "Smells like dirt." · "The Thane's called a moot." / "The Thane's called a meeting. The Dale calls moots." · "Humans on the ship again." / "Tall, aren't they? All that way to fall." · "Mind the cart!" / "Mind your own cart." · "Stone keep you." / "And the roof over it." |
| Dale and hill towns | "Rain by evening." / "You said that yesterday." · "And was I wrong?" / "It was a different rain." · "Ewes are restless." / "Something on the high ground. There always is." · "Good barley year." / "Don't say it out loud." · "Mountain cousin came down for the fair." / "Did he complain about the sky?" · "The whole time." / "Bless him." · "Reeve wants the wall mended." / "Reeve can hold the stones, then." · "Full barns to you." / "And a dry cellar." |
| Meridian villages | "Mill's still smoking, they say." / "Poor Cray. All that cider." · "Wolves are bold this year." / "Wolves are hungry this year." · "Saw a branded man on the north road." / "You saw a man with a burn. Don't start." · "Harvest fair's still on?" / "If there's a harvest." · "Warden's taking on hands." / "Warden's always taking on hands. Ask why." · "Bread's good today." / "Hobb's been at the flour again." · "Dawn keep you." / "And keep the wolves off." · "You heading to the city?" / "Not while there's sense in me." |
