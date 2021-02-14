from random import choice
import time
# from os import system

WORDS = ['floozy', 'moonwalking', 'serenaded', 'Australians', 'crame', 'scanline', 'wagonloads', 'trifluoperazine', 'sleuth', 'conduces', 'goldthread', 'fopperies', 'coverage', 'blateration', 'wreathy', 'walloons', 'virgularia', 'unheeded', 'sheep', 'sculpturer', 'licking', 'jaked', 'pealike', 'hallowed', 'spatt', 'minutiae', 'alienate', 'regenerate', 'Leakey', 'shood', 'updraft', 'Fielding', 'dissonancy', 'ottar', 'dislocated', 'fashionables', 'empery', 'tenters', 'coalier', 'riskless', 'neuroimaging', 'deepened', 'undersheet', 'radiohalos', 'spiderly', 'chiroplast', 'Lonchocarpus', 'haust', 'develope', 'unpolled', 'exponential', 'tussocks', 'spoken', 'sacksful', 'retorted', 'jogelrye', 'domesticated', 'femme', 'whiskey', 'astre', 'fonge', 'amikacin', 'destiny', 'prepupal', 'renationalized', 'reforms', 'Alexandros', 'igniting', 'sorrowful', 'unbuildable', 'faggy', 'ubiquitin', 'corydon', 'incontested', 'promiseth', 'fourrier', 'katana', 'buboes', 'halberdman', 'fishmouth', 'subdeacon', 'sulks', 'cassis', 'spader', 'hyphenations', 'lives', 'fenceposts', 'adessive', 'wider', 'unoperated', 'cirrhosis', 'theories', 'bunsen', 'squatting', 'Darlene', 'ultraviolent', 'irreligiously', 'Francis', 'disgust', 'coastal', 'funambulo', 'beebalm', 'warszawa', 'Louis XIV', 'drosometer', 'turvy', 'exposes', 
'poolish', 'consubstantial', 'Lojban', 'unshed', 'sternitic', 'derogate', 'establish', 'pigfucker', 'hinterhand', 'Taizhong', 'maniac', 'circumvention', 'cogitator', 'toxinogenic', 'christenings', 'deres', 'nucleole', 'phillibeg', 'nosegays', 'unmethodical', 'nyctitropic', 'protopresbyter', 'leucadendron', 'extatic', 'retrofits', 'palapa', 'nonblue', 'moule', 'isotherm', 'washiness', 'federationist', 'resuspensions', 'Prince Charming', 'priminery', 'remedies', 'Sistine', 'yardbird', 'cui bono', 'Heron', 'vaiselle', 'underinflating', 'speciesists', 'doubledome', 'yesternight', 'torchlight', 'streamlets', 'forenoon', 'weaning', 'Spencerian', 'insult', 'downtowners', 'blick', 'oncomings', 'livelock', 'colliquation', 'emerited', 'overspin', 'regressional', 'gallize', 'rancheria', 'reciprocating', 'sandless', 'quaternarily', 'comfortably', 'listers', 'miners', 'counterposed', 'godmoding', 'Colorado', 'fussbudget', 'Dutchwomen', 'arcanite', 'unremembering', 'importunateness', 'supersedeas', 'nitrosamines', 'whirl', 'citrange', 'bullyboy', 'teabag', 'templated', 'haberdashers', 'upgathers', 'banshie', 'unhealthy', 'budgetarily', 'unalterability', 'fifteenth', 'nuptse', 'unidactyl', 'ladders', 'tracery', 'actualized', 'sclat', 'clofarabine', 'cyanogen', 'symbiotic', 'arguments', 'livable', 'yttric', 'Aegeus', 'reinform', 'expounds', 'gravida', 'Charlie', 'hateful', 'masculinely', 'uteruses', 'sangomas', 'wineskin', 'dragged', 'handspike', 'aspens', 'duststorms', 'indefinability', 'incurrence', 'shrivelled', 'Grover', 'deluxe', 'discover', 'covings', 'untimeously', 'geographic', 'aureola', 'insensitively', 'nonheavyweight', 'microextraction', 'khoja', 'trepidatious', 'spectation', 'cooperators', 'ushering', 'redevelop', 'snazzy', 'unoriginate', 'exsolved', 'Mayans', 'farry', 'bonks', 'flavor', 'lypressin', 'screaks', 'squills', 'letterpress', 'metallization', 'extraneousness', 'reconfirmations', 'espaliered', 'Lagorchestes', 'elation', 'hatboxes', 'missionary', 'movement', 'saccharase', 'dunlin', 'pellere', 'restitch', 'pruce', 'cervelat', 'transfusible', 'merino', 'dishtowels', 'xyston', 'squalidly', 'gratulate', 'quarterstaffs', 'greedily', 'transfigure', 'sauceboat', 'multicolored', 'Affenpinscher', 'nomenclatorial', 'bzzzt', 'healthspans', 'impressibly', 'multicategory', 'offeree', 'close', 'Loxodonta', 'blagged', 'practicability', 'Prince', 'Noelene', 'megafaunas', 'lectures', 'encyclopedize', 'varicella', 'basepaths', 'underway', 'nautical', 'sniglets', 'Kuiper Belt', 'unboundedness', 'dealmakers', 'quantities', 'unfraternal', 'lipoid', 'epochal', 'vanpool', 'transference', 'isoptin', 'unrealness', 'commenced', 'regarded', 'arccosecant', 'pincushioning', 'sapadillo', 'Masters', 'butteries', 'topmost', 'shearing', 'boronate', 'racialist', 'thickens', 'paranal', 'scalenohedron', 'everie', 'verrucosis', 'educrat', 'rigidly', 
'urinose', 'encumbrancer', 'zygoma', 'foreseers', 'avoucher', 'foxhole', 'Enugu', 'reminds', 'bosas', 'resorptions', 'conservatrix', 'lauds', 'politeia', 'realise', 'disassociation', 'undescribable', 'souvlaki', 'blackleg', 'disagreeing', 'tizanidine', 'serpentaria', 'leavers', 'fuckpads', 'cabane', 'electrolytes', 'cajolery', 'sourish', 'oviposited', 'follers', '173xx', 'overview', 'tobramycin', 'ultramicrotome', 'downtake', 'madrassah', 'sitewide', 'Bushist', 'skullduggeries', 'damselfish', 'pondlife', 'subchronic', 'transclusions', 'unblended', 'pipped', 'Stephany', 'withdrawal', 'wigging', 'overcapitalise', 'classifications', 'recondensing', 'doctorial', 'furzy', 'besom', 'octavina', 'beseechers', 'agroindustry', 'duckism', 'continueth', 'defrayed', 'condoms', 'backdoor', 'squonks', 'doomy', 'consentaneously', 'diegetically', 'buphthalmos', 'introducing', 'chupacabra', 'punctuatim', 'Likud', 'thermoscopical', 'shitizen', 'ecohouse', 'shearwall', 'solfatara', 'kobold', 'unplaited', 'winterization', 'bribers', 'torcetrapib', 'shakes', 'phalloplasties', 'Eltanin', 'tuneful', 'umbellated', 'epimanikia', 'unbound', 'Caiaphas', 'unburned', 'fancied', 'bdellium', 'contemperation', 'inermis', 'acceptedly', 'arccoth', 'adlayers', 'Northumbrian', 'moratorium', 'leprosies', 'tauter', 'Pyrophorus', 'Bay Stater', 'réclame', 'viscount', 'disambiguated', 'alforja', 'patriarchalism', 'cybertronic', 'Flagler', 'waken', 'ultraslim', 'vertuous', 'melanuria', 'acaricidal', 'musquet', 'Ukraine', 'spoiling', 'dreamt', 'unceasingly', 'Chungking', 'unblanching', 'vialed', 'filially', 'trekking', 'teling', 'skelly', 'Marin', 'foundationwear', 'heliosis', 'alkalinize', 'subtexts', 'antithrombotic', 'tautophony', 'hypertense', 'roton', 'unpersuadable', 'pseudolarix', 'spokesmen', 'shabbiness', 'perspicacy', 'streaked', 'naïvely', 'depreciating', 'serpents', 'anastrophes', 'unwakeful', 'teenhood', 'unblocks', 'securitization', 'shisha', 'unconfidence', 'Alimos', 'Serpens', 'dissipating', 'outstep', 'supersensitive', 'deadness', 'honey', 'echoism', 'ethylacetate', 'Tania', 'featheriest', 'crawling', 'blissfulness', 'breachy', 'seagrass', 'dysphemisms', 'weaponeer', 'pinnie', 'decompressor', 'decipher', 'tranquilisers', 'Hooverphonic', 'alkalinized', 'colloquy', 'wallerian', 'multipage', 'outbear', 'framed', 'unlearnedness', 'stilt', 'beauties', 'Grógaldr', 'inquisitionary', 'tremulant', 'leint', 'rehears', 'brazenface', 'Broon', 'unsticks', 'macco', 'warpedness', 'demonist', 'heterochrony', 'fishways', 'urbanization', 'urgency', 'unshakenly', 'tragicalness', 'Bemba', 'claimes', 'lyric', 'wisheth', 'caissa', 'timework', 'extenuate', 'Balor', 'heterosexuality', 'copayments', 'excuse', 'dedolent', 'overweary', 'jibingly', 'herpes', 'tessellate', 'uncowardly', 'betrayment', 'earmarks', 'heaviness', 'feebled', 'lepidostrobus', 'neuroprotector', 'libertie', 'liquidated', "dursn't", 'mousepox', 'Nymphalis', 'quasar', 'besoms', 'xylaria', 'encheason', 'sanitory', 'allegorise', 'biteplate', 'refamiliarizing', 'girlishness', 'inwards', 'pistillum', 'upended', 'branchy', 'dishearten', 'understatements', 'viura', 'periwig', 'cynomorium', 'tuner', 'watchhouse', 'soever', 'yardful', 'jovial', 'topless', 'pepperonis', 'funloving', 'tropicalista', 'variograms', 'tinkler', 'manuka', 'bountifulness', 'sjambokked', 'sparer', 'hybrids', 'smorzando', 'massacrist', 'drachmae', 
'trowels', 'echolalia', 'generatively', 'overstraining', 'worthwhileness', 'brownism', 'convincible', 'sullies', 'intermix', 'siphonostome', 'medusa', 'forgette', 'dioptrical', 'dunked', 'hesychast', 'uncertainly', 'unflower', 'vesiculotubular', 'transcultural', 'language', 'indefinity', 'Chloris', 'narrowcasting', 'pantywaist', 'whizzes', 'clevy', 'lenticel', 'missionize', 'habutai', 'eburnean', 'apsidally', 'unfrayed', 'spaders', 'jacksnipes', 'creels', 'goodies', 'gloopiness', 'waning', 'trifling', 'roundly', 'shticks', 'tales', 'tunick', 'mountainward', 'moderately', 'urinated', 'neoteny', 'loneness', 'Russia', 'birthmothers', 'replaced', 'katsina', 'chikie', 'unbleeding', 'discontinuation', 'slitting', 'stook', 'squushed', 'steps', 'tharms', 'lasianthus', "Luts'k", 'Jubilee', 'foraminiferous', 'Lycopodium', 'harmonistic', 'reparational', 'catrina', 'communitive', 'swots', 'nonprison', 'peculiarly', 'clonic', 'termor', 'zygomatici', 'Wales', 'sloped', 'craturs', 'hypermutations', 'incrustata', 'humanless', 'squoze', 'sliest', 'brownishness', 'unfeelingly', 'availed', 'unsung', 'drudgeries', 'laziest', 'theopathy', 'bucks', 'disintegrative', 'triggerfish', 'generates', 'marshalled', 'triformity', 'wasser', 'entrusted', 'enlivener', 'Rambino', 'unstaffed', 'eirenic', 'revulsive', 'besiege', 'numbness', 'yisrael', 'tecolote', 'Tigrigna', 'wirche', 'limekilns', "Nuku'alofa", 'former', 'engobe', 'germane', 'Lipari', 'regularize', 'Bo Hai', 'bidisperse', 'ladies', 'poulet', 'squawberry', 'copyism', 'customizable', 'uncumbered', 'wisht', 'Puginesque', 'facilities', 'amphetamine', 'anatomise', 'Marguerite', 'consultive', 'hardpressed', 'prelims', 'visage', 'tvorog', 'aboideau', 'remission', 'Epicureanism', 'Shakhty', 'impone', 'lymphotoxin', 'sticky', 'scarification', 'gastronomes', 'focimeter', 'colics', 'inquisitively', 'hucked', 'oatlage', 'lowermost', 'fliskmahoy', 'respent', 'Peggys', 'falcula', 'unengaging', 'Brunswick', 'requires', 'hectometer', 'alimentative', 'retravelled', 'lettings', 'wastes', 'mononeuropathy', 'blackguardly', 'April', 'defibrillates', 'cogongrass', 'untactful', 'solicitor', 'doughier', 'frictional', 'apishly', 'racketballs', 'belays', 'weathermen', 'munging', 'triply', 'Malone', "Fidelia's", 'microvolt', 'humpies', 'planarized', 'unapprehensive', 'vlogs', 'oxcarts', 'pisolitic', 'dining', 'prophecy', 'complicatedness', 'Scunner', 'hustlers', 'Billy Bunter', 'unfoldment', 'randomization', 'chuff', 'zootheistic', 'seventyish', 'treen', 'mediciner', 'maxim', 'linked', 'rakhis', 'unmalicious', 'essentialists', 'chiastic', 'manchurian', 'termitary', 'ironing', 'Sanger', 'nostril', 'conclavist', 'cosmodromes', 'Hephzibah', 'reilluminating', 'wilderness', 'sippet', 'blinks', 'pacha', 'Anselm', 'fetishization', 'atherina', 'remonstrance', 'resolvin', 'Yaroslavl', 'laundered', 'supplicant', 'Louis XIII', 'shockvertising', 'drivel', 'cistus', 'unifying', 'collards', 'unteachability', 'Matty', 'bedraggled', 'kitting', 'twilling', 'methanotrophy', 'postpunk', 'Rustavi', 'bignose', 'ceston', 'viricidal', 'solve', 'stillest', 'neurosurgically', 'brewskies', 'nondiffusible', 'solicitousness', 'indulgenced', 'vibratile', 'wambles', 'rakes', 'torchless', 'apostil', 'rearwardly', 'contenting', 'upshifting', 'ursidae', 'rumps', 'soarings', 'paromomycin', 'Hellenophiles', 'saprophilous', 'unbirdlike', 'sectarist', 'utopianists', 'moaning', 'azoxystrobin', 'unfriendedness', 'donor', 'unspanked', 'unlucky', 'climp', 'plagiarizes', 'virginity', 'metastases', 'fangleness', 'Aspie', 'thwartedly', 'weirdsome', 'melanosome', 'retrograde', 'combovers', 'shmoe', 'merryandrew', 'mitzva', 'holloware', 'noncombustible', 'unmotherly', 'thurifer', 'Dameli', 'whiteworm', 'unbronzed', 'whizziness', 'transflux', 'meadowland', 'sawder', 'scandalized', 'Rajahmundry', 'doofi', 'botanizers', 'wassat', 'engrafting', 'bilaterally', 'forestall', 'wholly', 'articlealley', 'cutigeral', 'zionazi', 'pathlength', 'reselections', 'bloody', '2Kinda', 'vermis', 'unveilings', 'moniment', 'nonconvex', 'extinguishments', 'Painted Desert', 'lucklessly', 'cephalopterus', 'treble', 'turndowns', 'designees', 'efforce', 'unknightliness', 'undocumented', 'unbounded', 'unthinkableness', 'dreamlessly', 'alleluia', 'etherealising', 'seafront', 'sprigs', 'overwent', 'manganin', 'blesseth', 'parvorder', 'cornerbacks', 'furnituremaker', 'decohered', 'Dominick', 'pettyfogger', 'noncomplicated', 'futons', 'burden', 'upanayana', 'naphthalate', 'meteorologist', 'mucilage', 'ampler', 'shallowly', 'squalors', 'highroad', 'Aleut', 'exported', 'timeslips', 'sustainers', 'picometer', 'cilery', 'spigelia', 'dysphasia', 'uncurtained', 'fangled', 'crese', 'tergiversating', 'deric', 'hyalotype', 'brodiæa', 'fifthy', 'dismission', 'lasting', 'interosseal', 'Taman', 'altruist', 'viaticus', 'overhastily', 'virions', 'swelly', 'allegedly', 'Chukchi Sea', 'paratonic', 'poetomachia', 'deliriously', 'girlhood', 'Delany', 'tongkang', 'stunsail', 'distractions', 'triungulin', 'dhurries', 'handwrit', 'Quaker', 'apolegamic', 'bruins', 'Low Mass', 'jacobitically', 'aminolysis', 'rediscovered', "who's", 'Brahman', 'digresses', 'unreligious', 'iridio', 'enround', 'strict', 'gauntness', 'overdo', 'hagrode', 'relighting', 'multigenic', 'hatch', 'derriere', 'graphics', 'ingrave', 'tautie', 'papers', 'councilwomen', 'insupportably', 'termagants', 'heterografts', 'similies', 'intervocalic', 'thiol', 'SUDETENLAND', 'overlink', 'audacity', 'darers', 'incunable', 'fontein', 'robes', 'brewing', 'philosophises', 'consents', 'stuffiness', 'toenails', 'lintstock', 'bonnets', 'preservatives', 'arborous', 'trophotropic', 'rebozo', 'myxomatosis', 'poppet', 'culminates', 'albatross', 'reinscribes', 'degreaser', 'gophers', 'jizzes', 'panniers', 'gouramis', 'unhiding', 'ribosome', 'fluoranthene', 'quadrifoil', 'crumple', 'dependability', 'befriending', 'keffieh', 'Portage', 'Manchurians', 'appale', 'pentacrinites', 'kerchoo', 'barbarizes', 'audad', 'waggled', 'feigner', 'urotropin', 'roune', 'underling', 'toccatalike', 'flashtube', 'turnabout', 'clubwoman', 'clapperdudgeon', 'offloaded', 'bigmouths', 'rivets', 'betweenity', 'eligibly', 'vanished', 'whippable', 'imposed', 'Moradabad', 'rangefinders', 'unbrutalised', 'jangles', 'introductively', 'richard burton', 'relaxation', 'unthinkable', 'wealthier', 'justifications', 'floaters', 'huskier', 'moted', 'leavy', 'antithesis', 'mixtions', 'neuroplasm', 'clubbable', 'entranced', 'ganglial', 'Boeings', 'conglaciate', 'restauration', 'fanboyism', 'yacca', 'pullovers', 'juiciest', 'bypassed', 'salve', 'Babylonians', 'regulars', 'echis', 'decomposes', 'unrighteous', 'Tausug', 'froup', 'tombac', 'vilicate', 'radiatory', 'obstinately', 'EXtensible', 'schnitzel', 'nonliving', 'Bergsonism', 'undecide', 'climbs', 'distant', 'overreckon', 'perfecti', 'disputative', 'dichromat', 'upthrew', 'anodynous', 'factions', 'poesy', 'engagements', 'intoxicating', 'improsperity', 'accustomance', 'venerations', 'paleological', 'gambone', 'proceri', 'repairwoman', 'Parthenos', 'interveniency', 'Tesla', 'accoutres', 'kamchatkan', 'outros', 'letteral', 'footslogged', 'agraphobia', 'union', 'rishis', 'circar', 'noggins', 'latite', 'Elijah', 'thermology', 'ingredients', 'subfraction', 'cortically', 'soaped', 'shirking', 'mahzorim', 'noncensorship', 'heckelphone', 'cybersurfing', 'tepor', 'supper', 'unblock', 'hemosiderosis', 'integrative', 'amblypygids', 'yeeha', 'lackbeard', 'deafer', 'commotions', 'Bonaire', 'postulatory', 'pingos', "da'wa", 'antired', 'autoimmune', 'graduation', 'drudgery', 'turboshaft', 'imposure', 'cells', 'WHATmaster', 'suspicions', 'nahcolite', 'panellist', 'whings', 'accessibleness', 'leggier', 'toothcomb', 'formalizes', 'bandle', 'critique', 'unerase', 'antiserums', 'goral', 'torpedoist', 'noncatalog', 'ceylanite', 'emphasize', 'gasteropoda', 'formation', 'receptivities', 'federast', 'respiration', 'distemperate', 'cotilion', 'entamoeba', 'crushing', 'sirene', 'trifurcating', 'unquestionably', 'groanful', 'filching', 'statines', 'unsteadfast', 'trifled', 'Tennyson', 'tragedized', 'artful', 'owlets', 'elmes', 'paralytically', 'unusefulness', "that's", 'moshers', 'photosynthesis', 'weblogs', 'chaudron', 'butacaine', 'neuroglial', 'hearie', 'punchily', 'Calabrians', 'taccada', 'Ernestine', 'cryptates', 'brogan', 'bandolier', 'godchildren', 'proteosome', 'thiram', 'vermicides', 'bowsy', 'crumminess', 'hogwash', 'themer', 'Peribonca', 'accessorised', 'transportable', 'responsiable', 'gauntlet', 'oversing', 'ballooned', 'clecking', 'chieftain', 'barse', 'athetosic', 'surety', 'arthropathy', 'subcritical', 'unhabitual', 'wheatfield', 'kilter', 'suckiest', 'trenchand', 'eschevin', 'blights', 'Schiller', 'cleaners', 'dehydrated', 'morpho', 'insultive', 'polymerise', 'dragonless', 'whereases', 'shemale', 'Scotto', 'microscopically', 'automates', 'wolfing', 'Big Brotherism', 'underachiever', 'cyberman', 'haxx0r', 'beats', 'tirelire', 'nonperformers', 'obelize', 'tinctorial', 'experimentee', 'unfamiliarity', 'steno', 'vehicled', 'seasonable', 'Ioannina', 'bootlicking', 'togeather', 'ratlike', 'wholeheartedly', 'fiance', 'wordoid', 'wotting', 'cynipid', 'unreactive', 'Dreyfus', 'swinger', 'Hongen', 'exclusory', 'OMGWTFBBQ', 'marijauna', 'lilting', 'Eyemouth', 'tribasic', 'spermatogonium', 'imitativeness', 'detumesce', 'moviedom', 'ultrasounds', 'thunderbolts', 'slogo', 'switcheroos', 'embodiments', 'reenactor', 'fleshpots', 'D.R.I.', 'trenchermen', 'subcontractor', 'mustest', 'hemopoietic', 'windsurf', 'defuel', 'hydrophilicity', 'spacefaring', 'indebtedly', 'vituperated', 'bromelin', 'letting', 'chondrule', 'memorative', 'precious', 'algebraic', 'interquartile', 'meadow', 'unmiked', 'unprofitable', 'phylarchs', 'tusks', 'firmans', 'pseudogene', 'sinned', 'turn against', 'locks', 'screwtops', 'juttingly', 'optogenetics', 'lesser', 'lancing', 'autoclean', 'hexagonal', 'upbraideth', 'inequable', 'torchons', 'unavailingly', 'waivable', 'Heath', 'Alexander', 'spawners', 'gramicidin', 'blogrolls', 'comfortingly', 'trios', 'webzine', 'DuckTales', 'bialys', 'tooroo', 'refurbishes', 'anaerobiosis', 'conocephalus', 'apicad', 'adopted', 'unific', 'pewing', 'portenaunce', 'participancy', 'potion', 'instructress', 'leptogenesis', 'teazle', 'ticks', 'lollygaggers', 'dragee', 'pharisee', 'undercharging', 'panegyrical', 'mimosa', 'consular', 'urges', 'etiologies', 'includes', 'enforces', 'guested', 'countersigned', 'Spencer', 'understandingly', 'pentatomic', 'alkylbenzenes', 'viscometer', 'sails', 'cloisters', 'loaders', 'flecks', 'kraut', 'overfront', 'marshes', 'disagreeability', 'sireny', 'megalops', 'multifrequency', 'bepowdering', 'fordoes', 'Denglisch', 'unificatory', 'shaitans', 'coadjutors', 'dydoe', 'plethysmograph', 'tailwhip', 'cabinetmaker', 'unspun', 'Basilicata', 'databases', 'vulgarisation', 'unfull', 'sylvicultural', 'naiant', 'tagged', 'billy wilder', 'inebriates', 'midsong', 'cyberdeck', 'request', 'dobbin', 'hatchbacks', 'puisne', 'togeder', 'tuyeres', 'hesperis', 'dunno', 'slapp', 'barmbrack', 'byway', 'hydrophobins', 'teacher', 'outplaced', 'impuissant', 'reprief', 'microaneurism', 'anekantavada', 'bevelling', 'Galba', 'lucerna', 'restripe', 'boutefeu', 'rebaptisms', 'walkmans', 'visitest', 'ferrum', 'accidentary', 'kazoo', 'ongoing', "result's", 'acceptant', 'tussur', 'allied', 'cavalry', 'updraughts', 'unconcerned', 'queef', 'stokers', 'kommers', 'apatite', 'unsophisticated', 'daily', 'outswinger', 'Maurice', 
'langshan', 'vicariance', 'monogenesis', 'optometrically', 'stigmaria', 'beasts', 'sunbake', 'dishonor', 'dewatering', 'costate', 'resurge', 'crural', 'switchgrasses', 'offsetting', 'scoutmaster', 'shoeboxes', 'cammie', 'bursae', 'dissolv', 'usest', 'realistically', 'lengthened', 'ethereality', 'ragweeds', 'grandeur', 'unflowery', 'vulgarizes', 'potmen', 'acetogenins', 'midmeal', 'golfs', 'yuhinas', 'piraters', 'playlists', 'suggesting', 'refractor', 'whipstall', 'looking', 'dustcarts', 'degradations', 'unmistakeable', 'interpenetrant', 'bifurcated', 'tautology', 'keratosis', 'circumflect', 'lavishes', 'webbed', 'staddles', 'unilaterally', 'nervus', 'libdbnss4', 'dawed', 'starosty', 'Hutchinson', 'Monday', 'unallayed', 'narrowband', 'loper', 'transformism', 'planeload', 'us', 'appertain', 'postcode', 'lathery', 'harps', 'amulets', 'tinsel', 'dynamistic', 'forecasters', 'allargando', 'varying', 'enlivenment', 'farcical', 'exculpations', 'inferential', 'Hollands', 'stretch', 'transmitted', 'collateralized', 'Lucifer', 'defrostable', 'brownest', 'forego', 'sliders', 'hummus', 'cuteness', 'unspike', 'hallucinations', 'sheld', 'Banting', 'Stone', 'journeyman', 'multiramified', 'sperge', 'glamorized', 'geniculately', 'sitreps', 'pioted', 'togas', 'franckeite', 'multifocal', 'changeable', 'untenable', 'revanche', 'unvoiced', 'adenosine', 'alumin', 'mealies', 'bestower', 'compliance', 'lunched', 'unrolling', 'reemerging', 'underblows', 'wobulator', 'metalize', "Sha'aban", 'teleconferenced', 'Scheme', 'guiges', 'wingeing', 'latterday', 'copperwork', 'osteal', 'Memphis', 'advances', 'eukaryotic', 'indite', 'yogist', 'pipedreams', 'Britisher', 'egotisms', 'neurosurgery', 'bastite', 'motivationless', 'nontheater', 'sledgelike', 'paragraphing', 'Manets', 'onagraceae', 'frenne', 'Marena', 'docufantasy', 'regidors', 'skybox', 'untasted', 'uprooter', 'subheadlines', 'mullein', 'nastic', 'anchylosis', 'Ballard', 'notropis', 'multipass', 'NOFORN', 'duplicature', 'undergear', 'coalification', 'nondancer', 'cloned', 'resodded', 'foreseeingly', 'kamachi', 'tickseed', 'sufficed', 'sickener', 'sorries', 'Dunfermline', 'punkahs', 'paddies', 'ringsider', 'burst', 'magistrate', 'sterilizing', 'furrowed', 'mastupration', 'fluorography', 'inst.', 'abbreviature', 'verner', 'perfect', 'Tyron', 'stumbleth', 'bellite', 'alliaceous', 'agents', 'rebought', 'Nergal', 'wahoo', 'reemits', 'intradural', 'garotes', 'blastocoele', 'transbaikalian', 'quadripartite', 'exageration', 'skicross', 'trypan', 'advantage', 'waterless', 'nonattender', 'Entprise', 'injuncting', 'salinised', 'peirastic', 'scriptorial', 'sponges', 'uniformity', 'loogy', 'legateship', 'sacellum', 'unfathomably', 'copyfraud', 'praetorium', 'natrum', 'panners', 'nonfissionable', 'latrines', 'Skylar', 'manoeuvrings', 'floating', 'olingos', 'prezzies', 'unpromised', 'autofellatio', 'ovariotomy', 'bukshish', 'jandals', 'beamster', 'gallicè', 'adance', 'unbrace', 'follering', 'craniota', 'epiphytes', 'unrolled', 'ethyl', 'huffish', 'mailed', 'Cotton Belt', 'latitudinarian', 'crackberries', 'steroidogenic', 'indefectibility', 'hassocks', 'manjak', 'Cukor', 'Duala', 'minimised', 'transcytosis', 'monarchies', 'schrink', 'regimentals', 'fuggedaboudit', 'peason', 'spiderwort', 'Rabbie', 'exponentiating', 'roccus', 'salvour', 'henceforth', 'trend', 'wastebins', 'placenta', 'differing', 'upflowing', 'nortryptyline', 'MacGuffin', 'inspissation', 'Balinesian', 'deepsome', 'bondager', 'enucleates', 'disafforest', 'macrocytosis', 'partygoer', 'stags', 'coheir', 'autofluorescent', 'words', 'prelatism', 'Eames', 'triennial', 'nonhepatic', 'stims', 'undersecretary', 'Gardner', 'electrolyte', 'revolts', 'hazing', 'ribosomes', 'sceptral', 'quincuncially', 'Rumania', 'wholesome', 'underestimated', 'defogged', 'coregistered', 'particularness', 'unship', 'argued', 'workmate', 'presupposing', 'biographizing', 'bunch', 'blatant', 'ridicule', 'mercaptoethanol', 'shaggily', 'positions', 'Thammuz', 'arenophile', 'bleeding', 'kabobs', 'amusable', 'scurry', 'chewable', 'quaigh', 'solitary', 'tunes', 'willet', 'dreamcatcher', 'philosophical', 'prive', 'twattler', 'persued', 'philography', 'fictionists', 'Nunki', 'unstable', 'claik', 'monitorless', 'agronomists', 'muted', 'bludgeon', 'postfeudal', 'metastates', 'fillip', 'trembler', 'partim', 'antivirals', 'khitmatgars', 'radioelement', 'indivisible', 'ketyl', 'deliberated', 'exultations', 'unequivocal', 'fence', 'isotropic', 'auctioneered', 'serialization', 'hudood', 'coordinate', 'ladycow', 'audiologist', 'nonforeigners', 'federalisms', 'accelerations', 'haustellate', 'glacieret', 'prepackaged', 'servisable', 'souteneur', 'voiturette', 'unrusted', 'destigmatise', 'Bunburying', 'whippings', 'terrestrial', 'unblinking', 'creamed', 'hitting', 'kosmos', 'embargo', 'overruling', 'unsanctioned', 'pharmacist', 'kirgiz', 'besmirchment', 'redundancies', 'kinkers', 'mediating', 'bequeaths', 'zygomas', 'viscoid', 'cruræus', 'effectuate', 'commonizes', 'apoxia', 'spookiest', 'linearising', 'moisturizer', 'Earth Mother', 'jutted', 'cheery', 'wordle', 'salivating', 'unequal', 'zombifying', 'conferred', 'isotropically', 'thinkfree', 'wingdings', 'vulcanologist', 'changers', 'unintelligible', 'flashguns', 'Gestuno', 'roweling', 'domiciliaries', 'wheaty', 'cladrastis', 'oxtongue', 'foremost', 'arrondissements', 'prokinetic', 'Presocratic', 'ordnance', 'affectible', 'larrea', 'paperweights', 'desegregated', 'podcatcher', 'piony', 'troublemaking', 
'sacrificios', 'populizer', 'gumshoe', 'wireless', 'maniraptoran', 'elderish', 'tressed', 'envisaging', 'appams', 'cellulate', 'transferrable', 'Melchior', 'flatbill', 'superhighways', 'steadfastness', 'Reaganites', 'bighorn', 'calluna', 'perlitic', 'ursid', 'tentage', 'Babism', 'feeing', 'bivouacking', 'Issas', 'discouragements', 'brewpub', 'excerption', 'premies', 'taira', 'myomectomies', 'orbities', 'Gunnison', 'trudgers', 'muleskinner', 'midwifery', 'saker', 'ceraceous', 'hypomagnesaemia', 'accessible', 'panspermic', 'consolute', 'baken', 'Josephus', 'Oblomovism', 'unaffiliated', 'nullability', 'kiosk', 'distinguish', 'underivative', 'interflow', 'digitally', 'mutant', 'haemolysin', 'emotionally', 'tutus', 'thrashel', 'abgregate', 'shipwrights', 'offset', 'amido', 'amissibility', 'vanishment', 'waxless', 'fieldfares', 'postpositive', 'réchauffé', 'hypnone', 'infoscape', 'resew', 'incorporeality', 'idyls', 'phendimetrazine', 'hirundine', 'glyoxal', 'confesseth', 'reaccreditation', 'decagrams', 'didanosine', 'Copland', 'regelate', 'invigilators', 'superpipes', 'noxiousness', 'pandeism', 'extrasolar', 'unsatiate', 'transhumans', 'sextant', 'dextrans', 'cigarless', 'agritourist', 'trema', 'futuristically', 'sortileges', 'spelaeology', 'fanciful', 'therf', 'underfed', 'tweedling', 'brevets', 'valkyr', 'ululates', 'vloggers', 'subglacial', 'phalansteric', 'inaccurate', 'cosmocampus', 'nonallowable', 'unbiodegradable', 'quarrelous', 'periodontal', 'osmoregulate', 'encamps', 'charterer', 'grottos', 'extinguish', 'wildly']

HM_BASE = """      __________                    .
      |        |                    .
               |                    .
               |                    .
               |   Lives left = 5   .
               |                    .
               |                    .
               |                    .
    ============                    .
:::::::::::::::::::::::::::::::::::::
"""
HM_1 = """      __________                    .
      |        |                    .
    (>.<)      |                    .
      |        |                    .
               |   Lives left = 4   .
               |                    .
               |                    .
               |                    .
    ============                    .
:::::::::::::::::::::::::::::::::::::
"""
HM_2 = """      __________
      |        |                    .
    (>.<)      |                    .
      |_       |                    .
      | \      |   Lives left = 3   .
      |  \     |                    .
               |                    .
               |                    .
    ============                    .
:::::::::::::::::::::::::::::::::::::
"""
HM_3 = """      __________                    .
      |        |                    .
    (>.<)      |                    .
     _|_       |                    .
    / | \      |   Lives left = 2   .
   /  |  \     |                    .
               |                    .
               |                    .
    ============                    .
:::::::::::::::::::::::::::::::::::::
"""
HM_4 = """      __________                    .
      |        |                    .
    (>.<)      |                    .
     _|_       |                    .
    / | \      |   Lives left = 1   .
   /  |  \     |                    .
       \       |                    .
        \      |                    .
    ============                    .
:::::::::::::::::::::::::::::::::::::
"""
HM_5 = """      __________                    .
      |        |                    .
    (>.<)      |                    .
     _|_       |                    .
    / | \      |   Lives left = 0   .
   /  |  \     |                    .
     / \       |                    .
    /   \      |                    .
    ============                    .
:::::::::::::::::::::::::::::::::::::
"""
def print_choices_tries():
    print("\n--------------------------------------------------------------")
    print("All guessed letters till now : "," , ".join(choices_done))
    print("Total guesses done           : ",tries)
    print("--------------------------------------------------------------\n")
    time.sleep(1)

# def clear_screen():
#     _ = system('cls')

STRIKES=[HM_BASE,HM_1,HM_2,HM_3,HM_4,HM_5]
print("**  STARTING HANG-MAN  **\n")
playAgain = True

while playAgain :
    random_word = list(choice(WORDS).upper())
    visited = [False]*len(random_word)
    choices_done=set()
    cur_strike=0
    tries=0

    while cur_strike != 5:
        print('............<< HANGMAN >>............')
        print(STRIKES[cur_strike])
        ## print Letter Holders
        user_word=""
        for letter,status in zip(random_word,visited):
            if status:
                user_word += letter
            else:
                user_word += " _ "
        print("Guess the WORD => ",user_word, "  | ( Word length =",len(random_word),")")
        ## END
        letter_ip = input('\n[choice] Please Enter your letter choice -> ')
        # Handle the input letter
        if letter_ip == '':
            print("\n[ALERT] Please Enter a valid alphabet. DO NOT enter special characters, number or spaces!\n")
            continue
        elif letter_ip[0] == ' ':
            print("\n[ALERT] Please Enter a valid alphabet. DO NOT enter special characters, number or spaces!\n")
            continue
        letter_ip = letter_ip[0].upper()
        if not letter_ip.isalpha():
            print("\n[ALERT] Please Enter a valid alphabet. DO NOT enter special characters, number or spaces!")
            print("Entered input entered : ",letter_ip,"\n")
            continue
        tries+=1
        if letter_ip not in choices_done:
            choices_done.add(letter_ip)
        else:
            print("\n[ALERT!] You have already tried this letter. Please guess a new letter.")
            print_choices_tries()
            continue
        #End 

        ## Validate input chocie
        update_Flag=False
        for idx, i in enumerate(random_word):
            if i == letter_ip:
                visited[idx] = True
                update_Flag=True
        if update_Flag:
            print("\n[**] Nice guess! Keep Going!")
        else:
            print("\n[**] OOPS! Incorrect guess! Life reduced by 1.")
            cur_strike+=1
        ## END
        
        print_choices_tries()

    if sum(visited) == len(visited):
        print("\nWohoo!! You have guesed the Word correctly!!")
        print("The word you guessed is : ","".join(random_word))
    else:
        print("\nOut of Lives...Better luck next time!")
        print("The word to be guessed was : ","".join(random_word))

    print_choices_tries()

    print("\nDo you wish to play again!?\n1. Yes.\n2. No.\n")
    choice_pg = input("Choice -> ")
    choice_pg = choice_pg[0]
    if choice_pg.isdigit() and choice_pg != "1":
        playAgain = False
    else:
        playAgain = False

print("Thank you for playing Hangman!\nPlease do play again!")
print("** THE END **")
